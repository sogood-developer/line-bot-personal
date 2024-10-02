# -*- coding: utf-8 -*-
from linepy import *
from akad.ttypes import *
from akad.SecondaryQrCodeLoginService import Client as LoginClient
from akad.SecondaryQrCodeLoginPermitNoticeService import Client as CertClient
from linepy.e2ee import *
from linepy.server import Server as config
from thrift.protocol import TCompactProtocol, TBinaryProtocol, TProtocol
from thrift.transport import THttpClient, TTransport
from thrift.Thrift import TProcessor
from threading import Thread
from datetime import datetime
import os, threading, livejson, requests, json, sys, time, traceback, random, subprocess, pytz, codecs
        
LOGINTOKEN = "token"
#================= [ LOGIN ] =================#
def HeadDestopWin():
	destopwin =["DESKTOPWIN\t6.6.0\tPC-nhTURp\t8.1","DESKTOPWIN\t6.3.2\tPC-4jVXmD\t8","DESKTOPWIN\t6.3.0\tPC-VELBlO\t7","DESKTOPWIN\t6.2.2\tPC-t3RE6S\t7","DESKTOPWIN\t6.5.2\tPC-Xrsx0c\t7","DESKTOPWIN\t6.0.3\tPC-zMfqiu\t8.1","DESKTOPWIN\t6.5.2\tPC-9R8KfN\t10","DESKTOPWIN\t6.6.0\tPC-SfTWbi\t8","DESKTOPWIN\t6.6.0\tPC-1jYwov\t10","DESKTOPWIN\t6.5.2\tPC-NgVvFS\t8.1","DESKTOPWIN\t6.1.1\tPC-faVx7A\t10","DESKTOPWIN\t6.1.1\tPC-4-EJQ3\t8.1","DESKTOPWIN\t6.3.0\tPC-eDOdSs\t10","DESKTOPWIN\t6.0.3\tPC-NOFrK8\t10","DESKTOPWIN\t6.2.2\tPC-BRXKxa\t8.1","DESKTOPWIN\t6.2.2\tPC-kkZShM\t8","DESKTOPWIN\t6.3.0\tPC-zGCyxg\t8.1","DESKTOPWIN\t6.3.2\tPC-SUYQVF\t10","DESKTOPWIN\t6.1.1\tPC-cAEFoc\t7","DESKTOPWIN\t6.5.2\tPC-XXgNwb\t8","DESKTOPWIN\t6.2.2\tPC-a-xT84\t10","DESKTOPWIN\t6.3.0\tPC-5QBUtX\t8","DESKTOPWIN\t6.3.2\tPC-35XfXF\t7","DESKTOPWIN\t6.1.1\tPC-65IdH8\t8","DESKTOPWIN\t6.6.0\tPC-eZyJgZ\t7","DESKTOPWIN\t6.0.3\tPC-UYKwN8\t8","DESKTOPWIN\t6.3.2\tPC-RX1IJe\t8.1","DESKTOPWIN\t6.0.3\tPC-deAVK5\t7"]
	return random.choice(destopwin)
Destopwin = HeadDestopWin() 
def HeadSysWindows():
	syswindows =["DESKTOPWIN\t7.5.0\tWindows4\t10","DESKTOPWIN\t7.3.1\tWindows1\t10","DESKTOPWIN\t7.4.0\tWindows11\t10","DESKTOPWIN\t6.2.0\tWindows2\t10","DESKTOPWIN\t7.3.0\tWindows3\t10","DESKTOPWIN\t7.2.0\tWindows10\t10","DESKTOPWIN\t6.3.2\tWindows9\t10","DESKTOPWIN\t6.5.4\tWindows8\t10","DESKTOPWIN\t6.6.0\tWindows7\t10","DESKTOPWIN\t6.7.0\tWindows6\t10","DESKTOPWIN\t6.7.2\tWindows5\t10","DESKTOPWIN\t7.7.0\tWindows12\t10","DESKTOPWIN\t7.8.0\tWindows13\t10","DESKTOPWIN\t7.9.0\tWindows14\t10","DESKTOPWIN\t7.10.1\tWindows15\t10","DESKTOPWIN\t6.2.1\tWindows16\t10","DESKTOPWIN\t6.2.2\tWindows17\t10","DESKTOPWIN\t6.2.1\tWindows18\t10","DESKTOPWIN\t6.3.0\tWindows19\t10","DESKTOPWIN\t6.5.0\tWindows20\t10","DESKTOPWIN\t6.5.2\tWindows21\t10","DESKTOPWIN\t6.7.1\tWindows22\t10","DESKTOPWIN\t7.0.0\tWindows23\t10","DESKTOPWIN\t6.5.4.2441\tWindows24\t10","DESKTOPWIN\t6.5.2.2431\tWindows25\t10"]
	return random.choice(syswindows)
Syswindows = HeadSysWindows()
nameApp1 = Syswindows
nameApp2 = Destopwin
nameApp = random.choice([Destopwin,Syswindows])
#================= [ LOGIN ] =================#
client = LINE("tetok78321@ioxmail.net","kim095200023",appName=nameApp)#id:newloginsb#k6
client.log("Auth Token : " + str(client.authToken))
clientPoll = OEPoll(client)
clientMID = client.getProfile().mid

ColorReset  =  "\033[0m"
ColorPurple =  "\033[35m"
print(f"""{ColorPurple}
APP : {nameApp}
NAME : {client.getProfile().displayName}
MID : {clientMID}
AuthToken : {client.authToken}
{ColorReset}
""")

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

admin = ["u4f277756fcca495d02e3292e317bec8b","uf17ac0aaec776a55460f0e50fa78fe61","u96f77decf42e3598ffdac8770787f946"]
settings = livejson.File("settings.json")
if "mid" not in settings:
    settings["mid"] = []
if "login" not in settings:
    settings["login"] = {}

wait = {
    'info':{},       
    'name':{}
}
try:
    waitOpen = codecs.open("userall/userlogin4.json","r","utf-8")
    wait = json.load(waitOpen)
    print("file user Go!!! ✔ ✔ ✔")
except:
    print("Couldn't file user  ⛔ ⛔ ⛔")
    
BotOpen = codecs.open("userall/usermaker.json","r","utf-8")
BotMaker = json.load(BotOpen)    
def Botdtext_install():  
    if "G_ticket" not in BotMaker: BotMaker["G_ticket"] =  {}
    if "token_user" not in BotMaker: BotMaker["token_user"] =  {}    
    if "scomd" not in BotMaker: BotMaker["scomd"] =  {}
    if "dtext" not in BotMaker: BotMaker["dtext"] =  {}
    if "dcomd" not in BotMaker: BotMaker["dcomd"] =  {}    
    if "dimage" not in BotMaker: BotMaker["dimage"] =  {}
    if "picz" not in BotMaker: BotMaker["picz"] =  {}    
    if "AutoTrans" not in BotMaker: BotMaker["AutoTrans"] =  {}	
Botdtext_install()
botticket = BotMaker['G_ticket']
botusercert = BotMaker['token_user']
botscomd = BotMaker['scomd']
botdtext = BotMaker['dtext']
botdcomd = BotMaker['dcomd']
botdimage = BotMaker['dimage']
botpicz = BotMaker['picz']
botAutoTrans = BotMaker['AutoTrans']   

Note  = """╭━━ 𝐈𝐍𝐅𝐎 𝐑𝐄𝐕𝐈𝐒𝐄 ━━╮
• add userlogin4.json
• add login alarm
• add login4
• add login6
• update clone-{directory}
• update for login

• update(12-12-64)
• update DESKTOPMAC

• update(15-03-65)
• update channel,config

• update(31-05-65)
• update createQrURL

• update(*04-07-65)
• update newloginv3

• update(29-08-65)
• update newloginv3
• update headRan"""

For_Login  = """╭━━ วิธีใช้งาน ━━╮
วิธีเข้าระบบ
https://youtu.be/yXTKDKIfZVw

*หมายเหตุ*
1.ถ้าบอทหลุดสามารถล็อคอินเองได้ตลอดเวลา

2.เซลบอทจะเสียค่าบริการเป็นรายเดือน แต่ตอนนี้เจ้าของบอทยังไม่ได้ทำระบบตัดบอทอัตโนมัติเมื่อครบเวลา เนื่องจากไม่มีเวลา จึงอนุโลมให้ใช้ยาวๆไปก่อน

3.บอทบัคขึ้นอยู่กับผู้ใช้งาน ว่าใช้งานหนักแค่ไหน หรือใช้งานประเภทที่ทำให้ไลน์คิดว่ามีการละเมิดเกิดขึ้น ไลน์จึงตัดระบบเพื่อป้องกัน หรือที่เราเรียกว่าบัค และเมื่อบัค จะหายภายใน 1 ชม.  24 ชม.  7 วัน 1 เดือน หรือเท่าไร่ไม่ทราบได้ ขึ้นอยู่กับไลน์

4.บางกลุ่มหรือบางแชทอาจใช้เซลบอทไม่ได้ อาจจะเพราะเนื่องจากกลุ่มนั้นเปิดระบบletter Sealing(https://sv1.picz.in.th/images/2021/09/06/CZoIWV.jpg)"""

from requests import get
file = os.path.splitext(os.path.basename(__file__))[0]
ip = get('https://api.ipify.org').text
tx ="╭━━ 𝐈𝐍𝐅𝐎 𝐒𝐄𝐑𝐕𝐄𝐑 ━━╮\n"
tx += "┃• ꜰɪʟᴇɴᴀᴍᴇ : {} .ᴘʏ\n".format(file)
tx += "┃• ɪᴘ ᴄʟɪᴇɴᴛ : {}\n".format(ip)
tx += "╰━━ {} ━━╯".format(client.getProfile().displayName)
allcontacts = client.getAllContactIds()
for mid in admin:
    if mid not in allcontacts:     
        try:
            client.findAndAddContactsByMid(mid)
            print(f"แอดมิดนี้สำเร็จ>>  {mid} 👍")
            time.sleep(2)
        except:
            pass
    amessage = "\n"
    status = client.getSettings().e2eeEnable
    if status == True:
        try:
            nego = client.talk.negotiateE2EEPublicKey(client.profile.mid)
            if nego.publicKey != None:
                client.talk.removeE2EEPublicKey(nego.publicKey)
                amessage += "Public key E2EE removed!"
            else: amessage += "Bad request! None type object is not iterable."
        except Exception as e:
            if 'code=85' in str(e): pass
    else:amessage += "Public key E2EE is inactive."
    x=mid
    try:
        client.sendMessage(x,"[ bot:"+f"{client.getProfile().displayName}"+" ]\n"+tx+amessage)
        client.sendMessage(x,"•hostname: {}•ip: {}\n•run:\ncd {} && python3.6 {}.py".format(host,ip,mypath,file))
    except:print("creator : " ,x)      
print("พร้อมใช้งานแล้ว")
 
def generateName(tipe,kelamin):
    a = requests.get(f"https://story-shack-cdn-v2.glitch.me/generators/fake-name-generator/{kelamin}?count=6").json()["data"]
    theName = f"{a[0]['name']} {a[0]['lastName']}"
    return theName[0:12]

kelamin = random.choice(["male","female"])
negara_nama = random.choice(["fake"])
MyName = generateName(negara_nama,kelamin)
DISPLAY_NAME = MyName
print(f"NAME: {DISPLAY_NAME}")

times = {
    "clock": True,
    "name": DISPLAY_NAME
    #"name": "LoginK6 Flex"#Login Niranam
}

Servers = """「 Help Servers Cmds 」

Servers
Commands:
- check:screen
- userfile
- resetuser"""

Commands = """「 Botlogin Commands 」

version4
(15-06-66)
Commands:
- login4
- login6
- loginself
- logout/ออกระบบ
- addsb (@)
- delsb (@)
- checkuser
- botleave
- botgroups
- delusernumber
- botreboot
- certificate reset
- note(admin)
- forlogin(admin)

- linux(admin)
- help:server(admin)
- sp
- runcom(admin)
- cto (token)
- .exec(↰)(code)

Note:
- (@) Tag members"""

Warning = """「 Warning 」
- User : {}
- Mid : {}
- Status : Not Found.
*Please Contact Admin."""

login = """「 LoginSelfBot 」
- Name : {}
- Mid : {}
- Day-Time : {} {}
- Status : Success Login in.

*Please click link below.:
- {}"""

NewUser = """「 UserList 」
Add User Success.
User_Status:
- Name : {}
- Mid : {}
- Time : {} {}
Please type "login" to login."""

DeletedUser = """「 UserList 」
Deleted User Success.
User_Status:
- Name : {}
- Mid : {}
- Time : {} {}"""

logout = """「 Logout Bots 」
- Name : {}
- Mid : {}
- Day-Time : {} {}
- Status : Your selfbot has been logout ♪"""

def helpLinux():
    with open('helpLinux.txt', 'r') as f:
        text = f.read()
    helpMsg1 = text.format()
    return helpMsg1

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def getNameByMid(mids):
    return client.getContact(mids).displayName

#===Loginpin===#
from qrv2.SecondaryQrCodeLoginService import Client as SecondaryService
from qrv2.ttypes import *
from qrv2.SecondaryQrCodeLoginPermitService import Client as PermitService
import qrcode
install = """thrift
rsa
pycryptodome
ffmpy
googletrans
wikipedia
requests_futures
python-axolotl_curve25519
six
httpx
hyper
youtube_dl
null
livejson
pafy
html5lib
httplib2"""
def createQrURL(auth,session):
    e2ee = E2EE()
    qrCode = auth.createQrCode(LoginQrCode_CreateQrCodeRequest(session)).callbackUrl + e2ee.generateParams()
    return qrCode

def sendConnect(endpoint,service,headers):
    transport = THttpClient.THttpClient("https://legy-jp-addr.line.naver.jp" + endpoint)
    transport.setCustomHeaders(headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    auth = service(iprot=protocol)
    transport.open()
    return auth

    """Headers = {
        "X-Line-Application": "DESKTOPMAC\t7.0.3\tMAC\t10.15.1",
        "User-Agent": "Line/7.0.3",
        "X-lal": "en_US"
    }
    auth = sendConnect("/acct/lgn/sq/v1",SecondaryService,Headers)
    session = auth.createSession(LoginQrCode_CreateQrSessionRequest()).authSessionId
    qr = createQrURL(auth,session)
    Headersx = {
        "X-Line-Application": "DESKTOPMAC\t7.0.3\tMAC\t10.15.1",
        "User-Agent": "Line/7.0.3",
        "X-lal": "en_US",
        "X-Line-Access": session
    }
    client.sendMessage(to,str(qr))
    img = qrcode.make(qr)
    img.save("qr.png")
    try:
        client.sendImage(to,"qr.png")
    except:
         client.sendImage(to,"qr.png")
    os.system("rm -rf qr.png")"""    
#===Loginpin===#

def LoginWithCertificate(to,sender,directory,file_name,certificate):
    """nameApp = random.choice([Destopwin,Syswindows])
    appname_ = nameApp
    useragent_ = appname_.split("\t")[1]
    headers = {
        "X-Line-Application": appname_,
        "User-Agent": "Line/"+useragent_,
        "X-lal": "en_US"
    }"""

    headers = {
        "X-Line-Application": "DESKTOPWIN\t6.5.2.2431\tWindows25\t10",
        "User-Agent": "Line/6.5.2.2431",
        "X-lal": "en_US"
    }
    transport = THttpClient.THttpClient(config.LINE_QRCODE_LOGIN_PATH)
    transport.setCustomHeaders(headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    secondary = LoginClient(iprot=protocol)
    transport.open()
    session = secondary.createSession(CreateQrSessionRequest()).authSessionId
    client.sendMessage(to,"Please wait...")
    e2ee = E2EE()
    """Headers = {
        "X-Line-Application": appname_,
        "User-Agent": "Line/"+useragent_,
        "X-lal": "en_US"
    }"""
    Headers = {
        "X-Line-Application": "DESKTOPWIN\t6.5.2.2431\tWindows25\t10",
        "User-Agent": "Line/6.5.2.2431",
        "X-lal": "en_US"
    }
    auth = sendConnect("/acct/lgn/sq/v1",SecondaryService,Headers)
    session = auth.createSession(LoginQrCode_CreateQrSessionRequest()).authSessionId
    qr = createQrURL(auth,session)
    client.sendMessage(to,str(qr))
    img = qrcode.make(qr)
    img.save("qr.png")
    try:
        client.sendImage(to,"qr.png")
    except:
         client.sendImage(to,"qr.png")
    os.system("rm -rf qr.png") 
    """Headers = {
        "X-Line-Application": appname_,
        "User-Agent": "Line/"+useragent_,
        "X-lal": "en_US",
        "X-Line-Access": session
    }"""
    Headers = {
        "X-Line-Application": "DESKTOPWIN\t6.5.2.2431\tWindows25\t10",
        "User-Agent": "Line/6.5.2.2431",
        "X-lal": "en_US",
        "X-Line-Access": session
    }
    transport = THttpClient.THttpClient(config.LINE_PERMIT_NOTICE_PATH)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    permit = CertClient(iprot=protocol)
    transport.open()
    try:
        permit.checkQrCodeVerified(CheckQrCodeVerifiedRequest(session))
    except:
        client.sendMessage(to,"QR code verification failed.")
        pass
    client.sendMessage(to,"Please wait...")
    try:
        secondary.verifyCertificate(VerifyCertificateRequest(session, certificate))
    except:
        client.sendMessage(to,"Certificate verification failed, please contact admin")
        pass
    try:
        token = secondary.qrCodeLogin(QrCodeLoginRequest(session, config.SYSTEM_NAME, False))
    except:
        client.sendMessage(to,"Token requests failed.\nUser account login limit")
        pass    
    os.system("screen -S {} -X kill".format(sender))
    os.system("cp -r {} clone-{}/{}".format(directory, directory,sender))    
    os.system('cd clone-{}/{} && echo -n "{} \c" > token.txt'.format(directory ,sender, token.accessToken))
    os.system('screen -dmS {}'.format(sender))
    os.system('screen -r {} -X stuff "cd clone-{}/{} && python3.6 {} \n"'.format(sender, directory, sender,str(file_name)))    
    settings["login"][sender] = True
    now2 = datetime.now()
    times = datetime.strftime(now2,"%X")
    days = datetime.strftime(now2,"%d/%m/%y")
    client.sendMessage(
        to,
        login.format(
            getNameByMid(sender),
            str(sender)[:25],
            str(days),
            str(times),
            "กรุณากดลิ้งด้านล่างด้วย(กดแค่ครั้งแรกพอ) :\nline://app/1602687308-GXq4Vvk9?type=text&text=「NiranamBotline」"            
        )
    )

def LoginWithSecondary(to,sender,directory,file_name):
    """nameApp = random.choice([Destopwin,Syswindows])
    appname_ = nameApp
    useragent_ = appname_.split("\t")[1]
    headers = {
        "X-Line-Application": appname_,
        "User-Agent":"Line/"+useragent_
    }"""
    headers = {"X-Line-Application": "DESKTOPWIN\t6.5.2.2431\tWindows25\t10","User-Agent": "Line/6.5.2.2431"}
    transport = THttpClient.THttpClient(config.LINE_QRCODE_LOGIN_PATH)
    transport.setCustomHeaders(headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    secondary = LoginClient(iprot=protocol)
    transport.open()
    session = secondary.createSession(CreateQrSessionRequest()).authSessionId
    client.sendMessage(to,"Please wait...")
    e2ee = E2EE()
    """Headers = {
        "X-Line-Application": appname_,
        "User-Agent": "Line/"+useragent_,
        "X-lal": "en_US"
    }"""
    Headers = {
        "X-Line-Application": "DESKTOPWIN\t6.5.2.2431\tWindows25\t10",
        "User-Agent": "Line/6.5.2.2431",
        "X-lal": "en_US"
    }
    auth = sendConnect("/acct/lgn/sq/v1",SecondaryService,Headers)
    session = auth.createSession(LoginQrCode_CreateQrSessionRequest()).authSessionId
    qr = createQrURL(auth,session)
    client.sendMessage(to,str(qr))
    img = qrcode.make(qr)
    img.save("qr.png")
    try:
        client.sendImage(to,"qr.png")
    except:
         client.sendImage(to,"qr.png")
    os.system("rm -rf qr.png")    
#___LoginpinSecond___#
    """Headers = {
        "X-Line-Application": appname_,
        "User-Agent": "Line/"+useragent_,
        "X-lal": "en_US",
        "X-Line-Access": session
    }"""
    Headers = {
        "X-Line-Application": "DESKTOPWIN\t6.5.2.2431\tWindows25\t10",
        "User-Agent": "Line/6.5.2.2431",
        "X-lal": "en_US",
        "X-Line-Access": session
    }
    transport = THttpClient.THttpClient(config.LINE_PERMIT_NOTICE_PATH)
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    permit = CertClient(iprot=protocol)
    transport.open()
    try:
        permit.checkQrCodeVerified(CheckQrCodeVerifiedRequest(session))
    except:
        client.sendMessage(to,"QR code verification failed.")
        pass
    try:
        secondary.verifyCertificate(VerifyCertificateRequest(session, None))
    except:
        pincode = secondary.createPinCode(CreatePinCodeRequest(session)).pinCode
        client.sendMessage(to,"PinCode : " + str(pincode))
        try:
           permit.checkPinCodeVerified(CheckPinCodeVerifiedRequest(session))
        except:
            client.sendMessage(to,"PinCode verification failed.\n\nYou entered wrong PinCode.")
            pass
    try:
        token = secondary.qrCodeLogin(QrCodeLoginRequest(session, config.SYSTEM_NAME, False))
    except:
        client.sendMessage(to,"Token requests failed.\nUser account login limit")
        pass       
    os.system("screen -S {} -X kill".format(sender))#
    os.system("cp -r {} clone-{}/{}".format(directory, directory,sender))  
    os.system('cd clone-{}/{} && echo -n "{} \c" > token.txt'.format(directory ,sender, token.accessToken))
    os.system('screen -dmS {}'.format(sender))
    os.system('screen -r {} -X stuff "cd clone-{}/{} && python3.6 {} \n"'.format(sender, directory, sender,str(file_name)))   
    settings["login"][sender] = True
    now2 = datetime.now()
    times = datetime.strftime(now2,"%X")
    days = datetime.strftime(now2,"%d/%m/%y")
    client.sendMessage(
        to,
        login.format(
            getNameByMid(sender),
            str(sender)[:25],
            str(days),
            str(times),
            "กรุณากดลิ้งด้านล่างด้วย(กดแค่ครั้งแรกพอ) :\nline://app/1602687308-GXq4Vvk9?type=text&text=「NiranamBotline」"                        
        )
    )
    return token

#=========== [ DEF ] ===========#
from qrv3.SecondaryQrCodeLoginService import Client as SecondaryService
from qrv3.ttypes import *
from qrv3.SecondaryQrCodeLoginPermitService import Client as PermitService
from qrv3.e2eeLogin import E2EELOGIN
import qrcode
def LoginSQR(to, appname_, useragent_, certi=None):
    Headersx = {
        "X-Line-Application": appname_,
        "User-Agent": useragent_
    }
    transport = THttpClient.THttpClient(config.LINE_HOST +"/acct/lgn/sq/v1")
    transport.setCustomHeaders(Headersx)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    secondary = SecondaryService(iprot=protocol)
    transport.open()
    session = secondary.createSession(LoginQrCode_CreateQrSessionRequest()).authSessionId
    e2ee = E2EELOGIN()
    qrcode = secondary.createQrCode(LoginQrCode_CreateQrCodeRequest(session)).callbackUrl + e2ee.generateParams()
    client.sendMessage(to, f"| Login qrcode |\n\n{qrcode}\n\nedited by KoHpRiW")    
#"""____________________________________"""
    Headers = {
        "X-Line-Application": appname_,
        "User-Agent": useragent_,
        "X-Lal": "en_US",
        "X-Line-Access": session
    }
    transport = THttpClient.THttpClient(config.LINE_HOST+"/acct/lp/lgn/sq/v1")
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    permit = PermitService(iprot=protocol)
    transport.open()    
#"""_____________________________________"""
    try:
        permit.checkQrCodeVerified(LoginQrCode_CheckQrCodeVerifiedRequest(session))
    except:
        traceback.print_exc()
        client.sendMessage(to, "Login error")
        pass
    try:
        secondary.verifyCertificate(LoginQrCode_VerifyCertificateRequest(session, certi))
    except:
        pincode = secondary.createPinCode(LoginQrCode_CreatePinCodeRequest(session)).pinCode
        client.sendMessage(to, f"| pin code |\n{pincode}\nedited by KoHpRiW")
        try:
            permit.checkPinCodeVerified(LoginQrCode_CheckPinCodeVerifiedRequest(session))
        except:
            traceback.print_exc()
            client.sendMessage(to, "Login error")
        pass
    try:
        result = secondary.qrCodeLogin(LoginQrCode_QrCodeLoginRequest(session, "QrV3 PROJECT", True))
    except:
        traceback.print_exc()
        client.sendMessage(to, "Login error")
    return [result.accessToken, result.certificate]
#=========== [ DEF ] ===========#

def mentionMembers2(to, mids, result):
    parsed_len = len(mids)//20+1
    mention = '@titanxasyn\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '%i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:result += f'ทั้งหมด {len(mids)} รายการ'
        if result:
            if result.endswith('\n'): result = result[:-1]
            client.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

def backupData():
    try:
        backup = BotMaker
        f = codecs.open('usermaker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)
               
def execute(op):
    try:
        timeis = time.localtime()
        theTime = time.strftime('%H:%M:%S', timeis)
        
        if op.type == 0:
            return

        if op.type in [13, 124]:
            if op.param2 in admin and op.param3 in clientMID:
                client.acceptGroupInvitation(op.param1)
        if op.type in [25, 26]:
            msg = op.message
            to = msg.to
            text = str(msg.text)
            sender = msg._from

            if msg.text is None:
                return

            if msg.text.lower().startswith(":help") or msg.text.lower().startswith("/คำสั่ง"):	
                if msg.toType != 2:
                    return
                client.sendMessage(to,Commands)

            if msg.text.lower().startswith("note") and sender in admin:	
                if msg.toType != 2:
                    return
                client.sendMessage(to,Note)

            if msg.text.lower().startswith("linux") and sender in admin:	
                if msg.toType != 2:
                    return
                client.sendMessage(to,helpLinux())

            if msg.text.lower().startswith("help:server") and sender in admin:	
                if msg.toType != 2:
                    return
                client.sendMessage(to,Servers)                  
               
            if msg.text.lower() == "sp" and sender in admin:
                if msg.toType != 2:
                    return
                start = time.time()	
                elapsed_time = time.time() - start
                tx = "{}\n".format(client.getProfile().displayName)				
                tx += "[ speed " + str(int(round((time.time() - start) * 1000)))+" ms ]"                
                client.sendMessage(to,tx)

            if msg.text.lower().startswith("runcom") and sender in admin:	
                if msg.toType != 2:
                    return
                from requests import get
                ip = get('https://api.ipify.org').text
                from pathlib import Path
                mypath = Path().absolute()
                host = os.popen('cd /etc && hostname').read()
                file = os.path.splitext(os.path.basename(__file__))[0]
                tx = ""
                tx += "🔘 bot : {}\n".format(client.getProfile().displayName)
                tx += "🔘 hostname : {}".format(host)
                tx += "🔘 ip : {}\n".format(ip)
                tx += "🔘 คำสั่งรัน :\ncd {} && python3.6 {}.py".format(mypath,file)			
                client.sendMessage(to,tx)

            if msg.text.lower().startswith("appname") and sender in admin:	
                if msg.toType != 2:
                    return
                van = "    แอปล็อคอิน :\n"+Destopwin		
                client.sendMessage(to,van)

            if msg.text.lower().startswith('cto '):
                a = msg.text.lower().replace('cto ','')
                b = a[:33]
                try:
                    client.sendContact(to, b)
                except:
                    client.sendMessage(to, "contact not found") 

            if msg.text.lower().startswith(".exec\n") and sender in admin:	
                if msg.toType != 2:
                    return
                try: exec(msg.text.split(".exec\n")[1])
                except Exception as error:
                    client.sendMessage(msg.to, str(error))

            if msg.text.lower() == "appname" or msg.text.lower() == "เช็คแอป":
                if msg.toType != 2:return
                van = "    แอปล็อคอิน :\n"+nameApp
                client.sendMessage(to,van)
     
            if msg.text.lower().startswith("forlogin") and sender in admin:	
                if msg.toType != 2:
                    return
                client.sendMessage(to,For_Login)                

            if msg.text.lower() == "ออกระบบ" or msg.text.lower() == "logout":
                if msg.toType != 2:
                    return
                if sender in settings["mid"]:
                    if settings["login"][sender] == True:
                        os.system('screen -S {} -X quit'.format(sender))
                        #os.system('rm -rf temp_login/{}'.format(sender))#ออกและลบไฟล์                        
                        now2 = datetime.now()
                        times = datetime.strftime(now2,"%X")
                        days = datetime.strftime(now2,"%d/%m/%y")
                        client.sendMessage(
                            to,
                            logout.format(
                                getNameByMid(sender),
                                str(sender)[:25],
                                str(days),
                                str(times)
                            )
                        )
                        settings["login"][sender] = False
                    else:
                        client.sendMessage(to,"You are not login selfbot!")
                else:
                    client.sendMessage(
                        to,
                        Warning.format(
                            getNameByMid(sender),
                            str(sender)[:25]
                        )
                    )

            if msg.text.lower() == "login4":
                if msg.toType != 2:
                    return
                if sender in settings["mid"]:
                    if settings["login"][sender] == False:
                        client.sendMessage(to, "Checking database")
                        data = livejson.File("user_list/%s.json" % sender)
                        if "certificate" not in data:
                            data["certificate"] = ""
                        if data["certificate"] == "":
                            res = LoginWithSecondary(to, sender,"login4", "staff15.py")#staff14newtalk.py
                            data["certificate"] = res.certificate
                        else:
                            LoginWithCertificate(to, sender, "login4", "staff15.py", data["certificate"])#staff14newtalk.py
                    else:
                        client.sendMessage(to,"You have already login selfbot♪")
                else:
                    client.sendMessage(to,Warning.format(getNameByMid(sender),str(sender)[:25])) 

            if msg.text.lower() == "login6":
                if msg.toType != 2:
                    return
                if sender in settings["mid"]:
                    if settings["login"][sender] == False:
                        client.sendMessage(to, "Checking database")
                        data = livejson.File("user_list/%s.json" % sender)
                        if "certificate" not in data:
                            data["certificate"] = ""
                        if data["certificate"] == "":
                            res = LoginWithSecondary(to, sender,"chromebek", "sbkoh5.py")#sbkoh4.py
                            data["certificate"] = res.certificate
                            client.sendMessage(to, "กรุณากดลิ้งด้านล่างอีกครั้ง(กดแค่ครั้งแรกพอ) :\n\nline://app/1647207293-rNJ7MlJm?type=text&text=โก้พริ้วหล่อที่สุดใน3โลก")
                        else:
                            LoginWithCertificate(to, sender, "chromebek", "sbkoh5.py", data["certificate"])#sbkoh4.py
                            client.sendMessage(to, "กรุณากดลิ้งด้านล่างอีกครั้ง(กดแค่ครั้งแรกพอ) :\n\nline://app/1647207293-rNJ7MlJm?type=text&text=โก้พริ้วหล่อที่สุดใน3โลก")
                    else:
                        client.sendMessage(to,"You have already login selfbot♪")
                else:
                    client.sendMessage(to,Warning.format(getNameByMid(sender),str(sender)[:25]))                     

            if msg.text.lower() == "loginself":
                if msg.toType != 2:
                    return
                if sender in settings["mid"]:
                    if settings["login"][sender] == False:
                        client.sendMessage(to, "Checking database")
                        data = livejson.File("user_list/%s.json" % sender)
                        if "certificate" not in data:
                            data["certificate"] = ""
                        if data["certificate"] == "":
                            res = LoginWithSecondary(to, sender,"selfbot", "maink1.py")#staff14newtalk.py
                            data["certificate"] = res.certificate
                        else:
                            LoginWithCertificate(to, sender, "selfbot", "maink1.py", data["certificate"])#staff14newtalk.py
                    else:
                        client.sendMessage(to,"You have already login selfbot♪")
                else:
                    client.sendMessage(to,Warning.format(getNameByMid(sender),str(sender)[:25]))

            if msg.text.lower() == "certificate reset":
               if sender in settings["mid"]:
                   data = livejson.File("user_list/%s.json" % sender)
                   if data["certificate"] != "":
                       data["certificate"] = ""
                       client.sendMessage(to,"Reset Certificate Success")
                   else:
                       client.sendMessage(to,"certificate is not defined")
                       
            if msg.text.lower().startswith("addsb ") and sender in admin:
                if msg.toType != 2:
                    return
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    if key1 not in settings["mid"]:
                        settings["mid"].append(key1)
                        settings["login"][key1] = False
                        now2 = datetime.now()
                        times = datetime.strftime(now2,"%X")
                        days = datetime.strftime(now2,"%d/%m/%y")
                        client.sendMessage(
                            to,
                            NewUser.format(
                                getNameByMid(key1),
                                str(key1)[:25],
                                str(days),
                                str(times)
                            )
                        )
                    else:
                        client.sendMessage(to,"「 AddUser 」\nUser : {}\nAlready in database\nCan use the command to login".format(getNameByMid(key1)))
   
            if msg.text.lower().startswith("delsb ") and sender in admin:
                if msg.toType != 2:
                    return
                if 'MENTION' in msg.contentMetadata.keys()!= None:
                    key = eval(msg.contentMetadata["MENTION"])
                    key1 = key["MENTIONEES"][0]["M"]
                    if key1 in settings["mid"]:
                        settings["mid"].remove(key1)
                        os.system("screen kill {}".format(getNameByMid(key1)))
                        now2 = datetime.now()
                        times = datetime.strftime(now2,"%X")
                        days = datetime.strftime(now2,"%d/%m/%y")
                        client.sendMessage(
                            to,
                            DeletedUser.format(
                                getNameByMid(key1),
                                str(key1)[:25],
                                str(days),
                                str(times)
                            )
                        )
                    else:
                        client.sendMessage(to,"「 DelteleUser 」\nUser : {} Not in database".format(getNameByMid(key1)))

#=========== [ COMMAND ] ===========#
            if msg.text.lower().startswith("login") and sender in client.getAllContactIds():	
                if msg.toType != 2:
                    return
                split = msg.text.split(" ")
                auth = ""
                cert = "" 
                if "destopwin" == str(split[1]):
                    client.sendMessage(to, "test login!!")
                    appname_ = Destopwin
                    agent_ = appname_.split("\t")[1]
                    useragent_ = "Line/t{}".format(agent_)
                    client.sendMessage(to, f"Appname: {appname_}\nUseragent: Line/{agent_}")
                    if sender in settings["mid"]:
                        if settings["login"][sender] == False:
                            client.sendMessage(to, "Checking database")
                            data = livejson.File("user_list/%s.json" % sender)
                            if "certificate" not in data:
                                args = LoginSQR(to, appname_, useragent_)
                                cert,auth = args[1],args[0]
                                with open('dataSb/{}.txt'.format(sender), 'a') as c:
                                    c.write("{}".format(auth))
                                data["certificate"] = str(cert)
                            else:
                                certi_  = str(data["certificate"])
                                args = LoginSQR(to, appname_, useragent_, certi=certi_)
                                cert,auth  = str(data["certificate"]),args[0]
                                with open('dataSb/{}.txt'.format(sender), 'a') as c:
                                    c.write("{}".format(auth))
                            client.sendMessage(to, f"accessToken: {auth}\ncertificate: {cert}\nAppname: {appname_}\nUseragent: Line/{useragent_}")
                            os.system("screen -S {} -X quit".format(msg._from))
                            os.system('screen -dmS {}'.format(msg._from))
                            os.system('screen -r {} -X stuff "python3.6 selfbot.py {}\n"'.format(msg._from, msg._from,msg._from))
                            client.sendMention(to,"User @!\nLogin success...\nPlease allow liff : line://app/1602687308-GXq4Vvk9 ",[msg._from])
                            return
                        else:
                            client.sendMessage(to,"You have already login selfbot♪")
                    else:
                        client.sendMessage(to,Warning.format(getNameByMid(sender),str(sender)[:25])) 
                if "window" == str(split[1]):
                    client.sendMessage(to, "test login window")
                    appname_ = HeadDestopWin()
                    useragent_ = appname_.split("\t")[1]
                    args = LoginSQR(to, appname_, useragent_)
                    accessToken = args[0]
                    certificate = args[1]
                    tx  = f"Appname: {appname_}"+"\n"
                    tx += f"Useragent: Line/{useragent_}"+"\n"
                    tx += f"AccessToken: \n{accessToken}"+"\n"
                    tx += f"Certificate: \n{certificate}"+""
                    client.sendMessage(to, tx)
                    return
                        
            if msg.text.lower().startswith("delusernumber "):
                if sender in admin or sender in clientMID:
                    sep = msg.text.split(" ")[1]
                    duser = settings["mid"][int(sep)-1]
                    settings["mid"].remove(duser)
                    client.sendMessage(to,"DeleteUserNumber {} Success".format(str(sep)))
                     
            if msg.text.lower().startswith("checkuser"):
                if msg.toType != 2:
                    return
                if sender in admin or sender in client.profile.mid:
                    if settings["mid"] == []:
                        client.sendMessage(to,"Not Found")
                    else:
                        ls = ""
                        nums = 1
                        for us in settings["mid"]:
                            try:
                                ls += "{}. {}\n".format(str(nums),str(getNameByMid(us)))
                                nums = nums+1
                            except TalkException as e:
                                if "code=3" in str(e):
                                    ls += "{}. User deleted account\n".format(str(nums))
                                    nums = nums+1
                        client.sendMessage(to,"「 ListUser 」\n"+ls+"\n「 Total {} User 」".format(len(settings["mid"])))
#== [SERVERS] ==#
            if msg.text.lower() == "check:screen" or msg.text.lower() == "screen":           
                if msg.toType != 2:
                    return
                if sender in admin or sender in client.profile.mid:
                    process = os.popen('screen -list')
                    a = process.read()
                    client.sendMessage(to, "╭━━━━[「ɴɪʀᴀɴᴀᴍ ʙᴏᴛ」]━━━━╮\n\n{}\n╰━━━━━━━━━━━━━━━━━╯".format(a))
                    process.close()

            if msg.text.lower().startswith("userfile"):
                if msg.toType != 2:
                    return
                if sender in admin:
                    if settings["mid"] == []:
                        client.sendMessage(to,"Not Found")
                    else:
                        ls = ""
                        nums = 1
                        for us in settings["mid"]:
                            try:
                                ls += "{}. {}\n".format(str(nums),str(getNameByMid(us)))
                                nums = nums+1
                            except TalkException as e:
                                if "code=3" in str(e):
                                    ls += "{}. User deleted account\n".format(str(nums))
                                    nums = nums+1
                        client.sendMessage(to,"「 ListUser_File 」\n"+ls+"\n• killuser (num)\n• resetuser (user & file)\n\n「 Total {} UserFile 」".format(len(settings["mid"])))               

            if msg.text.lower() == "botgroups":           
                if msg.toType != 2:
                    return
                if sender in admin:
                    groups = client.groups
                    ret_ = "╭──[ กลุ่มที่บอทอยู่ ]"
                    no = 1                     
                    for gid in groups:
                        group = client.getGroup(gid)
                        ret_ += "\n│ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                        no = no+1                        
                    ret_ += "\n╰──[ จำนวน {} กลุ่ม ]".format(str(len(groups)))
                    k = len(ret_)//10000
                    for aa in range(k+1):
                        client.sendMessage(to,'{}'.format(ret_[aa*10000 : (aa+1)*10000])) 

            if msg.text.lower().startswith("killuser "):
                if sender in admin:
                    sep = msg.text.split(" ")[1]
                    duser = settings["mid"][int(sep)-1]
                    settings["mid"].remove(duser)
                    settings["login"][duser] = False                    
                    os.system('screen -S {} -X quit'.format(duser))
                    os.system('rm -rf clone-login4/{}'.format(duser))
                    #os.system('screen -S {} -X quit'.format(duser))
                    #os.system('rm -rf clone-loginsb03/{}'.format(duser))
                    nameduser = client.getContact(duser).displayName                                                          
                    client.sendMessage(to,"DeleteUserFile\nNumber : {}\nName : {}\nId : {}".format(str(sep),nameduser,duser))
                    client.sendContact(to,duser)
#== [ resetuser ] ==#
            if msg.text.lower() == "resetuser":           
                if msg.toType != 2:
                    return
                if sender in admin:
                    if settings["mid"] == []:
                        client.sendMessage(to,"Not Found")
                    else:         
                        client.sendMessage(to,"Wait..")
                        ls = "Remove User\n"                        
                        nums = 1
                        for us in settings["mid"]:
                            #ls += "\n\n•{}".format(us)#mid
                            try:
                                ls += "{}. {}\n".format(str(nums),str(getNameByMid(us)))
                                nums = nums+1
                            except TalkException as e:
                                if "code=3" in str(e):
                                    ls += "{}. User deleted account\n".format(str(nums))
                                    nums = nums+1                         
                            os.system('screen -S {} -X quit'.format(us)) 
                            os.system('rm -rf clone-login4/{}'.format(us))
                            os.system('screen -S {} -X quit'.format(us))                         
                        os.system('rm -rf clone-login4') 
                        #os.system('rm -rf clone-loginsb03') 
                        #print("⛔️remove\nclone-login4\nclone-loginsb03")
                        #time.sleep(5)
                        os.system('mkdir clone-login4')
                        
                        os.system('rm -rf clone-chromebek') 
                        os.system('mkdir clone-chromebek')
                        #os.system('mkdir clone-loginsb03') 
                       # print("☑️make directory\nclone-login4\nclone-loginsb03")  

                        os.system('rm -rf clone-selfbot') 
                        os.system('mkdir clone-selfbot')                       
                        ls += "\n「 Delete {} User 」".format(len(settings["mid"]))
                        client.sendMessage(to,ls)   
                        settings["mid"] = []
                        settings["login"] = {}                        
                        if sender not in settings["mid"]:
                            settings["mid"].append(sender)            
                        settings["login"] = {sender: False} 					
#== [SERVERS] ==#
            if msg.text.lower() == "botleave":
                if sender in admin:
                    if msg.toType != 2:
                        return
                    #client.deleteSelfFromChat(to)
                    client.leaveGroup(to)
            if msg.text.lower() == "botreboot":
                if sender in admin:
                    if msg.toType != 2:
                        return
                    client.sendMessage(to,"กำลังรีบอท....")
                    restartBot()

        if op.type == 25:
            print ("[ 25 ]["+theTime+"] NOTIFIED SEND MESSAGE")
            backupData()
                    
        #backupData()                  
    except TalkException as talk_error:
        import traceback
        trace = talk_error.__traceback__
        print("Error Line: "+str(trace.tb_lineno)+"\nError: "+str(talk_error))

def nameUpdate():
    while True:
        try:
            if times["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                client.updateProfileAttribute(2,times["name"] + nowT)
            time.sleep(120)
        except TalkException as talk_error:
            trace = talk_error.__traceback__
            print("Error Line: "+str(trace.tb_lineno)+"\nError: "+str(talk_error))

#threading.Thread(target=generateName, args=(peoplesian,)).start()
threading.Thread(target=nameUpdate).start()

#threading.Thread(target=DISPLAY_NAME).start()

while True:
    try:
        ops = clientPoll.singleTrace(count=50)
        if ops != None:
            for op in ops:
                threading.Thread(target=execute,args=(op,)).start()
                clientPoll.setRevision(op.revision)
    except TalkException as talk_error:
        import traceback
        trace = talk_error.__traceback__
        print("Error Line: "+str(trace.tb_lineno)+"\nError: "+str(talk_error))