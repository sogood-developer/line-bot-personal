# -*- coding: utf-8 -*-
from lib.akad.ttypes import (
    CreateQrSessionRequest, CreateQrCodeRequest, CheckQrCodeVerifiedRequest,
    VerifyCertificateRequest, CreatePinCodeRequest, CheckPinCodeVerifiedRequest,
    SecondaryQrCodeException, QrCodeLoginRequest,
    IdentityProvider, LoginResultType, LoginRequest, LoginType)
from lib.akad import SecondaryQrCodeLoginService, SecondaryQrCodeLoginPermitNoticeService
from thrift.transport import THttpClient
from thrift.protocol import TCompactProtocol
from .server import Server
from .session import Session
from .callback import Callback

import urllib, base64, os, rsa, requests, urllib.parse, json
import axolotl_curve25519 as curve

def createSecondaryQrCodeLoginService(host, headers):
    transport = THttpClient.THttpClient(host)
    transport.setCustomHeaders(headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = SecondaryQrCodeLoginService.Client(protocol)
    return client

def createSecondaryQrCodeLoginPermitNoticeService(host, headers):
    transport = THttpClient.THttpClient(host)
    transport.setCustomHeaders(headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    client = SecondaryQrCodeLoginPermitNoticeService.Client(protocol)
    return client
    
class Auth(object):
    isLogin     = False
    authToken   = ""
    certificate = ""

    def __init__(self):
        self.server = Server(self.appType)
        self.callback = Callback(self.__defaultCallback)
        self.server.setHeadersWithDict({
            'User-Agent': self.server.USER_AGENT,
            'X-Line-Application': self.server.APP_NAME,
            'x-lal': 'en_US'
        })

    def __loadSession(self):
        self.talk       = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_API_QUERY_PATH_FIR, self.customThrift).Talk()
        self.poll       = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_POLL_QUERY_PATH_FIR, self.customThrift).Talk()
        self.call       = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_CALL_QUERY_PATH, self.customThrift).Call()
        self.channel    = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_CHAN_QUERY_PATH, self.customThrift).Channel()
        #self.square     = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_SQUARE_QUERY_PATH, self.customThrift).Square()
        self.liff       = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_LIFF_QUERY_PATH, self.customThrift).Liff()
        self.shop       = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_SHOP_QUERY_PATH, self.customThrift).Shop()

        self.revision = self.poll.getLastOpRevision()
        self.isLogin = True

    def __loginRequest(self, type, data):
        lReq = LoginRequest()
        if type == '0':
            lReq.type = LoginType.ID_CREDENTIAL
            lReq.identityProvider = data['identityProvider']
            lReq.identifier = data['identifier']
            lReq.password = data['password']
            lReq.keepLoggedIn = data['keepLoggedIn']
            lReq.accessLocation = data['accessLocation']
            lReq.systemName = data['systemName']
            lReq.certificate = data['certificate']
            lReq.e2eeVersion = data['e2eeVersion']
        elif type == '1':
            lReq.type = LoginType.QRCODE
            lReq.keepLoggedIn = data['keepLoggedIn']
            if 'identityProvider' in data:
                lReq.identityProvider = data['identityProvider']
            if 'accessLocation' in data:
                lReq.accessLocation = data['accessLocation']
            if 'systemName' in data:
                lReq.systemName = data['systemName']
            lReq.verifier = data['verifier']
            lReq.e2eeVersion = data['e2eeVersion']
        else:
            lReq=False
        return lReq

    def loginWithCredential(self, _id, passwd):
        if self.systemName is None:
            self.systemName=self.server.SYSTEM_NAME
        if self.server.EMAIL_REGEX.match(_id):
            self.provider = IdentityProvider.LINE       # LINE
        else:
            self.provider = IdentityProvider.NAVER_KR   # NAVER
        
        if self.appName is None:
            self.appName=self.server.APP_NAME
        self.server.setHeaders('X-Line-Application', self.appName)
        self.tauth = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_AUTH_QUERY_PATH).Talk(isopen=False)

        rsaKey = self.tauth.getRSAKeyInfo(self.provider)
        
        message = (chr(len(rsaKey.sessionKey)) + rsaKey.sessionKey +
                   chr(len(_id)) + _id +
                   chr(len(passwd)) + passwd).encode('utf-8')
        pub_key = rsa.PublicKey(int(rsaKey.nvalue, 16), int(rsaKey.evalue, 16))
        crypto = rsa.encrypt(message, pub_key).hex()

        try:
            with open(_id + '.crt', 'r') as f:
                self.certificate = f.read()
        except:
            if self.certificate is not None:
                if os.path.exists(self.certificate):
                    with open(self.certificate, 'r') as f:
                        self.certificate = f.read()

        self.auth = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_LOGIN_QUERY_PATH).Auth(isopen=False)

        lReq = self.__loginRequest('0', {
            'identityProvider': self.provider,
            'identifier': rsaKey.keynm,
            'password': crypto,
            'keepLoggedIn': self.keepLoggedIn,
            'accessLocation': self.server.IP_ADDR,
            'systemName': self.systemName,
            'certificate': self.certificate,
            'e2eeVersion': 0
        })

        result = self.auth.loginZ(lReq)
        
        if result.type == LoginResultType.REQUIRE_DEVICE_CONFIRM:
            self.callback.PinVerified(result.pinCode)

            self.server.setHeaders('X-Line-Access', result.verifier)
            getAccessKey = self.server.getJson(self.server.parseUrl(self.server.LINE_CERTIFICATE_PATH), allowHeader=True)

            self.auth = Session(self.server.LINE_HOST_DOMAIN, self.server.Headers, self.server.LINE_LOGIN_QUERY_PATH).Auth(isopen=False)

            try:
                lReq = self.__loginRequest('1', {
                    'keepLoggedIn': self.keepLoggedIn,
                    'verifier': getAccessKey['result']['verifier'],
                    'e2eeVersion': 0
                })
                result = self.auth.loginZ(lReq)
            except:
                raise Exception('Login failed')
            
            if result.type == LoginResultType.SUCCESS:
                if result.certificate is not None:
                    with open(_id + '.crt', 'w') as f:
                        f.write(result.certificate)
                    self.certificate = result.certificate
                if result.authToken is not None:
                    self.loginWithAuthToken(result.authToken)
                else:
                    return False
            else:
                raise Exception('Login failed')

        elif result.type == LoginResultType.REQUIRE_QRCODE:
            self.loginWithQrCode()
            pass

        elif result.type == LoginResultType.SUCCESS:
            self.certificate = result.certificate
            self.loginWithAuthToken(result.authToken)
        
    def loginWithQrCode(self):
        headers = {
            'User-Agent': self.server.USER_AGENT,
            'X-Line-Application': self.server.APP_NAME,
            'x-lal': 'en_US'
        }
        client = createSecondaryQrCodeLoginService('https://gxx.line.naver.jp' + self.server.LINE_LOGIN_REQUEST_V1, headers)
        session = client.createSession(CreateQrSessionRequest())
        qrcode = client.createQrCode(CreateQrCodeRequest(session.authSessionId)).callbackUrl
        secret = self.genE2EESecret()
        self.callback.QrUrl(f'{qrcode}{secret}')
        headers = {
            'User-Agent': self.server.USER_AGENT,
            'X-Line-Application': self.server.APP_NAME,
            'X-Line-Access': session.authSessionId,
            'x-lal': 'en_US'
        }
        client_verif = createSecondaryQrCodeLoginPermitNoticeService('https://gxx.line.naver.jp' + self.server.LINE_LOGIN_CHECK_V1, headers)
        qrverified = client_verif.checkQrCodeVerified(CheckQrCodeVerifiedRequest(session.authSessionId))
        try:
            certverified = client.verifyCertificate(VerifyCertificateRequest(session.authSessionId, None))
        except SecondaryQrCodeException as e:
            print("SQR ERROR: {}".format(e))
            pincode = client.createPinCode(CreatePinCodeRequest(session.authSessionId)).pinCode
            self.callback.PinVerified(pincode)
            pincodeverified = client_verif.checkPinCodeVerified(CheckPinCodeVerifiedRequest(session.authSessionId))
        except Exception as e:
            print("ERROR: {}".format(e))
        lReq = client.qrCodeLogin(QrCodeLoginRequest(session.authSessionId, self.server.SYSTEM_NAME, True))
        self.loginWithAuthToken(lReq.accessToken)

    def loginWithAuthToken(self, authToken=None):
        if authToken is None:
            raise Exception('Please provide Auth Token')
        if self.appName is None:
            self.appName=self.server.APP_NAME
        self.server.setHeadersWithDict({
            'X-Line-Application': self.appName,
            'X-Line-Access': authToken
        })
        self.authToken = authToken
        self.__loadSession()

    def genE2EESecret(self):
        private_key = curve.generatePrivateKey(os.urandom(32))
        public_key = curve.generatePublicKey(private_key)

        secret = urllib.parse.quote(base64.b64encode(public_key).decode())
        version = 1
        return f"?secret={secret}&e2eeVersion={version}"
    
    def __defaultCallback(self, str):
        print(str)

    def logout(self):
        self.isLogin = False
        self.auth.logoutZ()
