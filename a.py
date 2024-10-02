#!usr/bin/python
# -*- coding: utf-8 -*-
from important import *
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
import schedule, qrcode, openai
from minzrestapi import *
from lib.qrv3.SecondaryQrCodeLoginService import Client as SecondaryService
from lib.qrv3.ttypes import *
from lib.qrv3.SecondaryQrCodeLoginPermitService import Client as PermitService
from lib.qrv3.e2eeLogin import E2EELOGIN
from lib.thrift.protocol import TCompactProtocol, TBinaryProtocol, TProtocol
from lib.thrift.transport import THttpClient, TTransport
from lib.thrift.Thrift import TProcessor
from lib.linepy.server import Server as config

minz_api = MinzRestApi("INDEAR")


def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open("tmp/errors/%s.txt" % errid, "w") if write else None
    if args.traceback:
        traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open("tmp/errorLog.txt", "a") as e:
            e.write("\n%s : %s" % (errid, str(error)))
    print("\033[1;32m++ Error : {error}\033[0m".format(error=error))


# Setup Argparse
parser = argparse.ArgumentParser(description="Selfbot Self Bot")
parser.add_argument(
    "-t",
    "--token",
    type=str,
    metavar="",
    required=False,
    help="Token | Example : Exxxx",
)
parser.add_argument(
    "-e",
    "--email",
    type=str,
    default="",
    metavar="",
    required=False,
    help="Email Address | Example : example@xxx.xx",
)
parser.add_argument(
    "-p",
    "--passwd",
    type=str,
    default="",
    metavar="",
    required=False,
    help="Password | Example : xxxx",
)
parser.add_argument(
    "-a",
    "--apptype",
    type=str,
    default="",
    metavar="",
    required=False,
    choices=list(ApplicationType._NAMES_TO_VALUES),
    help="Application Type | Example : CHROMEOS",
)
parser.add_argument(
    "-s",
    "--systemname",
    type=str,
    default="",
    metavar="",
    required=False,
    help="System Name | Example : Chrome_OS",
)
parser.add_argument(
    "-c",
    "--channelid",
    type=str,
    default="",
    metavar="",
    required=False,
    help="Channel ID | Example : 1341209950",
)
parser.add_argument(
    "-T",
    "--traceback",
    type=str2bool,
    nargs="?",
    default=False,
    metavar="",
    required=False,
    const=True,
    choices=[True, False],
    help="Using Traceback | Use : True/False",
)
parser.add_argument(
    "-S",
    "--showqr",
    type=str2bool,
    nargs="?",
    default=False,
    metavar="",
    required=False,
    const=True,
    choices=[True, False],
    help="Show QR | Use : True/False",
)
args = parser.parse_args()

# Login Client
listAppType = ["DESKTOPWIN"]
try:
    print("\033[1;32m##----- LOGIN CLIENT -----##\033[0m")
    line = None
    for appType in listAppType:
        tokenPath = Path("authToken.txt")
        if tokenPath.exists():
            tokenFile = tokenPath.open("r")
        else:
            tokenFile = tokenPath.open("w+")
        savedAuthToken = tokenFile.read().strip()
        authToken = savedAuthToken if savedAuthToken and not args.token else args.token
        idOrToken = authToken if authToken else args.email
        try:
            # line = LINE(idOrToken, args.passwd, appType=appType) #login qr/token
            line = LINE(
                "concoursecharismarkbmhx6@gmail.com", "Chrome112233$", appType=appType
            )  # login email
            tokenFile.close()
            tokenFile = tokenPath.open("w+")
            tokenFile.write(line.authToken)
            tokenFile.close()
            break
        except TalkException as talk_error:
            print(
                "\033[1;32m++ Error : %s\033[0m" % talk_error.reason.replace("_", " ")
            )
            if args.traceback:
                traceback.print_tb(talk_error.__traceback__)
            if talk_error.code == 1:
                continue
            sys.exit(1)
        except Exception as error:
            logError(error)
            if args.traceback:
                traceback.print_tb(error.__traceback__)
            sys.exit(1)
except Exception as error:
    logError(error)
    if args.traceback:
        traceback.print_tb(error.__traceback__)
    sys.exit(1)

if not line:
    sys.exit("\033[1;32m##----- LOGIN FAILED (Client) -----##\033[0m")

oepoll = OEPoll(line)

programStart = time.time()
owner = [
    "ULqXghNr7OquqsMZ5MJrIRNCRupxu66v1WXLbIKo5KBY",
    "CUjUzgJ4ZC2S9PfzlzIcRuPQ7KQLtjONI5DGhLPTWigc",
    "UTYprRZ-y7JJEQbVeV4PSKRve6pHjcxfsdGxZLieRbUE",
]

bool_dict = {
    True: ["Yes", "Active", "Success", "Open", "ON"],
    False: ["No", "Not Active", "Failed", "Close", "OFF"],
}


def mentionMembers(to, mids=[], sort=False, **kwargs):
    if line.profile.mid in mids:
        mids.remove(line.profile.mid)
    if sort:
        mids = sorted(mids, key=lambda name: line.getContact(name).displayName.lower())
    result = "𝗠𝗲𝗻𝘁𝗶𝗼𝗻 𝗔𝗹𝗹 𝗠𝗲𝗺𝗯𝗲𝗿𝘀\n"
    for i in range(0, len(mids), 20):
        target = []
        for no, mid in enumerate(mids[i : i + 20], i + 1):
            result += "➡️ › @!\n"
            if mid == mids[-1]:
                result += "𝗧𝗼𝘁𝗮𝗹: %i 𝗠𝗲𝗺𝗯𝗲𝗿𝘀" % len(mids)
            target.append(mid)
        if target:
            if result.endswith("\n"):
                result = result[:-1]
            line.sendMention(to, result, target)
        result = ""


def command(text):
    pesan = text.lower()
    if line.settings["setKey"]["status"]:
        if pesan.startswith(line.settings["setKey"]["key"]):
            cmd = pesan[len(line.settings["setKey"]["key"]) :]
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd


def removeCmd(text, key=""):
    if key == "":
        setKey = (
            ""
            if not line.settings["setKey"]["status"]
            else line.settings["setKey"]["key"]
        )
    else:
        setKey = key
    text_ = text[len(setKey) :]
    sep = text_.split(" ")
    return text_[len(sep[0] + " ") :]


def timeChange(secs):
    mins, secs = divmod(secs, 60)
    hours, mins = divmod(mins, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    months, weeks = divmod(weeks, 4)
    text = ""
    if months != 0:
        text += "%02d Bulan" % (months)
    if weeks != 0:
        text += " %02d minggu" % (weeks)
    if days != 0:
        text += " %02d hari" % (days)
    if hours != 0:
        text += " %02d jam" % (hours)
    if mins != 0:
        text += " %02d menit" % (mins)
    if secs != 0:
        text += " %02d detik" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text


def make_list(dict):
    data = list(dict)
    return data


def clearcache():
    a = os.popen("sync; echo 3 > /proc/sys/vm/drop_caches").read()
    b = os.popen("cd ../../ && cd tmp && rm *.bin").read()


def restartProgram():
    print("\033[1;32m##----- PROGRAM RESTARTED -----##\033[0m")
    python = sys.executable
    os.execl(python, python, *sys.argv)


def getExpired(userTime):
    waktu = userTime - time.time()
    minu = int(waktu / 60 % 60)
    hours = int(waktu / 60 / 60 % 24)
    days = int(waktu / 60 / 60 / 24)
    expiredDate = datetime.fromtimestamp(
        userTime, tz=pytz.timezone("Asia/Jakarta")
    ).strftime("%d-%m-%Y")
    text = ""
    if days != 0:
        text += " %02d day" % (days)
    if hours != 0:
        text += " %02d hours" % (hours)
    if minu != 0:
        text += " %02d minute" % (minu)
    if text[0] == " ":
        text = text[1:]
    return f"Expired\n  • Date: {expiredDate}\n  • {text}"


def createQRCode(
    url, back_color="white", fill_color="black", logo_path=None, saveAs=""
):
    if logo_path is not None:
        logo = Image.open(logo_path).convert("RGBA")
        wpercent = 100 / float(logo.size[0])
        hsize = int((float(logo.size[1]) * float(wpercent)))
        logo = logo.resize((100, hsize), Image.LANCZOS)
        QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        QRcode.add_data(url)
        QRcode.make()
        QRimg = QRcode.make_image(fill_color=fill_color, back_color=back_color).convert(
            "RGBA"
        )
        pos = ((QRimg.size[0] - logo.size[0]) // 2, (QRimg.size[1] - logo.size[1]) // 2)
        QRimg.paste(logo, pos, logo)

        if saveAs == "":
            QRimg.save("qr_code.png")
            return "qr_code.png"
        else:
            QRimg.save(saveAs)
            return saveAs
    else:
        QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
        QRcode.add_data(url)
        QRcode.make()
        QRimg = QRcode.make_image(fill_color=fill_color, back_color=back_color).convert(
            "RGB"
        )

        if saveAs == "":
            QRimg.save("qr_code.png")
            return "qr_code.png"
        else:
            QRimg.save(saveAs)
            return saveAs


def LoginSQRv2(msg, appname_, useragent_, certificate=None):
    to = msg.to
    filetext = open(f"countrytext.txt", "r").read()
    city = filetext.split("\n")
    system = random.choice(city)
    Headersx = {"X-Line-Application": appname_, "User-Agent": useragent_}
    transport = THttpClient.THttpClient(config.LINE_HOST_DOMAIN + "/acct/lgn/sq/v1")
    transport.setCustomHeaders(Headersx)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    secondary = SecondaryService(iprot=protocol)
    transport.open()
    session = secondary.createSession(
        LoginQrCode_CreateQrSessionRequest()
    ).authSessionId
    e2ee = E2EELOGIN()
    qrcode_link = (
        secondary.createQrCode(LoginQrCode_CreateQrCodeRequest(session)).callbackUrl
        + e2ee.generateParams()
    )
    line.sendMessage(msg.to, f"{appname_}\nLine/{useragent_}\n\n{qrcode_link}")
    img = qrcode.make(qrcode_link)
    img.save("qr.png")
    try:
        line.sendReplyImage(msg.to, "qr.png", msgIds=msg.id)
    except:
        line.sendReplyImage(msg.to, "qr.png", msgIds=msg.id)
    os.system("rm -rf qr.png")
    Headers = {
        "X-Line-Application": appname_,
        "User-Agent": useragent_,
        "X-Lal": "en_US",
        "X-Line-Access": session,
    }
    transport = THttpClient.THttpClient(config.LINE_HOST_DOMAIN + "/acct/lp/lgn/sq/v1")
    transport.setCustomHeaders(Headers)
    protocol = TCompactProtocol.TCompactProtocol(transport)
    permit = PermitService(iprot=protocol)
    transport.open()
    permit.checkQrCodeVerified(LoginQrCode_CheckQrCodeVerifiedRequest(session))
    try:
        secondary.verifyCertificate(
            LoginQrCode_VerifyCertificateRequest(session, certificate)
        )  #
    except:
        pincode = secondary.createPinCode(
            LoginQrCode_CreatePinCodeRequest(session)
        ).pinCode
        line.sendMessage(msg.to, f"pin code: \n{pincode}")
        permit.checkPinCodeVerified(LoginQrCode_CheckPinCodeVerifiedRequest(session))
    result = secondary.qrCodeLogin(
        LoginQrCode_QrCodeLoginRequest(session, f"Elfox live in {system}", True)
    )
    # elfox.sendMessage(msg.to,result.accessToken)
    return [result.accessToken, result.certificate]


def loginEmail(to, sender, user, app_type, emailx, passx):
    if line.settings["list"][user]["token"][app_type] != "":
        try:
            test_token = LINE(
                line.settings["list"][user]["token"][app_type], appType=app_type
            )
            if test_token:
                print("token not expired")
        except:
            line.settings["list"][user]["token"][app_type] = ""
            line.sendMessage(
                to, "Authtoken Expired, trying to get new QR code wait a minute"
            )
    try:
        base_url = "https://jvrestapi.site"
        email = emailx
        passwd = passx
        randomName = "".join(random.choice("0123456789") for i in range(6))
        win = f"DESKTOPWIN\t8.6.0.3277\tWINDOWS\t10.{randomName}"
        sysname = "WINDOWS"
        apikey = "ahamad"
        cert = None
        proxy = None
        logemail = "/lineemailV2"
        etoken = "/etokenV2"
        e2eeloc = "jv"
        params1 = {
            "appname": win,
            "sysname": sysname,
            "apikey": apikey,
            "cert": cert,
            "proxy": proxy,
            "email": email,
            "passwd": passwd,
        }
        reqpin = requests.post(base_url + logemail, params=params1).json()
        if reqpin["status"] == 200:
            pin = reqpin["result"]["pin"]
            line.sendMessage(to, f"pin code: \n{pin}")
            params2 = {"apikey": apikey}
            reqtoken = requests.post(base_url + etoken, params=params2).json()
            if reqtoken["status"] == 200:
                authToken = reqtoken["result"]["authToken"]
                certificate = reqtoken["result"]["cert"]
                line.settings["list"][user]["cert"] = certificate
                line.settings["list"][user]["token"][app_type] = authToken
        line.settings["listLogin"][sender] = "%s" % user
        os.system("cp -r mibot {}".format(user))
        if not line.settings["list"][user]["folderStatus"]:
            os.system("cd jsonUser && mkdir {}".format(user))
            line.settings["list"][user]["folderStatus"] = True
        else:
            os.system("cd {} && rm -rf json".format(user))
            os.system("cd jsonUser && cd {} && mv json ../../{}".format(user, user))
        if line.settings["list"][user]["ajs"]:
            if line.settings["list"][user]["token"]["antijs"] != "":
                os.system(
                    'cd {} && echo -n "{}" > tokenAjs.txt'.format(
                        user, line.settings["list"][user]["token"]["antijs"]
                    )
                )
            else:
                return line.sendMessage(to, "Invalid antijs account, token not found!")
        os.system(
            'cd {} && echo -n "{}" > authToken.txt'.format(
                user, line.settings["list"][user]["token"][app_type]
            )
        )
        os.system("screen -dmS {}".format(user))
        time.sleep(0.5)
        if line.settings["list"][user]["ajs"]:
            os.system(
                'screen -r {} -X stuff "cd {} && python3 ajs.py \n"'.format(user, user)
            )
        else:
            os.system(
                'screen -r {} -X stuff "cd {} && python3 a.py \n"'.format(user, user)
            )
        line.sendMessage(
            to,
            "Login Successful!\n\nType `Help` to see commands\nType `MyStatus` to see your expired time",
        )
    except Exception as e:
        if str(e) == "LINE 9201":
            line.sendMessage(
                to,
                "LINE v9.20.1 detected!!!\n\n1. Update LINE ke versi selain v9.20.1\n\n2. Login SELFBOT\n\n3. Jika login berhasil, anda dapat mengganti LINE ke v9.20.1 kembali",
            )
        else:
            line.sendMessage(to, str(e))


def loginSelfbot(msg, to, sender, user, app_type, msg_id, api_provider="elfox"):
    if line.settings["list"][user]["token"][app_type] != "":
        try:
            test_token = LINE(
                line.settings["list"][user]["token"][app_type], appType=app_type
            )
            if test_token:
                print("token not expired")
        except:
            line.settings["list"][user]["token"][app_type] = ""
            line.sendMessage(
                to, "Authtoken Expired, trying to get new QR code wait a minute"
            )
    try:
        params = {
            "appType": app_type,
            "appVer": line.server.APP_VERSION[app_type],
            "sysName": "Sozi",
            "sysVer": line.server.SYSTEM_VERSION[app_type],
            "cert": None,
            "apikey": "INDEAER",
        }
        if line.settings["list"][user]["token"][app_type] == "":
            if line.settings["list"][user]["cert"] != "":
                params["cert"] = line.settings["list"][user]["cert"]

            if api_provider == "elfox":
                try:
                    randomName = "".join(random.choice("0123456789") for i in range(6))
                    win = f"DESKTOPWIN\t8.6.0.3277\tWINDOWS\t10.{randomName}"
                    token, cert = LoginSQRv2(
                        msg, win, "Mozilla/5.0 (X11; Linux x86_64) Chrome/51.0.2704.106"
                    )
                    line.settings["list"][user]["cert"] = cert
                    line.settings["list"][user]["token"][app_type] = token
                except Exception as e:
                    print(e)
                    raise Exception("ErOR")

        line.settings["listLogin"][sender] = "%s" % user
        os.system("cp -r mibot {}".format(user))
        if not line.settings["list"][user]["folderStatus"]:
            os.system("cd jsonUser && mkdir {}".format(user))
            line.settings["list"][user]["folderStatus"] = True
        else:
            os.system("cd {} && rm -rf json".format(user))
            os.system("cd jsonUser && cd {} && mv json ../../{}".format(user, user))
        if line.settings["list"][user]["ajs"]:
            if line.settings["list"][user]["token"]["antijs"] != "":
                os.system(
                    'cd {} && echo -n "{}" > tokenAjs.txt'.format(
                        user, line.settings["list"][user]["token"]["antijs"]
                    )
                )
            else:
                return line.sendMessage(to, "Invalid antijs account, token not found!")
        os.system(
            'cd {} && echo -n "{}" > authToken.txt'.format(
                user, line.settings["list"][user]["token"][app_type]
            )
        )
        os.system("screen -dmS {}".format(user))
        time.sleep(0.5)
        if line.settings["list"][user]["ajs"]:
            os.system(
                'screen -r {} -X stuff "cd {} && python3 ajs.py \n"'.format(user, user)
            )
        else:
            os.system(
                'screen -r {} -X stuff "cd {} && python3 a.py \n"'.format(user, user)
            )
        line.sendMessage(
            to,
            "Login Successful!\n\nType `Help` to see commands\nType `MyStatus` to see your expired time",
        )
    except Exception as e:
        if str(e) == "LINE 9201":
            line.sendMessage(
                to,
                "LINE v9.20.1 detected!!!\n\n1. Update LINE ke versi selain v9.20.1\n\n2. Login SELFBOT\n\n3. Jika login berhasil, anda dapat mengganti LINE ke v9.20.1 kembali",
            )
        else:
            line.sendMessage(to, str(e))


from lib_token import *
from sms_active import *

line.reg_auto = False
line.tokenlist = []


def reg_auto(to, qty):
    cl = line
    region = "ID"
    kodenomer = "6"
    attempt = 0
    human = 0

    try:
        pushAuto(cl, ["reset"])
    except:
        pass

    while True:
        try:
            attempt += 1
            pinfail = False

            print(f"[ REG AUTO ] ATTEMP {attempt}")

            display_name = generateName()

            result = generatePhoneNumber(kodenomer)
            phoneNumber = result["number"]

            print(f"[ REG AUTO ] NUMBER : {phoneNumber}")
            pushAuto(cl, ["new", phoneNumber, region])

            print(f"[ REG AUTO ] WAITING PINCODE...")
            pin = "NONE"

            for x in range(13):
                time.sleep(5)
                st = getPhonePincode(result["otpid"])
                if st["status"] == "STATUS_OK":
                    pin = st["otp"]
                    break
                elif st["status"] == "STATUS_CANCEL":
                    break

            if pin == "NONE":
                cancelActivation(result["otpid"])
                raise Exception("GET PIN FAILED")
            else:
                completeActivation(result["otpid"])

            print(f"[ REG AUTO ] PINCODE : " + pin)
            pushAuto(cl, ["pincode", pin])

            print(f"[ REG AUTO ] DISPLAY NAME : " + display_name)
            time.sleep(random.uniform(6, 10))
            pushAuto(cl, ["display_name", f"'{display_name}'"])

            while True:
                try:
                    password = GeneratePass()
                    print(f"[ REG AUTO ] PASSWORD : " + password)
                    time.sleep(random.uniform(10, 15))
                    authToken = pushAuto(cl, ["password", password])
                    break
                except Exception as e:
                    print(e)

            open("tmp/token_backup.txt", "a").write("\n" + authToken)

            print(f"[ REG AUTO ] AUTH TOKEN : " + authToken)
            print("\n\n")

            cl.tokenlist.append(authToken)

        except Exception as e:
            print("\n\n")
            error_msg = str(e)

            print("[ ERROR ] " + str(e))
            print("")
            if "authexception(code=1," in str(e).lower():
                time.sleep(5)
                cancelActivation(result["otpid"])
                # time.sleep(5)
            if "human" in str(e).lower():
                cancelActivation(result["otpid"])
                human += 1
                if human == 99:
                    break
            if "get pin" in str(e).lower() or "number" in str(e).lower():
                time.sleep(5)
                pinfail = True

            try:
                pushAuto(cl, ["reset"])
            except:
                pass

        if pinfail == False:
            if len(cl.tokenlist) == qty:
                break
            time.sleep(random.uniform(60, 100))

    cl.sendMessage(to, f"[ {qty} TOKEN ANDROID ]\n\n" + "\n".join(cl.tokenlist))
    cl.reg_auto = False
    cl.tokenlist = []
    open("tmp/token_backup.txt", "w").write("")


def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    mibot = command(text)
    cmd = " ".join(mibot.split())
    for cmd in mibot.split(" & "):

        if sender in owner:
            # ========= HELP REG ======== #

            cl = line

            try:
                text = str(text)
                cmd = text.lower()
                spl = cmd.split(" ")

                if cmd == "help reg":
                    cl.sendMessage(
                        to,
                        "[ REG MENU ]\n- Reset Reg\n- RegNum [country code] [phone number]\n- RegAuto [1-10]",
                    )

                if cmd == "reset reg":
                    pushData(cl, ["reset"])
                    cl.sendMessage(to, "Success reset session")

                if cmd.startswith("regauto "):
                    qty = int(spl[1])
                    if qty < 1:
                        return cl.sendMessage(to, "Minimum 1 pcs")
                    if qty > 10:
                        return cl.sendMessage(to, "Maximum 10 pcs")
                    if cl.reg_auto:
                        return cl.sendMessage(
                            to,
                            "Auto Registration On Process. Please wait until complete",
                        )
                    cl.reg_auto = True
                    Thread(
                        target=reg_auto,
                        args=(
                            to,
                            qty,
                        ),
                    ).start()
                    cl.sendMessage(to, "Auto Registration Started !!!")

                if cmd.startswith("regnum "):
                    region, phoneNumber = spl[1].upper(), spl[2]
                    # if region not in ["ID", "TH"]:raise Exception("Invalid region")

                    cl.sendMessage(to, "Loading...")
                    pushData(cl, ["new", phoneNumber, region])
                    cl.sendMessage(to, "[ Enter Pincode ]\nType Pincode [code]")

                if cmd.startswith("pincode "):
                    pushData(cl, ["pincode", spl[1]])
                    cl.sendMessage(to, "[ Enter Display Name ]\nType SetName [name]")

                if cmd.startswith("setname "):
                    pushData(cl, ["display_name", f"'{text[8:]}'"])
                    cl.sendMessage(to, "[ Enter Password ]\nType SetPW [password]")

                if cmd.startswith("setpw "):
                    cl.sendMessage(to, "Please wait...")
                    authToken = pushData(cl, ["password", text[6:]])
                    cl.sendMessage(
                        to, "[ REGISTER SUCCESS ]\nAuth Token : " + authToken
                    )
                    cl.sendContact(to, authToken.split(":")[0])

                if cmd.startswith("goqr "):
                    tokenlist = removeCmd(text, setKey).split("\n")

                    group = line.getChats([to], False, False)
                    if group.chats[0].extra.groupExtra.preventedJoinByTicket == True:
                        group.chats[0].extra.groupExtra.preventedJoinByTicket = False
                        line.updateChat(group.chats[0], 4)
                    else:
                        cl.sendMessage(to, "Checking...")

                    ticket = str(line.reissueChatTicket(to).ticketId)
                    for x in tokenlist:

                        if "ey" == x[0:2]:
                            payload = x.split(".")[1] + "="
                            data = base64.b64decode(payload + "=").decode("utf-8")
                            token_mid = re.findall("u[0-9a-f]{32}", data)[0]
                        else:
                            token_mid = x.split(":")[0]

                        os.system("chmod 777 goqr")
                        os.system(f"./goqr {x} {ticket}")
                        time.sleep(1)

                        if token_mid not in str(
                            line.getChats([to]).chats[0].extra.groupExtra.memberMids
                        ):
                            cl.sendMention(to, "@! Banned / Limit\n\n" + x, [token_mid])

                    cl.sendMessage(to, "Success check token")

                if cmd.startswith("addsquad "):
                    tokenlist = removeCmd(text, setKey).split("\n")
                    if len(tokenlist) < 2:
                        return cl.sendMessage(to, "Put minimum 2 token")
                    list_squad = re.findall("u[0-9a-f]{32}", text)
                    for x in tokenlist:
                        try:
                            NEW = CHRLINE(
                                x,
                                device="ANDROID",
                                version="11.17.0",
                                os_name="Android OS",
                                os_version=f"8.0.{random.randint(1, 9999)}",
                            )
                            token_mid = NEW.profile[1]

                            for sq_mid in list_squad:
                                if sq_mid == token_mid:
                                    continue
                                NEW.findAndAddContactsByMid(sq_mid)
                                time.sleep(5)

                            all_fl = NEW.getAllContactIds()
                            l = "\n"
                            n = 1
                            for fl_mid in all_fl:
                                l += f"\n{n}. {cl.getContact(fl_mid).displayName}"
                                n += 1

                            cl.sendMention(to, "@! Friendlist" + l, [token_mid])

                        except Exception as e:
                            if "blocked" in str(e):
                                cl.sendMention(to, "@! " + str(e), [token_mid])
                            else:
                                cl.sendMessage(to, "OTHER ERROR : " + str(e))
                                break

                        time.sleep(2)

            except Exception as e:
                error_msg = str(e)

                if "temporarily blocked" in error_msg:
                    timeleft = re.findall("(?:Please wait )(.+\(s\))", error_msg)
                    cl.sendMessage(
                        to,
                        f"Verification is temporarily blocked.\nPlease wait {timeleft} then try again.",
                    )

                elif "enter a valid" in error_msg:
                    cl.sendMessage(to, "Please enter a valid phone number.")

                else:
                    cl.sendMessage(to, "Exception Error\n" + error_msg)

            # ================================== #

        """ CHAT GPT """

        if cmd.startswith("chatgpt "):
            unsend_id = [line.sendMessage(to, "Processing your quest...").id]

            openai.organization = "org-FyAvJHp6dcQuW0BO4EZTSMO5"
            openai.api_key = "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"

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": removeCmd(text, setKey)}],
                    temperature=0,
                    stream=True,  # again, we set stream=True
                )
            except Exception as e:
                return line.sendMessage(to, str(e))

            full_msg = ""
            tmp_msg = ""

            skip_first_enter = True
            max_sec = 2.5
            show_tmp_msg_at = time.time() + max_sec

            for chunk in response:
                info = chunk["choices"][0]["delta"]
                if "content" not in info:
                    continue

                letter = info["content"]

                tmp_msg += letter
                full_msg += letter

                if letter[-1] == "\n":
                    if time.time() < show_tmp_msg_at:
                        continue
                    show_tmp_msg_at = time.time() + max_sec
                    # print(tmp_msg);
                    unsend_id.append(line.sendMessage(to, tmp_msg).id)

                    tmp_msg = ""

            line.sendReplyMessage(to, full_msg, msgIds=msg_id)
            for x in unsend_id:
                line.unsendMessage(x)

        # ================================== #

        if cmd == "helper logout":
            if sender in owner:
                line.sendMessage(to, "Helper stopped.")
                sys.exit("##----- PROGRAM STOPPED -----##")

        elif cmd == "helper restart":
            if sender in owner:
                line.sendMessage(to, "wait a moment....")
                line.settings["restartPoint"] = {"to": to, "msgId": msg_id}
                restartProgram()

        elif cmd == "helper bye":
            if sender in owner:
                line.deleteSelfFromChat(to)

        elif txt == "helper":
            res = "𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗨𝘀𝗲𝗿"
            res += "\n\n› Login Mac"
            res += "\n› Login Chrome"
            res += "\n› Login Win"
            res += "\n› Addmail email:pass"
            res += "\n› Login Email"
            res += "\n› Logout Sb"
            res += "\n› Mystatus"
            res += "\n› Cert Reset"
            res += "\n› Helpo"
            res += "\n› Tagall"
            line.sendMessage(to, res)

        elif txt == "flex":
            flex_message = [
                {
                    "type": "bubble",
                    "size": "mega",
                    "header": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "FROM",
                                        "color": "#ffffff66",
                                        "size": "sm",
                                    },
                                    {
                                        "type": "text",
                                        "text": "Akihabara",
                                        "color": "#ffffff",
                                        "size": "xl",
                                        "flex": 4,
                                        "weight": "bold",
                                    },
                                ],
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "TO",
                                        "color": "#ffffff66",
                                        "size": "sm",
                                    },
                                    {
                                        "type": "text",
                                        "text": "Shinjuku",
                                        "color": "#ffffff",
                                        "size": "xl",
                                        "flex": 4,
                                        "weight": "bold",
                                    },
                                ],
                            },
                        ],
                        "paddingAll": "20px",
                        "backgroundColor": "#0367D3",
                        "spacing": "md",
                        "height": "154px",
                        "paddingTop": "22px",
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Total: 1 hour",
                                "color": "#b7b7b7",
                                "size": "xs",
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "20:30",
                                        "size": "sm",
                                        "gravity": "center",
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {"type": "filler"},
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [],
                                                "cornerRadius": "30px",
                                                "height": "12px",
                                                "width": "12px",
                                                "borderColor": "#EF454D",
                                                "borderWidth": "2px",
                                            },
                                            {"type": "filler"},
                                        ],
                                        "flex": 0,
                                    },
                                    {
                                        "type": "text",
                                        "text": "Akihabara",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "sm",
                                    },
                                ],
                                "spacing": "lg",
                                "cornerRadius": "30px",
                                "margin": "xl",
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [{"type": "filler"}],
                                        "flex": 1,
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {"type": "filler"},
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [],
                                                        "width": "2px",
                                                        "backgroundColor": "#B7B7B7",
                                                    },
                                                    {"type": "filler"},
                                                ],
                                                "flex": 1,
                                            }
                                        ],
                                        "width": "12px",
                                    },
                                    {
                                        "type": "text",
                                        "text": "Walk 4min",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "color": "#8c8c8c",
                                    },
                                ],
                                "spacing": "lg",
                                "height": "64px",
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "20:34",
                                                "gravity": "center",
                                                "size": "sm",
                                            }
                                        ],
                                        "flex": 1,
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {"type": "filler"},
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [],
                                                "cornerRadius": "30px",
                                                "width": "12px",
                                                "height": "12px",
                                                "borderWidth": "2px",
                                                "borderColor": "#6486E3",
                                            },
                                            {"type": "filler"},
                                        ],
                                        "flex": 0,
                                    },
                                    {
                                        "type": "text",
                                        "text": "Ochanomizu",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "sm",
                                    },
                                ],
                                "spacing": "lg",
                                "cornerRadius": "30px",
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "baseline",
                                        "contents": [{"type": "filler"}],
                                        "flex": 1,
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "horizontal",
                                                "contents": [
                                                    {"type": "filler"},
                                                    {
                                                        "type": "box",
                                                        "layout": "vertical",
                                                        "contents": [],
                                                        "width": "2px",
                                                        "backgroundColor": "#6486E3",
                                                    },
                                                    {"type": "filler"},
                                                ],
                                                "flex": 1,
                                            }
                                        ],
                                        "width": "12px",
                                    },
                                    {
                                        "type": "text",
                                        "text": "Metro 1hr",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "xs",
                                        "color": "#8c8c8c",
                                    },
                                ],
                                "spacing": "lg",
                                "height": "64px",
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "20:40",
                                        "gravity": "center",
                                        "size": "sm",
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {"type": "filler"},
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [],
                                                "cornerRadius": "30px",
                                                "width": "12px",
                                                "height": "12px",
                                                "borderColor": "#6486E3",
                                                "borderWidth": "2px",
                                            },
                                            {"type": "filler"},
                                        ],
                                        "flex": 0,
                                    },
                                    {
                                        "type": "text",
                                        "text": "Shinjuku",
                                        "gravity": "center",
                                        "flex": 4,
                                        "size": "sm",
                                    },
                                ],
                                "spacing": "lg",
                                "cornerRadius": "30px",
                            },
                        ],
                    },
                }
            ]
            print(to)

            line.sendLiff(
                "c5e6b6a1eb652425e26ed80f203ac5195", flex_message, mainType=False
            )
        elif txt == "get":
            friends = line.getAllContactIds()
            for user_id in friends:
                print(user_id)
                flex_message = [
                            {
                                "type": "bubble",
                                "hero": {
                                    "type": "image",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/01_3_movie.png",
                                    "size": "full",
                                    "aspectRatio": "20:13",
                                    "aspectMode": "cover",
                                    "action": {
                                        "type": "uri",
                                        "uri": "https://line.me/",
                                    },
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "md",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "BROWN'S ADVENTURE\nIN MOVIE",
                                            "wrap": True,
                                            "weight": "bold",
                                            "gravity": "center",
                                            "size": "xl",
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "margin": "md",
                                            "contents": [
                                                {
                                                    "type": "icon",
                                                    "size": "sm",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png",
                                                },
                                                {
                                                    "type": "icon",
                                                    "size": "sm",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png",
                                                },
                                                {
                                                    "type": "icon",
                                                    "size": "sm",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png",
                                                },
                                                {
                                                    "type": "icon",
                                                    "size": "sm",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png",
                                                },
                                                {
                                                    "type": "icon",
                                                    "size": "sm",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png",
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "4.0",
                                                    "size": "sm",
                                                    "color": "#999999",
                                                    "margin": "md",
                                                    "flex": 0,
                                                },
                                            ],
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "margin": "lg",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "Date",
                                                            "color": "#aaaaaa",
                                                            "size": "sm",
                                                            "flex": 1,
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "Monday 25, 9:00PM",
                                                            "wrap": True,
                                                            "size": "sm",
                                                            "color": "#666666",
                                                            "flex": 4,
                                                        },
                                                    ],
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "Place",
                                                            "color": "#aaaaaa",
                                                            "size": "sm",
                                                            "flex": 1,
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "7 Floor, No.3",
                                                            "wrap": True,
                                                            "color": "#666666",
                                                            "size": "sm",
                                                            "flex": 4,
                                                        },
                                                    ],
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "Seats",
                                                            "color": "#aaaaaa",
                                                            "size": "sm",
                                                            "flex": 1,
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "C Row, 18 Seat",
                                                            "wrap": True,
                                                            "color": "#666666",
                                                            "size": "sm",
                                                            "flex": 4,
                                                        },
                                                    ],
                                                },
                                            ],
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "margin": "xxl",
                                            "contents": [
                                                {
                                                    "type": "image",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/linecorp_code_withborder.png",
                                                    "aspectMode": "cover",
                                                    "size": "xl",
                                                    "margin": "md",
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "You can enter the theater by using this code instead of a ticket",
                                                    "color": "#aaaaaa",
                                                    "wrap": True,
                                                    "margin": "xxl",
                                                    "size": "xs",
                                                },
                                            ],
                                        },
                                    ],
                                },
                            }
                        ]
                line.sendLiff(user_id, flex_message, mainType=False)

        elif cmd == "grouplist":
            gids = make_list(line.getAllChatMids(True, False).memberChatMids)
            res = "› L I S T\n"
            if gids:
                no = 0
                if len(gids) > 200:
                    parsed_len = len(gids) // 200 + 1
                    for point in range(parsed_len):
                        for gid in gids[point * 200 : (point + 1) * 200]:
                            no += 1
                            group = line.getChats([gid], True, False).chats[0]
                            gids = line.getGroupIdsByName(group.chatName)
                            res += "\n%i. %s//%s" % (no, group.chatName, gids)
                        if res:
                            if res.startswith("\n"):
                                res = res[1:]
                            line.sendMessage(to, res)
                        if point != parsed_len - 1:
                            res = ""
                else:
                    for gid in gids:
                        group = line.getChats([gid], True, False).chats[0]
                        no += 1
                        gids = line.getGroupIdsByName(group.chatName)
                        print(gids[0])
                        flex_message = [
                            {
                                "type": "bubble",
                                "hero": {
                                    "type": "image",
                                    "url": "https://developers-resource.landpress.line.me/fx/img/01_3_movie.png",
                                    "size": "full",
                                    "aspectRatio": "20:13",
                                    "aspectMode": "cover",
                                    "action": {
                                        "type": "uri",
                                        "uri": "https://line.me/",
                                    },
                                },
                                "body": {
                                    "type": "box",
                                    "layout": "vertical",
                                    "spacing": "md",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": "BROWN'S ADVENTURE\nIN MOVIE",
                                            "wrap": True,
                                            "weight": "bold",
                                            "gravity": "center",
                                            "size": "xl",
                                        },
                                        {
                                            "type": "box",
                                            "layout": "baseline",
                                            "margin": "md",
                                            "contents": [
                                                {
                                                    "type": "icon",
                                                    "size": "sm",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png",
                                                },
                                                {
                                                    "type": "icon",
                                                    "size": "sm",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png",
                                                },
                                                {
                                                    "type": "icon",
                                                    "size": "sm",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png",
                                                },
                                                {
                                                    "type": "icon",
                                                    "size": "sm",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png",
                                                },
                                                {
                                                    "type": "icon",
                                                    "size": "sm",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/review_gray_star_28.png",
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "4.0",
                                                    "size": "sm",
                                                    "color": "#999999",
                                                    "margin": "md",
                                                    "flex": 0,
                                                },
                                            ],
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "margin": "lg",
                                            "spacing": "sm",
                                            "contents": [
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "Date",
                                                            "color": "#aaaaaa",
                                                            "size": "sm",
                                                            "flex": 1,
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "Monday 25, 9:00PM",
                                                            "wrap": True,
                                                            "size": "sm",
                                                            "color": "#666666",
                                                            "flex": 4,
                                                        },
                                                    ],
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "Place",
                                                            "color": "#aaaaaa",
                                                            "size": "sm",
                                                            "flex": 1,
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "7 Floor, No.3",
                                                            "wrap": True,
                                                            "color": "#666666",
                                                            "size": "sm",
                                                            "flex": 4,
                                                        },
                                                    ],
                                                },
                                                {
                                                    "type": "box",
                                                    "layout": "baseline",
                                                    "spacing": "sm",
                                                    "contents": [
                                                        {
                                                            "type": "text",
                                                            "text": "Seats",
                                                            "color": "#aaaaaa",
                                                            "size": "sm",
                                                            "flex": 1,
                                                        },
                                                        {
                                                            "type": "text",
                                                            "text": "C Row, 18 Seat",
                                                            "wrap": True,
                                                            "color": "#666666",
                                                            "size": "sm",
                                                            "flex": 4,
                                                        },
                                                    ],
                                                },
                                            ],
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "margin": "xxl",
                                            "contents": [
                                                {
                                                    "type": "image",
                                                    "url": "https://developers-resource.landpress.line.me/fx/img/linecorp_code_withborder.png",
                                                    "aspectMode": "cover",
                                                    "size": "xl",
                                                    "margin": "md",
                                                },
                                                {
                                                    "type": "text",
                                                    "text": "You can enter the theater by using this code instead of a ticket",
                                                    "color": "#aaaaaa",
                                                    "wrap": True,
                                                    "margin": "xxl",
                                                    "size": "xs",
                                                },
                                            ],
                                        },
                                    ],
                                },
                            }
                        ]
                        line.sendLiff(gids[0], flex_message, mainType=False)
                        # res += "\n%s" % (gids)
                    # line.sendMessage(to, res)

            else:
                line.sendMessage(to, "Nothing")

        elif txt == "helpo":
            resO = "𝗖𝗼𝗺𝗺𝗮𝗻𝗱 𝗢𝘄𝗻𝗲𝗿"
            resO += "\n\n›  Adduser <name> @Mention"
            resO += "\n›  Deluser <folder/@Mention>"
            resO += "\n›  Delmid <mid>"
            resO += "\n›  Addday <num> @Mention"
            resO += "\n›  Delday <num> @Mention"
            resO += "\n›  Addhours <num> @Mention"
            resO += "\n›  Delhours <num> @Mention"
            resO += "\n›  Status <folder/@Mention>"
            resO += "\n›  Helper Logout"
            resO += "\n›  Helper Restart"
            resO += "\n›  Helper bye"
            resO += "\n›  List User"
            resO += "\n›  Hunsend number"
            resO += "\n›  Clear chat"
            resO += "\n›  Glist"
            resO += "\n›  Cpict"
            resO += "\n›  Ccover"
            resO += "\n›  Cbio <text>"
            line.sendMessage(to, resO)

        elif txt.startswith("addmail "):
            if sender in line.settings["myService"]:
                mid = removeCmd(text, setKey)
                pemisah = mid.split(":")
                emailx = pemisah[0]
                passx = pemisah[1]
                print(emailx)
                print(passx)
                nama = line.settings["myService"][sender]
                line.settings["list"][nama]["dataemail"] = {
                    "email": emailx,
                    "password": passx,
                }
                line.sendMessage(to, "Succes Add Email ♪")

        elif txt == "login email":
            if sender in line.settings["myService"]:
                user = line.settings["myService"][sender]
                if sender not in line.settings["listLogin"]:
                    nama = line.settings["myService"][sender]
                    emailx = line.settings["list"][nama]["dataemail"]["email"]
                    passx = line.settings["list"][nama]["dataemail"]["password"]
                    loginEmail(to, sender, user, "DESKTOPWIN", emailx, passx)
                else:
                    line.sendMessage(
                        to, "You are still logged in, logout first, type `Logout Sb`"
                    )

        elif txt.startswith("login "):
            if sender in line.settings["myService"]:
                sep = text.split(" ")
                headers = text.replace(sep[0] + " ", "")
                user = line.settings["myService"][sender]
                if headers.lower() not in ["mac", "chrome", "win"]:
                    return line.sendMessage(
                        to,
                        "Command wrong!!\n1. Login Mac\n2. Login Chrome\n\nOwner recommends number 2",
                    )
                if sender not in line.settings["listLogin"]:
                    if line.settings["list"][user]["expired"] <= time.time():
                        return line.sendMessage(
                            to,
                            f"› Folder: {user}\nYour service has been expired, contact admin!",
                        )
                    if headers.lower() == "mac":
                        loginSelfbot(msg, to, sender, user, "DESKTOPMAC", msg_id)
                    elif headers.lower() == "chrome":
                        loginSelfbot(msg, to, sender, user, "CHROMEOS", msg_id)
                    elif headers.lower() == "win":
                        loginSelfbot(msg, to, sender, user, "DESKTOPWIN", msg_id)
                else:
                    line.sendMessage(
                        to, "You are still logged in, logout first, type `Logout Sb`"
                    )

        elif txt.startswith("logout sb"):
            if sender in line.settings["myService"]:
                sep = text.split(" ")
                sb = text.replace(sep[0] + " ", "")
                if sb.lower() != "sb":
                    return line.sendMessage(
                        to, "Command wrong!!, type `Logout Sb`", messageId=msg_id
                    )
                user = line.settings["myService"][sender]
                if line.settings["list"][user]["ajs"]:
                    ajsnya = "True"
                else:
                    ajsnya = "False"
                if sender in line.settings["listLogin"]:
                    del line.settings["listLogin"][sender]
                    os.system("screen -S {} -X quit".format(str(user)))
                    time.sleep(0.5)
                    os.system("cd {} && cp -r json ../jsonUser/{}".format(user, user))
                    time.sleep(0.5)
                    os.system("rm -rf {}".format(str(user)))
                    line.sendMessage(to, "Logout Successful!")
                else:
                    line.sendMessage(
                        to, "You are not logged in, type `Login <mac/chrome>`"
                    )

        elif cmd.startswith("addme ") and sender in owner:
            nama = removeCmd(text, setKey)
            if sender not in line.settings["myService"]:
                line.settings["myService"][sender] = "%s" % nama
                line.settings["list"][nama] = {
                    "ex": False,
                    "mid": sender,
                    "expired": time.time() + 60 * 60 * 24 * 31,
                    "folderStatus": False,
                    "ajs": False,
                    "token": {
                        "antijs": "",
                        "DESKTOPMAC": "",
                        "DESKTOPWIN": "",
                        "CHROMEOS": "",
                        "IOSIPAD": "",
                    },
                    "cert": "",
                }
                if line.settings["list"][nama]["ajs"]:
                    ajsnya = "True"
                else:
                    ajsnya = "False"
                line.sendMention(
                    to,
                    f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {nama}\n› {getExpired(line.settings['list'][nama]['expired'])}",
                    [sender],
                )
            else:
                line.sendMessage(to, "You are already in service")

        elif cmd.startswith("delmid ") and sender in owner:
            mid = removeCmd(text, setKey)
            if mid in line.settings["myService"]:
                user = line.settings["myService"][mid]
                if mid in line.settings["listLogin"]:
                    del line.settings["listLogin"][mid]
                    os.system("screen -S {} -X kill".format(user))
                    os.system("rm -r {}".format(user))
                if line.settings["list"][user]["folderStatus"]:
                    os.system("cd jsonUser && rm -r {}".format(user))
                del line.settings["myService"][mid]
                del line.settings["list"][user]
                line.sendMention(
                    to, f"› User: @!\n› Folder: {user}\n\nDATA HAS BEEN DELETED", [mid]
                )
            else:
                line.sendMention(to, "› User: @!\nUser not in service", [mid])

        elif cmd.startswith("adduser ") and sender in owner:
            if "MENTION" in msg.contentMetadata != None:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                sep = removeCmd(text, setKey)
                nama = sep.split(" ")[0]
                if key1 not in line.settings["myService"]:
                    for mid in line.settings["myService"]:
                        if line.settings["myService"][mid] == nama:
                            return line.sendMessage(
                                to,
                                "Failed add user, name '%s' is already in service"
                                % nama,
                            )
                    line.settings["myService"][key1] = "%s" % nama
                    line.settings["list"][nama] = {
                        "ex": False,
                        "mid": key1,
                        "expired": time.time() + 60 * 60 * 24 * 31,
                        "folderStatus": False,
                        "ajs": False,
                        "token": {
                            "antijs": "",
                            "DESKTOPMAC": "",
                            "DESKTOPWIN": "",
                            "CHROMEOS": "",
                            "IOSIPAD": "",
                        },
                        "cert": "",
                        "dataemail": {},
                    }
                    time.sleep(1)
                    if line.settings["list"][nama]["ajs"]:
                        ajsnya = "True"
                    else:
                        ajsnya = "False"
                    line.sendMention(
                        to,
                        f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {nama}\n› {getExpired(line.settings['list'][nama]['expired'])}",
                        [key1],
                    )
                else:
                    line.sendMention(to, "› User: @!\nUser already on service", [key1])

        elif cmd.startswith("deluser ") and sender in owner:
            if "MENTION" in msg.contentMetadata != None:
                key = eval(msg.contentMetadata["MENTION"])
                mid = key["MENTIONEES"][0]["M"]
                if mid in line.settings["myService"]:
                    user = line.settings["myService"][mid]
                    if mid in line.settings["listLogin"]:
                        del line.settings["listLogin"][mid]
                        os.system("screen -S {} -X kill".format(user))
                        os.system("rm -r {}".format(user))
                    if line.settings["list"][user]["folderStatus"]:
                        os.system("cd jsonUser && rm -r {}".format(user))
                    del line.settings["myService"][mid]
                    del line.settings["list"][user]
                    line.sendMention(
                        to,
                        f"› User: @!\n› Folder: {user}\n\nDATA HAS BEEN DELETED",
                        [mid],
                    )
                else:
                    line.sendMention(to, "› User: @!\nUser not in service", [mid])
            else:
                nama = removeCmd(text, setKey)
                for mid in line.settings["myService"]:
                    if line.settings["myService"][mid] == nama:
                        user = line.settings["myService"][mid]
                        if mid in line.settings["listLogin"]:
                            del line.settings["listLogin"][mid]
                            os.system("screen -S {} -X kill".format(user))
                            os.system("rm -r {}".format(user))
                        if line.settings["list"][user]["folderStatus"]:
                            os.system("cd jsonUser && rm -r {}".format(user))
                        del line.settings["myService"][mid]
                        del line.settings["list"][user]
                        line.sendMention(
                            to,
                            f"› User: @!\n› Folder: {user}\n\nDATA HAS BEEN DELETED",
                            [mid],
                        )
                        return
                line.sendMessage(to, f"`{nama}` not in service")

        elif cmd.startswith("addday ") and sender in owner:
            if "MENTION" in msg.contentMetadata != None:
                key = eval(msg.contentMetadata["MENTION"])
                mid = key["MENTIONEES"][0]["M"]
                if mid in line.settings["myService"]:
                    user = line.settings["myService"][mid]
                    sep = removeCmd(text, setKey)
                    a = sep.split(" ")
                    jumlah = int(a[0])
                    biling = int(60 * 60 * 24 * jumlah)
                    line.settings["list"][user]["expired"] = (
                        line.settings["list"][user]["expired"] + biling
                    )
                    time.sleep(1)
                    if line.settings["list"][user]["ajs"]:
                        ajsnya = "True"
                    else:
                        ajsnya = "False"
                    line.sendMention(
                        to,
                        f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {user}\n› {getExpired(line.settings['list'][user]['expired'])}\n\nSUCCESS INCREASE DAY",
                        [mid],
                    )

        elif cmd.startswith("addhours ") and sender in owner:
            if "MENTION" in msg.contentMetadata != None:
                key = eval(msg.contentMetadata["MENTION"])
                mid = key["MENTIONEES"][0]["M"]
                if mid in line.settings["myService"]:
                    user = line.settings["myService"][mid]
                    sep = removeCmd(text, setKey)
                    a = sep.split(" ")
                    jumlah = int(a[0])
                    biling = int(60 * 60 * jumlah)
                    line.settings["list"][user]["expired"] = (
                        line.settings["list"][user]["expired"] + biling
                    )
                    time.sleep(1)
                    if line.settings["list"][user]["ajs"]:
                        ajsnya = "True"
                    else:
                        ajsnya = "False"
                    line.sendMention(
                        to,
                        f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {user}\n› {getExpired(line.settings['list'][user]['expired'])}\n\nSUCCESS INCREASE HOUR",
                        [mid],
                    )

        elif cmd.startswith("delday ") and sender in owner:
            if "MENTION" in msg.contentMetadata != None:
                key = eval(msg.contentMetadata["MENTION"])
                mid = key["MENTIONEES"][0]["M"]
                if mid in line.settings["myService"]:
                    user = line.settings["myService"][mid]
                    sep = removeCmd(text, setKey)
                    a = sep.split(" ")
                    jumlah = int(a[0])
                    biling = int(60 * 60 * 24 * jumlah)
                    line.settings["list"][user]["expired"] = (
                        line.settings["list"][user]["expired"] - biling
                    )
                    time.sleep(1)
                    if line.settings["list"][user]["ajs"]:
                        ajsnya = "True"
                    else:
                        ajsnya = "False"
                    line.sendMention(
                        to,
                        f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {user}\n› {getExpired(line.settings['list'][user]['expired'])}\n\nSUCCESS DECREASE DAY",
                        [mid],
                    )

        elif cmd.startswith("delhours ") and sender in owner:
            if "MENTION" in msg.contentMetadata != None:
                key = eval(msg.contentMetadata["MENTION"])
                mid = key["MENTIONEES"][0]["M"]
                if mid in line.settings["myService"]:
                    user = line.settings["myService"][mid]
                    sep = removeCmd(text, setKey)
                    a = sep.split(" ")
                    jumlah = int(a[0])
                    biling = int(60 * 60 * jumlah)
                    line.settings["list"][user]["expired"] = (
                        line.settings["list"][user]["expired"] - biling
                    )
                    time.sleep(1)
                    if line.settings["list"][user]["ajs"]:
                        ajsnya = "True"
                    else:
                        ajsnya = "False"
                    line.sendMention(
                        to,
                        f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {user}\n› {getExpired(line.settings['list'][user]['expired'])}\n\nSUCCESS DECREASE HOUR",
                        [mid],
                    )

        elif cmd.startswith("status ") and sender in owner:
            if "MENTION" in msg.contentMetadata != None:
                key = eval(msg.contentMetadata["MENTION"])
                mid = key["MENTIONEES"][0]["M"]
                if mid in line.settings["myService"]:
                    user = line.settings["myService"][mid]
                    if line.settings["list"][user]["ajs"]:
                        ajsnya = "True"
                    else:
                        ajsnya = "False"
                    if line.settings["list"][user]["expired"] <= time.time():
                        line.sendMention(
                            to,
                            f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {user}\nYour service has been expired, contact admin!",
                            [mid],
                        )
                    else:
                        line.sendMention(
                            to,
                            f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {user}\n› {getExpired(line.settings['list'][user]['expired'])}",
                            [mid],
                        )
            else:
                nama = removeCmd(text, setKey)
                for mid in line.settings["myService"]:
                    if line.settings["myService"][mid] == nama:
                        user = line.settings["myService"][mid]
                        if line.settings["list"][user]["ajs"]:
                            ajsnya = "True"
                        else:
                            ajsnya = "False"
                        if line.settings["list"][user]["expired"] <= time.time():
                            line.sendMention(
                                to,
                                f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {user}\nYour service has been expired, contact admin!",
                                [mid],
                            )
                        else:
                            line.sendMention(
                                to,
                                f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {user}\n› {getExpired(line.settings['list'][user]['expired'])}",
                                [mid],
                            )
                        return
                line.sendMessage(to, f"`{nama}` not in service")

        elif txt == "mystatus":
            if sender in line.settings["myService"]:
                user = line.settings["myService"][sender]
                if line.settings["list"][user]["ajs"]:
                    ajsnya = "True"
                else:
                    ajsnya = "False"
                if line.settings["list"][user]["expired"] <= time.time():
                    line.sendMention(
                        to,
                        f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {user}\nYour service has been expired, contact admin!",
                        [sender],
                    )
                else:
                    line.sendMention(
                        to,
                        f"› User: @!\n› Antijs: {ajsnya}\n› Folder: {user}\n› {getExpired(line.settings['list'][user]['expired'])}",
                        [sender],
                    )

        elif cmd == "list user":
            if sender in owner:
                if line.settings["myService"]:
                    myservice = make_list(line.settings["myService"])
                    res = "「 List Service 」"
                    for i in range(0, len(myservice), 20):
                        mids = []
                        for no, mid in enumerate(myservice[i : i + 20], i + 1):
                            mids.append(mid)
                            cd = line.settings["myService"][mid]
                            if line.settings["list"][cd]["ajs"]:
                                ajsnya = "True"
                            else:
                                ajsnya = "False"
                            if line.settings["list"][cd]["expired"] <= time.time():
                                exnya = "Expired"
                            else:
                                waktu = (
                                    line.settings["list"][cd]["expired"] - time.time()
                                )
                                days = int(waktu / 60 / 60 / 24)
                                exnya = "{} Days".format(days)
                            res += "\n{}. @!\nFolder : {}\nAntijs : {}\nStatus: {}\n".format(
                                no, cd, ajsnya, exnya
                            )
                        if mids:
                            if res.startswith("\n"):
                                res = res[1 : len(res)]
                            if res.endswith("\n"):
                                res = res[:-1]
                            line.sendMention(to, res, mids)
                        res = ""
                else:
                    line.sendMessage(to, "List is empty")

        elif cmd == "clear chat":
            line.removeAllMessages(to)
            line.sendMessage(to, "Success.")

        elif cmd.startswith("cbio "):
            if sender in owner:
                textt = removeCmd(text, setKey)
                profile = line.getProfile()
                profile.statusMessage = textt
                line.updateProfile(profile)
                line.sendMessage(to, "Success.")

        elif cmd == "cpict":
            if sender in owner:
                line.setts["changePicture"] = True
                line.sendMessage(to, "Send picture ~~")

        elif cmd == "ccover":
            if sender in owner:
                line.setts["changeCover"] = True
                line.sendMessage(to, "Send picture ~~")

        elif cmd == "speed":
            start = time.time()
            batas = line.getProfile()
            elapse = time.time() - start
            last = elapse * 1000
            line.sendMessage(to, "%s ms" % (round(last, 2)))

        elif cmd.startswith("hunsend "):
            if sender in owner:
                textt = removeCmd(text, setKey)
                if textt.isdigit():
                    data = line.getRecentMessagesV2(to)
                    msgid = []
                    for m in data:
                        if m._from == line.profile.mid:
                            line.unsendMessage(m.id)
                            msgid.append(m.id)
                            if len(msgid) == int(textt) + 1:
                                break

        elif cmd == "tagall":
            members = []
            if msg.toType == 1:
                room = line.getCompactRoom(to)
                members = [mem.mid for mem in room.contacts]
            elif msg.toType == 2:
                group = line.getChats([to], True, False).chats[0]
                members = [mem for mem in group.extra.groupExtra.memberMids]
            else:
                return line.sendMessage(
                    to, "Use this command only for the room or group chat!"
                )
            if members:
                mentionMembers(to, members)


def operation(op):
    try:
        print(
            "\033[36m++ Operation : ( %i ) %s\033[37m"
            % (op.type, OpType._VALUES_TO_NAMES[op.type].replace("_", " "))
        )
        if op.type == 124:  # NOTIFIED_INVITE_INTO_CHAT
            if line.settings["autoJoin"]["status"] and line.profile.mid in op.param3:
                if op.param2 in owner:
                    line.acceptChatInvitation(op.param1)

        elif op.type == 26:  # RECEIVE_MESSAGE
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = sender if not msg.toType and sender != line.profile.mid else receiver
            txt = text.lower()
            cmd = command(text)
            setKey = (
                line.settings["setKey"]["key"]
                if line.settings["setKey"]["status"]
                else ""
            )
            if msg.contentMetadata is None:
                msg.contentMetadata = {}

            if msg.contentType == 0:  # Content type is None
                try:
                    executeCmd(
                        msg, text, txt, cmd, msg_id, receiver, sender, to, setKey
                    )
                except TalkException as e:
                    logError(e)
                    if e.code in [7, 8, 20]:
                        sys.exit(1)
                    elif "suspended" in e.reason:
                        sys.exit(1)
                    line.sendMessage(
                        to,
                        "TalkException Error, Code: "
                        + str(e.code)
                        + "\nReason: "
                        + str(e.reason),
                    )
                except Exception as e:
                    logError(e)
                    line.sendMessage(to, f"Exception Error\n{e}")

            elif msg.contentType == 1:  # Content type is IMAGE
                if line.setts["changePicture"]:
                    path = line.downloadObjectMsg(msg_id, saveAs="tmp/pict.jpg")
                    line.updateProfilePicture(path)
                    line.sendMessage(to, "Picture profile has been updated")
                    line.setts["changePicture"] = False
                    line.deleteFile(path)
                elif line.setts["changeCover"]:
                    path = line.downloadObjectMsg(msg_id, saveAs="tmp/pict.jpg")
                    line.updateProfileCover(path)
                    line.sendMessage(to, "Picture cover has been updated")
                    line.setts["changeCover"] = False
                    line.deleteFile(path)

    except TalkException as e:
        logError(e)
        if e.code in [7, 8, 20]:
            sys.exit(1)
        elif "suspended" in e.reason:
            sys.exit(1)
    except Exception as e:
        logError(e)
    except KeyboardInterrupt:
        sys.exit(" -- Keyboard Interrupt --")


def check_check():
    if line.settings["myService"]:
        for mid in line.settings["myService"]:
            user = line.settings["myService"][mid]
            if line.settings["list"][user]["expired"] <= time.time():
                if not line.settings["list"][user]["ex"]:
                    line.settings["list"][user]["ex"] = True
                    if mid in line.settings["listLogin"]:
                        del line.settings["listLogin"][mid]
                        os.system("screen -S {} -X quit".format(str(user)))
                        time.sleep(0.5)
                        os.system(
                            "cd {} && cp -r json ../jsonUser/{}".format(user, user)
                        )
                        time.sleep(0.5)
                        os.system("rm -rf {}".format(str(user)))
                    targetss = [mid]
                    # add your gid to targetss, example [mid, 'YOUR_GID']
                    for gidd in targetss:
                        line.sendMention(
                            gidd,
                            f"› User: @!\n› Folder: {user}\nYour service has been Expired, Contact owner to reorder",
                            [mid],
                        )
            elif line.settings["list"][user]["ex"]:
                line.settings["list"][user]["ex"] = False


sch_clearcache = schedule.every(60).minutes.do(clearcache)
executor = ThreadPoolExecutor(max_workers=1)


def main():
    if line.settings["restartPoint"] is not None:
        try:
            line.sendMessage(
                line.settings["restartPoint"]["to"],
                "the program has been successfully restarted",
            )
        except TalkException:
            pass
        line.settings["restartPoint"] = None
    # DONT DELETE THIS, THIS IMPORTANT
    line.server.auth(line)
    # for publicKey in line.talk.getE2EEPublicKeys():
    # line.talk.removeE2EEPublicKey(publicKey)

    while True:
        try:
            task = executor.submit(check_check)
            ops = line.fetchOps(
                oepoll.localRev, 15, oepoll.globalRev, oepoll.individualRev
            )
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit("##---- KEYBOARD INTERRUPT -----##")
        except ShouldSyncException:
            oepoll.localRev = max(line.poll.getLastOpRevision(), oepoll.localRev)
            continue
        except Exception as error:
            logError(error, write=False)
            continue
        if ops:
            for op in ops:
                if op.revision == -1 and op.param2 != None:
                    oepoll.globalRev = int(op.param2.split("\x1e")[0])
                if op.revision == -1 and op.param1 != None:
                    oepoll.individualRev = int(op.param1.split("\x1e")[0])
                operation(op)
                oepoll.localRev = max(op.revision, oepoll.localRev)


if __name__ == "__main__":
    main()
