from qrv3.SecondaryQrCodeLoginService import Client as SecondaryService
from qrv3.ttypes import *
from qrv3.SecondaryQrCodeLoginPermitService import Client as PermitService
from qrv3.e2eeLogin import E2EELOGIN
import qrcode

#============================#
def HeadDestopWin():
	destopwin =["DESKTOPWIN\t6.6.0\tPC-nhTURp\t8.1","DESKTOPWIN\t6.3.2\tPC-4jVXmD\t8","DESKTOPWIN\t6.3.0\tPC-VELBlO\t7","DESKTOPWIN\t6.2.2\tPC-t3RE6S\t7","DESKTOPWIN\t6.5.2\tPC-Xrsx0c\t7","DESKTOPWIN\t6.0.3\tPC-zMfqiu\t8.1","DESKTOPWIN\t6.5.2\tPC-9R8KfN\t10","DESKTOPWIN\t6.6.0\tPC-SfTWbi\t8","DESKTOPWIN\t6.6.0\tPC-1jYwov\t10","DESKTOPWIN\t6.5.2\tPC-NgVvFS\t8.1","DESKTOPWIN\t6.1.1\tPC-faVx7A\t10","DESKTOPWIN\t6.1.1\tPC-4-EJQ3\t8.1","DESKTOPWIN\t6.3.0\tPC-eDOdSs\t10","DESKTOPWIN\t6.0.3\tPC-NOFrK8\t10","DESKTOPWIN\t6.2.2\tPC-BRXKxa\t8.1","DESKTOPWIN\t6.2.2\tPC-kkZShM\t8","DESKTOPWIN\t6.3.0\tPC-zGCyxg\t8.1","DESKTOPWIN\t6.3.2\tPC-SUYQVF\t10","DESKTOPWIN\t6.1.1\tPC-cAEFoc\t7","DESKTOPWIN\t6.5.2\tPC-XXgNwb\t8","DESKTOPWIN\t6.2.2\tPC-a-xT84\t10","DESKTOPWIN\t6.3.0\tPC-5QBUtX\t8","DESKTOPWIN\t6.3.2\tPC-35XfXF\t7","DESKTOPWIN\t6.1.1\tPC-65IdH8\t8","DESKTOPWIN\t6.6.0\tPC-eZyJgZ\t7","DESKTOPWIN\t6.0.3\tPC-UYKwN8\t8","DESKTOPWIN\t6.3.2\tPC-RX1IJe\t8.1","DESKTOPWIN\t6.0.3\tPC-deAVK5\t7"]
	return random.choice(destopwin)
Destopwin = HeadDestopWin() 
def HeadSysWindows():
	syswindows =["DESKTOPWIN\t7.5.0\tWindows4\t10","DESKTOPWIN\t7.3.1\tWindows1\t10","DESKTOPWIN\t7.4.0\tWindows11\t10","DESKTOPWIN\t6.2.0\tWindows2\t10","DESKTOPWIN\t7.3.0\tWindows3\t10","DESKTOPWIN\t7.2.0\tWindows10\t10","DESKTOPWIN\t6.3.2\tWindows9\t10","DESKTOPWIN\t6.5.4\tWindows8\t10","DESKTOPWIN\t6.6.0\tWindows7\t10","DESKTOPWIN\t6.7.0\tWindows6\t10","DESKTOPWIN\t6.7.2\tWindows5\t10","DESKTOPWIN\t7.7.0\tWindows12\t10","DESKTOPWIN\t7.8.0\tWindows13\t10","DESKTOPWIN\t7.9.0\tWindows14\t10","DESKTOPWIN\t7.10.1\tWindows15\t10","DESKTOPWIN\t6.2.1\tWindows16\t10","DESKTOPWIN\t6.2.2\tWindows17\t10","DESKTOPWIN\t6.2.1\tWindows18\t10","DESKTOPWIN\t6.3.0\tWindows19\t10","DESKTOPWIN\t6.5.0\tWindows20\t10","DESKTOPWIN\t6.5.2\tWindows21\t10","DESKTOPWIN\t6.7.1\tWindows22\t10","DESKTOPWIN\t7.0.0\tWindows23\t10","DESKTOPWIN\t6.5.4.2441\tWindows24\t10","DESKTOPWIN\t6.5.2.2431\tWindows25\t10"]
	return random.choice(syswindows)
Syswindows = HeadSysWindows()

#============================#
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
#============================#

#=========== [ DEF ] ===========#
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
"""____________________________________"""
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
"""_____________________________________"""
    transport.open()
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