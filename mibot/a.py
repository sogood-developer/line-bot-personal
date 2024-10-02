'''
all credits belong to, Alm. Zero Cool.
© Self Bot 2018

reworking by
© Sozi 2020

'''
from important import *
from urllib.parse import parse_qsl, urlparse
from requests_html import HTML
from requests_html import HTMLSession
from concurrent.futures import ThreadPoolExecutor
import hmac, math, hashlib, base64, platform, humanize, time, timeit, subprocess, threading, string, urllib, html5lib, lxml, youtube_dl
from minzrestapi import *

minz_api = MinzRestApi("SYDEAR")

def logError(error, write=True):
    errid = str(random.randint(100, 999))
    filee = open('tmp/errors/%s.txt'%errid, 'w') if write else None
    if args.traceback: traceback.print_tb(error.__traceback__)
    if write:
        traceback.print_tb(error.__traceback__, file=filee)
        filee.close()
        with open('tmp/errorLog.txt', 'a') as e:
            e.write('\n%s : %s'%(errid, str(error)))
    print ('\033[1;32m++ Error : {error}\033[0m'.format(error=error))

# Setup Argparse
parser = argparse.ArgumentParser(description='Selfbot Self Bot')
parser.add_argument('-t', '--token', type=str, metavar='', required=False, help='Token | Example : Exxxx')
parser.add_argument('-e', '--email', type=str, default='', metavar='', required=False, help='Email Address | Example : example@xxx.xx')
parser.add_argument('-p', '--passwd', type=str, default='', metavar='', required=False, help='Password | Example : xxxx')
parser.add_argument('-a', '--apptype', type=str, default='', metavar='', required=False, choices=list(ApplicationType._NAMES_TO_VALUES), help='Application Type | Example : CHROMEOS')
parser.add_argument('-s', '--systemname', type=str, default='', metavar='', required=False, help='System Name | Example : Chrome_OS')
parser.add_argument('-c', '--channelid', type=str, default='', metavar='', required=False, help='Channel ID | Example : 1341209950')
parser.add_argument('-T', '--traceback', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Using Traceback | Use : True/False')
parser.add_argument('-S', '--showqr', type=str2bool, nargs='?', default=False, metavar='', required=False, const=True, choices=[True, False], help='Show QR | Use : True/False')
args = parser.parse_args()
    
# Login Client
listAppType = ['DESKTOPWIN']
try:
    print ('\033[1;32m##----- LOGIN CLIENT -----##\033[0m')
    line = None
    for appType in listAppType:
        tokenPath = Path('authToken.txt')
        if tokenPath.exists():
            tokenFile = tokenPath.open('r')
        else:
            tokenFile = tokenPath.open('w+')
        savedAuthToken = tokenFile.read().strip()
        authToken = savedAuthToken if savedAuthToken and not args.token else args.token
        idOrToken = authToken if authToken else args.email
        try:
            line = LINE(idOrToken, appType=appType)
            tokenFile.close()
            tokenFile = tokenPath.open('w+')
            tokenFile.write(line.authToken)
            tokenFile.close()
            break
        except TalkException as talk_error:
            print ('\033[1;32m++ Error : %s\033[0m' % talk_error.reason.replace('_', ' '))
            if args.traceback: traceback.print_tb(talk_error.__traceback__)
            if talk_error.code == 1:
                continue
            sys.exit(1)
        except Exception as error:
            logError(error)
            if args.traceback: traceback.print_tb(error.__traceback__)
            sys.exit(1)
except Exception as error:
    logError(error)
    if args.traceback: traceback.print_tb(error.__traceback__)
    sys.exit(1)

if not line:
    sys.exit('\033[1;32m##----- LOGIN FAILED (Client) -----##\033[0m')

oepoll = OEPoll(line)
template = Template()

programStart = time.time()
sozi = "udec79e367fb60cf779b15dfbfef0b775"
vhApikey = "024b60c7980547efb098d395ea6a6ef9"
rendyApikey = "f62NV9SbVvn0NaSM"
eaterApikey = "eq6KpI4G3CCN"
trojansApikey = "fahmiudin"

bool_dict = {
    True: ['Yes', 'Active', 'Success', 'Open', '✓'],
    False: ['No', 'Not Active', 'Failed', 'Close', '✘']
}
            
def executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    mibot = command(text)
    cmd = " ".join(mibot.split())
    for cmd in mibot.split(' & '):
        if line.settings["textKick"] != "":
            if line.settings["textKick"].lower() in txt:
                if msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        for mention in mentions['MENTIONEES']:
                            mid = mention['M']
                            time.sleep(0.8)
                            if mid in line.getChats([to], True, False).chats[0].extra.groupExtra.memberMids:
                                deleteOtherFromChat(to, [mid])
                            
        if cmd == "help":
            isi = ["Self", "Group", "Media", "Settings", "Template", "Status", "Spam", "Shareurl", "Sider", "Story Line", "List", "Admins", "Broadcast", "Banning", "Protect", "Kick", "Clone", "Remote", "Mimic", "Greet"]
            profile = line.getProfile()
            if line.settings["setFlag"]["icon"] == "https://i.ibb.co/7tmGYQ1/FOOTER-ACODE44.gif":
                if profile.pictureStatus: picture = "https://obs.line-scdn.net/" + str(profile.pictureStatus)
                else: picture = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
            else:
                picture = line.settings["setFlag"]["icon"]
            if line.settings["setFlag"]["name"] == 'sozibot': name = str(profile.displayName)
            else: name = line.settings["setFlag"]["name"]
            line.mainMenu(to, picture, name, setKey, line.settings["tempBackground"], isi)
        
        elif cmd == "self":
            isi = ["Me", "MyLiff", "MyProfile", "Profile", "Cekpc", "Creator", "Check limit", "Restartbot", "Logoutbot", "Error", "ChatBot", "Clear Data", "About", "Admins", "Adders", "Friendlist", "Friends", "Blocklist", "Blocks", "Fancy Text"]
            profile = line.getProfile()
            if line.settings["setFlag"]["icon"] == "https://i.ibb.co/7tmGYQ1/FOOTER-ACODE44.gif":
                if profile.pictureStatus: picture = "https://obs.line-scdn.net/" + str(profile.pictureStatus)
                else: picture = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
            else:
                picture = line.settings["setFlag"]["icon"]
            if line.settings["setFlag"]["name"] == 'sozibot': name = str(profile.displayName)
            else: name = line.settings["setFlag"]["name"]
            line.mainMenu(to, picture, name, setKey, line.settings["tempBackground"], isi)

        elif cmd == "group":
            isi = ["GroupList", "GroupInfo", "Gpict", "Gcover", "Gname", "GID", "Gift", "GetCall", "GetAnnounce", "Chat @Mention/Contact <text>", "ChatId <idline> <text>", "Callgroup <num>", "Call @Mention <num>", "CreateGroup <text>", "ChangeGroupPict", "ChangeGroupCover", "ChangeGroupName <text>", "MemberList", "PendingList", "InvitationList", "OpenQR", "CloseQR", "Who Tag", "TagName <text>", "GetNote", "SearchNote <text>", "-", "Set/Del Detect Resid", "Set/Del Detect Kick", "Setfaketag sticker / <text>", "Setfaketag delSticker", line.settings["setcommand"]["faketag"].title(), "Setmentionall sticker / <text>", "Setmentionall delSticker", line.settings["setcommand"]["mentionall"].title(), "SetMentionEmoji <emoji> / delEmoji", "Setleave <text>", line.settings["setcommand"]["leave"].title(), "Createtl", "Createnote", "Mentionnote", "Mentionnote @Mention", "Lastseen @Mention / contact", "Likepost @Mention", "Track @Mention", "Timeline @Mention", "Timelinecv <url>", "Wordban", "Sendnomor <num> <name>", "Sendpicture <url>", "Sendaudio <url>", "Sendvideo <url>", "Sendgif <url>", "Sendcontact <mid>"]
            res = "› G R O U P\n\n"
            for point in range(len(isi)):
                if point == 0: res += "• %s%s" % (setKey.title(), isi[point])
                else: res += "\n• %s%s" % (setKey.title(), isi[point])
            if line.settings["templateMode"]:
                if line.settings["tempMode"] == "footer":
                    line.sendFooter(to, res, line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)
                else:
                    line.sendMode(msg, to, sender, cmd, res)
            else:
                line.sendReplyMessage(to, res, msgIds=msg_id)
            
        elif cmd == "settings":
            isi = ["Public Mode", "Protect", "Setkey", "ShareURL", "Sleepmode", "AutoAdd", "AutoBlock", "AutoJoin", "AutoLeave", "AutoRespondTag", "AntiTag", "AutoComment", "AutoLike", "AutoRead", "CheckPost <On/Off>", "CheckContact <On/Off>", "CheckSticker <On/Off>", "Detectcall <On/Off>", "Template <On/Off>", "VideoTL <On/Off>", "Notif <On/Off>", "DetectUpdate <On/Off>", "DetectUnsend <On/Off>", "Detect Mid <On/Off>", "Detect Gid <On/Off>"]
            res = "› S E T T I N G S\n\n"
            for point in range(len(isi)):
                if point == 0: res += "• %s%s" % (setKey.title(), isi[point])
                else: res += "\n• %s%s" % (setKey.title(), isi[point])
            if line.settings["templateMode"]:
                if line.settings["tempMode"] == "footer":
                    line.sendFooter(to, res, line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)
                else:
                    line.sendMode(msg, to, sender, cmd, res)
            else:
                line.sendReplyMessage(to, res, msgIds=msg_id)
            
        elif cmd == "media":
            isi = ["Instagram <username>", "Instastory <username>", "Instapost <url>", "Twitter <username>", "Twitter#", "Twitterpost <url>", "Fbpost <url>", "Tiktok <username>", "Tiktokpost <url>", "Cocofun <url>", "Smule <username>", "Smulepost <url>", "Pinterestpost <url>",  "Image <text>", "GIF <text>", "Wallpaper <text>", "Joox <text>", "Soundcloud <text>", "Getchord <text>", "Getlyric <text>", "Photofunia", "TextPro", "Tulis <text>", "Memegen", "Youtube", "Shareurl", "Alquran", "Acaratv <text>", "Arti <name>", "Sifat <name>", "Zodiak <text>", "Ssweb <url>", "Maps <city>", "Sholat <city>", "Cuaca <city>", "Cookpad <text>", "CheckResi <courier> <resi>", "Quotes", "Translate", "GTTS", "BMKG", "Nhentai <codeId>/N/P/R", "NekopoiDL <url>", "Porn <text>", "Urlshort <url>", "Uploadimage", "9Gag", "Themeline <url>", "Wikipedia <text>", "Kbbi <text>", "Github <user>", "Rnumber <num1>-<num2>", "Primary <authkey>", "Secondary <app> <token>"]
            res = "› M E D I A\n\n"
            for point in range(len(isi)):
                if point == 0: res += "• %s%s" % (setKey.title(), isi[point])
                else: res += "\n• %s%s" % (setKey.title(), isi[point])
            if line.settings["templateMode"]:
                if line.settings["tempMode"] == "footer":
                    line.sendFooter(to, res, line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)
                else:
                    line.sendMode(msg, to, sender, cmd, res)
            else:
                line.sendReplyMessage(to, res, msgIds=msg_id)
        
        elif cmd == "clone":
            isi = ["Backup", "Restore", "Clone Contact", "Clone @Mention"]
            res = looping_command(setKey.title(), "› C L O N E", isi)
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd == 'list':
            res = 'Type Active: {}'.format(line.settings["listType"])
            res += '\n1 : Friends'
            res += '\n2 : Groups'
            res += '\n0 : All'
            isi = ["Sticker List / Clear", "Sticker Add <text>", "Sticker Del <text>", "Sticker Deln <num>", "Sticker Save <text>", "Sticker Template <on/off>", "Text List / Clear", "Text Add <text>", "Text Del <text>", "Text Deln <num>", "Picture List / Clear", "Picture Add <text>", "Picture Del <text>", "Picture Deln <num>", "Audio List / Clear", "Audio Add <text>", "Audio Del <text>", "Audio Deln <num>", "Video List / Clear", "Video Add <text>", "Video Del <text>", "Video Deln <num>", "Team List / Clear", "Team Add <text> Reply / Contact", "Team Add <text> @Mention", "Team Del <text>", "Team Deln <num>", "Multi List / Clear", "Multi Add <amount> <text>", "Multi Del <text>", "Multi Deln <num>", "Multi Tutor", "List Type <type>"]
            res += '\n\n{}'.format(looping_command(setKey.title(), "› L I S T", isi))
            res += '\n\n› FUNCTION  T Y P E\n\n1 : other people can only use command List in Personal Chat\n\n2 : others can only use the List command in the group\n\n0 : other people can use command List anywhere'
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd.startswith('list type '):
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if len(sep) == 2:
                if sep[1].isdigit():
                    num = int(sep[1])
                    if num not in [0, 1, 2]: return line.sendMode(msg, to, sender, cmd, 'Failed to set type, type only 1, 2, or 0')
                    line.settings["listType"] = num
                    if num == 0: mode = 'All Chat'
                    elif num == 1: mode = 'Friend Only'
                    elif num == 2: mode = 'Group Only'
                    line.sendMode(msg, to, sender, cmd, 'Successfully changed the list mode to `{}`'.format(mode))
            
        elif cmd == 'status':
            if line.settings["templateMode"] and line.settings["tempMode"] != "footer":
                data = template.main_toggle()
                data2 = template.main_toggle()
                data["body"]["contents"].append(template.second_toggle("AutoAdd", line.settings['autoAdd']['status']))
                data["body"]["contents"].append(template.second_toggle("AutoBlock", line.settings['autoBlock']['status']))
                data["body"]["contents"].append(template.second_toggle("AutoLeave", line.settings['autoLeave']['status']))
                data["body"]["contents"].append(template.second_toggle("AutoJoin", line.settings['autoJoin']['status']))
                data["body"]["contents"].append(template.second_toggle("AutoRespondTag", line.settings['autoRespondMention']['status']))
                data["body"]["contents"].append(template.second_toggle("AutoRead 1", line.settings['autoRead']))
                data["body"]["contents"].append(template.second_toggle("AutoRead 2", line.settings['autoReadG']))
                data["body"]["contents"].append(template.second_toggle("AutoLike", line.settings['autoLike']['status']))
                data["body"]["contents"].append(template.second_toggle("AutoLike Note", line.settings['autoLike']['note']))
                data["body"]["contents"].append(template.second_toggle("AutoLike Story", line.settings['autoLike']['story']))
                data["body"]["contents"].append(template.second_toggle("AutoComment", line.settings['autoComment']['status']))
                data["body"]["contents"].append(template.second_toggle("AutoComment Note", line.settings['autoComment']['note']))
                data["body"]["contents"].append(template.second_toggle("AutoComment Story", line.settings['autoComment']['story']['status']))
                data["body"]["contents"].append(template.second_toggle("Setkey", line.settings['setKey']['status']))
                data["body"]["contents"].append(template.second_toggle("SleepMode", line.settings['autoRespond']['status']))
                data["body"]["contents"].append(template.second_toggle("Mimic", line.settings['mimic']['status']))
                if to in line.settings['greet']['join']['group'] or line.settings['greet']['join']["allText"]: data2["body"]["contents"].append(template.second_toggle("Greet Join Text", True))
                else: data2["body"]["contents"].append(template.second_toggle("Greet Join Text", False))
                if to in line.settings['greet']['join']['groupSticker'] or line.settings['greet']['join']["allSticker"]: data2["body"]["contents"].append(template.second_toggle("Greet Join Sticker", True))
                else: data2["body"]["contents"].append(template.second_toggle("Greet Join Sticker", False))
                if to in line.settings['greet']['join']['groupImage'] or line.settings['greet']['join']["allImage"]: data2["body"]["contents"].append(template.second_toggle("Greet Join Image", True))
                else: data2["body"]["contents"].append(template.second_toggle("Greet Join Image", False))
                if to in line.settings['greet']['leave']['group'] or line.settings['greet']['leave']["allText"]: data2["body"]["contents"].append(template.second_toggle("Greet Leave Text", True))
                else: data2["body"]["contents"].append(template.second_toggle("Greet Leave Text", False))
                if to in line.settings['greet']['leave']['groupSticker'] or line.settings['greet']['leave']["allSticker"]: data2["body"]["contents"].append(template.second_toggle("Greet Leave Sticker", True))
                else: data2["body"]["contents"].append(template.second_toggle("Greet Leave Sticker", False))
                if to in line.settings['greet']['leave']['groupImage'] or line.settings['greet']['leave']["allImage"]: data2["body"]["contents"].append(template.second_toggle("Greet Leave Image", True))
                else: data2["body"]["contents"].append(template.second_toggle("Greet Leave Image", False))
                data2["body"]["contents"].append(template.second_toggle("CheckContact", line.settings['checkContact']))
                data2["body"]["contents"].append(template.second_toggle("CheckPost", line.settings['checkPost']))
                data2["body"]["contents"].append(template.second_toggle("DetectCall", line.settings['responCall']))
                if to in line.settings['updateProfile']: data2["body"]["contents"].append(template.second_toggle("Detect Update Profile", True))
                else: data2["body"]["contents"].append(template.second_toggle("Detect Update Profile", False))
                data2["body"]["contents"].append(template.second_toggle("Detect Mid", line.setts["detectID"]["mid"]))
                data2["body"]["contents"].append(template.second_toggle("Detect Gid", line.setts["detectID"]["gid"]))
                if to in line.settings['detectUnsend']: data2["body"]["contents"].append(template.second_toggle("Detect Unsend", True))
                else: data2["body"]["contents"].append(template.second_toggle("Detect Unsend", False))
                if to in line.settings['publicBot'] or line.settings["allPublic"]: data2["body"]["contents"].append(template.second_toggle("Public Mode", True))
                else: data2["body"]["contents"].append(template.second_toggle("Public Mode", False))
                data2["body"]["contents"].append(template.second_toggle("Template Mode", line.settings['templateMode']))
                data2["body"]["contents"].append(template.second_toggle("Video Timeline", line.settings['videotl']))
                line.sendLiff(to, [data, data2], mainType=False)
            else:
                res = "S T A T U S"
                res += "\n    {} › AutoAdd".format(bool_dict[line.settings['autoAdd']['status']][4])
                res += "\n    {} › AutoBlock".format(bool_dict[line.settings['autoBlock']['status']][4])
                res += "\n    {} › AutoLeave".format(bool_dict[line.settings['autoLeave']['status']][4])
                res += "\n    {} › AutoJoin".format(bool_dict[line.settings['autoJoin']['status']][4])
                res += "\n    {} › AutoRespondTag".format(bool_dict[line.settings['autoRespondMention']['status']][4])
                res += "\n    {} › AutoRead 1".format(bool_dict[line.settings['autoRead']][4])
                res += "\n    {} › AutoRead 2".format(bool_dict[line.settings['autoReadG']][4])
                res += "\n    {} › AutoLike".format(bool_dict[line.settings['autoLike']['status']][4])
                res += "\n    {} › AutoLike Note".format(bool_dict[line.settings['autoLike']['note']][4])
                res += "\n    {} › AutoLike Story".format(bool_dict[line.settings['autoLike']['story']][4])
                res += "\n    {} › AutoComment".format(bool_dict[line.settings['autoComment']['status']][4])
                res += "\n    {} › AutoComment Note".format(bool_dict[line.settings['autoComment']['note']][4])
                res += "\n    {} › AutoComment Story".format(bool_dict[line.settings['autoComment']['story']['status']][4])
                res += "\n    {} › SetKey".format(bool_dict[line.settings['setKey']['status']][4])
                res += "\n    {} › Sleepmode".format(bool_dict[line.settings['autoRespond']['status']][4])
                res += "\n    {} › Mimic".format(bool_dict[line.settings['mimic']['status']][4])
                if to in line.settings['greet']['join']['group'] or line.settings['greet']['join']["allText"]: res += '\n    ✓ › Greetings Join Text'
                else: res += '\n    ✘ › Greetings Join Text'
                if to in line.settings['greet']['join']['groupSticker'] or line.settings['greet']['join']["allSticker"]: res += '\n    ✓ › Greetings Join Sticker'
                else: res += '\n    ✘ › Greetings Join Sticker'
                if to in line.settings['greet']['join']['groupImage'] or line.settings['greet']['join']["allImage"]: res += '\n    ✓ › Greetings Join Image'
                else: res += '\n    ✘ › Greetings Join Image'
                if to in line.settings['greet']['leave']['group'] or line.settings['greet']['leave']["allText"]: res += '\n    ✓ › Greetings Leave Text'
                else: res += '\n    ✘ › Greetings Leave Text'
                if to in line.settings['greet']['leave']['groupSticker'] or line.settings['greet']['leave']["allSticker"]: res += '\n    ✓ › Greetings Leave Sticker'
                else: res += '\n    ✘ › Greetings Leave Sticker'
                if to in line.settings['greet']['leave']['groupImage'] or line.settings['greet']['leave']["allImage"]: res += '\n    ✓ › Greetings Leave Image'
                else: res += '\n    ✘ › Greetings Leave Image'
                res += "\n    {} › CheckContact".format(bool_dict[line.settings['checkContact']][4])
                res += "\n    {} › CheckPost".format(bool_dict[line.settings['checkPost']][4])
                res += "\n    {} › CheckSticker".format(bool_dict[line.settings['checkSticker']][4])
                res += "\n    {} › DetectCall".format(bool_dict[line.settings['responCall']][4])
                if to in line.settings['updateProfile']: res += "\n    ✓ › Detect Update Profile"
                else: res += "\n    ✘ › Detect Update Profile"
                res += "\n    {} › Detect Mid".format(bool_dict[line.setts["detectID"]["mid"]][4])
                res += "\n    {} › Detect Gid".format(bool_dict[line.setts["detectID"]["gid"]][4])
                if to in line.settings['detectUnsend']: res += '\n    ✓ › Detect Unsend'
                else: res += '\n    ✘ › Detect Unsend'
                if to in line.settings['publicBot'] or line.settings["allPublic"]: res += '\n    ✓ › Public Mode'
                else: res += '\n    ✘ › Public Mode'
                res += "\n    {} › TemplateMode".format(bool_dict[line.settings['templateMode']][4])
                res += "\n    {} › Video Timeline".format(bool_dict[line.settings['videotl']][4])
                line.sendFooter(to, res, reply=True)
                
        elif cmd == 'remote':
            rGroup = ["RCallGroup <numGroup> <num>", "Gpict <num>", "Gcover <num>", "Gname <num>", "Gleave <num>", "GID <num>", "OpenQR <num>", "CloseQR <num>", "Groupinfo <num>", "Groupmem <num>", "Grouppend <num>", "Groupcontact <num>", "Mentionall <num>", "RFakeTag <num>", "Protect Kick <num> <on/off>", "Protect Invite <num> <on/off>", "Protect Cancel <num> <on/off>", "Protect QR <num> <on/off>", "Protect All <num> <on/off>", "Welcome Text <on/off> <num>", "Welcome Image <on/off> <num>", "Welcome Sticker <on/off> <num>", "Leave Text <on/off> <num>", "Leave Image <on/off> <num>", "Leave Sticker <on/off> <num>"]
            rJs = ["Rkickall <num>", "Rcancelall <num>"]
            res = "to view  number group\nType 'Grouplist'"
            res += "\n\n"+str(looping_command(setKey.title(), "› R E M O T E", rGroup))
            res += "\n\n"+str(looping_command(setKey.title(), "› J S  R E M O T E", rJs))
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd == 'system':
            ac = subprocess.getoutput('lsb_release -a')
            am = subprocess.getoutput('cat /proc/meminfo')
            ax = subprocess.getoutput('lscpu')
            core = subprocess.getoutput('grep -c ^processor /proc/cpuinfo ')
            syst = subprocess.getoutput('landscape-sysinfo')
            python_imp = platform.python_implementation()
            python_ver = platform.python_version()
            uptime = subprocess.getoutput('screenfetch')
            for linee in ac.splitlines():
                if 'Description:' in linee:
                    oss = linee.split('Description:')[1].replace(' ','')
            for linee in ax.splitlines():
                if 'Architecture:' in linee:
                    architecture =  linee.split('Architecture:')[1].replace(' ','')
                if 'Vendor ID:' in linee:
                    vendor = linee.split('Vendor ID:')[1].replace(' ','')
                if 'Model name:' in linee:
                    model = linee.split('Model name:')[1].replace(' ',' ')[22:]
            for linee in am.splitlines():
                if 'MemTotal:' in linee:
                    memm = linee.split('MemTotal:')[1].replace(' ','')
                    meme = memm.replace("kB","")
                    mem = convert_size(int(meme))
                if 'MemFree:' in linee:
                    frr = linee.split('MemFree:')[1].replace(' ','')
                    frre = frr.replace("kB","")
                    fr = convert_size(int(frre))
            for linee  in syst.splitlines():
                if 'Usage of /:' in linee:
                    use = linee.split('Usage of /:')[1].replace(' ',' ')[3:][:-27]
                if 'Memory usage:' in linee:
                    memUse = linee.split('Memory usage:')[1].replace(' ', ' ')[1:][:-49]
            res = "› S P E C I F I C A T I O N\n"
            res += "\n• {}CPU Core: {}".format(setKey.title(), core)
            res += "\n• {}Total Memory: {}".format(setKey.title(), mem)
            res += "\n• {}Free Memory: {}".format(setKey.title(), fr)
            res += "\n• {}Usage Of: {}".format(setKey.title(), use)
            res += "\n• {}Memory Usage: {}".format(setKey.title(), memUse)
            res += "\n• {}Architecture: {}".format(setKey.title(), architecture)
            res += "\n• {}Vendor ID: {}".format(setKey.title(), vendor)
            res += "\n• {}Model Name: {}".format(setKey.title(), model)
            res += "\n• {}OS: {}".format(setKey.title(), oss)
            res += "\n• {}Language: {}".format(setKey.title(), python_imp)
            res += "\n• {}Version: {}".format(setKey.title(), python_ver)
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd == 'about':
            if line.getProfile().allowSearchByUserid == True: id = 'ON'
            else: id = 'OFF'
            if line.getProfile().allowSearchByEmail == True: em = 'ON'
            else: em = 'OFF'
            if line.getSettings().privacySearchByPhoneNumber == True: ph = 'ON'
            else: ph = 'OFF'
            seal = line.getSettings().e2eeEnable
            fil = line.getSettings().privacyReceiveMessagesFromNotFriend
            if seal == True: letseal = 'ON'
            else: letseal = 'OFF'
            if fil == True: film = 'OFF'
            else: film = 'ON'
            isiBot = ["Type: SelfBot", "Library: linepy-modified", "By: Alm. Zero-Cool", "Rework: Sozi"]
            isiUser = ["Name: {}".format(line.getProfile().displayName), "IDLine: {}".format(line.getProfile().userid), "Region: {}".format(line.getProfile().regionCode), "Letter Sealing: {}".format(letseal), "Filter Message: {}".format(film), "Receive Message: {}".format(line.settings["amountMessage"]["receive"]), "Sent Message", "    Today: {}".format(line.settings["amountMessage"]["sent"]), "    Total: {}".format(line.settings["amountMessage"]["totalSent"]), "Kick User", "    Today: {}".format(line.settings["amountBackup"]["kick"]), "    Total: {}".format(line.settings["amountBackup"]["totalKick"]), "Invite User", "    Today: {}".format(line.settings["amountBackup"]["invite"]), "    Total: {}".format(line.settings["amountBackup"]["totalInvite"]), "Cancel User", "    Today: {}".format(line.settings["amountBackup"]["cancel"]), "    Total: {}".format(line.settings["amountBackup"]["totalCancel"]), "Allow Search", "    By UserID: {}".format(id), "    By Email: {}".format(em), "    By Phone Num: {}".format(ph)]
            isiThanks = ["SoziBot", "HelloWorld", "Alm. ZeroCool", "TeamNewbieCorp", "Trojans", "Migii"]
            res = "› B O T\n"
            for bot in isiBot:
                res += "\n• {}".format(bot)
            res += "\n\n› U S E R\n"
            for user in isiUser:
                res += "\n• {}".format(user)
            res += "\n\n› T H A N K S\n"
            for thanks in isiThanks:
                res += "\n• {}".format(thanks)
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd == 'points':
            if line.protect["pointMode"]["status"]:
                isi = ['Give <amount> @Mention/Reply', 'AddMember @Mention/Reply', 'DelMember @Mention/<num>', 'List Member', 'My Point']
                line.sendReplyMessage(to, looping_command(setKey.title(), "› P O I N T S", isi), msgIds=msg_id)
        
        elif cmd.startswith('give '):
            if line.protect["pointMode"]["status"]:
                textt = removeCmd(text, setKey)
                sep = textt.split(" ")
                target = []
                if len(sep) >= 2:
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        for mention in mentions['MENTIONEES']:
                            if mention['M'] not in target:
                                target.append(mention['M'])
                    else:
                        return line.sendMessage(to, 'failed give point, you must mention or reply message')
                elif msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        target.append(data._from)
                    else:
                        return line.sendMessage(to, 'Message not found')
                if target:
                    for mid in target:
                        profile = line.getContact(mid)
                        if len(sep) >= 2: poi = int(sep[0])
                        else: poi = int(textt)
                        if mid in line.protect["pointMode"]["user"]:
                            uData = line.protect["pointMode"]["userPoint"][mid]
                            uData["points"] = uData["points"] + poi
                            if '-' in str(poi): pp = 'DECREASE'
                            else: pp = 'INCREASE'
                            line.sendMessage(to, f'[ {pp} POINT ]\n___________________\n𖤬 User: {profile.displayName}\n𖤬 Poin: {uData["points"]}')
                        else:
                            line.sendMessage(to, 'User not found')
        
        elif cmd.startswith('addmember'):
            if line.protect["pointMode"]["status"]:
                target = []
                if cmd == 'addmember':
                    if msg.relatedMessageId:
                        data = line.getReplyMessage(to, msg.relatedMessageId)
                        if data is not None:
                            target.append(data._from)
                        else:
                            return line.sendMessage(to, 'Message not found')
                    else:
                        return line.sendMessage(to, 'failed add member, you must mention or reply message')
                elif 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] not in target:
                            target.append(mention['M'])
                else:
                    return line.sendMessage(to, 'failed add member, you must mention or reply message')
                if target:
                    for mid in target:
                        profile = line.getContact(mid)
                        if mid not in line.protect["pointMode"]["user"]:
                            line.protect["pointMode"]["user"].append(mid)
                            line.protect["pointMode"]["userPoint"][mid] = {
                                "created": str(datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%d-%m-%Y')),
                                "points": 0
                            }
                            line.sendMessage(to, f'[ ADD MEMBER ]\n________________\n𖤬 Created: {line.protect["pointMode"]["userPoint"][mid]["created"]}\n𖤬 User: {profile.displayName}\n𖤬 Poin: {line.protect["pointMode"]["userPoint"][mid]["points"]}')
                        else:
                            line.sendMessage(to, 'failed add member, user already added')
                        time.sleep(0.8)
        
        elif cmd.startswith('delmember '):
            if line.protect["pointMode"]["status"]:
                textt = removeCmd(text, setKey)
                cond = textt.split(' ')
                texttl = textt.lower()
                if line.protect["pointMode"]["user"]:
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        parsed_len = len(mentions['MENTIONEES'])//20+1
                        no = 0
                        res = "╭「 Del Member 」\n"
                        for point in range(parsed_len):
                            mids = []
                            for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                                no += 1
                                if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                    if mid['M'] in line.protect["pointMode"]["user"]:
                                        res += '╰ %i. @! > Deleted\n' % (no)
                                        line.protect["pointMode"]["user"].remove(mid['M'])
                                        del line.protect["pointMode"]["userPoint"][mid]
                                    else:
                                        res += '╰ %i. @! > Not in list\n' % (no)
                                else:
                                    if mid['M'] in line.protect["pointMode"]["user"]:
                                        res += '├ %i. @! > Deleted\n' % (no)
                                        line.protect["pointMode"]["user"].remove(mid['M'])
                                        del line.protect["pointMode"]["userPoint"][mid]
                                    else:
                                        res += '├ %i. @! > Not in list\n' % (no)
                                mids.append(mid['M'])
                            if mids:
                                if res.endswith('\n'): res = res[:-1]
                                if point != 0:
                                    line.sendMention(to, res, mids)
                                else:
                                    line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                res = ""
                    else:
                        targets = filter_target(texttl.replace(cond[0] + " ",""), line.protect["pointMode"]["user"])
                        if targets:
                            parsed_len = len(targets)//20+1
                            no = 0
                            res = "╭「 Del Member 」\n"
                            for point in range(parsed_len):
                                mids = []
                                for mid in targets[point*20:(point+1)*20]:
                                    no += 1
                                    if mid == targets[-1]:
                                        if mid in line.protect["pointMode"]["user"]:
                                            res += '╰ %i. @! > Deleted\n' % (no)
                                            line.protect["pointMode"]["user"].remove(mid)
                                            del line.protect["pointMode"]["userPoint"][mid]
                                        else:
                                            res += '╰ %i. @! > Not in list\n' % (no)
                                    else:
                                        if mid in line.protect["pointMode"]["user"]:
                                            res += '├ %i. @! > Deleted\n' % (no)
                                            line.protect["pointMode"]["user"].remove(mid)
                                            del line.protect["pointMode"]["userPoint"][mid]
                                        else:
                                            res += '├ %i. @! > Not in list\n' % (no)
                                    mids.append(mid)
                                if mids:
                                    if res.endswith('\n'): res = res[:-1]
                                    if point != 0:
                                        line.sendMention(to, res, mids)
                                    else:
                                        line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                    res = ""
                else:
                    line.sendMessage(to, 'Member point empty')
        
        elif cmd == 'list member':
            if line.protect["pointMode"]["status"]:
                if line.protect["pointMode"]["user"]:
                    res = "[ LIST MEMBER POINT ]\n"
                    parsed_len = len(line.protect["pointMode"]["user"])//50+1
                    no = 0
                    for point in range(parsed_len):
                        for member in line.protect["pointMode"]["user"][point*50:(point+1)*50]:
                            no += 1
                            try:
                                profile = line.getContact(member)
                                res += "\n%i. %s  (%i Poin)" % (no, profile.displayName, line.protect["pointMode"]["userPoint"][member]["points"])
                            except:
                                res += "\n%i. %s  (%i Poin)" % (no, 'DELETED ACCOUNT', line.protect["pointMode"]["userPoint"][member]["points"])
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendMessage(to, res)
                        res = ''
                        time.sleep(0.8)
                else:
                    line.sendMessage(to, 'Member point empty')
        
        elif cmd == 'my point':
            if line.protect["pointMode"]["status"]:
                if sender in line.protect["pointMode"]["user"]:
                    line.sendMessage(to, f'[ POINT MEMBER ]\n__________________\n𖤬 Created: {line.protect["pointMode"]["userPoint"][sender]["created"]}\n𖤬 User: {line.getContact(sender).displayName}\n𖤬 Poin: {line.protect["pointMode"]["userPoint"][sender]["points"]}')
                    
        elif cmd.startswith('fancy '):
            sep = removeCmd(text, setKey)
            texttl = sep.lower()
            type = texttl.split(" ")[0]
            fonts = [{'type': 'antrophobia', 'example': 'тєѕт123'}, {'type': 'black_bubble', 'example': '🅣🅔🅢🅣➊➋➌'}, {'type': 'black_square', 'example': '🆃🅴🆂🆃123'}, {'type': 'bold_fraktur', 'example': '𝕿𝕰𝕾𝕿յշՅ'}, {'type': 'bold_script', 'example': '𝓣𝓔𝓢𝓣123'}, {'type': 'contouring1', 'example': 'ⓉⒺⓈⓉ①②③'}, {'type': 'contouring2', 'example': '⒯⒠⒮⒯⑴⑵⑶'}, {'type': 'contouring3', 'example': '[̲̅T][̲̅E][̲̅S][̲̅T][̲̅1][̲̅2][̲̅3]'}, {'type': 'contouring4', 'example': '(̲̅T)(̲̅E)(̲̅S)(̲̅T)(̲̅1)(̲̅2)(̲̅3)'}, {'type': 'currency', 'example': '₮Ɇ₴₮123'}, {'type': 'dirty', 'example': 'ẗệṩẗ123'}, {'type': 'dirty2', 'example': 'ṮỆṨṮ123'}, {'type': 'fancy1', 'example': 'тεsт123'}, {'type': 'fancy10', 'example': 'ɬɛʂɬ123'}, {'type': 'fancy11', 'example': 'ՇєรՇ123'}, {'type': 'fancy12', 'example': 'tєѕt123'}, {'type': 'fancy13', 'example': 'tєรt123'}, {'type': 'fancy14', 'example': 'ȶɛֆȶ123'}, {'type': 'fancy15', 'example': '✞ƎƧ✞123'}, {'type': 'fancy16', 'example': 'ΓΞSΓ123'}, {'type': 'fancy17', 'example': 'ᏆɛֆᏆ123'}, {'type': 'fancy18', 'example': 'ԵҽՏԵ123'}, {'type': 'fancy19', 'example': '꓄ꍟꌗ꓄123'}, {'type': 'fancy2', 'example': 'ㄒ乇丂ㄒ123'}, {'type': 'fancy20', 'example': 'ᵀᴱˢᵀ123'}, {'type': 'fancy21', 'example': 'тeѕт123'}, {'type': 'fancy22', 'example': 'ŤƐらŤ123'}, {'type': 'fancy23', 'example': 'ƬЄƧƬ123'}, {'type': 'fancy24', 'example': 'ϮꂅᏕϮ123'}, {'type': 'fancy25', 'example': 'ｲ乇丂ｲ123'}, {'type': 'fancy26', 'example': '†εš†123'}, {'type': 'fancy27', 'example': 'tēŞt123'}, {'type': 'fancy28', 'example': 'ƬΣƧƬ123'}, {'type': 'fancy29', 'example': '†È§†123'}, {'type': 'fancy3', 'example': 'ŤĔŚŤ123'}, {'type': 'fancy30', 'example': 'ᖶᘿSᖶ123'}, {'type': 'fancy31', 'example': 'ནპჰན123'}, {'type': 'fancy32', 'example': '꓄ꏂꑄ꓄123'}, {'type': 'fancy33', 'example': '꓅ꍟꌚ꓅123'}, {'type': 'fancy34', 'example': 'ꋖꈼꌚꋖ123'}, {'type': 'fancy35', 'example': '੮૯ς੮123'}, {'type': 'fancy36', 'example': 'ԵȝՏԵ123'}, {'type': 'fancy37', 'example': 'ꋖꏹꌚꋖ123'}, {'type': 'fancy38', 'example': 'ꋖꑀꈜꋖ123'}, {'type': 'fancy39', 'example': 'ፕቿነፕ123'}, {'type': 'fancy4', 'example': 'ᏆᎬsᏆ123'}, {'type': 'fancy40', 'example': '꓅ꑾꇘ꓅123'}, {'type': 'fancy41', 'example': 'ț£§ț123'}, {'type': 'fancy42', 'example': 'ţ€$ţ123'}, {'type': 'fancy43', 'example': 'ᖶᙍSᖶ123'}, {'type': 'fancy44', 'example': 'тεƨт123'}, {'type': 'fancy45', 'example': 'тEšт123'}, {'type': 'fancy46', 'example': 'էεʂէ1ԶՅ'}, {'type': 'fancy47', 'example': '†ε$†123'}, {'type': 'fancy48', 'example': 'էεรէ123'}, {'type': 'fancy49', 'example': 'ƬΣЅƬ123'}, {'type': 'fancy5', 'example': 'ᏖᏋᏕᏖ123'}, {'type': 'fancy50', 'example': 'ҬἝṨҬ123'}, {'type': 'fancy51', 'example': '7357123'}, {'type': 'fancy52', 'example': 'τEŠτ123'}, {'type': 'fancy53', 'example': 'ƮęsƮ123'}, {'type': 'fancy54', 'example': '⊥ÈS⊥123'}, {'type': 'fancy55', 'example': 'T£§T123'}, {'type': 'fancy56', 'example': '𝐓𝐄𝐒𝐓𝟏𝟐𝟑'}, {'type': 'fancy57', 'example': '𝚃𝙴𝚂𝚃𝟷𝟸𝟹'}, {'type': 'fancy58', 'example': '𝕿𝕰𝕾𝕿123'}, {'type': 'fancy59', 'example': '𝕋𝔼𝕊𝕋𝟙𝟚𝟛'}, {'type': 'fancy6', 'example': 'ƭεรƭ123'}, {'type': 'fancy60', 'example': '𝗧𝗘𝗦𝗧𝟭𝟮𝟯'}, {'type': 'fancy61', 'example': '𝑇𝐸𝑆𝑇123'}, {'type': 'fancy62', 'example': '𝘛𝘌𝘚𝘛123'}, {'type': 'fancy63', 'example': '𝑻𝑬𝑺𝑻123'}, {'type': 'fancy64', 'example': '𝙏𝙀𝙎𝙏123'}, {'type': 'fancy65', 'example': '𝒯𝐸𝒮𝒯𝟣𝟤𝟥'}, {'type': 'fancy66', 'example': '𝓣𝓔𝓢𝓣𝟏𝟐𝟑'}, {'type': 'fancy67', 'example': 'ＴＥＳＴ１２３'}, {'type': 'fancy68', 'example': '𝔗𝔈𝔖𝔗𝟷𝟸𝟹'}, {'type': 'fancy69', 'example': 'ᵀᴱᶳᵀ¹²³'}, {'type': 'fancy7', 'example': '丅ᗴᔕ丅123'}, {'type': 'fancy70', 'example': 'тEѕт123'}, {'type': 'fancy71', 'example': 'ƬƐѕƬ123'}, {'type': 'fancy72', 'example': 'ƬƐѕƬ123'}, {'type': 'fancy73', 'example': 'ŢĚŞŢ¹²³'}, {'type': 'fancy74', 'example': 'ŧεşŧ123'}, {'type': 'fancy75', 'example': 'ｲ乇ㄎｲ1ᆯ3'}, {'type': 'fancy76', 'example': 'էƐϚէ𝟙ϩӠ'}, {'type': 'fancy77', 'example': 'ƚҽʂƚ123'}, {'type': 'fancy78', 'example': 'tєรt123'}, {'type': 'fancy79', 'example': '†εš†123'}, {'type': 'fancy8', 'example': 'tєรt123'}, {'type': 'fancy80', 'example': 'ƭєƨƭ123'}, {'type': 'fancy81', 'example': 'ƚЄ$ƚ123'}, {'type': 'fancy82', 'example': 'Ŧ£ŞŦ123'}, {'type': 'fancy83', 'example': 'τεȘτ123'}, {'type': 'fancy84', 'example': 'TΞST123'}, {'type': 'fancy85', 'example': 'ŤĚŠŤ¹²³'}, {'type': 'fancy86', 'example': 'ᴛᴇSᴛ₁₂₃'}, {'type': 'fancy9', 'example': 'тeѕт123'}, {'type': 'flip', 'example': 'ꓕEƧꓕƖ53'}, {'type': 'fraktur2', 'example': '𝔗𝔈𝔖𝔗յշՅ'}, {'type': 'handwriting1', 'example': '𝒯𝐸𝒮𝒯123'}, {'type': 'handwriting2', 'example': 'TEST123'}, {'type': 'knight', 'example': 'ṮḕṠṮ123'}, {'type': 'knight2', 'example': 'ṮḔṠṮ123'}, {'type': 'love1', 'example': 'ƬƐSƬ123'}, {'type': 'love2', 'example': 'ŦƐSŦ123'}, {'type': 'mirror', 'example': 'ƸςƖTƧƎT'}, {'type': 'mirror_flip', 'example': 'ƐՇƖꓕSƎꓕ'}, {'type': 'paranormal', 'example': 'tєst123'}, {'type': 'superscript', 'example': 'ᵀᴱˢᵀ¹²³'}, {'type': 'symbols', 'example': '☂€ⓢ☂➊➋➌'}, {'type': 'thin2', 'example': 'ｔｅｓｔ123'}, {'type': 'thin3', 'example': 'ＴＥＳＴ１２３'}, {'type': 'tiny', 'example': 'ᴛᴇᴤᴛ123'}, {'type': 'tiny2', 'example': 'TEST123'}, {'type': 'upside_down', 'example': 'ʇǝsʇ123'}, {'type': 'white_bubble', 'example': 'ⓉⒺⓈⓉ①②③'}, {'type': 'white_square', 'example': '🅃🄴🅂🅃123'}]
            if texttl == 'text':
                res = '› T Y P E\n'
                no = 0
                for font in fonts:
                    no += 1
                    res += '\n• {} : {}'.format(no, font['example'])
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}Fancy <type> <text>'.format(setKey.title())
                res += '\nExample: Fancy 69 your_text'
                line.sendMode(msg, to, sender, cmd, res)
            elif type.isdigit():
                if int(type) <= len(fonts):
                    textts = sep.replace(type + ' ','')
                    texts = text2art(textts, font=fonts[int(type)-1]['type'], chr_ignore=True)
                    line.sendFooter(to, texts, reply=True)
                    
        elif cmd.startswith("bold "):
            sep = removeCmd(text, setKey)
            change = {"a": "𝗮", "b": "𝗯", "c": "𝗰", "d": "𝗱", "e": "𝗲", "f": "𝗳", "g": "𝗴", "h": "𝗵", "i": "𝗶", "j": "𝗷", "k": "𝗸", "l": "𝗹", "m": "𝗺", "n": "𝗻", "o": "𝗼", "p": "𝗽", "q": "𝗾", "r": "𝗿", "s": "𝘀", "t": "𝘁", "u": "𝘂", "v": "𝘃", "w": "𝘄", "x": "𝘅", "y": "𝘆", "z": "𝘇", "A": "𝗔", "B": "𝗕", "C": "𝗖", "D": "𝗗", "E": "𝗘", "F": "𝗙", "G": "𝗚", "H": "𝗛", "I": "𝗜", "J": "𝗝", "K": "𝗞", "L": "𝗟", "M": "𝗠", "N": "𝗡", "O": "𝗢", "P": "𝗣", "Q": "𝗤", "R": "𝗥", "S": "𝗦", "T": "𝗧", "U": "𝗨", "V": "𝗩", "W": "𝗪", "X": "𝗫", "Y": "𝗬", "Z": "𝗭"}
            textt = ""
            for t in sep:
                if t == " ":
                    textt += " "
                else:
                    try:
                        textt += change[t]
                    except:
                        textt += t
            line.sendFooter(to, textt)
            
        elif cmd == 'check limit':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
            status = {"kick": "", "invite": "", "cancel": "", "add": "", "tl": ""}
            try: line.cancelChatInvitation(to, ["u939275e9613cf19261c9945a3c9f0ab0"]);status["cancel"] = "✓ >"
            except: status["cancel"] = "✘ >"
            time.sleep(0.8)
            try: line.deleteOtherFromChat(to, ["u939275e9613cf19261c9945a3c9f0ab0"]);status["kick"] = "✓ >"
            except: status["kick"] = "✘ >"
            time.sleep(0.8)
            try: line.inviteIntoChat(to, [line.profile.mid]);status["invite"] = "✓ >"
            except: status["invite"] = "✘ >"
            time.sleep(0.8)
            idline = line.getProfile().userid
            try: line.findContactsByUserid(idline); status["add"] = "✓ >"
            except: status["add"] = "✘ >"
            cektl = line.getProfileDetail(line.profile.mid)
            if cektl["message"] == 'success': status["tl"] = "✓ >"
            else: status["tl"] = "✘ >"
            time.sleep(0.8)
            isi = ["%s Kick" % status["kick"], "%s Invite" % status["invite"], "%s Cancel" % status["cancel"], "%s Add" % status["add"], "%s Timeline" % status["tl"]]
            line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› A C C O U N T", isi, False))
            
        elif cmd == 'abort':
            aborted = False
            if to in line.settings['changeGroupPicture']:
                line.settings['changeGroupPicture'].remove(to)
                sendToggle(to, "CHANGE GROUP PICTURE", "Change Group Picture\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if to in line.settings['changeGroupCover']:
                line.settings['changeGroupCover'].remove(to)
                sendToggle(to, "CHANGE GROUP COVER", "Change Group Cover\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings['changevp']:
                line.settings['changevp'] = False
                sendToggle(to, "CHANGE VIDEO PROFILE", "Change Video Profile\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings['changePictureProfile']:
                line.settings['changePictureProfile'] = False
                sendToggle(to, "CHANGE PICTURE PROFILE", "Change Picture Profile\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings['changeCoverProfile']:
                line.settings['changeCoverProfile'] = False
                sendToggle(to, "CHANGE COVER PROFILE", "Change Cover Profile\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings['changeCoverVideo']["image"]:
                line.settings['changeCoverVideo']["image"] = False
                sendToggle(to, "CHANGE COVER VIDEO", "Change Cover Video\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings['changeCoverVideo']["video"]:
                line.settings['changeCoverVideo']["video"] = False
                sendToggle(to, "CHANGE COVER VIDEO", "Change Cover Video\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["upImage"]:
                line.setts["upImage"] = False
                sendToggle(to, "UPLOAD IMAGE", "Upload Image\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["autoAddImage"]:
                line.setts["autoAddImage"] = False
                sendToggle(to, "AUTO ADD IMAGE", "Auto Add Image\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["upBackground"]:
                line.setts["upBackground"] = False
                sendToggle(to, "CHANGE TEMP BACKGROUND", "Change Temp Background\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["upStory"]:
                line.setts["upStory"] = False
                sendToggle(to, "UPLOAD STORY", "Upload Story\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["invCon"]:
                line.setts["invCon"] = False
                sendToggle(to, "INVITE CONTACT", "Command Invite Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["delCon"]:
                line.setts["delCon"] = False
                sendToggle(to, "DELETE CONTACT", "Command Delete Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["storyCon"]:
                line.setts["storyCon"] = False
                sendToggle(to, "STORY CONTACT", "Command Story Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["chatCon"]["status"]:
                line.setts["chatCon"]["status"] = False
                sendToggle(to, "CHAT CONTACT", "Command Chat Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["banContact"]:
                line.setts["banContact"] = False
                sendToggle(to, "BAN CONTACT", "Command Ban Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["whiteContact"]:
                line.setts["whiteContact"] = False
                sendToggle(to, "WHITE CONTACT", "Command White Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["assContact"]:
                line.setts["assContact"] = False
                sendToggle(to, "ASSIST CONTACT", "Command Assist Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["adminContact"]:
                line.setts["adminContact"] = False
                sendToggle(to, "ADMIN CONTACT", "Command Admin Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["cloneContact"]:
                line.setts["cloneContact"] = False
                sendToggle(to, "CLONE CONTACT", "Command Clone Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["coverExtraContact"]:
                line.setts["coverExtraContact"] = False
                sendToggle(to, "COVER EXTRA", "Command Cover Extra\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["lastseen"]["status"]:
                line.setts["lastseen"]["status"] = False
                sendToggle(to, "LASTSEEN CONTACT", "Command Lastseen Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["trackCon"]:
                line.setts["trackCon"] = False
                sendToggle(to, "TRACK CONTACT", "Command Track Contact\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["bcImage"]["toFriend"]:
                line.setts["bcImage"]["toFriend"] = False
                sendToggle(to, "BROADCAST IMAGE", "Broadcast Image\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["bcImage"]["toGroup"]:
                line.setts["bcImage"]["toGroup"] = False
                sendToggle(to, "BROADCAST IMAGE", "Broadcast Image\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["bcImage"]["toAll"]:
                line.setts["bcImage"]["toAll"] = False
                sendToggle(to, "BROADCAST IMAGE", "Broadcast Image\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["bcPost"]["toFriend"]:
                line.setts["bcPost"]["toFriend"] = False
                sendToggle(to, "BROADCAST POST", "Broadcast Post\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["bcPost"]["toGroup"]:
                line.setts["bcPost"]["toGroup"] = False
                sendToggle(to, "BROADCAST POST", "Broadcast Post\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["bcPost"]["toAll"]:
                line.setts["bcPost"]["toAll"] = False
                sendToggle(to, "BROADCAST POST", "Broadcast Post\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings["setFlag"]["status"]:
                line.settings["setFlag"]["status"] = False
                sendToggle(to, "SET FLAG ICON", "Set Flag Icon\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["stickerss"]["status"]:
                line.setts["stickerss"]["status"] = False
                sendToggle(to, "ADD STICKER", "Add Sticker\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["greets"]["joinSticker"]:
                line.setts["greets"]["joinSticker"] = False
                sendToggle(to, "SET WELCOME STICKER", "Set Welcome Sticker\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["greets"]["leaveSticker"]:
                line.setts["greets"]["leaveSticker"] = False
                sendToggle(to, "SET LEAVE STICKER", "Set Leave Sticker\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["greets"]["wImage"]:
                line.setts["greets"]["wImage"] = False
                sendToggle(to, "SET WELCOME IMAGE", "Set Welcome Image\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["greets"]["lImage"]:
                line.setts["greets"]["lImage"] = False
                sendToggle(to, "SET LEAVE IMAGE", "Set Leave Image\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings["setcommand"]["mentionStiker"]["status"]:
                line.settings["setcommand"]["mentionStiker"]["status"] = False
                sendToggle(to, "SET MENTION STICKER", "Set Mention Sticker\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings["setcommand"]["fakeTagSticker"]["status"]:
                line.settings["setcommand"]["fakeTagSticker"]["status"] = False
                sendToggle(to, "SET FAKE MENTION STICKER", "Set Fake Mention Sticker\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings["autoComment"]["setsticker"]:
                line.settings["autoComment"]["setsticker"] = False
                sendToggle(to, "AUTO COMMENT STICKER", "Auto Comment Sticker\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["autoAddSticker"]:
                line.setts["autoAddSticker"] = False
                sendToggle(to, "AUTO RESPON ADD STICKER", "Auto Respon Add Sticker\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["tagSticker"]:
                line.setts["tagSticker"] = False
                sendToggle(to, "AUTO RESPON TAG STICKER", "Auto Respon Tag Sticker\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if to in line.setts["uploadNote"]:
                del line.setts["uploadNote"][to]
                sendToggle(to, "CREATE NOTE MEDIA", "Create Note Media\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if to in line.setts["uploadTL"]:
                del line.setts["uploadTL"][to]
                sendToggle(to, "CREATE TIMELINE MEDIA", "Create Timeline Media\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings["setcommand"]["kicks"]["status"]:
                line.settings["setcommand"]["kicks"]["status"] = False
                sendToggle(to, "AUTO KICK BY STICKER", "Auto Kick by Sticker\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.settings["setcommand"]["invites"]["status"]:
                line.settings["setcommand"]["invites"]["status"] = False
                sendToggle(to, "AUTO INVITE BY STICKER", "Auto Invite by Sticker\nStatus: ✘", text2="", toggle=False)
                aborted = True
            if line.setts["inviteAlot"]["status"]:
                line.setts["inviteAlot"]["status"] = False
                res = ""
                if line.setts["inviteAlot"]["name"] != "":
                    if line.setts["inviteAlot"]["name"] in line.protect['contact_list']:
                        res = f'Keyword: {line.setts["inviteAlot"]["name"]}\nTotal Team: {len(line.protect["contact_list"][line.setts["inviteAlot"]["name"]])}'
                line.setts["inviteAlot"]["name"] = ""
                sendToggle(to, "ADD TEAM CONTACT", f"Add Team by Contact\nStatus: ✘\n{res}", text2=res, toggle=False)
                aborted = True
            if not aborted:
                line.sendMode(msg, to, sender, cmd, 'There are no commands to cancel')

        elif cmd == "me":
            profile = line.getContact(sender)
            cover = line.getProfileCoverURL(sender)
            if "/vc/" in cover: cover = cover.replace("/vc/", "/c/")
            if profile.pictureStatus: picture = "https://obs.line-scdn.net/" + str(profile.pictureStatus)
            else: picture = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
            if profile.statusMessage == "": status = "empty"
            else: status = profile.statusMessage
            data = template.sendMe(profile.mid, profile.displayName, picture, cover, status)
            line.sendLiff(to, data, mainType=False)
            line.sendContact(to, line.profile.mid)
        
        elif cmd == 'logoutbot':
            line.sendFooter(to, 'Successfully logout\nhttps://line.me/R/nv/connectedDevices')
            sys.exit('##----- PROGRAM STOPPED -----##')
            
        elif cmd == 'restartbot':
            line.sendMessage(to, 'tunggu sebentar....')
            line.settings['restartPoint'] = to
            restartProgram()
            
        elif cmd == 'mytoken':
            line.sendFooter(to, "Authtoken:\n%s" % (line.authToken))
        
        elif cmd == 'check e2ee':
            line.sendFooter(to, 'E2EE Active: {}'.format(len(line.talk.getE2EEPublicKeys())))
        
        #elif cmd == 'remove e2ee':
            #for publicKey in line.talk.getE2EEPublicKeys():
                #line.talk.removeE2EEPublicKey(publicKey)
            #line.sendFooter(to, 'All E2EE Removed')
            
        elif cmd == "gift":
            line.sendGift(to, '5732b0cf-9954-4f95-b64a-9e57512bcd79', 'theme')
        
        elif cmd == 'speed':
            start = time.time()
            batas = line.getProfile()
            elapse = time.time() - start
            last = elapse * 1000
            line.sendMessage(to, "%s ms" % (round(last, 1)))
            
        elif cmd == 'clear sampah':
            a = os.popen('sync; echo 3 > /proc/sys/vm/drop_caches').read()
            am = subprocess.getoutput('cat /proc/meminfo')
            for linee in am.splitlines():
                if 'MemTotal:' in linee:
                    memm = linee.split('MemTotal:')[1].replace(' ','')
                    meme = memm.replace("kB","")
                    mem = convert_size(int(meme))
                if 'MemFree:' in linee:
                    frr = linee.split('MemFree:')[1].replace(' ','')
                    frre = frr.replace("kB","")
                    fr = convert_size(int(frre))
            tmp = os.popen('cd /tmp && rm *.bin').read()
            line.sendMode(msg, to, sender, cmd, "Total Memory: {}\nFree Memory: {}".format(mem, fr))
            
        elif cmd == 'creator':
            time.sleep(0.5)
            line.sendContact(to, sozi) #Creator jangan diganti ya :)
            line.sendMention(to, 'sozi  @!', [sozi])
            
        elif cmd == "backup":
            line.backupProfile(msg, sender, to)
            
        elif cmd == "restore":
            line.restoreProfile(msg, sender, to)
        
        elif cmd == "clear data":
            groups = line.getAllChatMids(True, False).memberChatMids
            if groups:
                line.sendMessage(to, "Check data....")
                for nUp in line.settings["updateProfile"]:
                    if nUp not in groups:
                        line.settings["updateProfile"].remove(nUp)
                for nFilter in line.settings["bcFilter"]:
                    if nFilter not in groups:
                        line.settings["bcFilter"].remove(nFilter)
                for nMute in line.settings["offbot"]:
                    if nMute not in groups:
                        line.settings["offbot"].remove(nMute)
                for proInv in line.protect["proInv"]:
                    if proInv not in groups:
                        line.protect["proInv"].remove(proInv)
                for proQr in line.protect["proQr"]:
                    if proQr not in groups:
                        line.protect["proQr"].remove(proQr)
                for proKick in line.protect["proKick"]:
                    if proKick not in groups:
                        line.protect["proKick"].remove(proKick)
                for proCancel in line.protect["proCancel"]:
                    if proCancel not in groups:
                        line.protect["proCancel"].remove(proCancel)
                for gUnsend in line.settings["detectUnsend"]:
                    if gUnsend not in groups:
                        line.settings["detectUnsend"].remove(gUnsend)
                    for idMsg in line.unsend:
                        if "image" in line.unsend[idMsg]:
                            line.deleteFile(line.unsend[idMsg]['image'])
                        elif "video" in line.unsend[idMsg]:
                            line.deleteFile(line.unsend[idMsg]['video'])
                        del line.unsend[idMsg]
                for gPub in line.settings["publicBot"]:
                    if gPub not in groups:
                        line.settings["publicBot"].remove(gPub)
                for gWel in line.settings["greet"]["join"]["group"]:
                    if gWel not in groups:
                        line.settings["greet"]["join"]["group"].remove(gWel)
                for gWels in line.settings["greet"]["join"]["groupSticker"]:
                    if gWels not in groups:
                        line.settings["greet"]["join"]["groupSticker"].remove(gWels)
                for gWeli in line.settings["greet"]["join"]["groupImage"]:
                    if gWeli not in groups:
                        line.settings["greet"]["join"]["groupImage"].remove(gWeli)
                for gLev in line.settings["greet"]["leave"]["group"]:
                    if gLev not in groups:
                        line.settings["greet"]["leave"]["group"].remove(gLev)
                for gLevs in line.settings["greet"]["leave"]["groupSticker"]:
                    if gLevs not in groups:
                        line.settings["greet"]["leave"]["groupSticker"].remove(gLevs)
                for gLevi in line.settings["greet"]["leave"]["groupImage"]:
                    if gLevi not in groups:
                        line.settings["greet"]["leave"]["groupImage"].remove(gLevi)
                if line.settings["getPc"]:
                    line.settings["getPc"] = {}
                if line.settings["dataAdders"]:
                    line.settings["dataAdders"].clear()
                line.sendMode(msg, to, sender, cmd, "Successfully cleared unused data")

        elif cmd.startswith("creategroup "):
            name = removeCmd(text, setKey)
            line.createChat(name, [line.profile.mid])
            gids = line.getGroupIdsByName(name)
            for gid in gids:
                chat = line.getChats([gid], False, False)
                chat.chats[0].extra.groupExtra.preventedJoinByTicket = False
                line.updateChat(chat.chats[0], 4)
                line.sendFooter(to, 'Group Name: {}\nQR: https://line.me/R/ti/g/{}'.format(str(name), str(line.reissueChatTicket(gid).ticketId)), reply=True)
                
        elif cmd.startswith("lastseen "):
            sep = removeCmd(text, setKey)
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    profile = line.getContact(mention['M'])
                    if profile.mid in line.setts["lastseen"]["user"]:
                        res = 'Name: {}\n'.format(profile.displayName)
                        sort = sorted(line.setts["lastseen"]["user"][profile.mid])
                        parsed_len = len(sort)//20+1
                        for point in range(parsed_len):
                            for gid in sort[point*20:(point+1)*20]:
                                secs = time.time() - line.setts["lastseen"]["user"][profile.mid][gid]["time"]
                                waktu = timeChange(secs)
                                res += '\nGroup: {}'.format(line.getChats([line.setts["lastseen"]["user"][profile.mid][gid]["group"]], False, False).chats[0].chatName)
                                res += '\nLastseen {} ago\n'.format(waktu)
                            if res.startswith('\n'): res = res[1:len(res)]
                            if res.endswith('\n'): res = res[:-1]
                            line.sendMode(msg, to, sender, cmd, res)
                            res = ''
                    else:
                        line.sendReplyMention(to, "Target: @!\nData empty", [profile.mid], msgIds=msg_id)
            elif sep.lower() == 'contact':
                line.setts["lastseen"]["status"] = True
                res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                sendToggle(to, "LASTSEEN CONTACT", res, res, True)
                
        elif cmd.startswith("track "):
            sep = removeCmd(text, setKey)
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    profile = line.getContact(mention['M'])
                    aa = line.getAllChatMids(True, False).memberChatMids
                    target = profile.mid
                    lacak = ""
                    num = 1
                    for gid in aa:
                        bb = line.getChats([gid], True, False).chats[0]
                        if target in bb.extra.groupExtra.memberMids:
                            lacak += "\n    {}. {}".format(num, bb.chatName)
                            num = (num+1)
                    if lacak == "":
                        line.sendMode(msg, to, sender, cmd, 'Not found')
                    else:
                        pesan = "Name: {}\nHe is in the group:{}".format(profile.displayName, lacak)
                        line.sendMode(msg, to, sender, cmd, pesan)
            elif sep.lower() == 'contact':
                line.setts["trackCon"] = True
                res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                sendToggle(to, "TRACK CONTACT", res, res, True)
        
        elif cmd.startswith("clonemid "):
            userMid = removeCmd(text, setKey)
            line.cloneContactProfile(msg, userMid, sender, to)

        elif cmd.startswith("clone "):
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    profile = line.getContact(mention['M'])
                    line.cloneContactProfile(msg, profile.mid, sender, to)
            elif cmd == 'clone contact':
                line.setts["cloneContact"] = True
                res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                sendToggle(to, "CLONE CONTACT", res, res, True)
        
        elif cmd.startswith('timelinecv '):
            urlnya = removeCmd(text, setKey)
            if 'timeline.line.me/post' in urlnya:
                sep = urlnya.split('/')
                postId = sep[len(sep)-1]
                r = line.getPost(line.profile.mid, postId)
                if r is None: return line.sendReplyMessage(to, 'LIMIT TIMELINE!!!\nwait untill limit done', msgIds=msg_id)
                data = r["result"]["feed"]["post"]["postInfo"]
                line.sendFooter(to, 'https://line.me/R/home/post?userMid={}&postId={}'.format(data["homeId"], data["postId"]))
            else:
                line.sendMode(msg, to, sender, cmd, 'You must enter the correct url')

        elif cmd.startswith('sendvideo '):
            textnya = removeCmd(text, setKey)
            line.sendMessage(to, 'wait a minute, the video is on download..')
            line.sendVideoWithURL(to, textnya)
            
        elif cmd.startswith('sendgif '):
            textnya = removeCmd(text, setKey)
            line.sendGIFWithURL(to, textnya)
            
        elif cmd.startswith('sendpicture '):
            textnya = removeCmd(text, setKey)
            line.sendLiffImage(to, textnya, line.settings["setFlag"]["icon"], " Picture", reply=True)
        
        elif cmd.startswith('sendnomor '):
            textt = removeCmd(text, setKey)
            noTe = textt.split(" ")
            nama = textt.replace(noTe[0] + " ","")
            if noTe[0].isdigit():
                contentMetadata = {
                    'vCard': 'BEGIN:VCARD\r\nVERSION:3.0\r\nPRODID:ANDROID 10.16.3 Android OS 8.1\r\nFN:\\{}\r\nTEL;TYPE=mobile:{}\r\nN:?;\\,\r\nEND:VCARD\r\n'.format(nama, noTe[0]),
                    'displayName': nama
                }
                line.sendMessage(to, text, contentMetadata, 13)
                
        elif cmd.startswith('sendcontact '):
            midnya = removeCmd(text, setKey)
            line.sendContact(to, midnya)
            
        elif cmd.startswith('sendaudio '):
            textnya = removeCmd(text, setKey)
            line.sendMessage(to, 'wait a minute, audio is on download..')
            line.sendAudioWithURL(to, textnya)
        
        elif cmd.startswith('say '):
            textnya = removeCmd(text, setKey)
            if "@!" in textnya:
                line.sendReplyMention(to, textnya, [sender], msgIds=msg_id)
            else:
                if 'MENTION' in msg.contentMetadata != None:
                    arrData = []
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        arrData.append({'S': str(int(mention['S'])-(len(setKey)+4)), 'E': str(int(mention['E'])-(len(setKey)+4)), 'M': mention['M']})
                    line.sendReplyMessage(to, textnya, {'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')}, 0, msgIds=msg_id)
                else:
                    line.sendReplyMessage(to, textnya, msgIds=msg_id)

        elif cmd == 'spam':
            isi = ["Spam 1 <text>|<num>", "Spam 2 @Mention|<num>", "Spam 3 @Mention|<num>", "Spam 3 <mid>|<num>", "Callgroup <num>", "Call @Mention <num>"]
            res = looping_command(setKey.title(), "› S P A M", isi)
            res += "\n\nExample: Spam 1 Sozi|10"
            res += "\n\nFYI: spam with a large number of dangerous, can cause the account to freeze 1 hour / 1 day"
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith("spam 1"):
            txtt = removeCmd(text, setKey)
            txt = txtt.replace(txtt.split(" ")[0] + " ","")
            cond = txt.split("|")
            if len(cond) == 2:
                text = str(cond[0])
                if cond[1].isdigit():
                    num = int(cond[1])
                    for var in range(0, num):
                        if var == 0:
                            line.sendReplyMessage(to, text, msgIds=msg_id)
                        else:
                            line.sendMessage(to, text)
                        
        elif cmd.startswith('spam 2'):
            sep = text.split("|")
            if len(sep) == 2:
                if sep[1].isdigit():
                    num = int(sep[1])
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        for mention in mentions['MENTIONEES']:
                            mid = mention['M']
                            for var in range(0, num):
                                if var == 0:
                                    line.sendReplyMention(to, '@!', [mid], msgIds=msg_id)
                                else:
                                    line.sendMention(to, '@!', [mid])
                            
        elif cmd.startswith("spam 3 "):
            txtt = removeCmd(text, setKey)
            txt = txtt.replace(txtt.split(" ")[0] + " ","")
            cond = txt.split("|")
            if len(cond) == 2:
                if cond[1].isdigit():
                    num = int(cond[1])
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        for mention in mentions['MENTIONEES']:
                            mid = mention['M']
                            for var in range(0, num):
                                line.sendGift(mid, '5732b0cf-9954-4f95-b64a-9e57512bcd79', 'theme')
                            line.sendMode(msg, to, sender, cmd, "Succeed Spam {} Gift".format(num))
                    else: 
                        mid = cond[0]
                        if mid.startswith("u"):
                            if len(mid) == 33:
                                for var in range(0, num):
                                    line.sendGift(mid, '5732b0cf-9954-4f95-b64a-9e57512bcd79', 'theme')
                                line.sendMode(msg, to, sender, cmd, "Succeed Spam {} Gift".format(num))
                            else:
                                line.sendFooter(to, " mid invalid", reply=True)
                        else:
                            line.sendFooter(to, " mid invalid", reply=True)
                            
        elif cmd == 'runtime':
            runtime = time.time() - programStart
            line.sendMode(msg, to, sender, cmd, '' + format_timespan(runtime))
            
        elif cmd.startswith('cekpc'):
            textt = removeCmd(text, setKey)
            if cmd == "cekpc":
                isi = ["Cekpc List", "Cekpc Clear", "Cekpc <num>", "Delpc <num>", "Replypc <num> <text>"]
                line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› C O M M A N D", isi))
            elif textt.lower() == 'list':
                if line.settings["getPc"]:
                    mids = [a for a in line.settings["getPc"]]
                    k = len(mids)//20+1
                    no = 0
                    for point in range(k):
                        res = f'**({len(mids)}) Pesan Masuk**'
                        midss = []
                        for mid in mids[point*20:(point+1)*20]:
                            no += 1
                            midss.append(mid)
                            res += f'\n{no}. @! {len(line.settings["getPc"][mid]["message"])}x'
                        if midss:
                            if point != 0:
                                ress = res.replace(f'**({len(mids)}) Pesan Masuk**\n', '')
                                if ress.endswith("\n"): ress = ress[:-1]
                                line.sendMention(to, ress, midss)
                            else:
                                line.sendReplyMention(to, res, midss, msgIds=msg_id)
                else:
                    line.sendMode(msg, to, sender, cmd, "No incoming messages")
            elif textt.lower() == 'clear':
                if line.settings["getPc"]:
                    line.settings["getPc"].clear()
                    line.sendMode(msg, to, sender, cmd, 'Data personal chat cleared successfully')
                else:
                    line.sendMode(msg, to, sender, cmd, "No incoming messages")
            elif textt.isdigit():
                num = int(textt)
                if line.settings["getPc"]:
                    midss = [a for a in line.settings["getPc"]]
                    target = midss[num - 1]
                    jumlah = len(line.settings["getPc"][target]["message"])
                    res = f'**({jumlah}) Pesan**'
                    res += '\nUser: @!'
                    for pc in range(jumlah):
                        waktu = time.time() - line.settings["getPc"][target]["time"][pc]
                        chat = line.settings["getPc"][target]["message"][pc]
                        final = timeChange(waktu)
                        res += f'\n\n=> {final} yang lalu\nPesan: {chat}'
                    if res.endswith("\n"): res = res[:-1]
                    long = len(res)//10000+1
                    for press in range(long):
                        if press != 0:
                            ress = res[press*10000 : (press+1)*10000]
                            line.sendFooter(to, ress)
                        else:
                            ress = res[press*10000 : (press+1)*10000]
                            line.sendReplyMention(to, ress, [target], msgIds=msg_id)
        elif cmd.startswith("delpc "):
            sep = removeCmd(text, setKey)
            if sep.isdigit():
                if line.settings["getPc"]:
                    midss = [a for a in line.settings["getPc"]]
                    target = midss[int(sep) - 1]
                    del line.settings["getPc"][target]
                    line.sendMention(to, '-> User: @!\nData telah dihapus', [target])
        elif cmd.startswith("replypc "):
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if len(sep) >= 2:
                if line.settings["getPc"]:
                    if sep[0].isdigit():
                        num = int(sep[0])
                        text_nya = textt.replace(sep[0] + " ","")
                        midss = [a for a in line.settings["getPc"]]
                        target = midss[num - 1]
                        line.sendMessage(target, str(text_nya))
                        line.sendMention(to, 'Successfully sent message to @!', [target])
                        del line.settings["getPc"][target]
                    
        elif cmd == "who tag":
            if sender in line.profile.mid:
                if msg.toType != 2: return line.sendFooter(to, 'command it can only be used in groups!!')
                if to in line.setts["whoTag"]:
                    moneys = {}
                    msgas = ''
                    for a in line.setts["whoTag"][to].items():
                        moneys[a[0]] = [a[1]['msg_id'],a[1]['timeChange']] if a[1] is not None else idnya
                    sort = sorted(moneys)
                    sort.reverse()
                    sort = sort[0:]
                    k = len(sort)//10+1
                    no = 0
                    for point in range(k):
                        msgas = '「 Data Mention 」'
                        h = []
                        for target in sort[point*10:(point+1)*10]:
                            no += 1
                            h.append(target)
                            has = ''
                            nol = -1
                            for kucing in moneys[target][0]:
                                nol += 1
                                has += '\nhttps://line.me/R/nv/chatMsg?chatId={}&messageId={} {}'.format(to,kucing,humanize.naturaltime(datetime.fromtimestamp(moneys[target][1][nol]/1000)))
                            if target == sort[0]:
                                msgas += '\n{}. @! {}x{}'.format(no,len(moneys[target][0]),has)
                            else:
                                msgas += '\n\n{}. @! {}x{}'.format(no,len(moneys[target][0]),has)
                        if h:
                            if point != 0:
                                msgass = msgas.replace('「 Data Mention 」\n\n','')
                                if msgass.endswith("\n"): msgass = msgass[:-1]
                                line.sendMention(to, msgass, h)
                            else:
                                line.sendReplyMention(to, msgas, h, msgIds=msg_id)
                        try:
                            del line.setts["whoTag"][to]
                        except:
                            pass
                else:
                    msgas = 'Group: {}\nNo data has been saved for this group'.format(line.getChats([to], False, False).chats[0].chatName)
                    line.sendMode(msg, to, sender, cmd, msgas)
        
        elif cmd.startswith('tagname '):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            name = removeCmd(text, setKey)
            if name == '' or name == " ": return
            group = line.getChats([to], True, True).chats[0]
            members = make_list(group.extra.groupExtra.memberMids) + make_list(group.extra.groupExtra.inviteeMids)
            mids = []
            for member in members:
                try: contact = line.getContact(member)
                except: continue
                if contact.displayNameOverridden:
                    if name in contact.displayNameOverridden.lower():
                        mids.append(member)
                        time.sleep(0.8)
                if name in contact.displayName.lower():
                    if member not in mids:
                        mids.append(member)
                        time.sleep(0.8)
            if not mids:
                line.sendMode(msg, to, sender, cmd, "No member found by name '{}'".format(name))
            else:
                if line.profile.mid in mids: mids.remove(line.profile.mid)
                parsed_len = len(mids)//20+1
                result = '𝗠𝗲𝗻𝘁𝗶𝗼𝗻 𝗡𝗮𝗺𝗲\n'
                for point in range(parsed_len):
                    target = []
                    for mid in mids[point*20:(point+1)*20]:
                        result += '➡️ › @!\n'
                        if mid == mids[-1]:
                            result += '𝗧𝗼𝘁𝗮𝗹: %i 𝗠𝗲𝗺𝗯𝗲𝗿𝘀' % len(mids)
                        target.append(mid)
                    if target:
                        if result.endswith('\n'): result = result[:-1]
                        line.sendReplyMention(to, result, target, msgIds=msg_id)
                    result = ''
                    
        elif cmd.startswith("unsend "):
            if line.server.APP_TYPE == 'CHROMEOS': return line.sendFooter(to, 'APP_TYPE CHROME not support fitur unsend')
            args = removeCmd(text, setKey)
            if args.isdigit():
                mes = int(args)
                M = line.getRecentMessagesV2(to, 1001)
                MId = []
                for ind,i in enumerate(M):
                    if ind == 0:
                        pass
                    else:
                        if i._from == line.profile.mid:
                            MId.append(i.id)
                            if len(MId) == mes:
                                break
                def unsMes(id):
                    line.unsendMessage(id)
                for i in MId:
                    thread1 = threading.Thread(target=unsMes, args=(i,))
                    thread1.daemon = True
                    thread1.start()
                    thread1.join()
                if sender == line.profile.mid:
                    line.unsendMessage(msg_id)
        #elif cmd == 'my location':
            #line.sendLocation(to, 'Jl. SELFBOT-sozi ©A_Code44', -6.573346, 106.721511)

        elif cmd == "uploadimage":
            line.setts["upImage"] = True
            res = 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
            sendToggle(to, "UPLOAD IMAGE", res, res, True)
        
        elif cmd == "api usage":
            eate = requests.get("https://api.coursehero.store/status?apikey={}".format(eaterApikey)).json()
            troj = requests.get("https://apitrojans.xyz/status?apikey={}".format(trojansApikey)).json()
            ren = requests.get("https://api.imjustgood.com/status?apikey={}".format(rendyApikey), headers={"apikey": rendyApikey, "User-Agent": "Justgood/5.0"}).json()
            res = '› EATER API ‹'
            res += '\n\nHost: https://api.coursehero.store'
            res += '\nGithub: https://github.com/hert0t'
            res += f'\nCredit: {eate["result"].split(" ")[-1]}'
            res += '\n\n› TROJANS API ‹'
            res += '\n\nHost: https://apitrojans.xyz'
            res += f'\nExpired: {troj["result"]["expired"]}'
            res += f'\nUsage: {troj["result"]["usage"]}'
            res += '\n\n› IMJUSTGOOD API ‹'
            res += '\n\nHost: https://api.imjustgood.com'
            res += f'\nExpired: {ren["result"]["expired"]}'
            res += f'\nUsage: {ren["result"]["usage"]}'
            line.sendMessage(to, res)
            
        elif cmd.startswith('primary '):
            authKey = removeCmd(text, setKey)
            if isinstance(authKey, str):
                authKey = authKey.encode()
            split = authKey.split(b':')
            if len(split) == 2:
                str1 = split[0]
                m = None
                str2 = split[1]
            elif len(split) == 3:
                str1 = split[0]
                m = split[1]
                str2 = split[2]
            else:
                return line.sendFooter(to, 'Invalid authKey: %s'%authKey)
            currentMillis = (int(time.time() * 1000))
            str3 = base64.b64encode(b"iat: %d\n" % currentMillis) + b'.'
            HMAC = hmac.new(base64.b64decode(str2), str3, hashlib.sha1)
            str4 = base64.b64encode(HMAC.digest())
            str5 = str3 + b"." + str4
            if m is None:
                aa = (str1 + b":" + str5).decode()
                line.sendFooter(to, 'Token Primary:\n{}'.format(str(aa)), line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)
            else:
                bb = (str1 + b":" + m + b":" + str5).decode()
                line.sendFooter(to, 'Token Primary:\n{}'.format(str(bb)), line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)
               
        elif cmd.startswith("secondary "):
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if len(sep) == 2:
                if sep[0].lower() not in ['mac', 'dwin', 'chrome', 'ipad', 'lite']:
                    return line.sendMode(msg, to, sender, cmd, 'Invalid APP\n\n1. Mac\n2. Dwin\n3. Ipad\n4. Chrome\n5. Lite')
                random.seed = (os.urandom(1024))
                randomName = ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(6))
                if sep[0].lower() == 'mac':
                    appN = 'DESKTOPMAC\t{}\tACODE-{}\t{};SECONDARY'.format(line.server.APP_VERSION["DESKTOPMAC"], randomName, line.server.SYSTEM_VERSION["DESKTOPMAC"])
                elif sep[0].lower() == 'dwin':
                    appN = 'DESKTOPWIN\t{}\tACODE-{}\t{};SECONDARY'.format(line.server.APP_VERSION["DESKTOPWIN"], randomName, line.server.SYSTEM_VERSION["DESKTOPWIN"])
                elif sep[0].lower() == 'chrome':
                    appN = 'CHROMEOS\t{}\tACODE-{}\t{};SECONDARY'.format(line.server.APP_VERSION["CHROMEOS"], randomName, line.server.SYSTEM_VERSION["CHROMEOS"])
                elif sep[0].lower() == 'ipad':
                    appN = 'IOSIPAD\t{}\tACODE-{}\t{};SECONDARY'.format(line.server.APP_VERSION["IOSIPAD"], randomName, line.server.SYSTEM_VERSION["IOSIPAD"])
                elif sep[0].lower() == 'lite':
                    appN = 'ANDROIDLITE\t{}\tACODE-{}\t{};SECONDARY'.format(line.server.APP_VERSION["ANDROIDLITE"], randomName, line.server.SYSTEM_VERSION["ANDROIDLITE"])
                headers = {
                    "apikey": eaterApikey,
                    "appname": appN,
                    "sysname": 'SOZI-{}'.format(randomName),
                    "authtoken": sep[1]
                }
                main = json.loads(requests.get("https://api.coursehero.store/lineprimary2second", headers=headers).text)
                if main["status"] != 200:
                    line.sendFooter(to, "✘ ERROR\n" + main["reason"])
                else:
                    line.sendFooter(to, "AuthToken: "+ main["result"]["token"], line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)
                
        elif cmd.startswith("likepost "):
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    profile = line.getContact(mention['M'])
                    data = line.getHomeProfile(profile.mid, 5)
                    if "feeds" in data["result"]:
                        for post in data["result"]["feeds"]:
                            line.likePost(profile.mid, int(post["feedInfo"]["id"]), 1001)
                            time.sleep(0.8)
                        line.sendMention(to, 'Successfully liked the post @!', [profile.mid])
                    else: line.sendFooter(to, 'There are no posts to like', reply=True)
            else: line.sendFooter(to, 'example:\nLikepost @Mention', reply=True)
            
        elif cmd.startswith("timeline "):
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    profile = line.getContact(mention['M'])
                    data = line.getHomeProfile(profile.mid)
                    if "feeds" in data["result"]:
                        no = 1
                        a = " 「 Timeline @! 」"#+str(data['result']['homeInfo']['userInfo']['nickname'])
                        for i in data['result']['feeds']:
                            gtime = i['post']['postInfo']['createdTime']
                            try: desc ="\n\n" + str(no) + ". Text : "+str(i['post']['contents']['text'])
                            except: desc ="\n\n" + str(no) + ". Text : None"
                            a += str(desc)
                            try: a +="\n    Total Like : "+str(i['post']['postInfo']['likeCount'])
                            except: a +="\n    Total Like : 0"
                            try: a +="\n    Total Comment : "+str(i['post']['postInfo']['commentCount'])
                            except: a +="\n    Total Comment : 0"
                            a += "\n    URL: https://line.me/R/home/post?userMid={}&postId={}".format(i['post']['postInfo']["homeId"], i['post']['postInfo']["postId"])
                            no = (no+1)
                        a +="\n\nTotal Post : "+str(data['result']['homeInfo']['postCount'])+" Post."
                        line.sendReplyMention(to, a, [profile.mid], msgIds=msg_id)
                    else: line.sendFooter(to, 'No posts', reply=True)
            else: line.sendFooter(to, 'example:\nTimeline @Mention', reply=True)
                    
        elif cmd.startswith('encode '):
            query = removeCmd(text, setKey)
            line.sendFooter(to, base64.b64encode(query.encode()).decode())
            
        elif cmd.startswith('decode '):
            query = removeCmd(text, setKey)
            line.sendFooter(to, base64.b64decode(query.encode()).decode())
        
        elif cmd.startswith('rnumber '):
            textt = removeCmd(text, setKey)
            sep = textt.split('-')
            if len(sep) == 2:
                if sep[0].isdigit() and sep[1].isdigit():
                    num1 = int(sep[0])
                    num2 = int(sep[1])
                    if num1 >= num2:
                        return line.sendReplyMessage(to, 'the first number must not exceed the second number', msgIds=msg_id)
                    line.sendMessage(to, 'Loading...')
                    time.sleep(3)
                    result = random.randint(num1, num2)
                    res = f'Min: {num1}'
                    res += f'\nMax: {num2}'
                    res += f'\n\nResult: {result}'
                    line.sendReplyMessage(to, res, msgIds=msg_id)
                else:
                    line.sendReplyMessage(to, 'Example: RandomNumber 0-100', msgIds=msg_id)
            else:
                line.sendReplyMessage(to, 'Example: RandomNumber 0-100', msgIds=msg_id)

        elif cmd.startswith('idline '):
            query = removeCmd(text, setKey)
            try:
                profile = line.findContactsByUserid(query)
                line.sendContact(to, profile.mid)
            except TalkException as e:
                if e.code == 5:
                    line.sendMode(msg, to, sender, cmd, "No account using ID '%s'" % (query))
            
        elif cmd.startswith('inviteid '):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            query = removeCmd(text, setKey)
            try:
                profile = line.findContactsByUserid(query)
                friends = line.getAllContactIds()
                if profile.mid not in friends:
                    line.findAndAddContactsByMid(profile.mid)
                    time.sleep(0.8)
                group = line.getChats([to], True, False).chats[0].extra.groupExtra.memberMids
                inviteIntoChat(to, [profile.mid])
                line.sendContact(to, profile.mid)
            except TalkException as e:
                if e.code == 5:
                    line.sendMode(msg, to, sender, cmd, "No account using ID '%s'" % (query))

        elif cmd == 'gtts':
            res = "› G T T S"
            res += "\n\n• {}Say-<countryCode> <text>".format(setKey.title())
            res += "\n• {}Say-<countryCode>".format(setKey.title())
            res += "\n\nExample: {}Say-en You".format(setKey.title())
            res += "\nWith Reply: {}Say-en".format(setKey.title())
            res += "\n\nCountry Code:"
            res += template.countryCode()
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith('say-'):
            sep = text.split("-")
            sep = sep[1].split(" ")
            cCode = sep[0]
            if len(sep) == 1:
                if msg.relatedMessageId is not None:
                    textts = line.getReplyMessage(to, msg.relatedMessageId)
                    if textts is not None:
                        if textts.id in msg.relatedMessageId:
                            textt = textts.text
                            try:
                                params = {"apikey": eaterApikey, "text": textt, "lang": cCode}
                                main = json.loads(requests.get("https://api.coursehero.store/tts", params=params).text)
                                line.sendAudioWithURL(to, main["result"])
                            except:
                                line.sendMode(msg, to, sender, cmd, "Failed text to speech in language '{}'".format(cCode))
                else:
                    line.sendMode(msg, to, sender, cmd, 'Failed to text to speech, reply to the message first!')
            else:
                try:
                    textt = removeCmd(text, setKey)
                    params = {"apikey": eaterApikey, "text": textt, "lang": cCode}
                    main = json.loads(requests.get("https://api.coursehero.store/tts", params=params).text)
                    line.sendAudioWithURL(to, main["result"])
                except:
                    line.sendMode(msg, to, sender, cmd, "Failed text to speech in language '{}'".format(cCode))
                    
        elif cmd == 'translate':
            res = "› T R A N S L A T E"
            res += "\n\n• {}Tr-<countryCode> <text>".format(setKey.title())
            res += "\n• {}Tr-<countryCode>".format(setKey.title())
            res += "\n\nExample: {}Tr-en You".format(setKey.title())
            res += "\nWith Reply: {}Tr-en".format(setKey.title())
            res += "\n\nCountry Code:"
            res += template.countryCode()
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith('tr-'):
            sep = text.split("-")
            sep = sep[1].split(" ")
            cCode = sep[0]
            if len(sep) == 1:
                if msg.relatedMessageId is not None:
                    textts = line.getReplyMessage(to, msg.relatedMessageId)
                    if textts is not None:
                        if textts.id in msg.relatedMessageId:
                            textt = textts.text
                            try:
                                tuxtt = translator(cCode, textt)
                                line.sendFooter(to, str(tuxtt))
                            except:
                                line.sendMode(msg, to, sender, cmd, "Failed to translate language '{}'".format(cCode))
                else:
                    line.sendMode(msg, to, sender, cmd, 'Failed to translate, reply to the message first!')
            else:
                try:
                    textt = removeCmd(text, setKey)
                    tuxtt = translator(cCode, textt)
                    line.sendFooter(to, str(tuxtt))
                except:
                    line.sendMode(msg, to, sender, cmd, "Failed to translate language '{}'".format(cCode))

        elif cmd.startswith('kbbi '):
            textt = removeCmd(text, setKey)
            params = {"apikey": eaterApikey, "search": textt}
            main = json.loads(requests.get("https://api.coursehero.store/kbbi", params=params).text)
            line.sendFooter(to, str(main["result"]))

        elif cmd == 'memegen':
            isi = ["Memegen", "Meme List", "Meme @Mention/<num> <text1>|<text2>"]
            line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› M E M E", isi))
            
        elif cmd == 'meme list':
            isi = ["10guy","afraid","blb","both","buzz","chosen","doge","elf","ermg","fa","fetch","fry","fwp","ggg","icanhas","interesting","iw","keanu","live","ll","mordor","morpheus","officiespace","oprah","philosoraptor","remembers","sb","ss","success","toohigh","wonka","xy","yallgot","yuno"]
            res = "› L I S T\n"
            no = 0
            for a in isi:
                no += 1
                res += "\n{}. {}".format(no, a)
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith("meme "):
            textt = removeCmd(text, setKey)
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    profile = line.getContact(mention['M'])
                    if profile.pictureStatus:
                        path = 'https://obs.line-scdn.net/' + profile.pictureStatus
                        textts = textt.replace("@" + profile.displayName + " ","")
                        text1 = textts.split("|")[0].replace(" ", "_")
                        text2 = textts.split("|")[1].replace(" ", "_")
                        gambar = "https://api.memegen.link/images/custom/{}/{}.jpg?background={}".format(text1, text2, path)
                        line.sendLiffImage(to, gambar, "https://is1-ssl.mzstatic.com/image/thumb/Purple125/v4/60/a4/6a/60a46ad4-12fe-67ea-67d7-ac4da1e44e0f/source/512x512bb.jpg", "Memegen")
                    else:
                        line.sendMode(msg, to, sender, cmd, "Pastikan target memilki profile picture")
            else:
                listt = ["10guy","afraid","blb","both","buzz","chosen","doge","elf","ermg","fa","fetch","fry","fwp","ggg","icanhas","interesting","iw","keanu","live","ll","mordor","morpheus","officiespace","oprah","philosoraptor","remembers","sb","ss","success","toohigh","wonka","xy","yallgot","yuno"]
                try:
                    num = textt.split(" ")[0]
                    text1 = textt.replace(num + " ","").split("|")[0].replace(" ", "_")
                    text2 = textt.replace(num + " ","").split("|")[1].replace(" ", "_")
                    category = listt[int(num) - 1]
                    if category in listt:
                        line.sendLiffImage(to, "https://memegen.link/{}/{}/{}.jpg".format(category, text1, text2), "https://is1-ssl.mzstatic.com/image/thumb/Purple125/v4/60/a4/6a/60a46ad4-12fe-67ea-67d7-ac4da1e44e0f/source/512x512bb.jpg", "Memegen")
                except:
                    line.sendMode(msg, to, sender, cmd, "example:\nMeme 10 sozi|bot")
                
        elif cmd == 'photofunia':
            isi = ["FList 1", "FList 2", "FList 3", "FList 4", "Funia1 <numList1> @Mention", "Funia2 <numList2> @Mention @Mention", "Funia3 <numList3> <text> @Mention", "Funia4 <numList4> <text>"]
            line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› P H O T O F U N I A", isi))
            
        elif cmd == 'flist 1':
            isi = ['concrete-jungle', 'at-the-gallery', 'halloween-pumpkins', 'harley-davidson', 'the-frame', 'vintage-scooter', 'card-with-flowers', 'giant-artwork', 'explorer-drawing', 'at-the-beach', 'in-the-woods', 'shopping-arcade', 'art-admirer', 'sketch-practicing', 'passage', 'travellers-sketch', 'mirror', 'ink-portrait', 'truck-advert', 'girl-with-bicycle', 'easter-flowers', 'easter-frame', 'puppy-with-frame', 'city-billboard', 'underground-poster', 'sparklers', 'famous-gallery', 'burning-fire', 'autumn-frame', 'tablet', 'black-and-white-mural', 'vintage-photos', 'art-experts', 'scroll', 'worker-by-the-billboard', 'old-camera', 'tokyo-crossing', 'in-the-cinema', 'spring-flowers', 'latte-art', 'love-letter', 'wall-poster', 'skydiver', 'national-gallery-in-london', 'watercolour-painting', 'summoning-spirits', 'stadium', 'coloured-pencils', 'piccadilly-arcade', 'drawing-photo', 'artistic-filter', 'winter-princess', 'train-station-poster', 'knight-with-sword', 'football-field', 'rainy-night', 'bunnies', 'roses-and-marshmallows', 'playful-cat', 'wall-mural', 'gallery-visitor', 'equestrienne', 'new-year-frames', 'ghostwood', 'frankenstein-monster', 'brass-frame', 'red-and-blue', 'painting-and-sketches', 'new-york-street', 'wedding-day', 'vhs', 'passing-by-the-painting', 'lemon-tree', 'evening-billboard', 'kitty-and-frame', 'pedestrian-crossing', 'press_conference', 'picture_at_the_gallery', 'on_the_mountain', 'building_painters', 'replacing_billboard_advert', 'warrior', 'heart_locket', 'painter_at_work', 'galeries_lafayette', 'mermaid', 'goats', 'golden_valentine', 'london_calling', 'drawing_near_the_sea', 'ornament', 'indian_beauty', 'apples', 'spring_memories', 'brugge', 'medieval_art', 'cappuccino', 'modern_art_exhibition', 'louvre', 'watercolours', 'woman_pilot', 'vintage_table', 'pavement_artist', 'bicycle', 'bunny_ears', 'crooked_gambler', 'frame_and_roses', 'crown', 'oxford', 'midnight_billboard', 'pisa_street', 'pictures_sale', 'citylight', 'film_scan', 'knight', 'picadilly_circus', 'graffiti_billboard', 'romantic_etude', 'broadway', 'yellow_wall', 'the_first_man_on_the_moon', 'large_painting', 'mint_frame', 'night_street', 'boardings', 'portrait_on_the_wall', 'easter', 'impressionists', 'biker', 'snow_in_london', 'vintage_frame', 'family_in_museum', 'museum_kid', 'oil_painting', 'xmas_tree', 'marilyn_autograph', 'graffiti_wall', 'graffiti_artist', 'pumpkins', 'lavander', 'fire', 'truck', 'obama', 'roses', 'late_autumn', 'graffiti', 'riverside_billboard', 'stacco', 'etude', 'surfer', 'ny_taxis', 'chinese_opera', 'sidewalk', 'the_kiss', 'snowboard', 'mysterious_painting', 'prince_of_wales_theatre', 'sphinx', 'swedish_billboard', 'witch', 'nyc', 'art_gallery', 'city', 'dj', 'the_gun', 'tulips', 'flower_frame', 'male_gambler', 'female_gambler', 'artist', 'last_advert', 'lego_portrait', 'bride_in_grass', 'cafe', 'ax', 'artist_in_the_dark', 'hammock', 'goalkeeper', 'billboard_workers', 'huge_billboard', 'ophelia', 'leftfield', 'pavement_art', 'osaka', 'hockey_team', 'street_artist', 'watercolor', 'drawing', 'night_ride', 'frosty_window', 'girls_with_poster', 'watchinng', '100_dollars', 'puzzle', 'pastel', 'library', 'twilight', 'urban_billboard', 'glass', 'singer', 'bodybuilder', 'female_soldier', 'cupid', 'night_walk', 'icecream', 'rainy_day', 'urban', 'odessa_opera_house', 'hockey', 'captivity', 'local_shop', 'tram', 'ethanol', 'taipei', 'jigsaw_puzzle', 'mount_rushmore', 'lego', 'stencil', 'esquire', 'glamour', 'galatea', 'reproduction', 'godfather', 'death_proof', 'coffee_break', 'chris_pirillo', 'old_book', 'shop_poster', 'retail_park', 'purple_sky', 'warhol', 'special_billboard', 'yo', 'reflection', 'wall_painting', 'bride', 'tv_girl', 'mini_cooper', 'lenin', 'reconstruction', 'two_cats', 'superman', 'frame', 'street_exhibition', 'wall', 'night', 'pilot', 'pavement_drawing', 'applying_makeup', 'polaroid_dress', 'torn_billboard', 'kitty', 'portrait', 'eye', 'posters', 'night_city', 'bad_santa', 'christmass_tree_balls', 'good_luck_chuck', 'paris_hilton', 'cinema', 'wall_banner', 'gas_mask_freaks', 'marilyn_monroe', 'two_female_fans', 'wanted_wizard', 'on_the_moon', 'art_exhibition', 'train_station', 'museum', 'madonna', 'mona_lisa', 'vogue', 'dollar', 'art_painting', 'behind_the_fence', 'newspaper', 'castle', 'angry_granny', 'victoria_beckham', 'putin', 'perfume_shop', 'billboard', 'shopping_center']
            res = "› L I S T\n"
            no = 0
            for a in isi:
                no += 1
                res += "\n{}. {}".format(no, a)
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd == 'flist 2':
            isi = ['broadway-at-night', 'painter', 'festive-days', 'old-tram', 'bronze-frames', 'urban-billboard', 'billboards-at-night', 'shop-posters', 'campaign', 'two-girls', 'antique_shop', 'art_book', 'two_citylights', 'brooches', 'queens_theatre', 'painter_on_the_bridge', 'streets_of_new_york', 'on_the_roof', 'copying_masterpiece', 'taxis_on_times_square', 'summer_love', 'reading', 'photo_exhibition', 'football_players', 'developing_photos', 'night_square', 'couple', 'underground', 'brad_pitt', 'times_square', 'smart_kitty', 'broken_glass', 'brick_wall', 'stamps', 'modern_art']
            res = "› L I S T\n"
            no = 0
            for a in isi:
                no += 1
                res += "\n{}. {}".format(no, a)
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd == 'flist 3':
            isi = ['morning-newspaper', 'easter-greetings', 'christmas-diary', 'activists', 'coffee-and-tulips', 'night-street', 'travellers-diary', 'festive-greetings', 'xmas-time', 'vinyl-store', 'easter-nest', 'travelers-suitcase', 'hanging-billboard', 'easter-card', 'santas-parcel-picture', 'double-decker', 'book_lover', 'new_world', 'quill', 'easter_postcard', 'daffodils', 'memories_of_paris', 'making_tattoo', 'instant_camera', 'another_magazine', 'pink_heart', 'new_year_presents', 'miss', 'affiche', 'rounded_billboard', 'hand_lens', 'vintage_photo', 'volunteer', 'valentine', 'coin', 'macho', 'guilty', 'music_shop']
            res = "› L I S T\n"
            no = 0
            for a in isi:
                no += 1
                res += "\n{}. {}".format(no, a)
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd == 'flist 4':
            isi = ['christmas-writing', 'beach-sign', 'yacht', 'water-writing', 'bracelet', 'light-graffiti', 'street-sign', 'cemetery-gates', 'plane-banner', 'love-lock', 'fortune-cookie', 'frosty-window-writing', 'einstein', 'lipstick-writing', 'typewriter', 'soup_letters', 'cookies_writing', 'blood_writing', 'wooden_sign', 'sand_writing']
            res = "› L I S T\n"
            no = 0
            for a in isi:
                no += 1
                res += "\n{}. {}".format(no, a)
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith('funia1 '):
            lists = ['concrete-jungle', 'at-the-gallery', 'halloween-pumpkins', 'harley-davidson', 'the-frame', 'vintage-scooter', 'card-with-flowers', 'giant-artwork', 'explorer-drawing', 'at-the-beach', 'in-the-woods', 'shopping-arcade', 'art-admirer', 'sketch-practicing', 'passage', 'travellers-sketch', 'mirror', 'ink-portrait', 'truck-advert', 'girl-with-bicycle', 'easter-flowers', 'easter-frame', 'puppy-with-frame', 'city-billboard', 'underground-poster', 'sparklers', 'famous-gallery', 'burning-fire', 'autumn-frame', 'tablet', 'black-and-white-mural', 'vintage-photos', 'art-experts', 'scroll', 'worker-by-the-billboard', 'old-camera', 'tokyo-crossing', 'in-the-cinema', 'spring-flowers', 'latte-art', 'love-letter', 'wall-poster', 'skydiver', 'national-gallery-in-london', 'watercolour-painting', 'summoning-spirits', 'stadium', 'coloured-pencils', 'piccadilly-arcade', 'drawing-photo', 'artistic-filter', 'winter-princess', 'train-station-poster', 'knight-with-sword', 'football-field', 'rainy-night', 'bunnies', 'roses-and-marshmallows', 'playful-cat', 'wall-mural', 'gallery-visitor', 'equestrienne', 'new-year-frames', 'ghostwood', 'frankenstein-monster', 'brass-frame', 'red-and-blue', 'painting-and-sketches', 'new-york-street', 'wedding-day', 'vhs', 'passing-by-the-painting', 'lemon-tree', 'evening-billboard', 'kitty-and-frame', 'pedestrian-crossing', 'press_conference', 'picture_at_the_gallery', 'on_the_mountain', 'building_painters', 'replacing_billboard_advert', 'warrior', 'heart_locket', 'painter_at_work', 'galeries_lafayette', 'mermaid', 'goats', 'golden_valentine', 'london_calling', 'drawing_near_the_sea', 'ornament', 'indian_beauty', 'apples', 'spring_memories', 'brugge', 'medieval_art', 'cappuccino', 'modern_art_exhibition', 'louvre', 'watercolours', 'woman_pilot', 'vintage_table', 'pavement_artist', 'bicycle', 'bunny_ears', 'crooked_gambler', 'frame_and_roses', 'crown', 'oxford', 'midnight_billboard', 'pisa_street', 'pictures_sale', 'citylight', 'film_scan', 'knight', 'picadilly_circus', 'graffiti_billboard', 'romantic_etude', 'broadway', 'yellow_wall', 'the_first_man_on_the_moon', 'large_painting', 'mint_frame', 'night_street', 'boardings', 'portrait_on_the_wall', 'easter', 'impressionists', 'biker', 'snow_in_london', 'vintage_frame', 'family_in_museum', 'museum_kid', 'oil_painting', 'xmas_tree', 'marilyn_autograph', 'graffiti_wall', 'graffiti_artist', 'pumpkins', 'lavander', 'fire', 'truck', 'obama', 'roses', 'late_autumn', 'graffiti', 'riverside_billboard', 'stacco', 'etude', 'surfer', 'ny_taxis', 'chinese_opera', 'sidewalk', 'the_kiss', 'snowboard', 'mysterious_painting', 'prince_of_wales_theatre', 'sphinx', 'swedish_billboard', 'witch', 'nyc', 'art_gallery', 'city', 'dj', 'the_gun', 'tulips', 'flower_frame', 'male_gambler', 'female_gambler', 'artist', 'last_advert', 'lego_portrait', 'bride_in_grass', 'cafe', 'ax', 'artist_in_the_dark', 'hammock', 'goalkeeper', 'billboard_workers', 'huge_billboard', 'ophelia', 'leftfield', 'pavement_art', 'osaka', 'hockey_team', 'street_artist', 'watercolor', 'drawing', 'night_ride', 'frosty_window', 'girls_with_poster', 'watchinng', '100_dollars', 'puzzle', 'pastel', 'library', 'twilight', 'urban_billboard', 'glass', 'singer', 'bodybuilder', 'female_soldier', 'cupid', 'night_walk', 'icecream', 'rainy_day', 'urban', 'odessa_opera_house', 'hockey', 'captivity', 'local_shop', 'tram', 'ethanol', 'taipei', 'jigsaw_puzzle', 'mount_rushmore', 'lego', 'stencil', 'esquire', 'glamour', 'galatea', 'reproduction', 'godfather', 'death_proof', 'coffee_break', 'chris_pirillo', 'old_book', 'shop_poster', 'retail_park', 'purple_sky', 'warhol', 'special_billboard', 'yo', 'reflection', 'wall_painting', 'bride', 'tv_girl', 'mini_cooper', 'lenin', 'reconstruction', 'two_cats', 'superman', 'frame', 'street_exhibition', 'wall', 'night', 'pilot', 'pavement_drawing', 'applying_makeup', 'polaroid_dress', 'torn_billboard', 'kitty', 'portrait', 'eye', 'posters', 'night_city', 'bad_santa', 'christmass_tree_balls', 'good_luck_chuck', 'paris_hilton', 'cinema', 'wall_banner', 'gas_mask_freaks', 'marilyn_monroe', 'two_female_fans', 'wanted_wizard', 'on_the_moon', 'art_exhibition', 'train_station', 'museum', 'madonna', 'mona_lisa', 'vogue', 'dollar', 'art_painting', 'behind_the_fence', 'newspaper', 'castle', 'angry_granny', 'victoria_beckham', 'putin', 'perfume_shop', 'billboard', 'shopping_center']
            try:
                textt = removeCmd(text, setKey)
                no = int(textt.split(" ")[0])
            except:
                return line.sendMode(msg, to, sender, cmd, "example:\n{}Funia1 10 @Mention".format(setKey.title()))
            if len(textt.split(" ")) < 2:
                return line.sendMode(msg, to, sender, cmd, "example:\n{}Funia1 10 @Mention".format(setKey.title()))
            category = lists[no - 1]
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    profile = line.getContact(mention['M'])
                    url = 'https://obs.line-scdn.net/' + profile.pictureStatus
                    params = {"apikey": eaterApikey, "effect": category, "image": url}
                    main = json.loads(requests.get("https://api.coursehero.store/photofunia",params=params).text)
                    if main["result"]["animated"]:
                        line.sendGIFWithURL(to, main["result"]["image"])
                    else:
                        line.sendLiffImage(to, main["result"]["image"], 'https://i.ibb.co/4sLv5n0/e186f948a282.jpg', ' Source: Photofunia')
                    
        elif cmd.startswith('funia2 '):
            lists = ['broadway-at-night', 'painter', 'festive-days', 'old-tram', 'bronze-frames', 'urban-billboard', 'billboards-at-night', 'shop-posters', 'campaign', 'two-girls', 'antique_shop', 'art_book', 'two_citylights', 'brooches', 'queens_theatre', 'painter_on_the_bridge', 'streets_of_new_york', 'on_the_roof', 'copying_masterpiece', 'taxis_on_times_square', 'summer_love', 'reading', 'photo_exhibition', 'football_players', 'developing_photos', 'night_square', 'couple', 'underground', 'brad_pitt', 'times_square', 'smart_kitty', 'broken_glass', 'brick_wall', 'stamps', 'modern_art']
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if len(sep) < 3:
                return line.sendMode(msg, to, sender, cmd, "example:\n{}Funia2 10 @Mention @Mention".format(setKey.title()))
            if sep[0].isdigit():
                category = lists[int(sep[0]) - 1]
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    path = []
                    if len(mentions['MENTIONEES']) != 2:
                        return line.sendFooter(to, "example:\n{}Funia2 10 @Mention @Mention".format(setKey.title()), reply=True)
                    for mention in mentions['MENTIONEES']:
                        profile = line.getContact(mention['M'])
                        url = 'https://obs.line-scdn.net/' + profile.pictureStatus
                        path.append(url)
                    params = {"apikey": eaterApikey, "effect": category, "image": path[0], "image2": path[1]}
                    main = json.loads(requests.get("https://api.coursehero.store/photofunia",params=params).text)
                    if main["result"]["animated"]:
                        line.sendGIFWithURL(to, main["result"]["image"])
                    else:
                        line.sendLiffImage(to, main["result"]["image"], 'https://i.ibb.co/4sLv5n0/e186f948a282.jpg', ' Source: Photofunia')
                
        elif cmd.startswith('funia3 '):
            lists = ['morning-newspaper', 'easter-greetings', 'christmas-diary', 'activists', 'coffee-and-tulips', 'night-street', 'travellers-diary', 'festive-greetings', 'xmas-time', 'vinyl-store', 'easter-nest', 'travelers-suitcase', 'hanging-billboard', 'easter-card', 'santas-parcel-picture', 'double-decker', 'book_lover', 'new_world', 'quill', 'easter_postcard', 'daffodils', 'memories_of_paris', 'making_tattoo', 'instant_camera', 'another_magazine', 'pink_heart', 'new_year_presents', 'miss', 'affiche', 'rounded_billboard', 'hand_lens', 'vintage_photo', 'volunteer', 'valentine', 'coin', 'macho', 'guilty', 'music_shop']
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if len(sep) < 3:
                return line.sendMode(msg, to, sender, cmd, "example:\n{}Funia3 10 Sozi @Mention".format(setKey.title()))
            try:
                no = int(sep[0])
            except:
                return line.sendMode(msg, to, sender, cmd, "example:\n{}Funia3 10 sozi @Mention".format(setKey.title()))
            category = lists[no - 1]
            a = textt.replace(sep[0] + " ","")
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    profile = line.getContact(mention['M'])
                    url = 'https://obs.line-scdn.net/' + profile.pictureStatus
                    textt = a.replace(" @"+profile.displayName,"")
                    params = {"apikey": eaterApikey, "effect": category, "image": url, "text": textt}
                    main = json.loads(requests.get("https://api.coursehero.store/photofunia",params=params).text)
                    if main["result"]["animated"]:
                        line.sendGIFWithURL(to, main["result"]["image"])
                    else:
                        line.sendLiffImage(to, main["result"]["image"], 'https://i.ibb.co/4sLv5n0/e186f948a282.jpg', ' Source: Photofunia')
                    
        elif cmd.startswith('funia4 '):
            lists = ['christmas-writing', 'beach-sign', 'yacht', 'water-writing', 'bracelet', 'light-graffiti', 'street-sign', 'cemetery-gates', 'plane-banner', 'love-lock', 'fortune-cookie', 'frosty-window-writing', 'einstein', 'lipstick-writing', 'typewriter', 'soup_letters', 'cookies_writing', 'blood_writing', 'wooden_sign', 'sand_writing']
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if len(sep) < 2:
                return line.sendMode(msg, to, sender, cmd, "example:\n{}Funia4 10 sozi".format(setKey.title()))
            try:
                no = int(sep[0])
            except:
                return line.sendMode(msg, to, sender, cmd, "example:\n{}Funia4 10 sozi".format(setKey.title()))
            category = lists[no - 1]
            textt = textt.replace(sep[0] + " ","")
            params = {"apikey": eaterApikey, "effect": category, "text": textt}
            main = json.loads(requests.get("https://api.coursehero.store/photofunia",params=params).text)
            line.sendLiffImage(to, main["result"]["image"], 'https://i.ibb.co/4sLv5n0/e186f948a282.jpg', ' Source: Photofunia')
        
        elif cmd.startswith('tulis '):
            textt = removeCmd(text, setKey)
            path = 'tmp/tulis.jpg'
            nulis = tulis(textt)
            for i in nulis:
                i.save(path)
            line.sendReplyImage(to, path, msgIds=msg_id)
            line.deleteFile(path)
            
        elif cmd == "textpro":
            isi = ["Tlist 1", "Tlist 2", "Textpro1 <numList1> <text>", "Textpro2 <numList2> <text>|<text>"]
            line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› T E X T P R O", isi))
        
        elif cmd == "tlist 1":
            style_id = {"christmas holiday snow": "2", "futuristic neon light": "3", "snow": "4", "cloud": "5", "3d luxury gold": "6", "3d gradient": "7", "blackpink logo": "8", "realistic cloud": "10", "cloudV2": "11", "sand summer beach": "12", "sand writing": "13", "sand engraved": "14", "summery sand writing": "15", "foil ballon": "16", "3d glue": "17", "metal dark gold": "19", "neon light": "22", "1917 style": "23", "minion": "25", "double exposure": "27", "3d holographic": "28", "metal purple dual": "30", "deluxe silver": "33", "full luxury metal": "34", "glossy blue metal": "35", "deluxe gold": "36", "glossy carbon": "37", "fabric": "38", "neon": "39", "3d new years card": "40", "happy new year": "41", "fullcolor ballon": "42", "avatar gold": "44", "3d xmas card": "49", "blood": "50", "halloween fire": "51", "metal dark goldV2": "52", "joker logo": "57", "wicker": "58", "natural leaves": "59", "firework sparkle": "60", "skeleton": "61", "steel": "69", "ultra gloss": "70", "denim": "71", "decorate green": "72", "decorate purple": "73", "peridot stone": "74", "rock": "75", "lava": "76", "yellow glass": "77", "captain america": "85", "robot r2": "86", "rainbow equalizer": "87", "toxic": "88", "blue sparkling": "90", "choclate cake": "98", "strawberry": "99", "koi fish": "100", "bread": "101", "matrix": "102", "horror blood": "103", "neon lightV2": "104", "thunder": "105", "3d box": "106", "neonV2": "107", "road warning": "108", "bokeh": "110", "green neon": "111", "advanced glow": "112", "dropwater": "113", "break wall": "114", "christmas gift": "115", "honey": "116", "plastic bag drug": "117", "horror gift": "118", "marble": "120", "marble slabs": "119", "ice cold": "121", "fruit juice": "122", "rusty metal": "123", "abstra gold": "124", "biscuit": "125", "bagel": "126", "wood": "127", "sci-fi": "128", "metal rainbow": "129", "hot metal": "140", "hexa golden": "141", "blue glitter": "142", "eroded metal": "149", "carbonV2": "150", "pink candy": "151", "3d glowing metal": "155", "3d chrome": "156"}
            res = "› L I S T"
            style = make_list(style_id)
            no = 0
            for sty in style:
                no += 1
                res += "\n{}. {}".format(no, sty)
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd == "tlist 2":
            style_id = {"wall graffiti": "1", "realistic vintage": "9", "3d space": "18", "glitch": "20", "stone": "21", "pornhub logo": "26", "3d avengers": "29", "marvel only": "32", "marvel metal": "31", "3d metal logo": "43", "3d metal silver": "45", "3d metal rose gold": "46", "3d metal gold": "47", "3d metal galaxy": "48", "lion logo mascot": "53", "wolf logo": "54", "wolf logo galaxy": "55", "ninja logo": "56", "3d steel": "109"}
            res = "› L I S T"
            style = make_list(style_id)
            no = 0
            for sty in style:
                no += 1
                res += "\n{}. {}".format(no, sty)
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd.startswith("textpro1 "):
            style_id = {"christmas holiday snow": "2", "futuristic neon light": "3", "snow": "4", "cloud": "5", "3d luxury gold": "6", "3d gradient": "7", "blackpink logo": "8", "realistic cloud": "10", "cloudV2": "11", "sand summer beach": "12", "sand writing": "13", "sand engraved": "14", "summery sand writing": "15", "foil ballon": "16", "3d glue": "17", "metal dark gold": "19", "neon light": "22", "1917 style": "23", "minion": "25", "double exposure": "27", "3d holographic": "28", "metal purple dual": "30", "deluxe silver": "33", "full luxury metal": "34", "glossy blue metal": "35", "deluxe gold": "36", "glossy carbon": "37", "fabric": "38", "neon": "39", "3d new years card": "40", "happy new year": "41", "fullcolor ballon": "42", "avatar gold": "44", "3d xmas card": "49", "blood": "50", "halloween fire": "51", "metal dark goldV2": "52", "joker logo": "57", "wicker": "58", "natural leaves": "59", "firework sparkle": "60", "skeleton": "61", "steel": "69", "ultra gloss": "70", "denim": "71", "decorate green": "72", "decorate purple": "73", "peridot stone": "74", "rock": "75", "lava": "76", "yellow glass": "77", "captain america": "85", "robot r2": "86", "rainbow equalizer": "87", "toxic": "88", "blue sparkling": "90", "choclate cake": "98", "strawberry": "99", "koi fish": "100", "bread": "101", "matrix": "102", "horror blood": "103", "neon lightV2": "104", "thunder": "105", "3d box": "106", "neonV2": "107", "road warning": "108", "bokeh": "110", "green neon": "111", "advanced glow": "112", "dropwater": "113", "break wall": "114", "christmas gift": "115", "honey": "116", "plastic bag drug": "117", "horror gift": "118", "marble": "120", "marble slabs": "119", "ice cold": "121", "fruit juice": "122", "rusty metal": "123", "abstra gold": "124", "biscuit": "125", "bagel": "126", "wood": "127", "sci-fi": "128", "metal rainbow": "129", "hot metal": "140", "hexa golden": "141", "blue glitter": "142", "eroded metal": "149", "carbonV2": "150", "pink candy": "151", "3d glowing metal": "155", "3d chrome": "156"}
            textt = removeCmd(text, setKey)
            number = textt.split(" ")[0]
            texttl = textt.replace(number + " ","")
            if number.isdigit():
                number = int(number)
                if number <= len(style_id):
                    style = make_list(style_id)
                    id = style_id[style[number-1]]
                    params = {"apikey": eaterApikey, "id": id, "text": texttl}
                    main = json.loads(requests.get("https://api.coursehero.store/textpro", params=params).text)
                    if main["status"] == 200:
                        line.sendLiffImage(to, main["result"], "https://tinyurl.com/y3yxcupt", " Source: TextPro.me")
                    else:
                        line.sendMode(msg, to, sender, cmd, "API ERROR, Report to owner")
                    
        elif cmd.startswith("textpro2 "):
            style_id = {"wall graffiti": "1", "realistic vintage": "9", "3d space": "18", "glitch": "20", "stone": "21", "pornhub logo": "26", "3d avengers": "29", "marvel only": "32", "marvel metal": "31", "3d metal logo": "43", "3d metal silver": "45", "3d metal rose gold": "46", "3d metal gold": "47", "3d metal galaxy": "48", "lion logo mascot": "53", "wolf logo": "54", "wolf logo galaxy": "55", "ninja logo": "56", "3d steel": "109"}
            textt = removeCmd(text, setKey)
            number = textt.split(" ")[0]
            texttl = textt.replace(number + " ","").split("|")
            if number.isdigit():
                number = int(number)
                if number <= len(style_id):
                    if len(texttl) == 2:
                        style = make_list(style_id)
                        id = style_id[style[number-1]]
                        params = {"apikey": eaterApikey, "id": id, "text": texttl[0], "text2": texttl[1]}
                        main = json.loads(requests.get("https://api.coursehero.store/textpro", params=params).text)
                        if main["status"] == 200:
                            line.sendLiffImage(to, main["result"], "https://tinyurl.com/y3yxcupt", " Source: TextPro.me")
                        else:
                            line.sendMode(msg, to, sender, cmd, "API ERROR, Report to owner")
                            
        elif cmd.startswith("porn "):
            query = removeCmd(text, setKey)
            result = requests.get("https://apitrojans.xyz/xnxx/search?query={}&apikey={}".format(query, trojansApikey))
            data = result.json()
            pornlist = []
            for xnx in data[0:10]:
                vids = requests.get("https://tinyurl.com/api-create.php?url={}".format(xnx["streamURL"])).text
                pornlist.append(template.data_square_temp(xnx["thumbnail"], 'https://line.me/R/app/1657710460-y83a8lNE?type=video&ocu={}&piu={}'.format(vids, xnx["thumbnail"])))
            data = {
                'type': 'flex',
                'altText': '%s sent a xvideos media' % line.profile.displayName,
                'contents': {
                    'type': 'carousel',
                    'contents': pornlist
                }
            }
            line.sendLiff(to, data)
        
        elif cmd.startswith("nhentai "):
            query = removeCmd(text, setKey)
            if query.isdigit():
                data = nhentai(query)
            elif query.lower() in ['r', 'n', 'p']:
                data = nhentai(query.lower())
            else:
                return line.sendMode(msg, to, sender, cmd, 'Example:\n    1. Nhentai R\n    2. Nhentai P\n    3. Nhentai N\n    4. Nhentai 355155')
            dataProfile = []
            thumb = []
            for ndata in data:
                thumb.append(ndata["thumb"])
                dataProfile.append(template.nhentai(ndata["title"], ndata["id"], ndata["page"], ndata["uploaded"]))
            if len(thumb) == 1:
                line.sendImageWithURL(to, thumb[0])
            else:
                objectId = line.sendMessage(to=to, text=None, contentType = 1).id
                for thum in thumb:
                    try:
                        path = line.downloadFileURL(thum, 'path')
                        id_nya = line.sendMessage(to=to, text=None, contentMetadata={'GID': objectId}, contentType = 1).id
                        upload = line.uploadObjTalk(path=path, type='image', returnAs='bool', objId=id_nya)
                    except:
                        continue
            data = {
                'type': 'flex',
                'altText': '%s sent a hentai' % line.profile.displayName,
                'contents': {
                    'type': 'carousel',
                    'contents': dataProfile
                }
            }
            line.sendLiff(to, data)
        
        elif cmd.startswith("nekopoidl "):
            url = removeCmd(text, setKey)
            if "nekopoi.care" not in url:
                return line.sendFooter(to, "Make sure the url is correct")
            ## scrape by trojans
            Headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive',
            }
            try:
                stream = []
                a = requests.get(url, headers=Headers)
                b = BeautifulSoup(a.content, "lxml")
                data = b.find("div", {"class": "postsbody"})
                line.sendImageWithURL(to, data.find("div", {"class": "thm"}).find("img").get("src"))
              #  res = "𝗡𝗲𝗸𝗼𝗽𝗼𝗶 𝗜??𝗳𝗼:"
           #     res += "\n    Judul: {}".format(data.find("h1").text)
            #    res += "\n    Genre: {}".format(data.find("div", {"class": "konten"}).findAll("p")[4].text.split("Genre : ")[1])
           #     res += "\n    Sinopsis: {}".format(data.find("div", {"class": "konten"}).findAll("p")[1].text)
          #      res += "\n    Upload: {}".format(data.find("div", {"class": "eroinfo"}).find("p").text.split("/")[1][1:])
              #  res += "\n    Durasi: {}".format(data.find("div", {"class": "konten"}).findAll("p")[7].text.split("Duration : ")[1])
               # res += "\n    Producer: {}".format(data.find("div", {"class": "konten"}).findAll("p")[6].text.split("Producers : ")[1])
             #   line.sendMode(msg, to, sender, cmd, res)
                res2 = "𝗦𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴:"
                no = 0
                for strm in data.findAll("div", {"class": "openstream"}):
                    no += 1
                    res2 += "\n    {}. {}".format(no, strm.find("iframe").get("src"))
                res2 += "\n\n𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱:"
                for link in data.find("div", {"class": "arealinker"}).findAll("div", {"class": "liner"}):
                    no = 0
                    down = "\n\n=> Resolusi: {}".format(link.find('div',attrs={'class':'name'}).text.split("[")[1][:-1])
                    uri = link.findAll('a')
                    for uri in uri:
                        no += 1
                        down += "\n    {}. Host: {}".format(no, uri.text)
                        down += "\n        Url: {}".format(uri.get("href"))
                    res2 += down
                line.sendFooter(to, res2)
            except:
                line.sendMode(msg, to, sender, cmd, "Failed to get nekopoi info")
            
        elif cmd.startswith("youtubedl "):
            search = removeCmd(text, setKey)
            ytSearch = SearchVideos("{}".format(search), offset=1, mode='json', max_results=10)
            result = json.loads(ytSearch.result())
            url = pafy.new("{}".format(result["search_result"][0]["link"]))
            vid = url.getbest()
            vid.resolution, vid.extension
            aux = url.getbestaudio()
            aux.bitrate
            try:
                likes = "{:,}".format(int(url.likes))
                dislikes = "{:,}".format(int(url.dislikes))
            except:
                likes = "Null"
                dislikes = "Null"
            res = "› I N F O\n"
            res += "\n• Title: {}".format(url.title)
            res += "\n• Author: {}".format(url.author)
            res += "\n• Category: {}".format(url.category)
            res += "\n• Duration: {}".format(url.duration)
            res += "\n• Likes: {}".format(likes)
            res += "\n• Dislikes: {}".format(dislikes)
            res += "\n• Views: {:,}".format(int(url.viewcount))
            line.sendMode(msg, to, sender, cmd, res)
            line.sendImageWithURL(to, "http://i.ytimg.com/vi/{}/hqdefault.jpg".format(url.videoid))
            videoNya = requests.get("https://tinyurl.com/api-create.php?url={}".format(vid.url)).text
            audioNya = requests.get("https://tinyurl.com/api-create.php?url={}".format(aux.url)).text
            line.sendFooter(to, '› D O W N L O A D\n\n• Mp3: {}\n• Mp4: {}'.format(audioNya, videoNya))
            
        elif cmd.startswith("youtube "):
            search = removeCmd(text, setKey)
            ytSearch = SearchVideos("{}".format(search), offset=1, mode='json', max_results=10)
            result = json.loads(ytSearch.result())
            dataProfile = []
            for data in result["search_result"][0:10]:
                mp3 = urllib.parse.quote("{}youtubemp3 {}".format(setKey, data["link"]))
                mp4 = urllib.parse.quote("{}youtubemp4 {}".format(setKey, data["link"]))
                dataProfile.append(template.youtube(data["thumbnails"][1], data["title"], mp3, mp4))
            line.sendLiff(to, dataProfile, mainType=False)
            
        elif cmd == 'youtube':
            isi = ["Youtube", "Youtube <text>", "Youtubedl <text>", "Youtubemp3 <linkYt>", "Youtubemp4 <linkYt>"]
            line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› Y O U T U B E", isi))
            
        elif cmd.startswith("youtubemp4 "):
            link = removeCmd(text, setKey)
            if 'youtube.com' not in link and 'youtu.be' not in link: return line.sendFooter(to, 'must use link youtube')
            line.sendMessage(to, 'wait a minute, the video is downloading..')
            youtubeMp4(to, link, sendLiff=False)
            
        elif cmd.startswith("youtubemp3 "):
            link = removeCmd(text, setKey)
            if 'youtube.com' not in link and 'youtu.be' not in link: return line.sendFooter(to, 'must use link youtube')
            line.sendMessage(to, 'wait a minute, the audio is downloading..')
            youtubeMp3(to, link)
        
        elif cmd.startswith("github "):
            query = removeCmd(text, setKey)
            data = requests.get('https://api.github.com/users/{}'.format(query)).json()
            if 'message' in data: return line.sendMode(msg, to, sender, cmd, 'User `{}` not found'.format(query))
            dataFollowers = requests.get('https://api.github.com/users/{}/followers'.format(query)).json()
            dataFollowing = requests.get('https://api.github.com/users/{}/following'.format(query)).json()
            dataRepositories = requests.get('https://api.github.com/users/{}/repos'.format(query)).json()
            followers_profile = []
            following_profile = []
            repos_profile = []
            if dataFollowers:
                more1 = 'More\n(Design by: Hellterhead)'
                for dataFoll in dataFollowers[0:10]:
                    followers_profile.append(template.github_followers(dataFoll['avatar_url'], dataFoll['login']))
            else:
                more1 = '(Design by: Hellterhead)'
            if dataFollowing:
                more2 = 'More\n(Design by: Hellterhead)'
                for dataFoll in dataFollowing[0:10]:
                    following_profile.append(template.github_following(dataFoll['avatar_url'], dataFoll['login']))
            else:
                more2 = '(Design by: Hellterhead)'
            if dataRepositories:
                more3 = 'More\n(Design by: Hellterhead)'
                for dataRep in dataRepositories[0:10]:
                    repos_profile.append(template.github_repos(dataRep['name'], dataRep['html_url']))
            else:
                more3 = '(Design by: Hellterhead)'
            if data['bio']: bio = data['bio']
            else: bio = 'None'
            if data['name']: name = data['name']
            else: name = 'None'
            black = "#000000"
            white = "#ffffff"
            data = {
                "type": "flex",
                "altText": "https://github.com/{}".format(query),
                "contents": {
                    "type": "carousel",
                    "contents": [template.github_main(query, name, data['avatar_url'], bio, str(data['followers']), str(data['following']), str(data['public_repos']), more1, "followers", black, white, white, followers_profile), template.github_main(query, name, data['avatar_url'], bio, str(data['followers']), str(data['following']), str(data['public_repos']), more2, "following", white, black, white, following_profile), template.github_main(query, name, data['avatar_url'], bio, str(data['followers']), str(data['following']), str(data['public_repos']), more3, "repositories", white, white, black, repos_profile)]
                }
            }
            line.sendLiff(to, data)

        elif cmd.startswith("smule "):
            search = removeCmd(text, setKey)
            params = {"apikey": eaterApikey, "user": search}
            main = json.loads(requests.get("https://api.coursehero.store/smule/performance", params=params).text)
            dataProfile = []
            for data in main["result"][0:10]:
                link = data["web_url"].replace("/ensembles", "")
                artist = str(data["artist"]) + " - " + str(data["ensemble_type"])
                dataProfile.append(template.smule(data["cover_url"], artist, urllib.parse.quote("{}smulepost {}".format(setKey, link))))
            line.sendLiff(to, dataProfile, mainType=False)
            
        elif cmd.startswith("smulepost "):
            search = removeCmd(text, setKey)
            params = {"apikey": eaterApikey, "url": search}
            main = json.loads(requests.get("https://api.coursehero.store/smule/post", params=params).text)
            if main["result"]["performance"]["type"] == "video": line.sendVideoWithURL(to, main["result"]["performance"]["video_media_mp4_url"])
            else: line.sendAudioWithURL(to, main["result"]["performance"]["media_url"])
            
        elif cmd.startswith("tiktok "):
            search = removeCmd(text, setKey)
            data = requests.get("https://apitrojans.xyz/tiktok/user?user={}&apikey={}".format(search, trojansApikey)).json()
            res = "› P R O F I L E\n"
            res += "\n• Username: "+data["result"]["username"]
            res += "\n• Nickname : "+data["result"]["nickname"]
            res += "\n• Description : "+data["result"]["description"]
            if data["result"]["verified"] == True: res += "\n• Verified : True"
            else: res += "\n• Verified : False"
            res += "\n• Followers : "+str(data["result"]["stats"]["followersCount"])
            res += "\n• Following : "+str(data["result"]["stats"]["followingCount"])
            res += "\n• Hearts : "+str(data["result"]["stats"]["heartCount"])
            res += "\n• Video : "+str(data["result"]["stats"]["videoCount"])
            line.sendImageWithURL(to, data["result"]["pictureUrl"])
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith("tiktokpost "):
            search = removeCmd(text, setKey)
            tiktokPost(to, search)
            
        elif cmd.startswith("urlshort "):
            search = removeCmd(text, setKey)
            req = requests.get('https://bitly.com/')
            cookie = req.headers.get('Set-Cookie').split(';')[0]
            token = cookie.split("=")[1]
            headers = {
                "origin": "https://bitly.com/",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "cookie": cookie,
                "X-XSRFToken": token,
                "X-Requested-With": "XMLHttpRequest"
            }
            data = {"url": search}
            post = requests.post("https://bitly.com/data/anon_shorten", data=data, headers=headers).json()
            if post["status_code"] == 200:
                line.sendFooter(to, f'URL: {post["data"]["link"]}', line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"])
            else:
                line.sendFooter(to, 'Failed to shorten link', line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"])
            
        elif cmd.startswith('9gag'):
            sep = removeCmd(text, setKey)
            if cmd == '9gag':
                res = '› T Y P E\n'
                info = json.loads(requests.get("https://api.coursehero.store/9gag/info").text)
                no = 0
                for type in info["result"]:
                    no += 1
                    res += '\n{}. {}'.format(no, type)
                res += '\n\nExample: {}9Gag <type>'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
            elif sep.isdigit():
                info = json.loads(requests.get("https://api.coursehero.store/9gag/info").text)
                params = {"apikey": eaterApikey, "category": info['result'][int(sep)-1]}
                main = json.loads(requests.get("https://api.coursehero.store/9gag-fresh", params=params).text)
                gag = []
                for data in main['result'][0:10]:
                    if data["type"] == "Photo":
                        gag.append({
                            'imageUrl': data["images"]["image700"]["url"],
                            'size': 'full',
                            'action': {
                                'type': 'uri',
                                'uri': 'https://line.me/R/app/1657710460-y83a8lNE?type=image&img={}'.format(data["images"]["image700"]["url"])
                            }
                        })
                    elif data["type"] == "Animated":
                        gag.append({
                            'imageUrl': data["images"]["imageFbThumbnail"]["url"],
                            'size': 'full',
                            'action': {
                                'type': 'uri',
                                'uri': 'https://line.me/R/app/1657710460-y83a8lNE?type=video&ocu={}&piu={}'.format(data["images"]["image460sv"]["url"], data["images"]["imageFbThumbnail"]["url"])
                            }
                        })
                data = {
                    'type': 'template',
                    'altText': '%s sent a 9gag' % line.profile.displayName,
                    'template': {
                        'type': 'image_carousel',
                        'columns': gag
                    }
                }
                print(json.dumps(data, indent=4))
                line.sendLiff(to, data)
                
        elif cmd.startswith("soundcloud "):
            query = removeCmd(text, setKey)
            cond = query.split('|')
            url = requests.get('https://soundcloud.com/search?q=%s' % cond[0])
            soup = BeautifulSoup(url.text,'lxml')
            data = soup.find_all(class_='soundTitle__titleContainer')
            data = soup.select('li > h2 > a')
            if len(cond) == 1:
                isi = []
                for rus in data:
                    isi.append(rus.text)
                res = "› M U S I C\n"
                no = 0
                for teex in isi:
                    no += 1
                    res += "\n{}. {}".format(no, teex)
                res += "\n\nTo send soundcloud music details, please use command Soundcloud {}|「number」".format(cond[0])
                line.sendMode(msg, to, sender, cmd, res)
            elif len(cond) == 2:
                res = data[int(cond[1]) - 1]
                line.sendMessage(to, 'tunggu sebentar, audio sedang di download..')
                process = subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output trojans_audio.mp3 %s' % 'https://soundcloud.com%s' % res.get('href'))
                line.sendAudio(to, 'trojans_audio.mp3')
                time.sleep(1)
                os.remove('trojans_audio.mp3')

        elif cmd.startswith("joox "):
            query = removeCmd(text, setKey)
            cond = query.split("/")
            main = json.loads(requests.get("https://apitrojans.xyz/joox/search?query={}&apikey={}".format(cond[0], trojansApikey)).text)
            ret_ = "「 Result Joox 」"
            if len(cond) == 1:
                dataProfile = []
                judul = cond[0].replace(" ","%20")
                for data in main[0:10]:
                    dataProfile.append(template.joox(data["thumbnail"], data["title"], urllib.parse.quote("{}sendaudio {}".format(setKey, data["m4aUrl"]))))
                line.sendLiff(to, dataProfile, mainType=False)
            elif len(cond) == 2:
                if int(cond[1]) <= len(main):
                    data = main[int(cond[1])-1]
                    line.sendLiffImage(to, data["thumbnail"], "https://apkmirror.co.id/wp-content/uploads/2020/01/joox-music.png", " Music Joox")
                    line.sendAudioWithURL(to, data["m4aUrl"])
        
        elif cmd.startswith("getchord "):
            query = removeCmd(text, setKey)
            session = HTMLSession()
            queri = urllib.parse.quote_plus(query)
            response = session.get("https://www.google.com/search?q=chordtela%20" + queri)
            uri = response.html.find(".yuRUbf a")[0].attrs['href']
            req = requests.get(uri)
            soup = BeautifulSoup(req.text, "lxml")
            try:
                title = soup.find("span", {"class": "bcurrent"}).text
                try: chord = soup.find("pre").text[:-2]
                except: chord = "Intro%s" % soup.find("div", {"class": "post"}).text.split("Intro")[1].split("Facebook")[0][:-4]
                ret = f'Title: {title}'
                ret += f'\n{chord}'
                long = len(ret)//10000+1
                for press in range(long):
                    if press != 0:
                        line.sendMessage(to, "{}".format(ret[press*10000 : (press+1)*10000]))
                    else:
                        line.sendReplyMessage(to, "{}".format(ret[press*10000 : (press+1)*10000]), msgIds=msg_id)
            except: 
                line.sendMode(msg, to, sender, cmd, "Chord not found")
                
        elif cmd.startswith("getlyric "):
            search = removeCmd(text, setKey)
            result = requests.get("https://apitrojans.xyz/lyrics?query={}&apikey={}".format(search, trojansApikey)).json()
            if result["status"] != 200:
                return line.sendMode(msg, to, sender, cmd, "Lyric not found")
            res = "Title: "+ result["result"]["title"]
            res += "\nSinger: "+ result["result"]["singer"]
            res += "\n\n"+ result["result"]["lyric"]
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith("acaratv "):
            search = removeCmd(text, setKey)
            result = requests.get("http://dolphinapi.herokuapp.com/api/television?channel={}".format(search)).json()
            res = "Channel: {}".format(search.upper())
            no = 0
            for data in result["result"]:
                no += 1
                res += "\n{}. Jam: {}\nJudul: {}".format(no, data["date"], data["title"])
            line.sendMode(msg, to, sender, cmd, res)
                    
        elif cmd.startswith("twitter "):
            user = removeCmd(text, setKey)
            data = requests.get("https://apitrojans.xyz/twitter?user={}&apikey={}".format(user, trojansApikey)).json()
            res = "› P R O F I L E\n"
            res += "\n• " + data["result"]["id"]
            res += "\n• Name: " + data["result"]["nama"]
            res += "\n• Bio: " + data["result"]["bio"]
            res += "\n• Tweets: {}".format(data["result"]["tweet"])
            res += "\n• Followers: {}".format(data["result"]["followers"])
            res += "\n• Following: {}".format(data["result"]["following"])
            res += "\n• Url: https://twitter.com/" + data["result"]["id"].replace("@", "")
            line.sendLiffImage(to, data["result"]["picture"], 'https://upload.wikimedia.org/wikipedia/id/thumb/9/9f/Twitter_bird_logo_2012.svg/1200px-Twitter_bird_logo_2012.svg.png', ' Twitter Picture')
            line.sendMode(msg, to, sender, cmd, res)

        elif cmd.startswith('twitter#'):
            result = requests.get("https://apitrojans.xyz/twitter/trends?apikey={}".format(trojansApikey))
            data = result.json()
            res = "› H A S H T A G"
            num = 0
            for hash in range(len(data)):
                num += 1
                res += "\n{}. {}".format(str(num), str(data[hash]["title"]))
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd.startswith("twitterpost "):
            url = removeCmd(text, setKey)
            twitterPost(to, url)
                    
        elif cmd.startswith("fbpost "):
            url = removeCmd(text, setKey)
            try:
                req  = requests.post("https://www.getfvid.com/downloader", data={"url": url}).text
                soup = BeautifulSoup(req, "lxml")
                data = soup.find("div", {"class": "col-md-4 btns-download"}).find_all("a")
                result = {}
                for uri in data:
                    if "HD" in  uri.text:
                        result["hd"] =  uri["href"]
                    if "Normal" in  uri.text:
                        result["normal"] =  uri["href"]
                if result:
                    if "hd" in result:
                        line.sendReplyMessage(to, 'wait a minute, the video is on download..', msgIds=msg_id)
                        line.sendVideoWithURL(to, result["hd"])
                    elif "normal" in result:
                        line.sendReplyMessage(to, 'wait a minute, the video is on download..', msgIds=msg_id)
                        line.sendVideoWithURL(to, result["normal"])
                    else:
                        line.sendMode(msg, to, sender, cmd, "Failed to get video")
                else:
                    line.sendMode(msg, to, sender, cmd, "Failed to get video")
            except:
                line.sendMode(msg, to, sender, cmd, "Failed to get video")
                
        elif cmd.startswith("themeline "):
            url_ni = removeCmd(text, setKey)
            if "shop/theme" not in url_ni and "themeshop/product" not in url_ni:
                return line.sendFooter(to, "Make sure the theme url is correct")
            req = requests.get(url_ni)
            data = BeautifulSoup(req.content, "lxml")
            theme_icon = json.loads(data.select('script[type="application/ld+json"]')[0].string)["image"]
            theme_android = theme_icon.split('/WEBSTORE/')[0]+'/ANDROID/theme.zip'
            line.sendMultiImageWithURL(to, [theme_icon, 'https://i.ibb.co/0MP67Pk/97ee4aec4564.jpg'])
            subprocess.getoutput("wget -O theme_android.zip {}".format(theme_android))
            line.sendFile(to, "theme_android.zip")
            line.deleteFile("theme_android.zip")
        
        elif cmd.startswith("pinterestpost "):
            url = removeCmd(text, setKey)
            if 'pin.it/' in url or 'pinterest.com/pin/' in url:
                get = requests.get("https://pinterestdownloader.com/download?url=%s" % url)
                soup = BeautifulSoup(get.text, "lxml")
                media = soup.findAll("a", {"class": "download_button"})
                images = []
                for data in media:
                    if '.gif' in data["href"]:
                        line.sendGIFWithURL(to, data["href"])
                    elif '.mp4' in data["href"]:
                        line.sendVideoWithURL(to, data["href"])
                    elif '/thumbnails/' not in data['href']:
                        images.append(data['href'])
                if images:
                    if len(images) >= 2:
                        line.sendMultiImageWithURL(to, images)
                    else:
                        line.sendReplyImageWithURL(to, images[0], msgIds=msg_id)
            
        elif cmd.startswith("instagram "):
            username = removeCmd(text, setKey)
            result = requests.get("https://apitrojans.xyz/instagram/user?username={}&apikey={}".format(username, trojansApikey))
            data = result.json()
            res = "› P R O F I L E\n"
            res += "\n• @" + data["result"]["username"]
            res += "\n• Name: " + data["result"]["fullname"]
            res += "\n• Bio: " + data["result"]["bio"]
            res += "\n• Followers: {}".format(data["result"]["followers"])
            res += "\n• Following: {}".format(data["result"]["following"])
            res += "\n• Post: {}".format(data["result"]["media"])
            res += "\n• Igtv: {}".format(data["result"]["igtv"])
            if data["result"]["private"] == True: res += "\n• Private: True"
            else: res += "\n• Private: False"
            if data["result"]["verified"] == True: res += "\n• Verified: True"
            else: res += "\n• Verified: False"
            if data["result"]["business"] == True: res += "\n• Business: True"
            else: res += "\n• Business: False"
            res += "\n• https://instagram.com/"+data["result"]["username"]
            line.sendLiffImage(to, data["result"]["profile_img"], 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e7/Instagram_logo_2016.svg/1200px-Instagram_logo_2016.svg.png', " Instagram Picture")
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith("instapost "):
            url = removeCmd(text, setKey)
            main = json.loads(requests.get("https://apitrojans.xyz/instagram/post?url={}&apikey={}".format(url, trojansApikey)).text)
            if main['status'] != 200:
                params = {'apikey': eaterApikey, "url": url}
                main = json.loads(requests.get("https://api.coursehero.store/igpost", params=params).text)
            videos = []
            images = []
            for item in range(len(main["result"]["media"])):
                if main["result"]["media"][item]["is_video"]:
                    line.sendVideoWithURL(to, main["result"]["media"][item]["video"])
                elif 'img' in main["result"]["media"][item]:
                    images.append(main["result"]["media"][item]["img"])
                else:
                    images.append(main["result"]["media"][item]["image"])
            if images:
                if len(images) >= 2:
                    line.sendMultiImageWithURL(to, images)
                else:
                    line.sendImageWithURL(to, images[0])
                
        elif cmd.startswith("instastory "):
            search = removeCmd(text, setKey)
            cond = search.split("/")
            username = str(cond[0])
            main = json.loads(requests.get("https://api.imjustgood.com/instastory={}".format(username), headers={"apikey": rendyApikey, "User-Agent": "Justgood/5.0"}).text)
            if main["status"] != 200:
                return line.sendMessage(to, 'error, make sure the username is correct and not private')
            if len(cond) == 1:
                parsed_len = len(main["result"]["stories"])//10+1
                no = 0
                for point in range(parsed_len):
                    paper = []
                    for wall in main["result"]["stories"][point*10:(point+1)*10]:
                        no += 1
                        if wall["type"] == 'video':
                         #   thumb = 'https://i.ibb.co/Lk8d6mv/a290b870d3be.jpg'
                            thumb = wall["thumbnail"]
                            cmmd = 'sendvideo'
                        else:
                            thumb = wall["url"]
                            cmmd = 'sendpicture'
                        paper.append({
                            "type": "bubble",
                            "size": "micro",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": thumb,
                                        "size": "full",
                                        "aspectRatio": "9:16",
                                        "aspectMode": "cover"
                                    }
                                ],
                                "paddingAll": "0px",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": "https://line.me/R/app/1657710460-y83a8lNE?type=text&text={}".format(urllib.parse.quote("{}{} {}".format(setKey, cmmd, wall["url"])))
                                }
                            }
                        })
                    data = {
                        'type': 'flex',
                        'altText': '%s sent a stories' % line.profile.displayName,
                        'contents': {
                            'type': 'carousel',
                            'contents': paper
                        }
                    }
                    line.sendLiff(to, data)
                    time.sleep(1)
            elif len(cond) == 2:
                num = cond[1]
                if num.isdigit():
                    data = main["result"]["stories"][int(num) - 1]
                    if data["type"] == 'video':
                        line.sendVideoWithURL(to, data["url"])
                    else:
                        line.sendImageWithURL(to, data["url"])
        
        elif cmd.startswith("cocofun "):
            url = removeCmd(text, setKey)
            #scrape by trojans
            req = requests.get(url)
            soup = BeautifulSoup(req.text, "lxml")
            soup = soup.find("script", id={"appState"})
            tostr = "%s" % str(soup)
            tojson = json.loads(tostr[47:][:-9])
            data = tojson["share"]["post"]["post"]
            video_nowm = data["videos"][str(data["imgs"][0]["id"])]["urlext"]
            line.sendVideoWithURL(to, video_nowm)
            
        elif cmd.startswith("zodiak "):
            zodiak = removeCmd(text, setKey)
            url = "https://fimela.com/zodiak/%s" % zodiak.lower()
            soup = BeautifulSoup(requests.get(url).content, "lxml")
            data = soup.find("div", {"container-article"})
            zodiak = data.find("h5").text.capitalize()
            date = data.find("span", {"class": "zodiak--content-header__date"}).text
            perbarui = data.find("time", {"itemprop": "datePublished"}).get("datetime")
            umum = data.find("div", {"class": "zodiak--content__content"}).text
            single = data.findAll("p")[1].text.split("Single: ")[1].split("Couple:")[0]
            couple = data.findAll("p")[1].text.split("Couple: ")[1].split("Single:")[0]
            nomor = data.find("span", {"class": "zodiak--content__numbers"}).text
            img = "%s" % (data.find("img", {"class": "zodiak--content-header__img"}).get("src"))
            url2 = "https://wolipop.detik.com/zodiak/%s" % zodiak.lower()
            soup2 = BeautifulSoup(requests.get(url2).content, "lxml")
            data2 = soup2.find("div", {"class": "detail_text group detail_text2 detail_horoscope"})
            try: umum2 = soup2.findAll("p")[0].text.split("Peruntungan: ")[1].split("Keuangan:")[0]
            except: umum2 = data2.text.split("Peruntungan: ")[1].split("Keuangan:")[0]
            try: keu2 = soup2.findAll("p")[0].text.split("Keuangan: ")[1].split("Asmara:")[0]
            except: keu2 = data2.text.split("Keuangan: ")[1].split("Asmara:")[0]
            try: asmara = soup2.findAll("p")[0].text.split("Asmara: ")[1].split("Jam baik:")[0].split(".")[0]
            except:
                try: asmara = soup2.findAll("p")[0].text.split("Asmara: ")[1].split("Jam Baik:")[0]
                except: asmara = data2.text.split("Asmara: ")[1].split("Jam Baik:")[0]
            try: jam = soup2.findAll("p")[0].text.split("Jam baik: ")[1].split("Asmara:")[0][:-1]
            except:
                try: jam = soup2.findAll("p")[0].text.split("Jam Baik: ")[1].split("Asmara:")[0][:-1]
                except: jam = data2.text.split("Jam Baik: ")[1].split(" ")[0][:-15]
            try: profile = soup2.findAll("p")[1].text.split("Nasehat untuk")[0]
            except: profile = data2.find("p").text.split("Nasehat bagi zodiak")[0]
            iconn = "%s" % ("https://cdn.detik.net.id/wolipop/images/horoscope_icon_%s.png?v=156ecff7" % zodiak.lower())
            url3= "https://www.popbela.com/horoscope/zodiac-%s/full" % zodiak.lower()
            soup3 = BeautifulSoup(requests.get(url3).content, "lxml")
            if soup3.find("div", {"class": "detail-horoscope-item"}).findAll("p")[9].text == "Career":
                karir = soup3.find("div", {"class": "detail-horoscope-item"}).findAll("p")[10].text
            else: karir = soup3.find("div", {"class": "detail-horoscope-item"}).findAll("p")[9].text
            if soup3.find("div", {"class": "detail-horoscope-item"}).findAll("p")[9].text == "Written by : Aurelia Nelly":
                karir = soup3.find("div", {"class": "detail-horoscope-item"}).findAll("p")[5].text
            try:
                if soup3.find("div", {"class": "detail-horoscope-item"}).findAll("p")[11].text == "Friendship":
                    teman = soup3.find("div", {"class": "detail-horoscope-item"}).findAll("p")[12].text
                else: teman = soup3.find("div", {"class": "detail-horoscope-item"}).findAll("p")[11].text
            except: teman = soup3.find("div", {"class": "detail-horoscope-item"}).findAll("p")[7].text
            res = "› I N F O\n"
            res += "\n• Zodiak: {}".format(zodiak)
            res += "\n• Date: {}".format(date)
            res += "\n• Lucky Number: {}".format(nomor)
            res += "\n• Lucky Hour: Hour {}".format(jam)
            res += "\n• Finance: {}".format(keu2)
            res += "\n• Forecast: {}".format(umum)
            res += "\n• fortune: {}".format(umum2)
            res += "\n\n› L O V E\n"
            res += "\n• Single: {}".format(single)
            res += "\n• Couple: {}".format(couple)
            res += "\n• romance: {}".format(asmara)
            res += "\n\n› P R O F I L E\n"
            res += "\n• {}".format(profile)
            res += "\n\n› C A R E E R\n"
            res += "\n• {}".format(karir)
            res += "\n\n› F R I E N D S\n"
            res += "\n• {}".format(teman)
            line.sendMode(msg, to, sender, cmd, res)
          #  line.sendImageWithURL(to, img)
            
        elif cmd.startswith("sifat "):
            textnya = removeCmd(text, setKey)
            rom = random.randint(10, 100)
            tul = random.randint(10, 100)
            roy = random.randint(10, 100)
            mir = random.randint(10, 100)
            mes = random.randint(10, 100)
            res = "› S I F A T\n"
            res += "\n• Romantic: {}%".format(str(rom))
            res += "\n• Sincere: {}%".format(str(tul))
            res += "\n• royalty: {}%".format(str(roy))
            res += "\n• Pity: {}%".format(str(mir))
            res += "\n• Nasty: {}%".format(str(mes))
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith('cookpad '):
            textnya = removeCmd(text, setKey)
            cond = textnya.split("|")
            params = {"apikey": eaterApikey, "search": cond[0], "lang": "id"}
            main = json.loads(requests.get("https://api.coursehero.store/cookpad", params=params).text)
            if len(cond) == 1:
                no = 0
                res = "› C O O K P A D\n"
                for wall in main["result"][0:10]:
                    no += 1
                    res += "\n{}. {}".format(no, wall["title"])
                res += "\n\nTo send recipe details, please use command {}Cookpad {}|「number」".format(setKey.title(), cond[0])
                line.sendMode(msg, to, sender, cmd, res)
            elif len(cond) == 2:
                if cond[1].isdigit():
                    data = main["result"][int(cond[1])-1]
                    dataa = {
                        "type": "image",
                        "originalContentUrl": "{}.webp".format(data["image"]["url"].split(".webp")[0]),
                        "previewImageUrl": "{}.webp".format(data["image"]["url"].split(".webp")[0]),
                        "sentBy": {
                            "label": " source: cookpad",
                            "iconUrl": line.settings["setFlag"]["icon"],
                            "linkUrl": "https://line.me/ti/p/{}".format(line.generateUserTicket())
                        }
                    }
                    line.sendLiff(to, dataa)
                    res = "Ingredients:"
                    no = 0
                    for ingred in data["ingredients"]:
                        no += 1
                        res += "\n    {}. {}".format(no, ingred["quantity_and_name"])
                    res += "\n\nSteps:"
                    no = 0
                    for step in data["steps"]:
                        no += 1
                        res += "\n    {}. {}".format(no, step["description"])
                    line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd.startswith('checkresi '):
            cProvider = ['jne', 'pos', 'tiki', 'jnt', 'lion', 'ninja', 'ide', 'sicepat', 'sap', 'anteraja', 'ncs', 'rex', 'sc', 'wahana', 'jet', 'dse', 'first', 'idl', 'kgx', 'spx']
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if len(sep) >= 2:
                courier = sep[0]
                resi = sep[1]
                if courier.lower() not in cProvider:
                    res = 'Invalid Provider!!'
                    res += '\n\n1. Jalur Nugraha Ekakurir\nProvider: JNE'
                    res += '\n\n2. Pos Indonesia\nProvider: POS'
                    res += '\n\n3. Citra Van Titipan Kilat\nProvider: TIKI'
                    res += '\n\n4. J&T Express\nProvider: JNT'
                    res += '\n\n5. Ninja Express\nProvider: NINJA'
                    res += '\n\n6. ID Express\nProvider: IDE'
                    res += '\n\n7. SiCepat Express\nProvider: SICEPAT'
                    res += '\n\n8. SAP Express\nProvider: SAP'
                    res += '\n\n9. JET Express\nProvider: JET'
                    res += '\n\n10. 21 Express\nProvider: DSE'
                    res += '\n\n11. Lion Parcel\nProvider: LION'
                    res += '\n\n12. AnterAja\nProvider: ANTERAJA'
                    res += '\n\n13. Nusantara Card Semesta\nProvider: NCS'
                    res += '\n\n14. Royal Express Indonesia\nProvider: REX'
                    res += '\n\n15. Sentral Cargo\nProvider: SC'
                    res += '\n\n16. Wahana Prestasi Logistik\nProvider: WAHANA'
                    res += '\n\n17. First Logistics\nProvider: FIRST'
                    res += '\n\n18. IDL Cargo\nProvider: IDL'
                    res += '\n\n19. KGXpress\nProvider: KGX'
                    res += '\n\n20. Shopee Express\nProvider: SPX'
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    req = requests.get('https://cekresi.co.id/')
                    auth = req.headers.get('Set-Cookie').split('=')[1].split(";")[0]
                    headers = {
                        "origin": "https://cekresi.co.id/",
                        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36",
                        "authorization": "Bearer %s" % auth,
                        "x-requested-with": "XMLHttpRequest"
                    }
                    data = { "noResi": resi, "kodeKurir": courier.lower() }
                    post = requests.post("https://cekresi.co.id/service/api/v1/resi", data=data, headers=headers).json()
                    if post["success"]:
                        result = 'Resi: {}'.format(post['data']['summary']['resi'])
                        result += '\nCourier: {}'.format(post['data']['summary']['kurir'])
                        result += '\nStatus: {}'.format(post['data']['summary']['status'])
                        for dataResi in post['data']['history']:
                            result += '\n\nInfo: {}'.format(dataResi['ket'])
                            result += '\nLocation: {}'.format(dataResi['lokasi'])
                            result += '\nDate: {}'.format(dataResi['tanggal'])
                            result += '\nStatus: {}'.format(dataResi['status'])
                        line.sendMode(msg, to, sender, cmd, result)
                    else:
                        line.sendMode(msg, to, sender, cmd, post["message"])

        elif cmd.startswith('arti '):
            textnya = removeCmd(text, setKey)
            params = {"apikey": eaterApikey, "nama": textnya}
            main = json.loads(requests.get("https://api.coursehero.store/primbon", params=params).text)
            line.sendMode(msg, to, sender, cmd, main["result"])
            
        elif cmd.startswith('wallpaper '):
            sap = removeCmd(text, setKey)
            request = requests.get('https://wall.alphacoders.com/api2.0/get.php?auth=f9c33efef3cc523f4bb50f75394295ca&method=search&term={}'.format(sap))
            request_json = request.json()
            paper = []
            for p in request_json['wallpapers'][0:10]:
                img = p['url_image']
                paper.append(template.data_square_temp(img, 'https://line.me/R/app/1657710460-y83a8lNE?type=image&img={}'.format(img)))
            data = {
                'type': 'flex',
                'altText': '%s sent a wallpaper' % line.profile.displayName,
                'contents': {
                    'type': 'carousel',
                    'contents': paper
                }
            }
            line.sendLiff(to, data)
            
        elif cmd.startswith('gif '):
            query = removeCmd(text, setKey)
            r = requests.get("https://api.tenor.com/v1/search?key=PVS5D2UHR0EV&limit=10&q={}".format(str(query))).json()
            gif = []
            for giff in r["results"]:
                gif.append({
                    'imageUrl': str(giff["media"][0]["gif"]["url"]),
                    'size': 'full',
                    'action': {
                        'type': 'uri',
                        'uri': 'https://line.me/R/app/1657710460-y83a8lNE?type=text&text={}'.format(urllib.parse.quote("{}sendgif {}".format(setKey, giff["media"][0]["gif"]["url"])))
                    }
                })
            data = {
                'type': 'template',
                'altText': '%s sent a GIF' % line.profile.displayName,
                'template': {
                    'type': 'image_carousel',
                    'columns': gif
                }
            }
            line.sendLiff(to, data)
            
        elif cmd.startswith('cuaca '):
            kota = removeCmd(text, setKey)
            url = requests.get("http://api.weatherstack.com/current?access_key=1f67bd2db7bf82849516769f2a722283&query={}".format(kota))
            data = json.loads(url.text)
            res = "› W E A T H E R\n"
            res += "\n• Name: {}".format(data["location"]["name"])
            res += "\n• Country: {}".format(data["location"]["country"])
            res += "\n• Region: {}".format(data["location"]["region"])
            res += "\n• Timezone: {}".format(data["location"]["timezone_id"])
            res += "\n• Local Time: {}".format(data["location"]["localtime"])
            res += "\n• Temperature: {} c".format(int(data["current"]["temperature"]))
            res += "\n• Wind: {} m/s".format(int(data["current"]["wind_speed"]))
            res += "\n• Cloud: {}".format(data["current"]["cloudcover"])
            res += "\n• Visibility: {}".format(int(data["current"]["visibility"]))
            line.sendMode(msg, to, sender, cmd, res)
            line.sendLocation(to, data["location"]["name"], float(data["location"]["lat"]), float(data["location"]["lon"]))
            
        elif cmd.startswith('maps '):
            city = removeCmd(text, setKey)
            line.sendLiffImage(to, "https://image.maps.api.here.com/mia/1.6/mapview?app_id=BfZ8dcHfdbDsDyvIlbme&app_code=bVHueWcUAejl27n_Ip6mKg&ci={}&h=500&w=500&t=13".format(city), "https://i1.wp.com/getective.com/wp-content/uploads/2018/08/google-maps-1.png?fit=1600%2C1600&ssl=1", " Google Maps")
            
        elif cmd == "quotes":
            result = requests.get("https://apitrojans.xyz/quotes?apikey={}".format(trojansApikey))
            data = result.json()
            line.sendMode(msg, to, sender, cmd, str(data["result"]["quotes"]))
            
        elif cmd.startswith("ssweb "):
            url = removeCmd(text, setKey)
            result = requests.get("https://image.thum.io/get/{}".format(str(url)))
            link = "https://image.thum.io/get/{}".format(url)
            line.sendLiffImage(to, link, link, " Web Picture")
            
        elif cmd == "bmkg":
            result = requests.get("https://apitrojans.xyz/infobmkg?apikey={}".format(trojansApikey))
            data = result.json()
            dataProfile = template.bmkg(data["result"]["magnitudo"], "{} • {}".format(str(data["result"]["tanggal"]), str(data["result"]["jam"])), data["result"]["lokasi"], data["result"]["koordinat"], data["result"]["arahan"], data["result"]["images"])
            line.sendLiff(to, dataProfile, mainType=False)
            
        elif cmd.startswith("sholat "):
            textnya = removeCmd(text, setKey)
            url = requests.get("http://www.mahesajenar.com/scripts/adzan.php?kota={}".format(textnya))
            soup = BeautifulSoup(url.content,"html.parser")
            data = soup.find("table", id={"tableadzan"}).findAll("tr")
            res = "› T I M E\n"
            res += "\n• Imsyak: {}".format(data[2].text[7:])
            res += "\n• Subuh: {}".format(data[3].text[8:])
            res += "\n• Dzuhur: {}".format(data[5].text[8:])
            res += "\n• Ashar: {}".format(data[6].text[7:])
            res += "\n• Maghrib: {}".format(data[7].text[8:])
            res += "\n• Isya: {}".format(data[8].text[7:])
            line.sendMode(msg, to, sender, cmd, res)
                    
        elif cmd.startswith("image "):
            search = removeCmd(text, setKey)
            req = requests.get("https://www.google.ru/search?q={}&tbm=isch".format(search), headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.142 Safari/537.36"})
            html_output = req.text
            googleregex = "AF_initDataCallback\({key: 'ds:1', isError: {2}false , hash: '.', data:(.*), sideChannel: {}}\);<\/script><script"
            html_links = re.search(googleregex, html_output, re.M | re.I | re.S).group(1)
            full_json = json.loads(html_links)
            for a in full_json:
                if isinstance(a, Iterable):
                    for b in a:
                        if isinstance(b, Iterable):
                            for c in b:
                                if isinstance(c, Iterable):
                                    for d in c:
                                        if d == "GRID_STATE0":
                                            links_json = c[2]
                                            break
            googleImage = []
            for i in links_json[0:10]:
                img = i[1][3][0]
                googleImage.append(template.data_square_temp(img, 'https://line.me/R/app/1657710460-y83a8lNE?type=image&img={}'.format(img)))
            data = {
                'type': 'flex',
                'altText': '%s sent a google pictures' % line.profile.displayName,
                'contents': {
                    'type': 'carousel',
                    'contents': googleImage
                }
            }
            line.sendLiff(to, data)
            
        elif cmd == 'alquran':
            isi = ["Alquran", "Random Ayat", "List Quran", "Quran <num>"]
            line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› A L - Q U R A N", isi))
            
        elif cmd == 'random ayat':
            url = ("http://mahesajenar.com/scripts/ayat.php?r=15&n=20")
            r = requests.get(url)
            soup = BeautifulSoup(r.content,"html.parser")
            data = soup.text[16:][:-15]
            line.sendMode(msg, to, sender, cmd, str(data))
            
        elif cmd.startswith("quran "):
            query = removeCmd(text, setKey)
            url = requests.get("http://api.alquran.cloud/surah/{}".format(query))
            data = url.json()
            no = 0
            ret = ''
            ret += "Surah: {} ({})".format(str(data["data"]["englishName"]), str(data["data"]["name"]))
            ret += "\nType: {}".format(str(data["data"]["revelationType"]))
            ret += "\nTotal Ayat: {}\n".format(str(data["data"]["numberOfAyahs"]))
            for surah in data["data"]["ayahs"]:
                no += 1
                ret += "\n{}. {}".format(no, str(surah["text"]))
            long = len(ret)//10000+1
            for press in range(long):
                if press != 0:
                    line.sendMessage(to, "{}".format(ret[press*10000 : (press+1)*10000]))
                else:
                    line.sendReplyMessage(to, "{}".format(ret[press*10000 : (press+1)*10000]), msgIds=msg_id)
        
        elif cmd.startswith("wikipedia "):
            textt = removeCmd(text, setKey)
            data = requests.get("https://dolphinapi.herokuapp.com/api/wikipedia?query={}".format(textt)).json()
            res = ""
            for texttl in data["result"]["desc"]:
                res += texttl
            long = len(res)//10000+1
            for press in range(long):
                if press != 0:
                    line.sendMessage(to, "{}".format(res[press*10000 : (press+1)*10000]))
                else:
                    line.sendReplyMessage(to, "{}".format(res[press*10000 : (press+1)*10000]), msgIds=msg_id)
                
        elif cmd == "list quran":
            url = requests.get("http://api.alquran.cloud/surah")
            data = url.json()
            res = "› L I S T\n"
            if data["data"] != []:
                no = 0
                for music in data["data"]:
                    no += 1
                    res += "\n{}. {}".format(no, music['englishName'])
                line.sendMode(msg, to, sender, cmd, res)
                
    #----------COMMAND SETTINGS----------#
        elif cmd.startswith('template'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == "template":
                isi = ["Template <on/off>", "Temp Mode Line / Wa / Ig / Tele / Footer", "Temp Style Dark / Normal", "Temp Text <color code>", "Temp Bg Image / <url> / <color code>", "Setflag Name <text>", "Setflag Icon image / <url>", "Delflag Icon / Name", "Color Code"]
                line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› T E M P L A T E", isi))
                
            elif texttl == "on":
                if not line.settings['templateMode']:
                    line.settings['templateMode'] = True
                sendToggle(to, "TEMPLATE MODE", "Template Mode\nStatus: ✔︎", "", True)
            elif texttl == 'off':
                if line.settings['templateMode']:
                    line.settings['templateMode'] = False
                sendToggle(to, "TEMPLATE MODE", "Template Mode\nStatus: ✘", "", False)
            elif texttl == "reset":
                line.settings["tempColor"]["background"] = line.setts["backupTemp"]["color"]["background"]
                line.settings["tempColor"]["border"] = line.setts["backupTemp"]["color"]["border"]
                line.settings["tempColor"]["text"] = line.setts["backupTemp"]["color"]["text"]
                line.settings["tempBackground"] = line.setts["backupTemp"]["backgroundImage"]
                line.sendMode(msg, to, sender, cmd, "Reset Template\nStatus: ✓")
                
        elif cmd == 'color code':
            line.sendFooter(to, "https://www.rapidtables.com/web/color/html-color-codes.html", line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)
            
        elif cmd.startswith("temp "):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl.startswith("bg "):
                sep = textt.split(" ")
                code = textt.replace(sep[0] + " ","")
                if code.lower() == "image":
                    line.setts["upBackground"] = True
                    res = 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                    sendToggle(to, "CHANGE TEMP BACKGROUND", res, res, True)
                elif code.startswith("https"):
                    line.settings["tempBackground"] = code
                    line.sendMode(msg, to, sender, cmd, "Change Temp Background\nStatus: ✓")
                elif code.startswith("#"):
                    line.settings["tempColor"]["background"] = code+"73"
                    line.sendMode(msg, to, sender, cmd, "Change Temp Background Color\nStatus: ✓")
                else:
                    line.sendMode(msg, to, sender, cmd, "example:\n\nTemp Bg Image\n(to set background with image you sent)\nTemp Bg #FFFFFF\n(to set background color)\nTemp Bg URL\n(url image must https)")
            elif texttl.startswith("text "):
                sep = textt.split(" ")
                code = textt.replace(sep[0] + " ","")
                if code.startswith("#"):
                    line.settings["tempColor"]["text"] = code
                    line.sendMode(msg, to, sender, cmd, "Change Temp Text Color\nStatus: ✓")
                else:
                    line.sendMode(msg, to, sender, cmd, "Color code salah, example: #FFFFFF ( pakai # )")
            elif texttl.startswith("mode "):
                sep = textt.split(" ")
                code = textt.replace(sep[0] + " ","")
                if code.lower() == "line":
                    line.settings["tempMode"] = "line"
                    line.sendMode(msg, to, sender, cmd, "Change Temp Mode\nMode: LINE\nStatus: ✓")
                elif code.lower() == "wa":
                    line.settings["tempMode"] = "whatsapp"
                    line.sendMode(msg, to, sender, cmd, "Change Temp Mode\nMode: Whatsapp\nStatus: ✓")
                elif code.lower() == "tele":
                    line.settings["tempMode"] = "telegram"
                    line.sendMode(msg, to, sender, cmd, "Change Temp Mode\nMode: Telegram\nStatus: ✓")
                elif code.lower() == "ig":
                    line.settings["tempMode"] = "instagram"
                    line.sendMode(msg, to, sender, cmd, "Change Temp Mode\nMode: Instagram\nStatus: ✓")
                elif code.lower() == "footer":
                    line.settings["tempMode"] = "footer"
                    line.sendMode(msg, to, sender, cmd, "Change Temp Mode\nMode: Footer\nStatus: ✓")
                else:
                    line.sendMode(msg, to, sender, cmd, "𝗠𝗼𝗱𝗲 𝗟𝗶𝘀𝘁:\n    1. Line\n    2. Tele\n    3. Wa\n    4. Ig\n    5. Footer\n\nexample: Temp Mode Line")
            elif texttl.startswith("style "):
                sep = textt.split(" ")
                code = textt.replace(sep[0] + " ","")
                if code == "dark":
                    line.settings["tempStyle"] = "dark"
                    line.sendMode(msg, to, sender, cmd, "Change Temp Style\nStyle: Dark\nStatus: ✓")
                elif code == "normal":
                    line.settings["tempStyle"] = "normal"
                    line.sendMode(msg, to, sender, cmd, "Change Temp Style\nStyle: Normal\nStatus: ✓")
                    
        elif cmd.startswith("setflag "):
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if len(sep) < 2:
                return line.sendFooter(to, "Example:\n{}Setflag name sozibot\n{}Setflag icon image\n{}Setflag icon https://i.ibb.co/7tmGYQ1/FOOTER-ACODE44.gif".format(setKey.title(), setKey.title(), setKey.title()), reply=True)
            if sep[0].lower() == "name":
                textt = textt.replace(sep[0] + " ","")
                line.settings["setFlag"]["name"] = textt
                line.sendMode(msg, to, sender, cmd, "Successfully changed to '{}'".format(textt))
            elif sep[0].lower() == "icon":
                textt = textt.replace(sep[0] + " ","")
                if textt.startswith("http"):
                    line.settings["setFlag"]["icon"] = textt
                    line.sendMode(msg, to, sender, cmd, "Icon footer successfully changed to '{}'".format(textt))
                elif textt.lower() == "image":
                    line.settings["setFlag"]["status"] = True
                    res = 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                    sendToggle(to, "SET FLAG ICON", res, res, True)
        
        elif cmd.startswith("delflag "):
            textt = removeCmd(text, setKey)
            if textt.lower() == "name":
                line.settings["setFlag"]["name"] = "sozibot"
                line.sendMode(msg, to, sender, cmd, "Flag name reset successfully")
            elif textt.lower() == "icon":
                line.settings["setFlag"]["icon"] = "https://i.ibb.co/7tmGYQ1/FOOTER-ACODE44.gif"
                line.sendMode(msg, to, sender, cmd, "Flag icon reset successfully")

        elif cmd == 'liff type':
            res = "› C O M M A N D\n"
            res += "\n• {}Liff 1".format(setKey.title())
            res += "\n• {}Liff 2".format(setKey.title())
            res += "\n• {}Liff 3".format(setKey.title())
            res += "\n• {}Liff 4".format(setKey.title())
            line.sendReplyMessage(to, res, msgIds=msg_id)
            
        elif cmd == 'liff 1':
            line.settings["arLiff"] = "1657707255-WVxqmM35"
            line.sendMode(msg, to, sender, cmd, "Change Liff Type\nType: Liff 1\nStatus: ✓")
            
        elif cmd == 'liff 2':
            line.settings["arLiff"] = "1657710460-y83a8lNE"
            line.sendMode(msg, to, sender, cmd, "Change Liff Type\nType: Liff 2\nStatus: ✓")
        
        elif cmd == 'liff 3':
            line.settings["arLiff"] = "1656063202-j324n1by"
            line.sendMode(msg, to, sender, cmd, "Change Liff Type\nType: Liff 3\nStatus: ✓")
        
        elif cmd == 'liff 4':
            line.settings["arLiff"] = "1656174387-eqP4329A"
            line.sendMode(msg, to, sender, cmd, "Change Liff Type\nType: Liff 4\nStatus: ✓")
                
        elif cmd == 'set detect resid':
            if msg.toType == 0:
                profile = line.getContact(to)
                res = 'Detect Resid\nat Contact `{}`\nStatus: ON\n\nif you want to turn it off, type `{}del detect resid`'.format(profile.displayName, setKey.title())
            elif msg.toType == 2:
                group = line.getChats([to], False, False).chats[0].chatName
                res = 'Detect Resid\nat Group `{}`\nStatus: ON\n\nif you want to turn it off, type `{}del detect resid`'.format(group, setKey.title())
            else:
                res = 'Detect Resid\nat Unknown\nStatus: ON\n\nif you want to turn it off, type `{}del detect resid`'.format(setKey.title())
            line.settings["detectResidPoint"] = to
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd == 'del detect resid':
            if line.settings["detectResidPoint"] is not None:
                if line.settings["detectResidPoint"].startswith('u'):
                    try:
                        profile = line.getContact(line.settings["detectResidPoint"])
                        res = "Detect Resid\nat Contact `{}`\nStatus: OFF\n\nif you want to turn it on, type `{}set detect resid`".format(profile.displayName, setKey.title())
                    except:
                        res = "Detect Resid\nat Unknown\nStatus: OFF\n\nif you want to turn it on, type `{}set detect resid`".format(setKey.title())
                elif line.settings["detectResidPoint"].startswith('c'):
                    group = line.getChats([line.settings["detectResidPoint"]], False, False).chats[0].chatName
                    res = "Detect Resid\nat Group `{}`\nStatus: OFF\n\nif you want to turn it on, type `{}set detect resid`".format(group, setKey.title())
                else:
                    res = "Detect Resid\nat Unknown\nStatus: OFF\n\nif you want to turn it on, type `{}set detect resid`".format(setKey.title())
            line.settings["detectResidPoint"] = None
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd == 'set detect kick':
            if msg.toType == 0:
                profile = line.getContact(to)
                res = 'Detect Kick\nat Contact `{}`\nStatus: ON\n\nif you want to turn it off, type `{}del detect kick`'.format(profile.displayName, setKey.title())
            elif msg.toType == 2:
                group = line.getChats([to], False, False).chats[0].chatName
                res = 'Detect Kick\nat Group `{}`\nStatus: ON\n\nif you want to turn it off, type `{}del detect kick`'.format(group, setKey.title())
            else:
                res = 'Detect Kick\nat Unknown\nStatus: ON\n\nif you want to turn it off, type `{}del detect kick`'.format(setKey.title())
            line.settings["detectKickPoint"] = to
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd == 'del detect kick':
            if line.settings["detectKickPoint"] is not None:
                if line.settings["detectKickPoint"].startswith('u'):
                    try:
                        profile = line.getContact(line.settings["detectKickPoint"])
                        res = "Detect Kick\nat Contact `{}`\nStatus: OFF\n\nif you want to turn it on, type `{}set detect kick`".format(profile.displayName, setKey.title())
                    except:
                        res = "Detect Kick\nat Unknown\nStatus: OFF\n\nif you want to turn it on, type `{}set detect kick`".format(setKey.title())
                elif line.settings["detectKickPoint"].startswith('c'):
                    group = line.getChats([line.settings["detectKickPoint"]], False, False).chats[0].chatName
                    res = "Detect Kick\nat Group `{}`\nStatus: OFF\n\nif you want to turn it on, type `{}set detect kick`".format(group, setKey.title())
                else:
                    res = "Detect Kick\nat Unknown\nStatus: OFF\n\nif you want to turn it on, type `{}set detect kick`".format(setKey.title())
            line.settings["detectKickPoint"] = None
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith("public "):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl == "mode":
                if to in line.settings["publicBot"] or line.settings["allPublic"]: res = 'Status: ✓'
                else: res = 'Status: ✘'
                res += '\n\n› T Y P E\n'
                res += '\n1 : Groups'
                res += '\n0 : All'
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}Public <type> <on/off>'.format(setKey.title())
                res += '\n• {}Public List'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == "list":
                if line.settings["allPublic"]:
                    return line.sendMode(msg, to, sender, cmd, 'Public Mode has been activated in all groups')
                if line.settings["publicBot"]:
                    res = "› L I S T\n"
                    no = 0
                    for gid in line.settings["publicBot"]:
                        no += 1
                        group = line.getChats([gid], False, False).chats[0]
                        res += "\n{}. {}".format(no, group.chatName)
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    line.sendMode(msg, to, sender, cmd, "List empty")
            else:
                texttl = texttl.split(" ")
                if len(texttl) < 2:
                    return
                if texttl[0] == "1":
                    if texttl[1] == "on":
                        if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
                        gc = line.getChats([to], False, False)
                        if to not in line.settings["publicBot"]:
                            line.settings["publicBot"].append(to)
                        sendToggle(to, "PUBLIC MODE", "Command Public\nGroup: {}\nStatus: ✓".format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), True)
                    elif texttl[1] == "off":
                        if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
                        gc = line.getChats([to], False, False)
                        if to in line.settings["publicBot"]:
                            line.settings["publicBot"].remove(to)
                        sendToggle(to, "PUBLIC MODE", "Command Public\nGroup: {}\nStatus: ✘".format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), False)
                elif texttl[0] == "0":
                    if texttl[1] == "on":
                        if not line.settings["allPublic"]:
                            line.settings["allPublic"] = True
                        sendToggle(to, "PUBLIC MODE", "Command Public\nType: All Group\nStatus: ✓", "Type: All Group", True)
                    elif texttl[1] == "off":
                        if line.settings["allPublic"]:
                            line.settings["allPublic"] = False
                        sendToggle(to, "PUBLIC MODE", "Command Public\nType: All Group\nStatus: ✘", "Type: All Group", False)
                            
        elif cmd.startswith("protect"):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == "protect":
                isi = ["Protect List", "Protect Status", "Protect Kick <on/off>", "Protect Invite <on/off>", "Protect Cancel <on/off>", "Protect QR <on/off>", "Protect All <on/off>"]
                isi2 = ["Protect Kick <num> <on/off>", "Protect Invite <num> <on/off>", "Protect Cancel <num> <on/off>", "Protect QR <num> <on/off>", "Protect All <num> <on/off>"]
                res = looping_command(setKey.title(), "› P R O T E C T", isi)
                res += "\n\n"
                res += looping_command(setKey.title(), "› R E M O T E", isi2)
                res += "\nNum = GroupList"
                line.sendMode(msg, to, sender, cmd, res)
                
            elif texttl == 'list':
                res = 'P R O  K I C K:'
                if line.protect["proKick"]:
                    num = 0
                    for kick in line.protect["proKick"]:
                        num += 1
                        res += '\n    {}. {}'.format(num, str(line.getChats([kick], False, False).chats[0].chatName))
                else:
                    res += '\n    Nothing.'
                res += '\n\nP R O  I N V I T E'
                if line.protect["proInv"]:
                    num = 0
                    for kick in line.protect["proInv"]:
                        num += 1
                        res += '\n    {}. {}'.format(num, str(line.getChats([kick], False, False).chats[0].chatName))
                else:
                    res += '\n    Nothing.'
                res += '\n\nP R O  C A N C E L'
                if line.protect["proCancel"]:
                    num = 0
                    for kick in line.protect["proCancel"]:
                        num += 1
                        res += '\n    {}. {}'.format(num, str(line.getChats([kick], False, False).chats[0].chatName))
                else:
                    res += '\n    Nothing.'
                res += '\n\nP R O  Q R'
                if line.protect["proQr"]:
                    num = 0
                    for kick in line.protect["proQr"]:
                        num += 1
                        res += '\n    {}. {}'.format(num, str(line.getChats([kick], False, False).chats[0].chatName))
                else:
                    res += '\n    Nothing.'
                line.sendMode(msg, to, sender, cmd, res)
                
            elif texttl == 'status':
                if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
                gc = line.getChats([to], False, False)
                if to in line.protect['proKick']: res = '✓ Protect Kick'
                else: res = '✘ Protect Kick'
                if to in line.protect['proInv']: res += '\n✓ Protect Invite'
                else: res += '\n✘ Protect Invite'
                if to in line.protect['proCancel']: res += '\n✓ Protect Cancel'
                else: res += '\n✘ Protect Cancel'
                if to in line.protect['proQr']: res += '\n✓ Protect QR'
                else: res += '\n✘ Protect QR'
                res += "\n\nGroup: {}".format(gc.chats[0].chatName)
                line.sendMode(msg, to, sender, cmd, res)
                
            elif texttl.startswith("kick "):
                if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
                textts = texttl[5:]
                texttu = textts.split(" ")
                if textts == "on":
                    gc = line.getChats([to], False, False)
                    if to not in line.protect['proKick']:
                        line.protect['proKick'].append(to)
                    sendToggle(to, "PROTECT KICK", 'Protect Kick\nGroup: {}\nStatus: ✓'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), True)
                        
                elif textts == "off":
                    gc = line.getChats([to], False, False)
                    if to in line.protect['proKick']:
                        line.protect['proKick'].remove(to)
                    sendToggle(to, "PROTECT KICK", 'Protect Kick\nGroup: {}\nStatus: ✘'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), False)
                
                elif len(texttu) == 2:
                    if texttu[0].isdigit():
                        gc = make_list(line.getAllChatMids(True, False).memberChatMids)
                        if int(texttu[0]) <= len(gc):
                            gid = gc[int(texttu[0]) - 1]
                            if texttu[1] == "on":
                                gc = line.getChats([gid], False, False)
                                if gid not in line.protect['proKick']:
                                    line.protect['proKick'].append(gid)
                                sendToggle(to, "PROTECT KICK", 'Protect Kick\nGroup: {}\nStatus: ✓'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), True)
                            elif texttu[1] == "off":
                                gc = line.getChats([gid], False, False)
                                if gid in line.protect['proKick']:
                                    line.protect['proKick'].remove(gid)
                                sendToggle(to, "PROTECT KICK", 'Protect Kick\nGroup: {}\nStatus: ✘'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), False)
                                
            elif texttl.startswith("invite "):
                if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
                textts = texttl[7:]
                texttu = textts.split(" ")
                if textts == "on":
                    gc = line.getChats([to], False, False)
                    if to not in line.protect['proInv']:
                        line.protect['proInv'].append(to)
                    sendToggle(to, "PROTECT INVITE", 'Protect Invite\nGroup: {}\nStatus: ✓'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), True)
                        
                elif textts == "off":
                    gc = line.getChats([to], False, False)
                    if to in line.protect['proInv']:
                        line.protect['proInv'].remove(to)
                    sendToggle(to, "PROTECT INVITE", 'Protect Invite\nGroup: {}\nStatus: ✘'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), False)
                
                elif len(texttu) == 2:
                    if texttu[0].isdigit():
                        gc = make_list(line.getAllChatMids(True, False).memberChatMids)
                        if int(texttu[0]) <= len(gc):
                            gid = gc[int(texttu[0]) - 1]
                            if texttu[1] == "on":
                                gc = line.getChats([gid], False, False)
                                if gid not in line.protect['proInv']:
                                    line.protect['proInv'].append(gid)
                                sendToggle(to, "PROTECT INVITE", 'Protect Invite\nGroup: {}\nStatus: ✓'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), True)
                            elif texttu[1] == "off":
                                gc = line.getChats([gid], False, False)
                                if gid in line.protect['proInv']:
                                    line.protect['proInv'].remove(gid)
                                sendToggle(to, "PROTECT INVITE", 'Protect Invite\nGroup: {}\nStatus: ✘'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), False)
                    
            elif texttl.startswith("cancel "):
                if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
                textts = texttl[7:]
                texttu = textts.split(" ")
                if textts == "on":
                    gc = line.getChats([to], False, False)
                    if to not in line.protect['proCancel']:
                        line.protect['proCancel'].append(to)
                    sendToggle(to, "PROTECT CANCEL", 'Protect Cancel\nGroup: {}\nStatus: ✓'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), True)
                        
                elif textts == "off":
                    gc = line.getChats([to], False, False)
                    if to in line.protect['proCancel']:
                        line.protect['proCancel'].remove(to)
                    sendToggle(to, "PROTECT CANCEL", 'Protect Cancel\nGroup: {}\nStatus: ✘'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), False)
                
                elif len(texttu) == 2:
                    if texttu[0].isdigit():
                        gc = make_list(line.getAllChatMids(True, False).memberChatMids)
                        if int(texttu[0]) <= len(gc):
                            gid = gc[int(texttu[0]) - 1]
                            if texttu[1] == "on":
                                gc = line.getChats([gid], False, False)
                                if gid not in line.protect['proCancel']:
                                    line.protect['proCancel'].append(gid)
                                sendToggle(to, "PROTECT CANCEL", 'Protect Cancel\nGroup: {}\nStatus: ✓'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), True)
                            elif texttu[1] == "off":
                                gc = line.getChats([gid], False, False)
                                if gid in line.protect['proCancel']:
                                    line.protect['proCancel'].remove(gid)
                                sendToggle(to, "PROTECT CANCEL", 'Protect Cancel\nGroup: {}\nStatus: ✘'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), False)
                    
            elif texttl.startswith("qr "):
                if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
                textts = texttl[3:]
                texttu = textts.split(" ")
                if textts == "on":
                    gc = line.getChats([to], False, False)
                    if to not in line.protect['proQr']:
                        line.protect['proQr'].append(to)
                    sendToggle(to, "PROTECT QR", 'Protect Qr\nGroup: {}\nStatus: ✓'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), True)
                        
                elif textts == "off":
                    gc = line.getChats([to], False, False)
                    if to in line.protect['proQr']:
                        line.protect['proQr'].remove(to)
                    sendToggle(to, "PROTECT QR", 'Protect Qr\nGroup: {}\nStatus: ✘'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), False)
                
                elif len(texttu) == 2:
                    if texttu[0].isdigit():
                        gc = make_list(line.getAllChatMids(True, False).memberChatMids)
                        if int(texttu[0]) <= len(gc):
                            gid = gc[int(texttu[0]) - 1]
                            if texttu[1] == "on":
                                gc = line.getChats([gid], False, False)
                                if gid not in line.protect['proQr']:
                                    line.protect['proQr'].append(gid)
                                sendToggle(to, "PROTECT QR", 'Protect Qr\nGroup: {}\nStatus: ✓'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), True)
                            elif texttu[1] == "off":
                                gc = line.getChats([gid], False, False)
                                if gid in line.protect['proQr']:
                                    line.protect['proQr'].remove(gid)
                                sendToggle(to, "PROTECT QR", 'Protect Qr\nGroup: {}\nStatus: ✘'.format(gc.chats[0].chatName), "Group: {}".format(gc.chats[0].chatName), False)
                    
            elif texttl.startswith("all "):
                if msg.toType != 2: return line.sendFooter(to, 'This command can only be used in groups!!')
                textts = texttl[4:]
                texttu = textts.split(" ")
                if textts == "on":
                    gc = line.getChats([to], False, False)
                    if to in line.protect['proKick']: pass
                    else: line.protect['proKick'].append(to)
                    if to in line.protect['proInv']: pass
                    else: line.protect['proInv'].append(to)
                    if to in line.protect['proCancel']: pass
                    else: line.protect['proCancel'].append(to)
                    if to in line.protect['proQr']: pass
                    else: line.protect['proQr'].append(to)
                    if to in line.protect['proKick']: res = '✓ Protect Kick'
                    else: res = '✘ Protect Kick'
                    if to in line.protect['proInv']: res += '\n✓ Protect Invite'
                    else: res += '\n✘ Protect Invite'
                    if to in line.protect['proCancel']: res += '\n✓ Protect Cancel'
                    else: res += '\n✘ Protect Cancel'
                    if to in line.protect['proQr']: res += '\n✓ Protect QR'
                    else: res += '\n✘ Protect QR'
                    res += "\n\nGroup: {}".format(gc.chats[0].chatName)
                    line.sendMode(msg, to, sender, cmd, res)
                
                elif textts == "off":
                    gc = line.getChats([to], False, False)
                    if to not in line.protect['proKick']: pass
                    else: line.protect['proKick'].remove(to)
                    if to not in line.protect['proInv']: pass
                    else: line.protect['proInv'].remove(to)
                    if to not in line.protect['proCancel']: pass
                    else: line.protect['proCancel'].remove(to)
                    if to not in line.protect['proQr']: pass
                    else: line.protect['proQr'].remove(to)
                    if to in line.protect['proKick']: res = '✓ Protect Kick'
                    else: res = '✘ Protect Kick'
                    if to in line.protect['proInv']: res += '\n✓ Protect Invite'
                    else: res += '\n✘ Protect Invite'
                    if to in line.protect['proCancel']: res += '\n✓ Protect Cancel'
                    else: res += '\n✘ Protect Cancel'
                    if to in line.protect['proQr']: res += '\n✓ Protect QR'
                    else: res += '\n✘ Protect QR'
                    res += "\n\nGroup: {}".format(gc.chats[0].chatName)
                    line.sendMode(msg, to, sender, cmd, res)
                
                elif len(texttu) == 2:
                    if texttu[0].isdigit():
                        gc = make_list(line.getAllChatMids(True, False).memberChatMids)
                        if int(texttu[0]) <= len(gc):
                            gid = gc[int(texttu[0]) - 1]
                            if texttu[1] == "on":
                                gc = line.getChats([gid], False, False)
                                if gid in line.protect['proKick']: pass
                                else: line.protect['proKick'].append(gid)
                                if gid in line.protect['proInv']: pass
                                else: line.protect['proInv'].append(gid)
                                if gid in line.protect['proCancel']: pass
                                else: line.protect['proCancel'].append(gid)
                                if gid in line.protect['proQr']: pass
                                else: line.protect['proQr'].append(gid)
                                if gid in line.protect['proKick']: res = '✓ Protect Kick'
                                else: res = '✘ Protect Kick'
                                if gid in line.protect['proInv']: res += '\n✓ Protect Invite'
                                else: res += '\n✘ Protect Invite'
                                if gid in line.protect['proCancel']: res += '\n✓ Protect Cancel'
                                else: res += '\n✘ Protect Cancel'
                                if gid in line.protect['proQr']: res += '\n✓ Protect QR'
                                else: res += '\n✘ Protect QR'
                                res += "\n\nGroup: {}".format(gc.chats[0].chatName)
                                line.sendMode(msg, to, sender, cmd, res)
                            
                            elif texttu[1] == "off":
                                gc = line.getChats([gid], False, False)
                                if gid not in line.protect['proKick']: pass
                                else: line.protect['proKick'].remove(gid)
                                if gid not in line.protect['proInv']: pass
                                else: line.protect['proInv'].remove(gid)
                                if gid not in line.protect['proCancel']: pass
                                else: line.protect['proCancel'].remove(gid)
                                if gid not in line.protect['proQr']: pass
                                else: line.protect['proQr'].remove(gid)
                                if gid in line.protect['proKick']: res = '✓ Protect Kick'
                                else: res = '✘ Protect Kick'
                                if gid in line.protect['proInv']: res += '\n✓ Protect Invite'
                                else: res += '\n✘ Protect Invite'
                                if gid in line.protect['proCancel']: res += '\n✓ Protect Cancel'
                                else: res += '\n✘ Protect Cancel'
                                if gid in line.protect['proQr']: res += '\n✓ Protect QR'
                                else: res += '\n✘ Protect QR'
                                res += "\n\nGroup: {}".format(gc.chats[0].chatName)
                                line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd.startswith('adders'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == 'adders':
                isi = ["Adders list", "Adders Clear"]
                line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› A D D E R S", isi))
            elif texttl == 'list':
                if line.settings["dataAdders"]:
                    no = 0
                    parsed_len = len(line.settings["dataAdders"])//20+1
                    res = "╭「 Adders List 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in line.settings["dataAdders"][point*20:(point+1)*20]:
                            no += 1
                            if mid == line.settings["dataAdders"][-1]:
                                res += '╰ %i. @!\n' % (no)
                            else:
                                res += '├ %i. @!\n' % (no)
                            mids.append(mid)
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
                else: line.sendMode(msg, to, sender, cmd, 'Adder list is empty')
            elif texttl == 'clear':
                jumlah = len(line.settings["dataAdders"])
                line.sendMode(msg, to, sender, cmd, 'Cleaned successfully\nTotal: {}'.format(jumlah))
                line.settings["dataAdders"].clear()
                
        elif cmd == 'admins':
            if sender == line.profile.mid:
                isi = ["Admin list/contact", "Admin add @Mention", "Admin del @Mention/<num>"]
                ress = "WARNING!!!\nEnglish:\nBe careful add user to admin, because user can use 98% command bot\n\nPakistan:\nمنتظم میں صارفین کو شامل کرنے میں محتاط رہیں، کیونکہ منتظم 98% بوٹ کمانڈ استعمال کر سکتا ہے۔"
                ress += "\n\n"
                ress += looping_command(setKey.title(), "› C O M M A N D", isi)
                ress += "\n\nExample multi add / del\n"
                ress += "\n• Admin add @ @ @ @"
                ress += "\n• Admin del @ @ @ @"
                ress += "\n• Admin del 10,5,8,4,2,11-15"
                line.sendMode(msg, to, sender, cmd, ress)

        elif cmd == 'banning':
            isi = ["Ban list", "ban contact", "Ban add @Mention", "Ban del @Mention/<num>", "White list/contact", "White add @Mention", "White del @Mention/<num>", "Assist list/contact", "Assist add @Mention", "Assist del @Mention/<num>", "Clear Ban/White/Assist", "BackupMode <max/normal>", "BlacklistMode <max/normal>"]
            if line.settings["backupStaff"]:
                bStatus = "Max"
            else:
                bStatus = "Normal"
            if line.settings["blmode"]:
                blStatus = "Max"
            else:
                blStatus = "Normal"
            ress = "Mode:"
            ress += "\n    Backup: `{}`".format(bStatus)
            ress += "\n    Blacklist: `{}`".format(blStatus)
            ress += "\n\nMAX Mode:\n    Backup: you will backup white/assist if they get kicked out in any group even though protect is Off\n\n    Blacklist: you will add user to blacklist if you get kicked out in any group and kick blacklist user in any group even though protect is Off"
            ress += "\n\nNORMAL Mode:\n    Backup: you will backup white/assist if they get kicked out only if protect is On, so if protect Off you will not back up it\n\n    Blacklist: you only add user to blacklist if you get kicked out only if protect is On and kick blacklist user in group only if protect is On"
            ress += "\n\n"
            ress += looping_command(setKey.title(), "› C O M M A N D", isi)
            ress += "\n\nExample multi add / del\n"
            ress += "\n• Ban add @ @ @ @"
            ress += "\n• Ban del @ @ @ @"
            ress += "\n• Ban del 10,5,8,4,2,11-15"
            ress += "\n\nFYI: This command can be used on White/Assist"
            line.sendMode(msg, to, sender, cmd, ress)
            
        elif cmd == 'clear ban':
            if line.protect["blacklist"]:
                jumlah = len(line.protect["blacklist"])
                line.sendMode(msg, to, sender, cmd, 'Clear banned list\nTotal: {}'.format(jumlah))
                line.protect["blacklist"].clear()
            else: 
                line.sendMode(msg, to, sender, cmd, 'Banned list empty!')
            
        elif cmd == 'clear white':
            if line.protect["whitelist"]:
                jumlah = len(line.protect["whitelist"])
                line.sendMode(msg, to, sender, cmd, 'Clear white list\nTotal: {}'.format(jumlah))
                line.protect["whitelist"].clear()
            else: 
                line.sendMode(msg, to, sender, cmd, 'White list empty!')
                
        elif cmd == 'clear assist':
            if line.protect["assistlist"]:
                jumlah = len(line.protect["assistlist"])
                line.sendMode(msg, to, sender, cmd, 'Clear assist list\nTotal: {}'.format(jumlah))
                line.protect["assistlist"].clear()
            else: 
                line.sendMode(msg, to, sender, cmd, 'Assist list empty!')
        
        elif cmd.startswith("backupmode "):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl == "max":
                if not line.settings["backupStaff"]:
                    line.settings["backupStaff"] = True
                res = "Backup Mode set to `Max`\nAssist/White will be backed up anywhere"
                sendToggle(to, "BACKUP MODE", res, res, True)
            elif texttl == "normal":
                if line.settings["backupStaff"]:
                    line.settings["backupStaff"] = False
                res = "Backup Mode set to `Normal`\nAssist/White will be backed up if protect on"
                sendToggle(to, "BACKUP MODE", res, res, False)
        
        elif cmd.startswith("blacklistmode "):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl == "max":
                if not line.settings["blmode"]:
                    line.settings["blmode"] = True
                res = "Blacklist Mode set to `Max`\nKick and Add Blacklist anywhere"
                sendToggle(to, "BLACKLIST MODE", res, res, True)
            elif texttl == "normal":
                if line.settings["blmode"]:
                    line.settings["blmode"] = False
                res = "Blacklist Mode set to `Normal`\nKick and Add Blacklist only if protect on"
                sendToggle(to, "BLACKLIST MODE", res, res, False)
            
        elif cmd.startswith('ban '):
            textt = removeCmd(text, setKey)
            cond = textt.split(' ')
            texttl = textt.lower()
            if texttl == 'list':
                if line.protect["blacklist"]:
                    no = 0
                    parsed_len = len(line.protect["blacklist"])//20+1
                    res = "╭「 Banned List 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in line.protect["blacklist"][point*20:(point+1)*20]:
                            if mid == '':
                                line.protect["blacklist"].remove('')
                                continue
                            no += 1
                            if mid == line.protect["blacklist"][-1]:
                                res += '╰ %i. @!\n' % (no)
                            else:
                                res += '├ %i. @!\n' % (no)
                            mids.append(mid)
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
                else: line.sendMode(msg, to, sender, cmd, 'Banned list empty')
                
            elif texttl == "contact":
                line.setts["banContact"] = True
                res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                sendToggle(to, "BAN CONTACT", res, res, True)
                
            elif texttl.startswith("add "):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    parsed_len = len(mentions['MENTIONEES'])//20+1
                    no = 0
                    res = "╭「 Add Ban 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                            no += 1
                            if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                if mid['M'] not in line.protect["blacklist"]:
                                    res += '╰ %i. @! > Added\n' % (no)
                                    line.protect["blacklist"].append(mid['M'])
                                else:
                                    res += '╰ %i. @! > Already\n' % (no)
                            else:
                                if mid['M'] not in line.protect["blacklist"]:
                                    res += '├ %i. @! > Added\n' % (no)
                                    line.protect["blacklist"].append(mid['M'])
                                else:
                                    res += '├ %i. @! > Already\n' % (no)
                            mids.append(mid['M'])
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
                            
            elif texttl.startswith("del "):
                if line.protect["blacklist"]:
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        parsed_len = len(mentions['MENTIONEES'])//20+1
                        no = 0
                        res = "╭「 Del Ban 」\n"
                        for point in range(parsed_len):
                            mids = []
                            for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                                no += 1
                                if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                    if mid['M'] in line.protect["blacklist"]:
                                        res += '╰ %i. @! > Deleted\n' % (no)
                                        line.protect["blacklist"].remove(mid['M'])
                                    else:
                                        res += '╰ %i. @! > Not in list\n' % (no)
                                else:
                                    if mid['M'] in line.protect["blacklist"]:
                                        res += '├ %i. @! > Deleted\n' % (no)
                                        line.protect["blacklist"].remove(mid['M'])
                                    else:
                                        res += '├ %i. @! > Not in list\n' % (no)
                                mids.append(mid['M'])
                            if mids:
                                if res.endswith('\n'): res = res[:-1]
                                if point != 0:
                                    line.sendMention(to, res, mids)
                                else:
                                    line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                res = ""
                    else:
                        targets = filter_target(texttl.replace(cond[0] + " ",""), line.protect["blacklist"])
                        if targets:
                            parsed_len = len(targets)//20+1
                            no = 0
                            res = "╭「 Del Ban 」\n"
                            for point in range(parsed_len):
                                mids = []
                                for mid in targets[point*20:(point+1)*20]:
                                    no += 1
                                    if mid == targets[-1]:
                                        if mid in line.protect["blacklist"]:
                                            res += '╰ %i. @! > Deleted\n' % (no)
                                            line.protect["blacklist"].remove(mid)
                                        else:
                                            res += '╰ %i. @! > Not in list\n' % (no)
                                    else:
                                        if mid in line.protect["blacklist"]:
                                            res += '├ %i. @! > Deleted\n' % (no)
                                            line.protect["blacklist"].remove(mid)
                                        else:
                                            res += '├ %i. @! > Not in list\n' % (no)
                                    mids.append(mid)
                                if mids:
                                    if res.endswith('\n'): res = res[:-1]
                                    if point != 0:
                                        line.sendMention(to, res, mids)
                                    else:
                                        line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                    res = ""
                else:
                    line.sendMode(msg, to, sender, cmd, 'Banned list empty')
                
        elif cmd.startswith('white '):
            textt = removeCmd(text, setKey)
            cond = textt.split(' ')
            texttl = textt.lower()
            if texttl == 'list':
                if line.protect["whitelist"]:
                    no = 0
                    parsed_len = len(line.protect["whitelist"])//20+1
                    res = "╭「 White List 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in line.protect["whitelist"][point*20:(point+1)*20]:
                            no += 1
                            if mid == line.protect["whitelist"][-1]:
                                res += '╰ %i. @!\n' % (no)
                            else:
                                res += '├ %i. @!\n' % (no)
                            mids.append(mid)
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
                else: line.sendMode(msg, to, sender, cmd, 'White list empty')
                
            elif texttl == "contact":
                line.setts["whiteContact"] = True
                res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                sendToggle(to, "WHITE CONTACT", res, res, True)
                
            elif texttl.startswith("add "):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    parsed_len = len(mentions['MENTIONEES'])//20+1
                    no = 0
                    res = "╭「 Add White 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                            no += 1
                            if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                if mid['M'] not in line.protect["whitelist"]:
                                    res += '╰ %i. @! > Added\n' % (no)
                                    line.protect["whitelist"].append(mid['M'])
                                else:
                                    res += '╰ %i. @! > Already\n' % (no)
                            else:
                                if mid['M'] not in line.protect["whitelist"]:
                                    res += '├ %i. @! > Added\n' % (no)
                                    line.protect["whitelist"].append(mid['M'])
                                else:
                                    res += '├ %i. @! > Already\n' % (no)
                            mids.append(mid['M'])
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
                            
            elif texttl.startswith("del "):
                if line.protect["whitelist"]:
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        parsed_len = len(mentions['MENTIONEES'])//20+1
                        no = 0
                        res = "╭「 Del White 」\n"
                        for point in range(parsed_len):
                            mids = []
                            for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                                no += 1
                                if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                    if mid['M'] in line.protect["whitelist"]:
                                        res += '╰ %i. @! > Deleted\n' % (no)
                                        line.protect["whitelist"].remove(mid['M'])
                                    else:
                                        res += '╰ %i. @! > Not in list\n' % (no)
                                else:
                                    if mid['M'] in line.protect["whitelist"]:
                                        res += '├ %i. @! > Deleted\n' % (no)
                                        line.protect["whitelist"].remove(mid['M'])
                                    else:
                                        res += '├ %i. @! > Not in list\n' % (no)
                                mids.append(mid['M'])
                            if mids:
                                if res.endswith('\n'): res = res[:-1]
                                if point != 0:
                                    line.sendMention(to, res, mids)
                                else:
                                    line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                res = ""
                    else:
                        targets = filter_target(texttl.replace(cond[0] + " ",""), line.protect["whitelist"])
                        if targets:
                            parsed_len = len(targets)//20+1
                            no = 0
                            res = "╭「 Del White 」\n"
                            for point in range(parsed_len):
                                mids = []
                                for mid in targets[point*20:(point+1)*20]:
                                    no += 1
                                    if mid == targets[-1]:
                                        if mid in line.protect["whitelist"]:
                                            res += '╰ %i. @! > Deleted\n' % (no)
                                            line.protect["whitelist"].remove(mid)
                                        else:
                                            res += '╰ %i. @! > Not in list\n' % (no)
                                    else:
                                        if mid in line.protect["whitelist"]:
                                            res += '├ %i. @! > Deleted\n' % (no)
                                            line.protect["whitelist"].remove(mid)
                                        else:
                                            res += '├ %i. @! > Not in list\n' % (no)
                                    mids.append(mid)
                                if mids:
                                    if res.endswith('\n'): res = res[:-1]
                                    if point != 0:
                                        line.sendMention(to, res, mids)
                                    else:
                                        line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                    res = ""
                else:
                    line.sendMode(msg, to, sender, cmd, 'White List empty')
                    
        elif cmd.startswith('assist '):
            textt = removeCmd(text, setKey)
            cond = textt.split(' ')
            texttl = textt.lower()
            if texttl == 'list':
                if line.protect["assistlist"]:
                    no = 0
                    parsed_len = len(line.protect["assistlist"])//20+1
                    res = "╭「 Assist List 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in line.protect["assistlist"][point*20:(point+1)*20]:
                            no += 1
                            if mid == line.protect["assistlist"][-1]:
                                res += '╰ %i. @!\n' % (no)
                            else:
                                res += '├ %i. @!\n' % (no)
                            mids.append(mid)
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
                else: line.sendMode(msg, to, sender, cmd, 'Assist list empty')
                
            elif texttl == "contact":
                line.setts["assContact"] = True
                res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                sendToggle(to, "ASSIST CONTACT", res, res, True)
                
            elif texttl.startswith("add "):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    parsed_len = len(mentions['MENTIONEES'])//20+1
                    no = 0
                    res = "╭「 Add Assist 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                            no += 1
                            if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                if mid['M'] not in line.protect["assistlist"]:
                                    res += '╰ %i. @! > Added\n' % (no)
                                    line.protect["assistlist"].append(mid['M'])
                                else:
                                    res += '╰ %i. @! > Already\n' % (no)
                            else:
                                if mid['M'] not in line.protect["assistlist"]:
                                    res += '├ %i. @! > Added\n' % (no)
                                    line.protect["assistlist"].append(mid['M'])
                                else:
                                    res += '├ %i. @! > Already\n' % (no)
                            mids.append(mid['M'])
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
                            
            elif texttl.startswith("del "):
                if line.protect["assistlist"]:
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        parsed_len = len(mentions['MENTIONEES'])//20+1
                        no = 0
                        res = "╭「 Del Assist 」\n"
                        for point in range(parsed_len):
                            mids = []
                            for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                                no += 1
                                if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                    if mid['M'] in line.protect["assistlist"]:
                                        res += '╰ %i. @! > Deleted\n' % (no)
                                        line.protect["assistlist"].remove(mid['M'])
                                    else:
                                        res += '╰ %i. @! > Not in list\n' % (no)
                                else:
                                    if mid['M'] in line.protect["assistlist"]:
                                        res += '├ %i. @! > Deleted\n' % (no)
                                        line.protect["assistlist"].remove(mid['M'])
                                    else:
                                        res += '├ %i. @! > Not in list\n' % (no)
                                mids.append(mid['M'])
                            if mids:
                                if res.endswith('\n'): res = res[:-1]
                                if point != 0:
                                    line.sendMention(to, res, mids)
                                else:
                                    line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                res = ""
                    else:
                        targets = filter_target(texttl.replace(cond[0] + " ",""), line.protect["assistlist"])
                        if targets:
                            parsed_len = len(targets)//20+1
                            no = 0
                            res = "╭「 Del Assist 」\n"
                            for point in range(parsed_len):
                                mids = []
                                for mid in targets[point*20:(point+1)*20]:
                                    no += 1
                                    if mid == targets[-1]:
                                        if mid in line.protect["assistlist"]:
                                            res += '╰ %i. @! > Deleted\n' % (no)
                                            line.protect["assistlist"].remove(mid)
                                        else:
                                            res += '╰ %i. @! > Not in list\n' % (no)
                                    else:
                                        if mid in line.protect["assistlist"]:
                                            res += '├ %i. @! > Deleted\n' % (no)
                                            line.protect["assistlist"].remove(mid)
                                        else:
                                            res += '├ %i. @! > Not in list\n' % (no)
                                    mids.append(mid)
                                if mids:
                                    if res.endswith('\n'): res = res[:-1]
                                    if point != 0:
                                        line.sendMention(to, res, mids)
                                    else:
                                        line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                    res = ""
                else:
                    line.sendMode(msg, to, sender, cmd, 'Assist List empty')
        
        elif cmd.startswith('admin '):
            if sender == line.profile.mid:
                textt = removeCmd(text, setKey)
                cond = textt.split(' ')
                texttl = textt.lower()
                if texttl == 'list':
                    if line.protect["adminlist"]:
                        no = 0
                        parsed_len = len(line.protect["adminlist"])//20+1
                        res = "╭「 Admin List 」\n"
                        for point in range(parsed_len):
                            mids = []
                            for mid in line.protect["adminlist"][point*20:(point+1)*20]:
                                no += 1
                                if mid == line.protect["adminlist"][-1]:
                                    res += '╰ %i. @!\n' % (no)
                                else:
                                    res += '├ %i. @!\n' % (no)
                                mids.append(mid)
                            if mids:
                                if res.endswith('\n'): res = res[:-1]
                                if point != 0:
                                    line.sendMention(to, res, mids)
                                else:
                                    line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                res = ""
                    else: line.sendMode(msg, to, sender, cmd, 'Admin list empty')
                    
                elif texttl == "contact":
                    line.setts["adminContact"] = True
                    res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                    sendToggle(to, "ADMIN CONTACT", res, res, True)
                    
                elif texttl.startswith("add "):
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        parsed_len = len(mentions['MENTIONEES'])//20+1
                        no = 0
                        res = "╭「 Add Admin 」\n"
                        for point in range(parsed_len):
                            mids = []
                            for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                                no += 1
                                if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                    if mid['M'] not in line.protect["adminlist"]:
                                        res += '╰ %i. @! > Added\n' % (no)
                                        line.protect["adminlist"].append(mid['M'])
                                    else:
                                        res += '╰ %i. @! > Already\n' % (no)
                                else:
                                    if mid['M'] not in line.protect["adminlist"]:
                                        res += '├ %i. @! > Added\n' % (no)
                                        line.protect["adminlist"].append(mid['M'])
                                    else:
                                        res += '├ %i. @! > Already\n' % (no)
                                mids.append(mid['M'])
                            if mids:
                                if res.endswith('\n'): res = res[:-1]
                                if point != 0:
                                    line.sendMention(to, res, mids)
                                else:
                                    line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                res = ""
                                
                elif texttl.startswith("del "):
                    if line.protect["adminlist"]:
                        if 'MENTION' in msg.contentMetadata != None:
                            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                            parsed_len = len(mentions['MENTIONEES'])//20+1
                            no = 0
                            res = "╭「 Del Admin 」\n"
                            for point in range(parsed_len):
                                mids = []
                                for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                                    no += 1
                                    if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                        if mid['M'] in line.protect["adminlist"]:
                                            res += '╰ %i. @! > Deleted\n' % (no)
                                            line.protect["adminlist"].remove(mid['M'])
                                        else:
                                            res += '╰ %i. @! > Not in list\n' % (no)
                                    else:
                                        if mid['M'] in line.protect["adminlist"]:
                                            res += '├ %i. @! > Deleted\n' % (no)
                                            line.protect["adminlist"].remove(mid['M'])
                                        else:
                                            res += '├ %i. @! > Not in list\n' % (no)
                                    mids.append(mid['M'])
                                if mids:
                                    if res.endswith('\n'): res = res[:-1]
                                    if point != 0:
                                        line.sendMention(to, res, mids)
                                    else:
                                        line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                    res = ""
                        else:
                            targets = filter_target(texttl.replace(cond[0] + " ",""), line.protect["adminlist"])
                            if targets:
                                parsed_len = len(targets)//20+1
                                no = 0
                                res = "╭「 Del Admin 」\n"
                                for point in range(parsed_len):
                                    mids = []
                                    for mid in targets[point*20:(point+1)*20]:
                                        no += 1
                                        if mid == targets[-1]:
                                            if mid in line.protect["adminlist"]:
                                                res += '╰ %i. @! > Deleted\n' % (no)
                                                line.protect["adminlist"].remove(mid)
                                            else:
                                                res += '╰ %i. @! > Not in list\n' % (no)
                                        else:
                                            if mid in line.protect["adminlist"]:
                                                res += '├ %i. @! > Deleted\n' % (no)
                                                line.protect["adminlist"].remove(mid)
                                            else:
                                                res += '├ %i. @! > Not in list\n' % (no)
                                        mids.append(mid)
                                    if mids:
                                        if res.endswith('\n'): res = res[:-1]
                                        if point != 0:
                                            line.sendMention(to, res, mids)
                                        else:
                                            line.sendReplyMention(to, res, mids, msgIds=msg_id)
                                        res = ""
                    else:
                        line.sendMode(msg, to, sender, cmd, 'Admin List empty')

        elif cmd == 'videotl on':
            if not line.settings['videotl']:
                line.settings['videotl'] = True
            sendToggle(to, "VIDEO TIMELINE", "Get Video Timeline\nStatus: ✓", "", True)
                
        elif cmd == 'videotl off':
            if line.settings['videotl']:
                line.settings['videotl'] = False
            sendToggle(to, "VIDEO TIMELINE", "Get Video Timeline\nStatus: ✘", "", False)
                
        elif cmd.startswith('autoblock'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            cond = textt.split(' ')
            res = 'Status: ' + bool_dict[line.settings['autoBlock']['status']][4]
            res += '\nMessage: ' + line.settings['autoBlock']['message']
            res += '\n\n› C O M M A N D\n'
            res += '\n• {}AutoBlock'.format(setKey.title())
            res += '\n• {}AutoBlock <on/off>'.format(setKey.title())
            res += '\n• {}AutoBlock <message>'.format(setKey.title())
            if cmd == 'autoblock':
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['autoBlock']['status']:
                    line.settings['autoBlock']['status'] = True
                sendToggle(to, "AUTOBLOCK", "Auto Block User\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['autoBlock']['status']:
                    line.settings['autoBlock']['status'] = False
                sendToggle(to, "AUTOBLOCK", "Auto Block User\nStatus: ✘", "", False)
            elif 'STICON_OWNERSHIP' in msg.contentMetadata:
                getEmoji = line.metadataFilter(msg.contentMetadata, len(setKey)+10, type='emoji')
                line.settings["autoBlock"]["contentMetadata"] = getEmoji
                line.settings['autoBlock']['message'] = textt
                getEmoji2 = line.metadataFilter(getEmoji, 32, type='emoji2')
                if "@!" in textt:
                    line.settings["autoBlock"]["contentMention"] = line.metadataFilter(getEmoji, text=textt, type='mention')
                    getEmoji2.update(line.metadataFilter(getEmoji, text='Message successfully changed to `{}`'.format(textt), type='mention'))
                line.sendReplyMessage(to, 'Message successfully changed to `{}`'.format(textt), getEmoji2, msgIds=msg_id)
            else:
                line.settings["autoBlock"]["contentMetadata"] = {}
                line.settings["autoBlock"]["contentMention"] = {}
                line.settings['autoBlock']['message'] = textt
                line.sendMode(msg, to, sender, cmd, 'Message successfully changed to \'%s\'' % textt)
                
        elif cmd.startswith('detectcall'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl == 'on':
                if not line.settings['responCall']:
                    line.settings['responCall'] = True
                sendToggle(to, "DETECTCALL", "Detect Group Call\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['responCall']:
                    line.settings['responCall'] = False
                sendToggle(to, "DETECTCALL", "Detect Group Call\nStatus: ✘", "", False)
                    
        elif cmd.startswith('wordban'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == "wordban":
                isi = ["Wordban List", "Wordban add <text>", "Wordban del <text>"]
                line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› W O R D B A N", isi))
            elif texttl == 'list':
                if line.settings['wordban']:
                    no = 1
                    res = "› W O R D B A N\n"
                    for teex in line.settings['wordban']:
                        no += 1
                        res += "\n{}. {}".format(no, teex)
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    line.sendMode(msg, to, sender, cmd, "Wordban empty!")
            elif texttl.startswith("add "):
                textu = texttl[4:]
                if textu not in line.settings['wordban']:
                    line.settings['wordban'].append(textu)
                    line.sendMode(msg, to, sender, cmd, "Add Wordban\nText: {}".format(textu))
                else:
                    line.sendMode(msg, to, sender, cmd, "Add Wordban\nText: {}".format(textu))
            elif texttl.startswith("del "):
                textu = texttl[4:]
                if textu in line.settings['wordban']:
                    line.settings['wordban'].remove(textu)
                    line.sendMode(msg, to, sender, cmd, "Del Wordban\nText: {}".format(textu))
                else:
                    line.sendMode(msg, to, sender, cmd, "Del Wordban\n'{}' not in list".format(textu))
            
        elif cmd.startswith('error'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == "error":
                isi = ["Error", "Error Logs", "Error Reset", "Error Detail <errid>"]
                line.sendMode(msg, to, sender, cmd, looping_command(setKey.title(), "› E R R O R", isi))
            elif texttl == 'logs':
                try:
                    filee = open('tmp/errorLog.txt', 'r')
                except FileNotFoundError:
                    return line.sendMode(msg, to, sender, cmd, 'File not found!')
                errors = [err.strip() for err in filee.readlines()]
                filee.close()
                if not errors: return line.sendMode(msg, to, sender, cmd, 'Failed display error logs, empty error logs')
                res = "› LIST"
                parsed_len = len(errors)//100+1
                no = 0
                for point in range(parsed_len):
                    for error in errors[point*100:(point+1)*100]:
                        if not error: continue
                        no += 1
                        res += '\n%i. %s' % (no, error)
                        if error == errors[-1]:
                            res += '\n'
                    if res:
                        if res.startswith('\n'): res = res[1:]
                        line.sendMode(msg, to, sender, cmd, res)
                    res = ''
            elif texttl == 'reset':
                filee = open('tmp/errorLog.txt', 'w')
                filee.write('')
                filee.close()
                shutil.rmtree('tmp/errors/', ignore_errors=True)
                os.system('mkdir tmp/errors')
                line.sendMode(msg, to, sender, cmd, 'Logs cleared successfully')
            elif texttl.startswith('detail'):
                jumlah = texttl.split(" ")
                if len(jumlah) < 2:
                    return line.sendMode(msg, to, sender, cmd, "example\nError detail 123")
                errid = texttl[7:]
                if os.path.exists('tmp/errors/%s.txt' % errid):
                    with open('tmp/errors/%s.txt' % errid, 'r') as f:
                        line.sendMode(msg, to, sender, cmd, f.read())
                else:
                    return line.sendMode(msg, to, sender, cmd, "No files found with ID '{}'".format(errid))
                    
        elif txt.startswith('setkey'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            res = 'Status: ' + bool_dict[line.settings['setKey']['status']][4]
            res += '\nKey: 「' + line.settings['setKey']['key'].title() + '」'
            res += '\n\n› C O M M A N D\n'
            res += '\n• Setkey'
            res += '\n• Setkey <on/off>'
            res += '\n• Setkey <key>'
            if txt == 'setkey':
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['setKey']['status']:
                    line.settings['setKey']['status'] = True
                sendToggle(to, "SETKEY", 'Set key: 「{}」\nStatus: ✓'.format(line.settings['setKey']['key'].title()), "Set key: 「{}」".format(line.settings['setKey']['key'].title()), True)
            elif texttl == 'off':
                if line.settings['setKey']['status']:
                    line.settings['setKey']['status'] = False
                sendToggle(to, "SETKEY", 'Set key: 「{}」\nStatus: ✘'.format(line.settings['setKey']['key'].title()), "Set key: 「{}」".format(line.settings['setKey']['key'].title()), False)
            else:
                line.settings['setKey']['key'] = texttl
                line.sendMode(msg, to, sender, cmd, 'Set key successfully changed to \'%s\'' % texttl)
                
        elif cmd.startswith("detect "):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl == 'mid on':
                line.setts["detectID"]["mid"] = True
                sendToggle(to, "DETECT MID", "Auto Detect Mid\nStatus: ✓", "", True)
            elif texttl == 'mid off':
                line.setts["detectID"]["mid"] = False
                sendToggle(to, "DETECT MID", "Auto Detect Mid\nStatus: ✘", "", False)
            elif texttl == 'gid on':
                line.setts["detectID"]["gid"] = True
                sendToggle(to, "DETECT GID", "Auto Detect Gid\nStatus: ✓", "", True)
            elif texttl == 'gid off':
                line.setts["detectID"]["gid"] = False
                sendToggle(to, "DETECT GID", "Auto Detect Gid\nStatus: ✘", "", False)
                
        elif cmd.startswith('shareurl'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == 'shareurl':
                isi = ["ShareURL Instagram <on/off>", "ShareURL Pinterest <on/off>", "ShareURL Youtube <on/off>", "ShareURL Smule <on/off>", "ShareURL Timeline <on/off>", "ShareURL Tiktok <on/off>", "ShareURL Twitter <on/off>", "ShareURL Fb <on/off>", "ShareURL Theme <on/off>", "ShareURL Cocofun <on/off>"]
                isi2 = []
                isi2.append("Instagram: "+ bool_dict[line.settings['shareIG']][4])
                isi2.append("Pinterest: "+ bool_dict[line.settings['sharePinterest']][4])
                isi2.append("Youtube: "+ bool_dict[line.settings['shareYoutube']][4])
                isi2.append("Smule: "+ bool_dict[line.settings['shareSmule']][4])
                isi2.append("Timeline: "+ bool_dict[line.settings['shareTimeline']][4])
                isi2.append("Tiktok: "+ bool_dict[line.settings['shareTiktok']][4])
                isi2.append("Twitter: "+ bool_dict[line.settings['shareTwitter']][4])
                isi2.append("Theme: "+ bool_dict[line.settings['shareTheme']][4])
                isi2.append("Facebook: "+ bool_dict[line.settings['shareFb']][4])
                isi2.append("Cocofun: "+ bool_dict[line.settings['shareCocofun']][4])
                res = looping_command(setKey.title(), "› S T A T U S", isi2)
                res += "\n\n"+str(looping_command(setKey.title(), "› C O M M A N D", isi))
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl.startswith('instagram '):
                ig = texttl[10:]
                if ig == 'on':
                    if not line.settings['shareIG']:
                        line.settings['shareIG'] = True
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Instagram\nStatus: ✓", "Type: Instagram", True)
                elif ig == 'off':
                    if line.settings['shareIG']:
                        line.settings['shareIG'] = False
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Instagram\nStatus: ✘", "Type: Instagram", False)
            elif texttl.startswith('pinterest '):
                pin = texttl[10:]
                if pin == 'on':
                    if not line.settings['sharePinterest']:
                        line.settings['sharePinterest'] = True
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Pinterest\nStatus: ✓", "Type: Pinterest", True)
                elif pin == 'off':
                    if line.settings['sharePinterest']:
                        line.settings['sharePinterest'] = False
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Pinterest\nStatus: ✘", "Type: Pinterest", False)
            elif texttl.startswith('youtube'):
                yt = texttl[8:]
                if yt == 'on':
                    if not line.settings['shareYoutube']:
                        line.settings['shareYoutube'] = True
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Youtube\nStatus: ✓", "Type: Youtube", True)
                elif yt == 'off':
                    if line.settings['shareYoutube']:
                        line.settings['shareYoutube'] = False
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Youtube\nStatus: ✘", "Type: Youtube", False)
            elif texttl.startswith('smule'):
                smu = texttl[6:]
                if smu == 'on':
                    if not line.settings['shareSmule']:
                        line.settings['shareSmule'] = True
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Smule\nStatus: ✓", "Type: Smule", True)
                elif smu == 'off':
                    if line.settings['shareSmule']:
                        line.settings['shareSmule'] = False
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Smule\nStatus: ✘", "Type: Smule", False)
            elif texttl.startswith('timeline'):
                tim = texttl[9:]
                if tim == 'on':
                    if not line.settings['shareTimeline']:
                        line.settings['shareTimeline'] = True
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Timeline\nStatus: ✓", "Type: Timeline", True)
                elif tim == 'off':
                    if line.settings['shareTimeline']:
                        line.settings['shareTimeline'] = False
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Timeline\nStatus: ✘", "Type: Timeline", False)
            elif texttl.startswith('tiktok'):
                tik = texttl[7:]
                if tik == 'on':
                    if not line.settings['shareTiktok']:
                        line.settings['shareTiktok'] = True
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Tiktok\nStatus: ✓", "Type: Tiktok", True)
                elif tik == 'off':
                    if line.settings['shareTiktok']:
                        line.settings['shareTiktok'] = False
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Tiktok\nStatus: ✘",  "Type: Tiktok", False)
            elif texttl.startswith('twitter'):
                tw = texttl[8:]
                if tw == 'on':
                    if not line.settings['shareTwitter']:
                        line.settings['shareTwitter'] = True
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Twitter\nStatus: ✓", "Type: Twitter", True)
                elif tw == 'off':
                    if line.settings['shareTwitter']:
                        line.settings['shareTwitter'] = False
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Twitter\nStatus: ✘", "Type: Twitter", False)
            elif texttl.startswith('fb'):
                ffb = texttl[3:]
                if ffb == 'on':
                    if not line.settings['shareFb']:
                        line.settings['shareFb'] = True
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Facebook\nStatus: ✓", "Type: Facebook", True)
                elif ffb == 'off':
                    if line.settings['shareFb']:
                        line.settings['shareFb'] = False
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Facebook\nStatus: ✘", "Type: Facebook", False)
            elif texttl.startswith('theme'):
                theme = texttl[6:]
                if theme == 'on':
                    if not line.settings['shareTheme']:
                        line.settings['shareTheme'] = True
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Theme LINE\nStatus: ✓", "Type: Theme LINE", True)
                elif theme == 'off':
                    if line.settings['shareTheme']:
                        line.settings['shareTheme'] = False
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Theme LINE\nStatus: ✘", "Type: Theme LINE", False)
            elif texttl.startswith('cocofun'):
                theme = texttl[8:]
                if theme == 'on':
                    if not line.settings['shareCocofun']:
                        line.settings['shareCocofun'] = True
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Cocofun\nStatus: ✓", "Type: Cocofun", True)
                elif theme == 'off':
                    if line.settings['shareCocofun']:
                        line.settings['shareCocofun'] = False
                    sendToggle(to, "DETECT URL", "Auto Detect Url\nType: Cocofun\nStatus: ✘", "Type: Cocofun", False)

        elif cmd.startswith('text'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl.startswith('add '):
                texts = textt[4:]
                if texts.lower() in line.textsx: 
                    line.sendMode(msg, to, sender, cmd, '"{}" already inside list' .format(texts))
                else:
                    line.setts["textss"]['name'] = texts.lower()
                    line.sendMode(msg, to, sender, cmd, '{}Send text to respond \'{}\' \n\nExample: Hey or Hey @! (@! to respond with tag)'.format(setKey.title(), texts))
                    time.sleep(1)
                    if line.settings["templateMode"]:
                        if line.settings["tempMode"] != "footer":
                            line.setts["textss"]['status'] = True
            elif texttl.startswith('del '):
                texts = textt[4:]
                texts = texts.lower()
                if texts not in line.textsx:
                    line.sendMode(msg, to, sender, cmd, '"{}" not on the list' .format(texts))
                else:
                    del line.textsx[texts]
                    line.sendMode(msg, to, sender, cmd, 'Successfully deleted text "%s"' % texts)
            elif texttl.startswith('deln '):
                texts = textt[5:]
                textts = filter_target(texts, make_list(line.textsx))
                if textts:
                    for tex in textts:
                        del line.textsx[tex]
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted {} text".format(len(textts)))
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl == 'clear':
                if line.textsx:
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted all text\nTotal: {}".format(len(textsx)))
                    textsx.clear()
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl == 'list':
                res = "› T E X T  L I S T\n"
                no  = 0
                if line.textsx:
                    for stc in line.textsx:
                        no += 1
                        res += "\n{}. {}".format(no, stc.title())
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
        
        elif cmd.startswith("send text to respond"):
            if line.settings["templateMode"]:
                if line.settings["tempMode"] == "footer":
                    line.setts["textss"]['status'] = True
            else:
                line.setts["textss"]['status'] = True
            
        elif cmd.startswith('video'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    profile = line.getContact(mention['M'])
                    if profile.videoProfile is not None:
                        line.sendVideoWithURL(to, 'https://obs.line-scdn.net/' + profile.pictureStatus + '/vp')
                    else:
                        line.sendFooter(to, "User not using the video profile")
            if texttl.startswith('add '):
                texts = textt[4:]
                if texts.lower() in line.vidsx: 
                    line.sendMode(msg, to, sender, cmd, '"{}" already inside list' .format(texts))
                else:
                    line.setts["vidss"]['status'] = True
                    line.setts["vidss"]['name'] = texts.lower()
                    line.sendMode(msg, to, sender, cmd, 'Send the video..')
            elif texttl.startswith('del '):
                texts = textt[4:]
                texts = texts.lower()
                if texts not in line.vidsx:
                    line.sendMode(msg, to, sender, cmd, '"{}" not insidelist' .format(texts))
                else:
                    line.deleteFile(line.vidsx[texts])
                    del line.vidsx[texts]
                    line.sendMode(msg, to, sender, cmd, 'Successfully deleted video "%s"' % texts)
            elif texttl.startswith('deln '):
                texts = textt[5:]
                textts = filter_target(texts, make_list(line.vidsx))
                if textts:
                    for tex in textts:
                        line.deleteFile(line.vidsx[tex])
                        del line.vidsx[tex]
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted {} video".format(len(textts)))
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl == 'clear':
                if line.vidsx:
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted all video\nTotal: {}".format(len(vidsx)))
                    for texts in line.vidsx:
                        line.deleteFile(line.vidsx[texts])
                    vidsx.clear()
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl == 'list':
                res = "› V I D E O  L I S T\n"
                no  = 0
                if line.vidsx:
                    for stc in line.vidsx:
                        no += 1
                        res += "\n{}. {}".format(no, stc.title())
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
                    
        elif cmd.startswith('audio'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl.startswith('add '):
                texts = textt[4:]
                if texts.lower() in line.audsx: 
                    line.sendMode(msg, to, sender, cmd, '"{}" already inside list' .format(texts))
                else:
                    line.setts["audss"]['status'] = True
                    line.setts["audss"]['name'] = texts.lower()
                    line.sendMode(msg, to, sender, cmd, 'Send the audio..')
            elif texttl.startswith('del '):
                texts = textt[4:]
                texts = texts.lower()
                if texts not in line.audsx:
                    line.sendMode(msg, to, sender, cmd, '"{}" not inside list' .format(texts))
                else:
                    line.deleteFile(line.audsx[texts])
                    del line.audsx[texts]
                    line.sendMode(msg, to, sender, cmd, 'Successfully deleted audio "%s"' % texts)
            elif texttl.startswith('deln '):
                texts = textt[5:]
                textts = filter_target(texts, make_list(line.audsx))
                if textts:
                    for tex in textts:
                        line.deleteFile(line.audsx[tex])
                        del line.audsx[tex]
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted {} audio".format(len(textts)))
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl == 'clear':
                if line.audsx:
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted all audio\nTotal: {}".format(len(audsx)))
                    for texts in line.audsx:
                        line.deleteFile(line.audsx[texts])
                    audsx.clear()
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl == 'list':
                res = "› A U D I O  L I S T\n"
                no  = 0
                if line.audsx:
                    for stc in line.audsx:
                        no += 1
                        res += "\n{}. {}".format(no, stc.title())
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
                    
        elif cmd.startswith('picture'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl.startswith('add '):
                texts = textt[4:]
                if texts.lower() in line.pictures: 
                    line.sendMode(msg, to, sender, cmd, '"{}" already inside list' .format(texts))
                else:
                    line.setts["pictss"]['status'] = True
                    line.setts["pictss"]['name'] = texts.lower()
                    line.sendMode(msg, to, sender, cmd, 'Send the photo..')
            elif texttl.startswith('del '):
                texts = textt[4:]
                texts = texts.lower()
                if texts not in line.pictures:
                    line.sendMode(msg, to, sender, cmd, '"{}" not inside list' .format(texts))
                else:
                    line.deleteFile(line.pictures[texts])
                    del line.pictures[texts]
                    line.sendMode(msg, to, sender, cmd, 'Successfully deleted photo "%s"' % texts)
            elif texttl.startswith('deln '):
                texts = textt[5:]
                textts = filter_target(texts, make_list(line.pictures))
                if textts:
                    for tex in textts:
                        line.deleteFile(line.pictures[tex])
                        del line.pictures[tex]
                    line.sendMode(msg, to, sender, cmd, "Successfully delete {} image".format(len(textts)))
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl == 'clear':
                if line.pictures:
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted the whole image\nTotal: {}".format(len(pictures)))
                    for texts in line.pictures:
                        line.deleteFile(line.pictures[texts])
                    pictures.clear()
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl == 'list':
                res = "› P I C T U R E  L I S T\n"
                no  = 0
                if line.pictures:
                    for stc in line.pictures:
                        no += 1
                        res += "\n{}. {}".format(no, stc.title())
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
                
        elif cmd.startswith('sticker'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl.startswith('add '):
                if sender == line.profile.mid:
                    texts = textt[4:]
                    if texts.lower() in line.stickers: 
                        line.sendMode(msg, to, sender, cmd, '"{}" already inside list' .format(texts))
                    else:
                        line.setts["stickerss"]['status'] = True
                        line.setts["stickerss"]['name'] = texts.lower()
                        line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            elif texttl.startswith('del '):
                texts = textt[4:]
                texts = texts.lower()
                if texts not in line.stickers:
                    line.sendMode(msg, to, sender, cmd, '"{}" not inside list' .format(texts))
                else:
                    del line.stickers[texts]
                    line.sendMode(msg, to, sender, cmd, 'Successfully deleted sticker "%s"' % texts)
            elif texttl.startswith('save '):
                texts = textt[5:]
                data = line.getReplyMessage(to, msg.relatedMessageId)
                if data is not None:
                    stickerId = data.contentMetadata['STKID']
                    stickerPid = data.contentMetadata['STKPKGID']
                    stickerVer = data.contentMetadata['STKVER']
                    if 'STKOPT' not in data.contentMetadata:
                        line.stickers[texts] = {'STKID': stickerId, 'STKPKGID': stickerPid, 'STKVER': stickerVer}
                    else:
                        stickerOpt = data.contentMetadata['STKOPT']
                        line.stickers[texts] = {'STKID': stickerId, 'STKPKGID': stickerPid, 'STKVER': stickerVer, 'STKOPT': stickerOpt}
                    line.sendMode(msg, to, sender, cmd, 'Save successfully sticker\ntext: "{}"' .format(texts))
                else:
                    line.sendMode(msg, to, sender, cmd, 'You have to reply to the sticker !')
            elif texttl.startswith('deln '):
                texts = textt[5:]
                textts = filter_target(texts, make_list(line.stickers))
                if textts:
                    for tex in textts:
                        del line.stickers[tex]
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted {} sticker".format(len(textts)))
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl == 'clear':
                if line.stickers:
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted all sticker\nTotal: {}".format(len(stickers)))
                    stickers.clear()
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl == 'list':
                res = "› S T I C K E R  L I S T\n"
                no  = 0
                if line.stickers:
                    for stc in line.stickers:
                        no += 1
                        res += "\n{}. {}".format(no, stc.title())
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif texttl.startswith('template '):
                texts = textt[9:]
                if texts.lower() == 'on':
                    if line.settings['stickertemplate']:
                        line.sendMode(msg, to, sender, cmd, "Big Sticker Mode\nStatus: ✓")
                    else:
                        line.settings['stickertemplate'] = True
                        line.sendMode(msg, to, sender, cmd, "Big Sticker Mode\nStatus: ✓")
                elif texts.lower() == 'off':
                    if not line.settings['stickertemplate']:
                        line.sendMode(msg, to, sender, cmd, "Big Sticker Mode\nStatus: ✘")
                    else:
                        line.settings['stickertemplate'] = False
                        line.sendMode(msg, to, sender, cmd, "Big Sticker Mode\nStatus: ✘")
        
        elif cmd.startswith('team '):
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            tuxt = textt.lower()
            if tuxt == 'list':
                res = "› T E A M  L I S T\n"
                no  = 0
                if line.protect['contact_list']:
                    for stc in line.protect['contact_list']:
                        no += 1
                        res += "\n{}. {} // ({})".format(no, stc.title(), len(line.protect['contact_list'][stc]))
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif tuxt == 'clear':
                if line.protect['contact_list']:
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted the entire multi\nTotal: {}".format(len(line.protect['contact_list'])))
                    line.protect['multi_list'].clear()
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif tuxt.startswith('add '):
                texttl = tuxt[4:]
                textts = texttl.split(" ")
                target = []
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if int(mention['S']) == len(setKey)+9: return line.sendMessage(to, 'failed to add team, keyword not found')
                        if mention['M'] not in target:
                            target.append(mention['M'])
                elif msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        target.append(data._from)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                elif len(textts) >= 2:
                    if textts[1] == 'contact':
                        line.setts['inviteAlot']['status'] = True
                        line.setts['inviteAlot']['name'] = textts[0]
                        res = "Keyword: {keyword}\nSend the contact...\ntype `{key}Abort` to cancel this".format(keyword=textts[0], key=setKey.title())
                        sendToggle(to, "ADD TEAM CONTACT", res, res, True)
                if target:
                    if textts[0] == "" or textts[0] == " ": return line.sendMessage(to, 'failed to add team, keyword not found')
                    friend = line.getAllContactIds()
                    if textts[0] not in line.protect['contact_list']:
                        line.protect['contact_list'][textts[0]] = []
                    if line.profile.mid in target: target.remove(line.profile.mid)
                    parsed_len = len(target)//20+1
                    no = 0
                    res = "╭「 Add Team 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in target[point*20:(point+1)*20]:
                            no += 1
                            if mid == target[-1]:
                                if mid not in line.protect['contact_list'][textts[0]]:
                                    res += '╰ %i. @! > Added\n' % (no)
                                    line.protect['contact_list'][textts[0]].append(mid)
                                else:
                                    res += '╰ %i. @! > Already\n' % (no)
                                res += '\nKeyword: %s\nTotal Team: %i' % (textts[0], len(line.protect['contact_list'][textts[0]]))
                            else:
                                if mid not in line.protect['contact_list'][textts[0]]:
                                    res += '├ %i. @! > Added\n' % (no)
                                    line.protect['contact_list'][textts[0]].append(mid)
                                else:
                                    res += '├ %i. @! > Already\n' % (no)
                            mids.append(mid)
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
            elif tuxt.startswith('del '):
                texttl = tuxt[4:]
                if texttl in line.protect['contact_list']:
                    del line.protect['contact_list'][texttl]
                    line.sendMode(msg, to, sender, cmd, 'Successfully deleted team "%s"' % texttl)
                else:
                    line.sendMode(msg, to, sender, cmd, '"{}" not inside list' .format(texttl))
            elif tuxt.startswith('deln '):
                texttl = tuxt[5:]
                textts = filter_target(texttl, make_list(line.protect['contact_list']))
                if textts:
                    for tex in textts:
                        del line.protect['contact_list'][tex]
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted {} team".format(len(textts)))
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")

        elif cmd.startswith('multi '):
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            tuxt = textt.lower()
            if tuxt.startswith('del '):
                texts = textt[4:]
                texts = texts.lower()
                if texts not in line.protect["multi_list"]:
                    line.sendMode(msg, to, sender, cmd, '"{}" not inside list' .format(texts))
                else:
                    for mul in line.protect["multi_list"][texts]:
                        if mul['type'] in ['image', 'video', 'audio']: line.deleteFile(mul['path'])
                    del line.protect["multi_list"][texts]
                    line.sendMode(msg, to, sender, cmd, 'Successfully delete multi "%s"' % texts)
            elif tuxt.startswith('deln '):
                texts = textt[5:]
                textts = filter_target(texts, make_list(line.protect['multi_list']))
                if textts:
                    for tex in textts:
                        for mul in line.protect["multi_list"][tex]:
                            if mul['type'] in ['image', 'video', 'audio']: line.deleteFile(mul['path'])
                        del line.protect["multi_list"][tex]
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted {} multi".format(len(textts)))
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif tuxt == 'tutor':
                pes = """Tutorial Multi List

1. arrange the message you want to save like the picture above

2. then count the total messages that you compose

3. take example 6, then type `multi add 6 KEYWORD`

FYI: Hanya Text, Image, Video, Saveable Audio and Contacts"""
                line.sendImageWithURL(to, 'https://i.ibb.co/5LSt3n3/fe2e6eefff2b.jpg')
                line.sendReplyMessage(to, pes)
            elif tuxt == 'clear':
                if line.protect['multi_list']:
                    line.sendMode(msg, to, sender, cmd, "Successfully deleted the entire multi\nTotal: {}".format(len(line.protect['multi_list'])))
                    for texts in line.protect['multi_list']:
                        for mul in line.protect['multi_list'][texts]:
                            if mul['type'] in ['image', 'video', 'audio']: line.deleteFile(mul['path'])
                    line.protect['multi_list'].clear()
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif tuxt == 'list':
                res = "› M U L T I  L I S T\n"
                no  = 0
                if line.protect['multi_list']:
                    for stc in line.protect['multi_list']:
                        no += 1
                        res += "\n{}. {}".format(no, stc.title())
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    line.sendMode(msg, to, sender, cmd, "Nothing")
            elif len(sep) >= 3:
                if sep[1].isdigit():
                    num = int(sep[1])
                    texttl = sep[0].lower()
                    if texttl == 'add':
                        texts = textt.replace(sep[0] + " " + sep[1] + " ","")
                        if texts.lower() in line.protect['multi_list']:
                            line.sendMode(msg, to, sender, cmd, '"{}" already inside list' .format(texts))
                        else:
                            datas = line.getRecentMessagesV2(to, num+1)
                            result = []
                            for data in reversed(datas):
                                if data._from == sender:
                                    if len(result) == num: break
                                    if data.contentType == 0:
                                        result.append({'type': 'text', 'text': data.text})
                                    elif data.contentType == 1:
                                        path = line.downloadObjectMsg(data.id, saveAs="json/{}.bin".format(data.id))
                                        result.append({'type': 'image', 'path': path})
                                    elif data.contentType == 2:
                                        path = line.downloadObjectMsg(data.id, saveAs="json/{}.bin".format(data.id))
                                        result.append({'type': 'video', 'path': path})
                                    elif data.contentType == 3:
                                        path = line.downloadObjectMsg(data.id, saveAs="json/{}.bin".format(data.id))
                                        result.append({'type': 'audio', 'path': path})
                                    elif data.contentType == 13:
                                        result.append({'type': 'contact', 'mid': data.contentMetadata['mid']})
                            if len(result) != num:
                                return line.sendMode(msg, to, sender, cmd, 'Failed to save multi list')
                            line.protect["multi_list"][texts.lower()] = result
                            line.sendMode(msg, to, sender, cmd, f'Save successfully {num} message\nText: {texts}')
                    
        elif cmd.startswith('autoadd'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            cond = texttl.split(" ")
            if cmd == 'autoadd':
                res = 'Status: ' + bool_dict[line.settings['autoAdd']['status']][4]
                res += '\nImage: ' + bool_dict[line.settings['autoAdd']['image']['status']][4]
                if line.settings['autoAdd']['sticker']['STKID'] != "": res += '\nSticker: ✔︎'
                else: res += '\nSticker: ✘'
                res += '\nReply Message: ' + line.settings['autoAdd']['message']
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}AutoAdd'.format(setKey.title())
                res += '\n• {}AutoAdd <on/off>'.format(setKey.title())
                res += '\n• {}AutoAdd <message>'.format(setKey.title())
                res += '\n• {}AutoAdd Image <on/off>'.format(setKey.title())
                res += '\n• {}AutoAdd setImage'.format(setKey.title())
                res += '\n• {}AutoAdd delImage'.format(setKey.title())
                res += '\n• {}AutoAdd setSticker'.format(setKey.title())
                res += '\n• {}AutoAdd delSticker'.format(setKey.title())
                res += "\n\nFYI: If you enable autoadd image and haven't set the image, the image that appears is the user's profile picture"
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['autoAdd']['status']:
                    line.settings['autoAdd']['status'] = True
                sendToggle(to, "AUTO RESPON ADD", "Auto Respon Add\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['autoAdd']['status']:
                    line.settings['autoAdd']['status'] = False
                sendToggle(to, "AUTO RESPON ADD", "Auto Respon Add\nStatus: ✘", "", False)
            elif texttl == 'setsticker':
                if sender == line.profile.mid:
                    if line.setts['autoAddSticker']:
                        line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
                    else:
                        line.setts['autoAddSticker'] = True
                        line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            elif texttl == 'delsticker':
                line.settings['autoAdd']['sticker']['STKID'] = ""
                line.settings['autoAdd']['sticker']['STKPKGID'] = ""
                line.settings['autoAdd']['sticker']['STKVER'] = ""
                line.sendMode(msg, to, sender, cmd, 'Auto Respon Add Sticker successfully deleted')
            elif texttl == 'setimage':
                if line.setts['autoAddImage']:
                    line.sendMode(msg, to, sender, cmd, 'Send the picture..\nType `{key}Abort` to cancel this'.format(key=setKey.title()))
                else:
                    line.setts['autoAddImage'] = True
                    line.sendMode(msg, to, sender, cmd, 'Send the picture..\nType `{key}Abort` to cancel this'.format(key=setKey.title()))
            elif texttl == 'delimage':
                if line.settings['autoAdd']['image']['path'] != "":
                    line.deleteFile(line.settings['autoAdd']['image']['path'])
                line.settings['autoAdd']['image']['path'] = ""
                line.sendMode(msg, to, sender, cmd, 'Auto Respon Add Image successfully deleted')
            elif texttl.startswith('image '):
                textts = texttl[6:]
                if textts == 'on':
                    if not line.settings['autoAdd']['image']['status']:
                        line.settings['autoAdd']['image']['status'] = True
                    sendToggle(to, "AUTO RESPON ADD IMAGE", "Auto Respon Add Image\nStatus: ✓", "", True)
                elif textts == 'off':
                    if line.settings['autoAdd']['image']['status']:
                        line.settings['autoAdd']['image']['status'] = False
                    sendToggle(to, "AUTO RESPON ADD IMAGE", "Auto Respon Add Image\nStatus: ✘", "", False)
            elif 'STICON_OWNERSHIP' in msg.contentMetadata:
                getEmoji = line.metadataFilter(msg.contentMetadata, len(setKey)+8, type='emoji')
                line.settings["autoAdd"]["contentMetadata"] = getEmoji
                line.settings['autoAdd']['message'] = textt
                getEmoji2 = line.metadataFilter(getEmoji, 32, type='emoji2')
                if "@!" in textt:
                    line.settings["autoAdd"]["contentMention"] = line.metadataFilter(getEmoji, text=textt, type='mention')
                    getEmoji2.update(line.metadataFilter(getEmoji, text='Message successfully changed to `{}`'.format(textt), type='mention'))
                line.sendReplyMessage(to, 'Message successfully changed to `{}`'.format(textt), getEmoji2, msgIds=msg_id)
            else:
                line.settings["autoAdd"]["contentMetadata"] = {}
                line.settings["autoAdd"]["contentMention"] = {}
                line.settings['autoAdd']['message'] = textt
                line.sendMode(msg, to, sender, cmd, 'Message successfully changed to \'%s\'' % textt)
        
        elif cmd.startswith('antitag'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            cond = texttl.split(" ")
            if cmd == 'antitag':
                res = 'Status: ' + bool_dict[line.settings['antiTag']['status']][4]
                res += '\nReply Message: ' + line.settings['antiTag']['message']
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}AntiTag'.format(setKey.title())
                res += '\n• {}AntiTag <on/off>'.format(setKey.title())
                res += '\n• {}AntiTag <message>'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['antiTag']['status']:
                    line.settings['antiTag']['status'] = True
                sendToggle(to, "ANTI TAG", "Anti Tag\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['antiTag']['status']:
                    line.settings['antiTag']['status'] = False
                sendToggle(to, "ANTI TAG", "Anti Tag\nStatus: ✘", "", False)
            elif 'STICON_OWNERSHIP' in msg.contentMetadata:
                getEmoji = line.metadataFilter(msg.contentMetadata, len(setKey)+8, type='emoji')
                line.settings["antiTag"]["contentMetadata"] = getEmoji
                line.settings['antiTag']['message'] = textt
                getEmoji2 = line.metadataFilter(getEmoji, 32, type='emoji2')
                if "@!" in textt:
                    line.settings["antiTag"]["contentMention"] = line.metadataFilter(getEmoji, text=textt, type='mention')
                    getEmoji2.update(line.metadataFilter(getEmoji, text='Message successfully changed to `{}`'.format(textt), type='mention'))
                line.sendReplyMessage(to, 'Message successfully changed to `{}`'.format(textt), getEmoji2, msgIds=msg_id)
            else:
                line.settings["antiTag"]["contentMetadata"] = {}
                line.settings["antiTag"]["contentMention"] = {}
                line.settings['antiTag']['message'] = textt
                line.sendMode(msg, to, sender, cmd, 'Message successfully changed to \'%s\'' % textt)
                
        elif cmd.startswith('autojoin'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            cond = textt.split(' ')
            if cmd == 'autojoin':
                res = 'Status: ' + bool_dict[line.settings['autoJoin']['status']][4]
                res += '\nKickpy: ' + bool_dict[line.settings['autoJoin']['kickpy']][4]
                res += '\nKickjs: ' + bool_dict[line.settings['autoJoin']['kickjs']][4]
                res += '\nReply: ' + bool_dict[line.settings['autoJoin']['reply']][0]
                res += '\nReply Message: ' + line.settings['autoJoin']['message']
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}AutoJoin'.format(setKey.title())
                res += '\n• {}AutoJoin <on/off>'.format(setKey.title())
                res += '\n• {}AutoJoin Reply <on/off>'.format(setKey.title())
                res += '\n• {}AutoJoin Kickpy <on/off>'.format(setKey.title())
                res += '\n• {}AutoJoin Kickjs <on/off>'.format(setKey.title())
                res += '\n• {}AutoJoin <message>'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['autoJoin']['status']:
                    line.settings['autoJoin']['status'] = True
                sendToggle(to, "AUTO JOIN GROUP", "Auto Join Group\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['autoJoin']['status']:
                    line.settings['autoJoin']['status'] = False
                sendToggle(to, "AUTO JOIN GROUP", "Auto Join Group\nStatus: ✘", "", False)
            elif texttl.startswith('reply '):
                con = texttl[6:]
                if con == 'on':
                    if not line.settings['autoJoin']['reply']:
                        line.settings['autoJoin']['reply'] = True
                    sendToggle(to, "AUTO JOIN REPLY", "Auto Join Reply\nStatus: ✓", "", True)
                elif con == 'off':
                    if line.settings['autoJoin']['reply']:
                        line.settings['autoJoin']['reply'] = False
                    sendToggle(to, "AUTO JOIN REPLY", "Auto Join Reply\nStatus: ✘", "", False)
            elif texttl.startswith('kickpy '):
                if sender == line.profile.mid:
                    con = texttl[7:]
                    if con == 'on':
                        if not line.settings['autoJoin']['kickpy']:
                            line.settings['autoJoin']['kickpy'] = True
                        sendToggle(to, "AUTO JOIN KICKALL", "Auto Join Kickall\nType: Python\nWarning!! using this command do with your own risk\nStatus: ✓", "Type: Python\nWarning!! using this command do with your own risk", True)
                    elif con == 'off':
                        if line.settings['autoJoin']['kickpy']:
                            line.settings['autoJoin']['kickpy'] = False
                        sendToggle(to, "AUTO JOIN KICKALL", "Auto Join Kickall\nType: Python\nWarning!! using this command do with your own risk\nStatus: ✘", "Type: Python\nWarning!! using this command do with your own risk", False)
            elif texttl.startswith('kickjs '):
                if sender == line.profile.mid:
                    con = texttl[7:]
                    if con == 'on':
                        if not line.settings['autoJoin']['kickjs']:
                            line.settings['autoJoin']['kickjs'] = True
                        sendToggle(to, "AUTO JOIN KICKALL", "Auto Join Kickall\nType: JavaScript\nWarning!! using this command do with your own risk\nStatus: ✓", "Type: JavaScript\nWarning!! using this command do with your own risk", True)
                    elif con == 'off':
                        if line.settings['autoJoin']['kickjs']:
                            line.settings['autoJoin']['kickjs'] = False
                        sendToggle(to, "AUTO JOIN KICKALL", "Auto Join Kickall\nType: JavaScript\nWarning!! using this command do with your own risk\nStatus: ✘", "Type: JavaScript\nWarning!! using this command do with your own risk", False)
            elif 'STICON_OWNERSHIP' in msg.contentMetadata:
                getEmoji = line.metadataFilter(msg.contentMetadata, len(setKey)+9, type='emoji')
                line.settings["autoJoin"]["contentMetadata"] = getEmoji
                line.settings['autoJoin']['message'] = textt
                getEmoji2 = line.metadataFilter(getEmoji, 32, type='emoji2')
                if "@!" in textt:
                    line.settings["autoJoin"]["contentMention"] = line.metadataFilter(getEmoji, text=textt, type='mention')
                    getEmoji2.update(line.metadataFilter(getEmoji, text='Message successfully changed to `{}`'.format(textt), type='mention'))
                line.sendReplyMessage(to, 'Message successfully changed to `{}`'.format(textt), getEmoji2, msgIds=msg_id)
            else:
                line.settings["autoJoin"]["contentMetadata"] = {}
                line.settings["autoJoin"]["contentMention"] = {}
                line.settings['autoJoin']['message'] = textt
                line.sendMode(msg, to, sender, cmd, 'Message successfully changed to \'%s\'' % textt)
                
        elif cmd.startswith('autoleave'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            cond = textt.split(' ')
            if cmd == 'autoleave':
                res = 'Status: ' + bool_dict[line.settings['autoLeave']['status']][4]
                res += '\nReply: ' + bool_dict[line.settings['autoLeave']['reply']][0]
                res += '\nReply Message: ' + line.settings['autoLeave']['message']
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}AutoLeave'.format(setKey.title())
                res += '\n• {}AutoLeave <on/off>'.format(setKey.title())
                res += '\n• {}AutoLeave Reply <on/off>'.format(setKey.title())
                res += '\n• {}AutoLeave <message>'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['autoLeave']['status']:
                    line.settings['autoLeave']['status'] = True
                sendToggle(to, "AUTO LEAVE MC", "Auto Leave Mc\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['autoLeave']['status']:
                    line.settings['autoLeave']['status'] = False
                sendToggle(to, "AUTO LEAVE MC", "Auto Leave Mc\nStatus: ✘", "", False)
            elif texttl.startswith('reply '):
                con = texttl[6:]
                if con == 'on':
                    if not line.settings['autoLeave']['reply']:
                        line.settings['autoLeave']['reply'] = True
                    sendToggle(to, "AUTO LEAVE REPLY", "Auto Leave Reply\nStatus: ✓", "", True)
                elif con == 'off':
                    if line.settings['autoLeave']['reply']:
                        line.settings['autoLeave']['reply'] = False
                    sendToggle(to, "AUTO LEAVE REPLY", "Auto Leave Reply\nStatus: ✘", "", False)
            elif 'STICON_OWNERSHIP' in msg.contentMetadata:
                getEmoji = line.metadataFilter(msg.contentMetadata, len(setKey)+10, type='emoji')
                line.settings["autoLeave"]["contentMetadata"] = getEmoji
                line.settings['autoLeave']['message'] = textt
                getEmoji2 = line.metadataFilter(getEmoji, 32, type='emoji2')
                if "@!" in textt:
                    line.settings["autoLeave"]["contentMention"] = line.metadataFilter(getEmoji, text=textt, type='mention')
                    getEmoji2.update(line.metadataFilter(getEmoji, text='Message successfully changed to `{}`'.format(textt), type='mention'))
                line.sendReplyMessage(to, 'Message successfully changed to `{}`'.format(textt), getEmoji2, msgIds=msg_id)
            else:
                line.settings["autoLeave"]["contentMetadata"] = {}
                line.settings["autoLeave"]["contentMention"] = {}
                line.settings['autoLeave']['message'] = textt
                line.sendMode(msg, to, sender, cmd, 'Message successfully changed to \'%s\'' % textt)
                
        elif cmd.startswith('autorespondtag'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == 'autorespondtag':
                res = 'Status: ' + bool_dict[line.settings['autoRespondMention']['status']][4]
                if line.settings['autoRespondMention']['sticker']['STKID'] is not None: res += '\nSticker: Active'
                else: res += '\nSticker: Deactive'
                res += '\nReply Message: ' + line.settings['autoRespondMention']['message']
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}AutoRespondTag'.format(setKey.title())
                res += '\n• {}AutoRespondTag <on/off>'.format(setKey.title())
                res += '\n• {}AutoRespondTag <message>'.format(setKey.title())
                res += '\n• {}AutoRespondTag setSticker'.format(setKey.title())
                res += '\n• {}AutoRespondTag delSticker'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['autoRespondMention']['status']:
                    line.settings['autoRespondMention']['status'] = True
                sendToggle(to, "AUTO RESPON TAG", "Auto Respon Tag\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['autoRespondMention']['status']:
                    line.settings['autoRespondMention']['status'] = False
                sendToggle(to, "AUTO RESPON TAG", "Auto Respon Tag\nStatus: ✘", "", False)
            elif texttl == 'setsticker':
                if sender == line.profile.mid:
                    if line.setts['tagSticker']:
                        line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
                    else:
                        line.setts['tagSticker'] = True
                        line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            elif texttl == 'delsticker':
                line.settings['autoRespondMention']['sticker']['STKID'] = None
                line.settings['autoRespondMention']['sticker']['STKPKGID'] = None
                line.settings['autoRespondMention']['sticker']['STKVER'] = None
                line.sendMode(msg, to, sender, cmd, 'Auto Respon Tag Sticker successfully deleted')
            elif 'STICON_OWNERSHIP' in msg.contentMetadata:
                getEmoji = line.metadataFilter(msg.contentMetadata, len(setKey)+15, type='emoji')
                line.settings["autoRespondMention"]["contentMetadata"] = getEmoji
                line.settings['autoRespondMention']['message'] = textt
                getEmoji2 = line.metadataFilter(getEmoji, 32, type='emoji2')
                if "@!" in textt:
                    line.settings["autoRespondMention"]["contentMention"] = line.metadataFilter(getEmoji, text=textt, type='mention')
                    getEmoji2.update(line.metadataFilter(getEmoji, text='Message successfully changed to `{}`'.format(textt), type='mention'))
                line.sendReplyMessage(to, 'Message successfully changed to `{}`'.format(textt), getEmoji2, msgIds=msg_id)
            else:
                line.settings["autoRespondMention"]["contentMetadata"] = {}
                line.settings["autoRespondMention"]["contentMention"] = {}
                line.settings['autoRespondMention']['message'] = textt
                line.sendMode(msg, to, sender, cmd, 'Message successfully changed to \'%s\'' % textt)
                
        elif cmd.startswith('sleepmode'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == 'sleepmode':
                res = 'Status: ' + bool_dict[line.settings['autoRespond']['status']][4]
                res += '\nReply Message: ' + line.settings['autoRespond']['message']
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}Sleepmode'.format(setKey.title())
                res += '\n• {}Sleepmode <on/off>'.format(setKey.title())
                res += '\n• {}Sleepmode <message>'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['autoRespond']['status']:
                    line.settings['autoRespond']['status'] = True
                sendToggle(to, "SLEED MODE", "Sleep Mode\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['autoRespond']['status']:
                    line.setts["sleepMode_user"] = []
                    line.settings['autoRespond']['status'] = False
                sendToggle(to, "SLEED MODE", "Sleep Mode\nStatus: ✘", "", False)
            else:
                line.settings['autoRespond']['message'] = textt
                line.sendMode(msg, to, sender, cmd, 'The response message was successfully changed to \'%s\'' % textt)
                
        elif cmd.startswith('autoread'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == 'autoread':
                res = 'Auto Read 1: ' + bool_dict[line.settings['autoRead']][4]
                res += '\nAuto Read 2: ' + bool_dict[line.settings['autoReadG']][4]
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}AutoRead'.format(setKey.title())
                res += '\n• {}AutoRead 1 <on/off>'.format(setKey.title())
                res += '\n• {}AutoRead 2 <on/off>'.format(setKey.title())
                res += '\n\n1 : Personal Chat'
                res += '\n2 : Group Chat'
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl.startswith('1 '):
                tux = texttl[2:]
                if tux == 'on':
                    if not line.settings['autoRead']:
                        line.settings['autoRead'] = True
                    sendToggle(to, "AUTO READ", "Auto Read\nType: Personal Chat\nStatus: ✓", "Type: Personal Chat", True)
                elif tux == 'off':
                    if line.settings['autoRead']:
                        line.settings['autoRead'] = False
                    sendToggle(to, "AUTO READ", "Auto Read\nType: Personal Chat\nStatus: ✘", "Type: Personal Chat", False)
            elif texttl.startswith('2 '):
                tux = texttl[2:]
                if tux == 'on':
                    if not line.settings['autoReadG']:
                        line.settings['autoReadG'] = True
                    sendToggle(to, "AUTO READ", "Auto Read\nType: Group Chat\nStatus: ✓", "Type: Group Chat", True)
                elif tux == 'off':
                    if line.settings['autoReadG']:
                        line.settings['autoReadG'] = False
                    sendToggle(to, "AUTO READ", "Auto Read\nType: Group Chat\nStatus: ✘", "Type: Group Chat", False)
                        
        elif cmd.startswith('checkcontact '):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl == 'on':
                if not line.settings['checkContact']:
                    line.settings['checkContact'] = True
                sendToggle(to, "CHECK CONTACT", "Check Contact\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['checkContact']:
                    line.settings['checkContact'] = False
                sendToggle(to, "CHECK CONTACT", "Check Contact\nStatus: ✘", "", False)
                    
        elif cmd.startswith('checkpost '):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl == 'on':
                if not line.settings['checkPost']:
                    line.settings['checkPost'] = True
                sendToggle(to, "CHECK POST", "Check Post\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['checkPost']:
                    line.settings['checkPost'] = False
                sendToggle(to, "CHECK POST", "Check Post\nStatus: ✘", "", False)
                    
        elif cmd.startswith('checksticker '):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl == 'on':
                if not line.settings['checkSticker']:
                    line.settings['checkSticker'] = True
                sendToggle(to, "CHECK STICKER", "Check Sticker\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['checkSticker']:
                    line.settings['checkSticker'] = False
                sendToggle(to, "CHECK STICKER", "Check Sticker\nStatus: ✘", "", False)
                    
        elif cmd == 'detectunsend on':
            if to not in line.settings['detectUnsend']:
                line.settings['detectUnsend'].append(to)
            sendToggle(to, "DETECT UNSEND CHAT", "Detect Unsend Chat\nStatus: ✓", "", True)
        elif cmd == 'detectunsend off':
            if to in line.settings['detectUnsend']:
                line.settings['detectUnsend'].remove(to)
            sendToggle(to, "DETECT UNSEND CHAT", "Detect Unsend Chat\nStatus: ✘", "", False)
                
        elif cmd.startswith("chat "):
            sup = removeCmd(text, setKey)
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    name = line.getContact(mid).displayName
                    texts = sup.replace("@"+name+" ","")
                    line.sendMessage(mid, texts)
                line.sendMode(msg, to, sender, cmd, 'Message sent successfully to personal chat')
            elif sup.split(" ")[0].lower() == "contact":
                texts = sup.replace(sup.split(" ")[0] + " ","")
                line.setts["chatCon"]["status"] = True
                line.setts["chatCon"]["message"] = texts
                res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                sendToggle(to, "CHAT CONTACT", res, res, True)
        
        elif cmd.startswith('chatid '):
            query = removeCmd(text, setKey)
            sep = query.split(" ")
            if len(sep) >= 2:
                try:
                    profile = line.findContactsByUserid(sep[0])
                    textt = query.replace(sep[0] + " ","")
                    line.sendMessage(profile.mid, textt)
                    line.sendMode(msg, to, sender, cmd, 'Message sent successfully to personal chat')
                except TalkException as e:
                    if e.code == 5:
                        line.sendMode(msg, to, sender, cmd, "No account using ID '%s'" % (query))

        elif cmd == 'invitecontact':
            line.setts["invCon"] = True
            res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
            sendToggle(to, "INVITE CONTACT", res, res, True)
            
        elif cmd.startswith("setleave "):
            set = removeCmd(text, setKey)
            line.settings["setcommand"]["leave"] = set
            line.sendMode(msg, to, sender, cmd, 'Command leave successfully changed to "{}"'.format(set))
            
        elif cmd == line.settings["setcommand"]["leave"].lower():
            if msg.toType == 1:
                line.leaveRoom(to)
            elif msg.toType == 2:
                line.deleteSelfFromChat(to)
        
        elif cmd == "myliff":
            line.sendFooter(to, "Sozi LIFF:\n• https://line.me/R/app/1657710460-y83a8lNE (v1.0)\n• https://line.me/R/app/1657707255-WVxqmM35 (v2.11.1)\n\nLIFF ACTIVE: https://line.me/R/app/{}".format(line.settings["arLiff"]), reply=True)
            
        elif cmd == 'myprofile':
            isi = ["MyProfile", "My ID", "My Mid", "My Ticket", "My Name", "My Bio", "My Pict", "My Video", "My Cover", "My Story", "My Sticker", "My Emoji", "My Theme", "Changename <text>", "Changebio <text>", "Changepict", "Changecover", "Changecovervideo", "Changevideo", "Changevideoyt <urlyoutube>"]
            isi2 = ["xChangePict", "xChangeVideo", "xChangeCover", "xChangeCoverVideo"]
            res = looping_command(setKey.title(), "› C O M M A N D", isi)
            res += "\n\n"
            res += looping_command(setKey.title(), "› W I T H  R E P L Y<", isi2)
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd == "my ticket":
            line.sendFooter(to, "https://line.me/ti/p/{}".format(line.generateUserTicket()), reply=True)
            
        elif cmd == 'my mid' or cmd == 'mid':
            profile = line.getProfile()
            line.sendFooter(to, '' + str(profile.mid), reply=True)
        
        elif cmd == 'my id':
            res = 'ID: {}'.format(line.getProfile().userid)
            res += '\nhttps://line.me/R/ti/p/~{}'.format(line.getProfile().userid)
            line.sendFooter(to, res, reply=True)
        
        elif cmd == 'my sticker':
            datas = line.getOwnedProducts(sid='sticker').productList
            parsed_len = len(datas)//50+1
            res = ""
            no = 0
            for point in range(parsed_len):
                for data in datas[point*50:(point+1)*50]:
                    no += 1
                    res += "{}. {}\nhttps://line.me/S/sticker/{}/?lang=en&ref=gnsh_stickerDetail\n\n".format(no, data.name, data.id)
                if res:
                    if res.endswith('\n\n'): res = res[:-2]
                    if point == 0:
                        line.sendReplyMessage(to, res, msgIds=msg_id)
                    else:
                        line.sendMessage(to, res)
                res = ""
        
        elif cmd == 'my emoji':
            datas = line.getOwnedProducts(sid='emoji').productList
            parsed_len = len(datas)//50+1
            res = ""
            no = 0
            for point in range(parsed_len):
                for data in datas[point*50:(point+1)*50]:
                    no += 1
                    res += "{}. {}\nhttps://line.me/S/emoji/?id={}&lang=en&ref=gnsh_sticonDetail\n\n".format(no, data.name, data.id)
                if res:
                    if res.endswith('\n\n'): res = res[:-2]
                    if point == 0:
                        line.sendReplyMessage(to, res, msgIds=msg_id)
                    else:
                        line.sendMessage(to, res)
                res = ""
        
        elif cmd == 'my theme':
            datas = line.getOwnedProducts(sid='theme').productList
            parsed_len = len(datas)//50+1
            res = ""
            no = 0
            for point in range(parsed_len):
                for data in datas[point*50:(point+1)*50]:
                    no += 1
                    res += "{}. {}\nhttps://line.me/S/shop/theme/detail?id={}&lang=en&ref=gnsh_themeDetail\n\n".format(no, data.name, data.id)
                if res:
                    if res.endswith('\n\n'): res = res[:-2]
                    if point == 0:
                        line.sendReplyMessage(to, res, msgIds=msg_id)
                    else:
                        line.sendMessage(to, res)
                res = ""
                
        elif cmd == 'my name':
            profile = line.getProfile()
            line.sendFooter(to, '' + str(profile.displayName), reply=True)
            
        elif cmd == 'my bio':
            profile = line.getProfile()
            if profile.statusMessage != '':
                line.sendFooter(to, '' + str(profile.statusMessage), reply=True)
            else:
                line.sendFooter(to, 'Bio is None', reply=True)
            
        elif cmd == 'my pict':
            profile = line.getProfile()
            if profile.pictureStatus:
                path = 'https://obs.line-scdn.net/' + profile.pictureStatus
                line.sendLiffImage(to, path, line.settings["setFlag"]["icon"], " Profile Picture")
              #  line.sendMessage(to, path)
            else:
                line.sendFooter(to, 'You are not using profile picture')
                
        elif cmd == 'my video':
            profile = line.getProfile()
            if profile.videoProfile is not None:
                path = 'https://obs.line-scdn.net/' + profile.pictureStatus + '/vp'
                line.sendVideoWithURL(to, path)
            #    line.sendMessage(to, path)
            else:
                line.sendFooter(to, 'You are not using video profile')
                
        elif cmd == 'my cover':
            profile = line.getProfile()
            cover = line.getProfileCoverURL(profile.mid)
            if "/vc/" in cover:
                line.sendVideoWithURL(to, cover)
            else:
                line.sendLiffImage(to, str(cover), line.settings["setFlag"]["icon"], " Profile Cover")
          #  line.sendMessage(to, str(cover))
        
        elif cmd == 'my story':
            data = line.getStoryMedia(sender)
            if data:
                line.sendMessage(to, 'Downloading {} stories..'.format(len(data)))
                dataImages = []
                dataVideos = []
                for media in data:
                    if media["type"] == "image":
                        dataImages.append(media["url"])
                    elif media["type"] == "video":
                        line.sendVideoWithURL(to, media["url"])
                if dataImages:
                    if len(dataImages) >= 2:
                        line.sendMultiImageWithURL(to, dataImages)
                    else:
                        line.sendImageWithURL(to, dataImages[0])
            else:
                line.sendFooter(to, 'You didnt upload any story')
            time.sleep(0.8)
            
        elif cmd.startswith('changename '):
            profile = line.getProfile()
            name = removeCmd(text, setKey)
            if len(name) <= 999:
                profile.displayName = name
                line.updateProfile(profile)
                line.sendMode(msg, to, sender, cmd, 'Successfully renamed to \'%s\'' % name)
            else:
                line.sendFooter(to, 'Failed to change the name, the text is too long')
                
        elif cmd.startswith('changebio '):
            profile = line.getProfile()
            bio = removeCmd(text, setKey)
            if len(bio) <= 999:
                profile.statusMessage = bio
                line.updateProfile(profile)
                line.sendMode(msg, to, sender, cmd, 'Successfully changed bio to \'%s\'' % bio)
            else:
                line.sendFooter(to, 'Failed to change bio, text is too long')
                
        elif cmd == 'changepict' or cmd == 'xchangepict':
            if cmd == 'changepict':
                line.settings['changePictureProfile'] = True
                res = 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                sendToggle(to, "CHANGE PICTURE PROFILE", res, res, True)
            elif cmd == 'xchangepict':
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        if data.contentType != 1:
                            return line.sendMode(msg, to, sender, cmd, 'You must reply the image')
                        path = line.downloadObjectMsg(data.id, saveAs='tmp/picture.jpg')
                        line.updateProfilePicture(path)
                        line.sendMode(msg, to, sender, "image", 'Update Profile Picture\nStatus: ✓')
                        line.settings['changePictureProfile'] = False
                        line.deleteFile(path)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the image')
                    
        elif cmd == 'changevideo' or cmd == 'xchangevideo':
            if cmd == 'changevideo':
                line.settings['changevp'] = True
                res = 'Send the video...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                sendToggle(to, "CHANGE VIDEO PROFILE", res, res, True)
            elif cmd == 'xchangevideo':
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        if data.contentType != 2:
                            return line.sendMode(msg, to, sender, cmd, 'You must reply the video')
                        contact = line.getProfile()
                        pict = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                        path = line.downloadFileURL(pict)
                        path1 = line.downloadObjectMsg(data.id)
                        line.settings["changevp"] = False
                        line.updateVideoAndPictureProfile(path, path1)
                        line.sendMode(msg, to, sender, "video", 'Update Video Profile\nStatus: ✓')
                        line.deleteFile(path)
                        line.deleteFile(path1)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the video')

        elif cmd == 'changecover' or cmd == 'xchangecover':
            if cmd == 'changecover':
                line.settings['changeCoverProfile'] = True
                res = 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                sendToggle(to, "CHANGE COVER IMAGE", res, res, True)
            elif cmd == 'xchangecover':
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        if data.contentType != 1:
                            return line.sendMode(msg, to, sender, cmd, 'You must reply the image')
                        path = line.downloadObjectMsg(data.id, saveAs='tmp/cover.jpg')
                        line.updateProfileCover(path)
                        line.sendMode(msg, to, sender, "image", 'Update Profile Cover\nStatus: ✓')
                        line.settings['changeCoverProfile'] = False
                        line.deleteFile(path)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the image')

        elif cmd == 'changecovervideo' or cmd == 'xchangecovervideo':
            if cmd == 'changecovervideo':
                line.settings['changeCoverVideo']["image"] = True
                res = 'Send the picture for cover preview\ntype `{key}Abort` to cancel this\n\nsend pictures and videos with share/forward'.format(key=setKey.title())
                sendToggle(to, "CHANGE COVER VIDEO", res, res, True)
            elif cmd == 'xchangecovervideo':
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        if data.contentType != 2:
                            return line.sendMode(msg, to, sender, cmd, 'You must reply the video')
                        cover = line.getProfileCoverURL(line.profile.mid)
                        if '/vc/' in cover:
                            cover = cover.replace('/vc/', '/c/')
                        path = line.downloadFileURL(cover)
                        path1 = line.downloadObjectMsg(data.id)
                        line.updateProfileCoverVideo(path, path1)
                        line.sendMode(msg, to, sender, "video", 'Update Cover Video\nStatus: ✓')
                        line.deleteFile(path)
                        line.deleteFile(path1)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the video')
            
        elif cmd.startswith("changevideoyt "):
            link = removeCmd(text, setKey)
            subprocess.getoutput('youtube-dl --format mp4 --output cvp.mp4 {}'.format(link))
            profile = line.getProfile()
            if profile.pictureStatus:
                pict = "https://obs.line-scdn.net/{}".format(profile.pictureStatus)
                line.sendMessage(to, 'wait a moment, the video is being downloaded..')
                path = line.downloadFileURL(pict)
                line.updateVideoAndPictureProfile(path, "cvp.mp4")
                line.sendMode(msg, to, sender, cmd, "Change Video Profile From Youtube\nStatus: ✓")
                time.sleep(1)
                os.remove('cvp.mp4')
            else:
                line.sendFooter(to, "Use the profile picture first")
                
        elif cmd == 'p':
            if msg.toType == 0:
                line.sendMention(to, '「@!」', [to])
        
        elif cmd == 'story line':
            res = "› S T O R Y\n"
            res += '\n• My Story'
            res += '\n• Story List'
            res += '\n• Story Contact'
            res += '\n• Story @Mention'
            res += '\n• xStory (Reply Message)'
            res += '\n• P Story (Personal Chat)'
            res += "\n\n› L I K E\n"
            res += '\n• Story Like @Mention'
            res += '\n• xStory Like (Reply Message)'
            res += '\n• AutoLike Story <on/off>'
            res += "\n\n› C O M M E N T\n"
            res += '\n• AutoComment Story <on/off>'
            res += '\n• AutoComment Story <message>'
            res += "\n\n› U P L O A D\n"
            res += '\n• UploadStory'
            res += '\n• xUploadStory (Reply Image/Video)'
            line.sendMode(msg, to, sender, cmd, res)
        
        elif cmd == 'profile':
            isi = ["Profile", "P Mid", "P Name", "P Bio", "P Pict", "P Video", "P Cover", "P CoverExtra", "P Contact", "P Story", "Steal @Mention", "Mid @Mention", "Name @Mention", "Bio @Mention", "Pict @Mention", "Video @Mention", "Cover @Mention", "CoverExtra @Mention/Contact", "Contact @Mention/<name>", "Story @Mention"]
            isi2 = ["xSteal", "xMid", "xName", "xBio", "xPict", "xVideo", "xCover", "xCoverExtra", "xContact", "xStory"]
            res = looping_command(setKey.title(), "› C O M M A N D", isi)
            res += "\n\n"
            res += looping_command(setKey.title(), "› W I T H  R E P L Y<", isi2)
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd == 'p mid':
            profile = line.getContact(to) if msg.toType == 0 else None
            if msg.toType != 0: return line.sendFooter(to, 'this command can only be used in Personal chat!!')
            line.sendMessage(to, '' + str(profile.mid))
            
        elif cmd == 'p name':
            profile = line.getContact(to) if msg.toType == 0 else None
            if msg.toType != 0: return line.sendFooter(to, 'this command can only be used in Personal chat!!')
            line.sendFooter(to, '' + str(profile.displayName), reply=True)
            
        elif cmd == 'p bio':
            profile = line.getContact(to) if msg.toType == 0 else None
            if msg.toType != 0: return line.sendFooter(to, 'this command can only be used in Personal chat!!')
            if profile.statusMessage != '':
                line.sendFooter(to, '' + str(profile.statusMessage), reply=True)
            else:
                line.sendFooter(to, 'Bio is None', reply=True)
            
        elif cmd == 'p pict':
            profile = line.getContact(to) if msg.toType == 0 else None
            if msg.toType != 0: return line.sendFooter(to, 'this command can only be used in Personal chat!!')
            if profile.pictureStatus:
                path = 'https://obs.line-scdn.net/' + profile.pictureStatus
                line.sendLiffImage(to, path, line.settings["setFlag"]["icon"], " Profile Picture")
              #  line.sendMessage(to, path)
            else:
                line.sendFooter(to, 'User is not using profile picture', reply=True)
                
        elif cmd == 'p video':
            profile = line.getContact(to) if msg.toType == 0 else None
            if msg.toType != 0: return line.sendFooter(to, 'this command can only be used in Personal chat!!')
            if profile.videoProfile is not None:
                line.sendVideoWithURL(to, 'https://obs.line-scdn.net/' + profile.pictureStatus + '/vp')
               # line.sendMessage(to, 'https://obs.line-scdn.net/' + profile.pictureStatus + '/vp')
            else:
                line.sendFooter(to, "User is not using video profile", reply=True)
                    
        elif cmd == 'p cover':
            profile = line.getContact(to) if msg.toType == 0 else None
            if msg.toType != 0: return line.sendFooter(to, 'this command can only be used in Personal chat!!')
            cover = line.getProfileCoverURL(profile.mid)
            if "/vc/" in cover:
                line.sendVideoWithURL(to, cover)
            else:
                line.sendLiffImage(to, str(cover), line.settings["setFlag"]["icon"], " Profile Cover")
        #    line.sendMessage(to, str(cover))
        
        elif cmd == 'p contact':
            profile = line.getContact(to) if msg.toType == 0 else None
            if msg.toType != 0: return line.sendFooter(to, 'this command can only be used in Personal chat!!')
            line.sendContact(to, to)
            
        elif cmd == 'p coverextra':
            profile = line.getContact(to) if msg.toType == 0 else None
            if msg.toType != 0: return line.sendFooter(to, 'this command can only be used in Personal chat!!')
            datas = line.getEffect(profile.mid)
            if datas['result']:
                res = "User: @!"
                res += "\nMid: {}\n".format(profile.mid)
                no = 0
                dataImages = []
                dataStickers = []
                dataText = False
                for data in datas['result']:
                    if data["type"] == "Sticker":
                        if data["packageId"] not in dataStickers:
                            dataStickers.append(data["packageId"])
                            no += 1
                            res += "\n{}. Type: {}".format(no, data["type"])
                            res += "\n     Link: https://line.me/S/sticker/{}\n".format(data["packageId"])
                    elif data["type"] == "Link":
                        if not dataText:
                            dataText = True
                        no += 1
                        res += "\n{}. Type: {}".format(no, data["type"])
                        res += "\n     Link: {}\n".format(data["url"])
                    elif data["type"] == "Text":
                        if not dataText:
                            dataText = True
                        no += 1
                        res += "\n{}. Type: {}".format(no, data["type"])
                        res += "\n     Text: {}\n".format(data["text"])
                    elif data["type"] == "Image":
                        if data["url"] not in dataImages:
                            dataImages.append(data["url"])
                if dataStickers:
                    if res.endswith('\n'): res = res[:-1]
                    line.sendReplyMention(to, res, [profile.mid], msgIds=msg_id)
                elif dataText:
                    if res.endswith('\n'): res = res[:-1]
                    line.sendReplyMention(to, res, [profile.mid], msgIds=msg_id)
                if dataImages:
                    try:
                        if len(dataImages) >= 2:
                            line.sendMultiImageWithURL(to, dataImages)
                        else:
                            line.sendImageWithURL(to, dataImages[0])
                    except:
                        line.sendMessage(to, 'Upload image failure, try again')
            else:
                line.sendMode(msg, to, sender, 'CoverExtra Contact', 'This user does not use extra cover at all')

        elif cmd == 'p story':
            profile = line.getContact(to) if msg.toType == 0 else None
            if msg.toType != 0: return line.sendFooter(to, 'this command can only be used in Personal chat!!')
            data = line.getStoryMedia(profile.mid)
            if data:
                line.sendMessage(to, 'Downloading {} stories..'.format(len(data)))
                dataImages = []
                dataVideos = []
                for media in data:
                    if media["type"] == "image":
                        dataImages.append(media["url"])
                    elif media["type"] == "video":
                        line.sendVideoWithURL(to, media["url"])
                if dataImages:
                    if len(dataImages) >= 2:
                        line.sendMultiImageWithURL(to, dataImages)
                    else:
                        line.sendImageWithURL(to, dataImages[0])
            else:
                line.sendFooter(to, 'This user didnt upload any story')
        
        elif cmd == 'uploadstory':
            line.setts["upStory"] = True
            res = 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
            sendToggle(to, "UPLOAD STORY", res, res, True)
        
        elif cmd == 'xuploadstory':
            if msg.relatedMessageId:
                data = line.getReplyMessage(to, msg.relatedMessageId)
                if data is not None:
                    if data.contentType not in [1, 2]:
                        return line.sendMode(msg, to, sender, cmd, 'You must reply the image/video')
                    if data.contentType == 1:
                        mediaT = 'image'
                    elif data.contentType == 2:
                        mediaT = 'video'
                    path = line.downloadObjectMsg(data.id, saveAs='tmp/uploadstory.bin')
                    data = line.uploadObjStory(path, mediaT)
                    line.updateStory(data["obsOid"], data["xObsHash"], mediaType=mediaT)
                    line.sendMode(msg, to, sender, cmd, 'Upload Story\nStatus: ✓')
                    line.setts['upStory'] = False
                    line.deleteFile(path)
                else:
                    return line.sendMode(msg, to, sender, cmd, 'Message not found')
            else:
                return line.sendMode(msg, to, sender, cmd, 'You must reply the image/video')

        elif cmd.startswith('steal ') or cmd == "xsteal":
            target = []
            if cmd.startswith('steal '):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] not in target:
                            target.append(mention['M'])
            elif cmd == "xsteal":
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        target.append(data._from)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the message')
            for mid in target:
                profile = line.getContact(mid)
                image = []
                video = []
                if profile.pictureStatus:
                    image.append('https://obs.line-scdn.net/' + profile.pictureStatus)
                cover = line.getProfileCoverURL(profile.mid)
                if "/vc/" in cover:
                    line.sendVideoWithURL(to, cover)
                else:
                    image.append(cover)
                if len(image) == 2:
                    line.sendMultiImageWithURL(to, image)
                elif len(image) == 1:
                    line.sendImageWithURL(to, image[0])
                res = 'MID: ' + profile.mid
                res += '\nDisplay Name: ' + str(profile.displayName)
                if profile.displayNameOverridden: res += '\nDisplay Name Overridden: ' + str(profile.displayNameOverridden)
                res += '\nStatus Message: ' + str(profile.statusMessage)
                time.sleep(0.5)
                line.sendContact(to, profile.mid)
                line.sendMode(msg, to, sender, cmd, res)
                
        elif cmd.startswith('mid ') or cmd == "xmid":
            target = []
            if cmd.startswith('mid '):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] not in target:
                            target.append(mention['M'])
            elif cmd == "xmid":
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        target.append(data._from)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the message')
            for mid in target:
                line.sendFooter(to, '' + str(mid), reply=True)
                time.sleep(0.8)
        
        elif cmd.startswith('story ') or cmd.startswith('xstory'):
            target = []
            sep = removeCmd(text, setKey)
            if cmd.startswith('story '):
                textt = sep.split(' ')
                if textt[0].lower() == 'like':
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        for mention in mentions['MENTIONEES']:
                            if mention['M'] not in target:
                                mid = mention['M']
                                data = line.getStory(mid)
                                if data['message'] == 'success':
                                    if data['result']['contents']:
                                        for media in data['result']['contents']:
                                            if not media["viewReaction"]["reaction"]["liked"]:
                                                line.likeStory(media['contentId'], 1003)
                                                time.sleep(0.8)
                                                if media['contentId'] == data['result']['contents'][-1]['contentId']:
                                                    line.commentStory(mid, media['contentId'], 'Done like your Line story\nLiked by: sozibot')
                                        return line.sendMention(to, 'User: @!\nTotal: {} stories'.format(len(data['result']['contents'])), [mid])
                                    else:
                                        return line.sendMode(msg, to, sender, cmd, 'This user didnt upload any story')
                elif 'MENTION' in msg.contentMetadata.keys() and textt[0].lower() != 'like':
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] not in target:
                            target.append(mention['M'])
                elif cmd == 'story list':
                    userStory = line.getMidRecentStory()
                    if userStory:
                        parsed_len = len(userStory)//20+1
                        res = "𝗨𝘀𝗲𝗿:"
                        no = 0 
                        for point in range(parsed_len):
                            target = []
                            for mid in userStory[point*20:(point+1)*20]:
                                no += 1
                                target.append(mid)
                                res += "\n    ◯ {}. @!".format(no)
                                if mid == userStory[-1]:
                                    res += '\n\nType `%sStory Contact` and then send contact that you want to get the stories' % setKey.title()
                            if target:
                                if res.startswith("\n"): res = res[1:]
                                if point != 0:
                                    line.sendReplyMention(to, res, target, msgIds=msg_id)
                                else:
                                    line.sendMention(to, res, target)
                            res = ""
                        return
                elif cmd == 'story contact':
                    line.setts["storyCon"] = True
                    res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                    sendToggle(to, "STORY CONTACT", res, res, True)
                    return
            elif cmd.startswith('xstory'):
                if msg.relatedMessageId:
                    textt = sep.split(' ')
                    if cmd == 'xstory':
                        data = line.getReplyMessage(to, msg.relatedMessageId)
                        if data is not None:
                            target.append(data._from)
                        else:
                            return line.sendMode(msg, to, sender, cmd, 'Message not found')
                    elif textt[0].lower() == 'like':
                        data = line.getReplyMessage(to, msg.relatedMessageId)
                        if data is not None:
                            mid = data._from
                        else:
                            return line.sendMode(msg, to, sender, cmd, 'Message not found')
                        data = line.getStory(mid)
                        if data['message'] == 'success':
                            if data['result']['contents']:
                                for media in data['result']['contents']:
                                    if not media["viewReaction"]["reaction"]["liked"]:
                                        line.likeStory(media['contentId'], 1003)
                                        time.sleep(0.8)
                                        if media['contentId'] == data['result']['contents'][-1]['contentId']:
                                            line.commentStory(mid, media['contentId'], 'Done like your Line story\nLiked by: sozibot')
                                return line.sendMention(to, 'User: @!\nTotal: {} stories'.format(len(data['result']['contents'])), [mid])
                            else:
                                return line.sendMode(msg, to, sender, cmd, 'This user didnt upload any story')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the message')
            for mid in target:
                data = line.getStoryMedia(mid)
                if data:
                    line.sendMessage(to, 'Downloading {} stories..'.format(len(data)))
                    dataImages = []
                    dataVideos = []
                    for media in data:
                        if media["type"] == "image":
                            dataImages.append(media["url"])
                        elif media["type"] == "video":
                            line.sendVideoWithURL(to, media["url"])
                    if dataImages:
                        if len(dataImages) >= 2:
                            line.sendMultiImageWithURL(to, dataImages)
                        else:
                            line.sendImageWithURL(to, dataImages[0])
                else:
                    line.sendFooter(to, 'This user didnt upload any story')
                time.sleep(0.8)
                
        elif cmd.startswith('name ') or cmd == "xname":
            target = []
            if cmd.startswith('name '):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] not in target:
                            target.append(mention['M'])
            elif cmd == "xname":
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        target.append(data._from)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the message')
            for mid in target:
                profile = line.getContact(mid)
                line.sendFooter(to, '' + profile.displayName, reply=True)
                time.sleep(0.8)
                
        elif cmd.startswith('bio ') or cmd == "xbio":
            target = []
            if cmd.startswith('bio '):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] not in target:
                            target.append(mention['M'])
            elif cmd == "xbio":
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        target.append(data._from)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the message')
            for mid in target:
                profile = line.getContact(mid)
                if profile.statusMessage != '':
                    line.sendFooter(to, '' + str(profile.statusMessage), reply=True)
                else:
                    line.sendFooter(to, 'Bio is None', reply=True)
                time.sleep(0.8)

        elif cmd.startswith('pict ') or cmd == "xpict":
            target = []
            if cmd.startswith('pict '):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] not in target:
                            target.append(mention['M'])
            elif cmd == "xpict":
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        target.append(data._from)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the message')
            for mid in target:
                profile = line.getContact(mid)
                if profile.pictureStatus:
                    line.sendLiffImage(to, 'https://obs.line-scdn.net/' + profile.pictureStatus, line.settings["setFlag"]["icon"], " Profile Picture")
                 #   line.sendMessage(to, 'https://obs.line-scdn.net/' + profile.pictureStatus)
                else:
                    line.sendFooter(to, "User not using picture profile", reply=True)
                        
        elif cmd.startswith('cover ') or cmd == "xcover":
            target = []
            if cmd.startswith('cover '):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] not in target:
                            target.append(mention['M'])
            elif cmd == "xcover":
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        target.append(data._from)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the message')
            for mid in target:
                profile = line.getContact(mid)
                cover = line.getProfileCoverURL(profile.mid)
                if "/vc/" in cover:
                    line.sendVideoWithURL(to, cover)
                else:
                    line.sendLiffImage(to, str(cover), line.settings["setFlag"]["icon"], " Profile Cover")
                #line.sendMessage(to, str(cover))
        
        elif cmd.startswith('coverextra ') or cmd == "xcoverextra":
            target = []
            if cmd.startswith('coverextra '):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] not in target:
                            target.append(mention['M'])
                elif cmd == "coverextra contact":
                    line.setts["coverExtraContact"] = True
                    res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                    sendToggle(to, "COVER EXTRA", res, res, True)
                    return
            elif cmd == "xcoverextra":
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        target.append(data._from)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the message')
            for mid in target:
                profile = line.getContact(mid)
                datas = line.getEffect(profile.mid)
                if datas['result']:
                    res = "User: @!"
                    res += "\nMid: {}\n".format(profile.mid)
                    no = 0
                    dataImages = []
                    dataStickers = []
                    dataText = False
                    for data in datas['result']:
                        if data["type"] == "Sticker":
                            if data["packageId"] not in dataStickers:
                                dataStickers.append(data["packageId"])
                                no += 1
                                res += "\n{}. Type: {}".format(no, data["type"])
                                res += "\n     Link: https://line.me/S/sticker/{}\n".format(data["packageId"])
                        elif data["type"] == "Link":
                            if not dataText:
                                dataText = True
                            no += 1
                            res += "\n{}. Type: {}".format(no, data["type"])
                            res += "\n     Link: {}\n".format(data["url"])
                        elif data["type"] == "Text":
                            if not dataText:
                                dataText = True
                            no += 1
                            res += "\n{}. Type: {}".format(no, data["type"])
                            res += "\n     Text: {}\n".format(data["text"])
                        elif data["type"] == "Image":
                            if data["url"] not in dataImages:
                                dataImages.append(data["url"])
                    if dataStickers:
                        if res.endswith('\n'): res = res[:-1]
                        line.sendReplyMention(to, res, [profile.mid], msgIds=msg_id)
                    elif dataText:
                        if res.endswith('\n'): res = res[:-1]
                        line.sendReplyMention(to, res, [profile.mid], msgIds=msg_id)
                    if dataImages:
                        try:
                            if len(dataImages) >= 2:
                                line.sendMultiImageWithURL(to, dataImages)
                            else:
                                line.sendImageWithURL(to, dataImages[0])
                        except:
                            line.sendMessage(to, 'Upload image failure, try again')
                else:
                    line.sendMode(msg, to, sender, 'CoverExtra Contact', 'This user does not use extra cover at all')

        elif cmd.startswith('contact ') or cmd == "xcontact":
            target = []
            if cmd.startswith('contact '):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] not in target:
                            target.append(mention['M'])
                else:
                    textt = removeCmd(text, setKey)
                    name = textt.lower()
                    if name == '' or name == " ":
                        return
                    friend = line.getAllContactIds()
                    targett = []
                    for teman in friend:
                        contact = line.getContact(teman)
                        if contact.displayNameOverridden:
                            if name in contact.displayNameOverridden.lower():
                                line.sendContact(to, teman)
                                targett.append(teman)
                        if name in contact.displayName.lower():
                            if teman not in targett:
                                line.sendContact(to, teman)
                                targett.append(teman)
                    if not targett:
                        return line.sendMode(msg, to, sender, cmd, "No user found with name '{}'".format(name))
            elif cmd == "xcontact":
                if msg.relatedMessageId:
                    data = line.getReplyMessage(to, msg.relatedMessageId)
                    if data is not None:
                        target.append(data._from)
                    else:
                        return line.sendMode(msg, to, sender, cmd, 'Message not found')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'You must reply the message')
            for mid in target:
                line.sendContact(to, mid)
                time.sleep(1)
                    
        elif cmd.startswith('autolike'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == 'autolike':
                res = 'Status: ' + bool_dict[line.settings['autoLike']['status']][4]
                res += '\nStatus Note: ' + bool_dict[line.settings['autoLike']['note']][4]
                res += '\nStatus Story: ' + bool_dict[line.settings['autoLike']['story']][4]
                res += '\nStatus Reply: ' + bool_dict[line.settings['autoLike']['reply']][4]
                res += '\nReply Message: ' + line.settings['autoLike']['message']
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}AutoLike'.format(setKey.title())
                res += '\n• {}AutoLike <on/off>'.format(setKey.title())
                res += '\n• {}AutoLike Note <on/off>'.format(setKey.title())
                res += '\n• {}AutoLike Story <on/off>'.format(setKey.title())
                res += '\n• {}AutoLike Reply <on/off>'.format(setKey.title())
                res += '\n• {}AutoLike Reply <message>'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['autoLike']['status']:
                    line.settings['autoLike']['status'] = True
                sendToggle(to, "AUTO LIKE POST", "Auto Like Post\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['autoLike']['status']:
                    line.settings['autoLike']['status'] = False
                sendToggle(to, "AUTO LIKE POST", "Auto Like Post\nStatus: ✘", "", False)
            elif texttl.startswith('reply '):
                textts = textt[6:]
                texttls = textts.lower()
                if texttls == 'on':
                    if not line.settings['autoLike']['reply']:
                        line.settings['autoLike']['reply'] = True
                    sendToggle(to, "AUTO REPLY LIKE POST", "Auto Reply Like Post\nStatus: ✓", "", True)
                elif texttls == 'off':
                    if line.settings['autoLike']['reply']:
                        line.settings['autoLike']['reply'] = False
                    sendToggle(to, "AUTO REPLY LIKE POST", "Auto Reply Like Post\nStatus: ✘", "", False)
                elif 'STICON_OWNERSHIP' in msg.contentMetadata:
                    getEmoji = line.metadataFilter(msg.contentMetadata, len(setKey)+15, type='emoji')
                    line.settings["autoLike"]["contentMetadata"] = getEmoji
                    line.settings['autoLike']['message'] = textts
                    getEmoji2 = line.metadataFilter(getEmoji, 37, type='emoji2')
                    if "@!" in textts:
                        line.settings["autoLike"]["contentMention"] = line.metadataFilter(getEmoji, text=textts, type='mention')
                        getEmoji2.update(line.metadataFilter(getEmoji, text='Reply like successfully changed to \'{}\''.format(textts), type='mention'))
                    line.sendReplyMessage(to, 'Reply like successfully changed to \'{}\''.format(textts), getEmoji2, msgIds=msg_id)
                else:
                    line.settings["autoLike"]["contentMetadata"] = {}
                    line.settings["autoLike"]["contentMention"] = {}
                    line.settings['autoLike']['message'] = textts
                    line.sendMode(msg, to, sender, cmd, 'Reply like successfully changed to \'%s\'' % textts)
            elif texttl.startswith('note '):
                textts = textt[5:]
                texttls = textts.lower()
                if texttls == 'on':
                    if not line.settings['autoLike']['note']:
                        line.settings['autoLike']['note'] = True
                    sendToggle(to, "AUTO LIKE NOTE", "Auto Like Note\nStatus: ✓", "", True)
                elif texttls == 'off':
                    if line.settings['autoLike']['note']:
                        line.settings['autoLike']['note'] = False
                    sendToggle(to, "AUTO LIKE NOTE", "Auto Like Note\nStatus: ✘", "", False)
            elif texttl.startswith('story '):
                textts = textt[6:]
                texttls = textts.lower()
                if texttls == 'on':
                    if not line.settings['autoLike']['story']:
                        line.settings['autoLike']['story'] = True
                    sendToggle(to, "AUTO LIKE STORY", "Auto Like Story\nStatus: ✓", "", True)
                elif texttls == 'off':
                    if line.settings['autoLike']['story']:
                        line.settings['autoLike']['story'] = False
                    sendToggle(to, "AUTO LIKE STORY", "Auto Like Story\nStatus: ✘", "", False)
            
        elif cmd.startswith('autocomment'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if cmd == 'autocomment':
                res = 'Status: ' + bool_dict[line.settings['autoComment']['status']][4]
                res += '\nStatus Note: ' + bool_dict[line.settings['autoComment']['note']][4]
                res += '\nStatus Story: ' + bool_dict[line.settings['autoComment']['story']['status']][4]
                res += '\nMessage: ' + line.settings['autoComment']['message']
                res += '\nMessage Story: ' + line.settings['autoComment']['story']['message']
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}AutoComment'.format(setKey.title())
                res += '\n• {}AutoComment <on/off>'.format(setKey.title())
                res += '\n• {}AutoComment <message>'.format(setKey.title())
                res += '\n• {}AutoComment Note <on/off>'.format(setKey.title())
                res += '\n• {}AutoComment Story <on/off>'.format(setKey.title())
                res += '\n• {}AutoComment Story <message>'.format(setKey.title())
                res += '\n• {}AutoComment Sticker'.format(setKey.title())
                res += '\n• {}AutoComment delSticker'.format(setKey.title())
                res += '\n\nExample: {}AutoComment Hello @! This program by Sozi'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['autoComment']['status']:
                    line.settings['autoComment']['status'] = True
                sendToggle(to, "AUTO COMMENT POST", "Auto Comment Post\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['autoComment']['status']:
                    line.settings['autoComment']['status'] = False
                sendToggle(to, "AUTO COMMENT POST", "Auto Comment Post\nStatus: ✘", "", False)
            elif texttl.startswith('note '):
                textts = textt[5:]
                texttls = textts.lower()
                if texttls == 'on':
                    if not line.settings['autoComment']['note']:
                        line.settings['autoComment']['note'] = True
                    sendToggle(to, "AUTO COMMENT NOTE", "Auto Comment Note\nStatus: ✓", "", True)
                elif texttls == 'off':
                    if line.settings['autoComment']['note']:
                        line.settings['autoComment']['note'] = False
                    sendToggle(to, "AUTO COMMENT NOTE", "Auto Comment Note\nStatus: ✘", "", False)
            elif texttl.startswith('story '):
                textts = textt[6:]
                texttls = textts.lower()
                if texttls == 'on':
                    if not line.settings['autoComment']['story']['status']:
                        line.settings['autoComment']['story']['status'] = True
                    sendToggle(to, "AUTO COMMENT STORY", "Auto Comment Story\nStatus: ✓", "", True)
                elif texttls == 'off':
                    if line.settings['autoComment']['story']['status']:
                        line.settings['autoComment']['story']['status'] = False
                    sendToggle(to, "AUTO COMMENT STORY", "Auto Comment Story\nStatus: ✘", "", False)
                else:
                    line.settings['autoComment']['story']['message'] = textts
                    line.sendMode(msg, to, sender, cmd, 'Comment story successfully changed to \'%s\'' % textts)
            elif texttl == 'sticker':
                if sender == line.profile.mid:
                    line.settings["autoComment"]["setsticker"] = True
                    line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            elif texttl == 'delsticker':
                line.settings["autoComment"]["sticker"] = {}
                line.sendMode(msg, to, sender, cmd, 'Auto Comment Sticker successfully deleted')
            elif 'STICON_OWNERSHIP' in msg.contentMetadata:
                getEmoji = line.metadataFilter(msg.contentMetadata, len(setKey)+12, type='emojiComment')
                getEmojii = line.metadataFilter(msg.contentMetadata, len(setKey)+12, type='emoji')
                line.settings["autoComment"]["contentMetadata"] = getEmoji
                line.settings['autoComment']['message'] = textt
                getEmoji2 = line.metadataFilter(getEmojii, 34, type='emoji2')
                if "@!" in textt:
                    line.settings["autoComment"]["contentMention"] = line.metadataFilter(getEmoji, text=textt, type='mentionComment')
                    getEmoji2.update(line.metadataFilter(getEmojii, text='Comment successfully changed to \'{}\''.format(textt), type='mention'))
                line.sendReplyMessage(to, 'Comment successfully changed to \'{}\''.format(textt), getEmoji2, msgIds=msg_id)
            else:
                line.settings["autoComment"]["contentMetadata"] = {}
                line.settings["autoComment"]["contentMention"] = {}
                line.settings['autoComment']['message'] = textt
                line.sendMode(msg, to, sender, cmd, 'Comment successfully changed to \'%s\'' % textt)
                
        elif cmd == 'sider':
            if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
            if msg.toType in [1, 2] and to not in line.setts["lurking"]:
                line.setts["lurking"][to] = {
                    'status': False,
                    'time': None,
                    'members': [],
                    'reply': {
                        'status': False,
                        'message': line.settings['sider']['defaultReplyReader']
                    }
                }
            if msg.toType in [1, 2]: res = 'Status: ' + bool_dict[line.setts["lurking"][to]['status']][4]
            if msg.toType in [1, 2]: res += '\nCyduk: ' + bool_dict[line.setts["lurking"][to]['reply']['status']][4]
            if msg.toType in [1, 2]: res += '\nCyduk Message: ' + line.setts["lurking"][to]['reply']['message']
            res += '\n\n› C O M M A N D\n'
            res += '\n• {}Sider'.format(setKey.title())
            res += '\n• {}Sider <on/off>'.format(setKey.title())
            res += '\n• {}Sider Result'.format(setKey.title())
            res += '\n• {}Sider Reset'.format(setKey.title())
            res += '\n• {}Cyduk <on/off>'.format(setKey.title())
            res += '\n• {}Cyduk set <message>'.format(setKey.title())
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd == 'sider on':
            if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
            if msg.toType in [1, 2] and to not in line.setts["lurking"]:
                line.setts["lurking"][to] = {
                    'status': False,
                    'time': None,
                    'members': [],
                    'reply': {
                        'status': False,
                        'message': line.settings['sider']['defaultReplyReader']
                    }
                }
            if not line.setts["lurking"][to]['status']:
                line.setts["lurking"][to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
            sendToggle(to, "CHECK READER", "Check reader activated, type '{}sider result' to view data reader".format(setKey.title()), "Type '{}sider result' to view data reader".format(setKey.title()), True)
                
        elif cmd == 'sider off':
            if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in deep group!!')
            if msg.toType in [1, 2] and to not in line.setts["lurking"]:
                line.setts["lurking"][to] = {
                    'status': False,
                    'time': None,
                    'members': [],
                    'reply': {
                        'status': False,
                        'message': line.settings['sider']['defaultReplyReader']
                    }
                }
            if line.setts["lurking"][to]['status']:
                line.setts["lurking"][to].update({
                    'status': False,
                    'time': None,
                    'members': []
                })
            sendToggle(to, "CHECK READER", "Check Reader disabled", "", False)
                
        elif cmd == 'sider result':
            if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
            if msg.toType in [1, 2] and to not in line.setts["lurking"]:
                line.setts["lurking"][to] = {
                    'status': False,
                    'time': None,
                    'members': [],
                    'reply': {
                        'status': False,
                        'message': line.settings['sider']['defaultReplyReader']
                    }
                }
            if not line.setts["lurking"][to]['status']:
                line.sendMode(msg, to, sender, cmd, 'Sider not yet active, type \'{}Sider on\' first'.format(setKey.title()))
            else:
                if not line.setts["lurking"][to]['members']:
                    line.sendMode(msg, to, sender, cmd, 'The data is still empty, no one has read it yet')
                else:
                    members = line.setts["lurking"][to]['members']
                    res = 'Check Sider'
                    if msg.toType == 2: res += '\nGroup: ' + line.getChats([to], False, False).chats[0].chatName + "\n"
                    parsed_len = len(members)//200+1
                    no = 0
                    for point in range(parsed_len):
                        for member in members[point*200:(point+1)*200]:
                            no += 1
                            try:
                                name = line.getContact(member).displayName
                            except TalkException:
                                name = 'Unknown'
                            if member == members[-1]:
                                res += '\n    %i. %s' % (no, name)
                            else:
                                res += '\n    %i. %s' % (no, name)
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendReplyMessage(to, res, msgIds=msg_id)
                        res = ''
                        
        elif cmd == 'sider reset':
            if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in deep group!!')
            if msg.toType in [1, 2] and to not in line.setts["lurking"]:
                line.setts["lurking"][to] = {
                    'status': False,
                    'time': None,
                    'members': [],
                    'reply': {
                        'status': False,
                        'message': line.settings['sider']['defaultReplyReader']
                    }
                }
            if not line.setts["lurking"][to]['status']:
                line.sendMode(msg, to, sender, cmd, 'Sider not yet active, type \'{}Sider on\' first'.format(setKey.title()))
            else:
                line.setts["lurking"][to].update({
                    'status': True,
                    'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                    'members': []
                })
                line.sendMode(msg, to, sender, cmd, 'Data sider reset successfully')
                
        elif cmd == 'cyduk on':
            if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
            if to not in line.setts["replyReader"]:
                line.setts["replyReader"][to] = {
                    'listmem': [],
                    'eply': {
                        'tatus': False,
                    }
                }
            if line.setts["replyReader"][to]['eply']['tatus']:
                line.sendMode(msg, to, sender, cmd, "Cyduk is active, turn it off first then reactivate it")
            else:
                line.setts["replyReader"][to]['eply']['tatus'] = True
                line.sendFooter(to, "Start scooping...")
                
        elif cmd == 'cyduk off':
            if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in deep group!!')
            if to not in line.setts["replyReader"]: line.sendMode(msg, to, sender, cmd, "Cyduk is inactive, turn it on first")
            elif not line.setts["replyReader"][to]['eply']['tatus']: line.sendMode(msg, to, sender, cmd, "Cyduk is inactive, turn it on first")
            else:
                line.setts["replyReader"][to].update({
                    'listmem': [],
                    'eply': {
                        'tatus': False,
                    }
                })
                line.sendFooter(to, "Stop scooping...")
                
        elif cmd.startswith('cyduk set '):
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if len(sep) < 2:
                return line.sendMode(msg, to, sender, cmd, "Example:\n{}Cyduk set Hai siderr..".format(setKey.title()))
            texts = textt.replace(sep[0] + " ","")
            if 'STICON_OWNERSHIP' in msg.contentMetadata:
                if "@!" not in textt:
                    return line.sendMode(msg, to, sender, cmd, "Failed to set cyduk message, paid emoji only support with mention\nExample: Hayo (emoji) @!".format(setKey.title()))
                getEmoji = line.metadataFilter(msg.contentMetadata, len(setKey)+10, type='emoji')
                line.settings["sider"]["contentMetadata"] = getEmoji
                line.settings['sider']['defaultReplyReader'] = texts
                getEmoji2 = line.metadataFilter(getEmoji, 39, type='emoji2')
                if "@!" in textt:
                    line.settings["sider"]["contentMention"] = line.metadataFilter(getEmoji, text=texts, type='mention')
                    getEmoji2.update(line.metadataFilter(getEmoji, text='Respon cyduk successfully changed to `{}`'.format(texts), type='mention'))
                line.sendReplyMessage(to, 'Respon cyduk successfully changed to `{}`'.format(texts), getEmoji2, msgIds=msg_id)
            else:
                line.settings["sider"]["contentMetadata"] = {}
                line.settings["sider"]["contentMention"] = {}
                line.settings['sider']['defaultReplyReader'] = texts
                line.sendMode(msg, to, sender, cmd, 'Respon cyduk successfully changed to \'%s\'' % texts)
            
        elif cmd == 'greet':
            res = '› W E L C O M E  S T A T U S\n'
            res += '\nText: '+ str(line.settings['greet']['join']['message'])
            if to in line.settings['greet']['join']['group'] or line.settings["greet"]["join"]["allText"]: res += '\nText Status: ✓'
            else: res += '\nText Status: ✘'
            if to in line.settings['greet']['join']['groupSticker'] or line.settings["greet"]["join"]["allSticker"]: res += '\nSticker Status: ✓'
            else: res += '\nSticker Status: ✘'
            if to in line.settings['greet']['join']['groupImage'] or line.settings["greet"]["join"]["allImage"]: res += '\nImage Status: ✓'
            else: res += '\nImage Status: ✘'
            res += '\n\n› L E A V E  S T A T U S\n'
            res += '\nText: '+ str(line.settings['greet']['leave']['message'])
            if to in line.settings['greet']['leave']['group'] or line.settings["greet"]["leave"]["allText"]: res += '\nText Status: ✓'
            else: res += '\nText Status: ✘'
            if to in line.settings['greet']['leave']['groupSticker'] or line.settings["greet"]["leave"]["allSticker"]: res += '\nSticker Status: ✓'
            else: res += '\nSticker Status: ✘'
            if to in line.settings['greet']['leave']['groupImage'] or line.settings["greet"]["leave"]["allImage"]: res += '\nImage Status: ✓'
            else: res += '\nImage Status: ✘'
            res += '\n\n› C O M M A N D\n'
            res += '\n• {}Welcome Text <on/off/list>'.format(setKey.title())
            res += '\n• {}Welcome Text <on/off> <num>'.format(setKey.title())
            res += '\n• {}Welcome Text All <on/off>'.format(setKey.title())
            res += '\n• {}Welcome Text <message>'.format(setKey.title())
            res += '\n• {}Welcome Sticker <on/off/list>'.format(setKey.title())
            res += '\n• {}Welcome Sticker <on/off> <num>'.format(setKey.title())
            res += '\n• {}Welcome Sticker All <on/off>'.format(setKey.title())
            res += '\n• {}Welcome setSticker'.format(setKey.title())
            res += '\n• {}Welcome Image <on/off/list>'.format(setKey.title())
            res += '\n• {}Welcome Image <on/off> <num>'.format(setKey.title())
            res += '\n• {}Welcome Image All <on/off>'.format(setKey.title())
            res += '\n• {}Welcome setImage / delImage'.format(setKey.title())
            res += '\n\n• {}Leave Text <on/off/list>'.format(setKey.title())
            res += '\n• {}Leave Text <on/off> <num>'.format(setKey.title())
            res += '\n• {}Leave Text All <on/off>'.format(setKey.title())
            res += '\n• {}Leave Text <message>'.format(setKey.title())
            res += '\n• {}Leave Sticker <on/off/list>'.format(setKey.title())
            res += '\n• {}Leave Sticker <on/off> <num>'.format(setKey.title())
            res += '\n• {}Leave Sticker All <on/off>'.format(setKey.title())
            res += '\n• {}Leave setSticker'.format(setKey.title())
            res += '\n• {}Leave Image <on/off/list>'.format(setKey.title())
            res += '\n• {}Leave Image <on/off> <num>'.format(setKey.title())
            res += '\n• {}Leave Image All <on/off>'.format(setKey.title())
            res += '\n• {}Leave setImage / delImage'.format(setKey.title())
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith("welcome"):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            gc = line.getChats([to], False, False).chats[0]
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl.startswith("text "):
                texts = textt[5:]
                textsl = texts.lower()
                if textsl == 'list':
                    if line.settings["greet"]["join"]["allText"]:
                        return line.sendMode(msg, to, sender, cmd, 'Group Welcome Text has been activated in all groups')
                    groups = line.settings['greet']['join']['group']
                    if groups:
                        res = '› L I S T\n'
                        no = 0
                        for group in groups:
                            no += 1
                            group = line.getChats([group], True, False).chats[0]
                            res += '\n{}. {}//{}'.format(no, group.chatName, len(group.extra.groupExtra.memberMids))
                        line.sendMode(msg, to, sender, cmd, res)
                    else:
                        line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                elif textsl.startswith('on'):
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                        targets = filter_target(sup[1], groups)
                        res = "› A D D E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target not in line.settings['greet']['join']['group']:
                                    line.settings['greet']['join']['group'].append(target)
                                    res += "\n{}. {} > Added".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Already".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                    elif textsl == 'on':
                        if to not in line.settings['greet']['join']['group']:
                            line.settings['greet']['join']['group'].append(to)
                        sendToggle(to, "COMMAND WELCOME", "Command Welcome Text\nGroup: {}\nStatus: ✓".format(gc.chatName), "Type: Text\nGroup: {}".format(gc.chatName), True)
                elif textsl.startswith('off'):
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        targets = filter_target(sup[1], line.settings['greet']['join']['group'])
                        res = "› D E L E T E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target in line.settings['greet']['join']['group']:
                                    line.settings['greet']['join']['group'].remove(target)
                                    res += "\n{}. {} > Deleted".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Not Found".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was deleted')
                    elif textsl == 'off':
                        if to in line.settings['greet']['join']['group']:
                            line.settings['greet']['join']['group'].remove(to)
                        sendToggle(to, "COMMAND WELCOME", "Command Welcome Text\nGroup: {}\nStatus: ✘".format(gc.chatName), "Type: Text\nGroup: {}".format(gc.chatName), False)
                elif textsl == 'all on':
                    if not line.settings["greet"]["join"]["allText"]:
                        line.settings["greet"]["join"]["allText"] = True
                    sendToggle(to, "COMMAND WELCOME", "Command Welcome Text\nGroup: All Group\nStatus: ✓", "Type: Text\nGroup: All Group", True)
                    line.settings["greet"]["join"]["group"].clear()
                elif textsl == 'all off':
                    if line.settings["greet"]["join"]["allText"]:
                        line.settings["greet"]["join"]["allText"] = False
                    sendToggle(to, "COMMAND WELCOME", "Command Welcome Text\nGroup: All Group\nStatus: ✘", "Type: Text\nGroup: All Group", False)
                    line.settings["greet"]["join"]["group"].clear()
                else:
                    line.settings['greet']['join']['message'] = texts
                    line.sendMode(msg, to, sender, cmd, 'Message welcome successfully changed to \'%s\'' % texts)
            
            elif texttl.startswith("sticker "):
                texts = textt[8:]
                textsl = texts.lower()
                if textsl == 'list':
                    if line.settings["greet"]["join"]["allSticker"]:
                        return line.sendMode(msg, to, sender, cmd, 'Group Welcome Sticker has been activated in all groups')
                    groups = line.settings['greet']['join']['groupSticker']
                    if groups:
                        res = '› L I S T\n'
                        no = 0
                        for group in groups:
                            no += 1
                            group = line.getChats([group], True, False).chats[0]
                            res += '\n{}. {}//{}'.format(no, group.chatName, len(group.extra.groupExtra.memberMids))
                        line.sendMode(msg, to, sender, cmd, res)
                    else:
                        line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                elif textsl.startswith('on'):
                    if line.settings['greet']['join']['sticker']["STKID"] == 'empty':
                        return line.sendMode(msg, to, sender, cmd, 'Sticker still empty, type \'{}Welcome SetSticker\' to add sticker'.format(setKey.title()))
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                        targets = filter_target(sup[1], groups)
                        res = "› A D D E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target not in line.settings['greet']['join']['groupSticker']:
                                    line.settings['greet']['join']['groupSticker'].append(target)
                                    res += "\n{}. {} > Added".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Already".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                    elif textsl == 'on':
                        if to not in line.settings['greet']['join']['groupSticker']:
                            line.settings['greet']['join']['groupSticker'].append(to)
                        sendToggle(to, "COMMAND WELCOME", "Command Welcome Sticker\nGroup: {}\nStatus: ✓".format(gc.chatName), "Type: Sticker\nGroup: {}".format(gc.chatName), True)
                elif textsl.startswith('off'):
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        targets = filter_target(sup[1], line.settings['greet']['join']['groupSticker'])
                        res = "› D E L E T E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target in line.settings['greet']['join']['groupSticker']:
                                    line.settings['greet']['join']['groupSticker'].remove(target)
                                    res += "\n{}. {} > Deleted".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Not Found".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was deleted')
                    elif textsl == 'off':
                        if to in line.settings['greet']['join']['groupSticker']:
                            line.settings['greet']['join']['groupSticker'].remove(to)
                        sendToggle(to, "COMMAND WELCOME", "Command Welcome Sticker\nGroup: {}\nStatus: ✘".format(gc.chatName), "Type: Sticker\nGroup: {}".format(gc.chatName), False)
                elif textsl == 'all on':
                    if line.settings['greet']['join']['sticker']["STKID"] == 'empty':
                        return line.sendMode(msg, to, sender, cmd, 'Sticker still empty, type \'{}Welcome SetSticker\' to add sticker'.format(setKey.title()))
                    if not line.settings["greet"]["join"]["allSticker"]:
                        line.settings["greet"]["join"]["allSticker"] = True
                    sendToggle(to, "COMMAND WELCOME", "Command Welcome Sticker\nGroup: All Group\nStatus: ✓", "Type: Sticker\nGroup: All Group", True)
                    line.settings["greet"]["join"]["groupSticker"].clear()
                elif textsl == 'all off':
                    if line.settings["greet"]["join"]["allSticker"]:
                        line.settings["greet"]["join"]["allSticker"] = False
                    sendToggle(to, "COMMAND WELCOME", "Command Welcome Sticker\nGroup: All Group\nStatus: ✘", "Type: Sticker\nGroup: All Group", False)
                    line.settings["greet"]["join"]["groupSticker"].clear()
                        
            elif texttl == 'setsticker':
                if sender == line.profile.mid:
                    line.setts["greets"]["joinSticker"] = True
                    line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            
            elif texttl.startswith("image "):
                texts = textt[6:]
                textsl = texts.lower()
                if textsl == 'list':
                    if line.settings["greet"]["join"]["allImage"]:
                        return line.sendMode(msg, to, sender, cmd, 'Group Welcome Image has been activated in all groups')
                    groups = line.settings['greet']['join']['groupImage']
                    if groups:
                        res = '› L I S T\n'
                        no = 0
                        for group in groups:
                            no += 1
                            group = line.getChats([group], True, False).chats[0]
                            res += '\n{}. {}//{}'.format(no, group.chatName, len(group.extra.groupExtra.memberMids))
                        line.sendMode(msg, to, sender, cmd, res)
                    else:
                        line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                elif textsl.startswith('on'):
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                        targets = filter_target(sup[1], groups)
                        res = "› A D D E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target not in line.settings['greet']['join']['groupImage']:
                                    line.settings['greet']['join']['groupImage'].append(target)
                                    res += "\n{}. {} > Added".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Already".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                    elif textsl == 'on':
                        if to not in line.settings['greet']['join']['groupImage']:
                            line.settings['greet']['join']['groupImage'].append(to)
                        sendToggle(to, "COMMAND WELCOME", "Command Welcome Image\nGroup: {}\nStatus: ✓".format(gc.chatName), "Type: Image\nGroup: {}".format(gc.chatName), True)
                elif textsl.startswith('off'):
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        targets = filter_target(sup[1], line.settings['greet']['join']['groupImage'])
                        res = "› D E L E T E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target in line.settings['greet']['join']['groupImage']:
                                    line.settings['greet']['join']['groupImage'].remove(target)
                                    res += "\n{}. {} > Deleted".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Not Found".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was deleted')
                    elif textsl == 'off':
                        if to in line.settings['greet']['join']['groupImage']:
                            line.settings['greet']['join']['groupImage'].remove(to)
                        sendToggle(to, "COMMAND WELCOME", "Command Welcome Image\nGroup: {}\nStatus: ✘".format(gc.chatName), "Type: Image\nGroup: {}".format(gc.chatName), False)
                elif textsl == 'all on':
                    if not line.settings["greet"]["join"]["allImage"]:
                        line.settings["greet"]["join"]["allImage"] = True
                    sendToggle(to, "COMMAND WELCOME", "Command Welcome Image\nGroup: All Group\nStatus: ✓", "Type: Image\nGroup: All Group", True)
                    line.settings["greet"]["join"]["groupImage"].clear()
                elif textsl == 'all off':
                    if line.settings["greet"]["join"]["allImage"]:
                        line.settings["greet"]["join"]["allImage"] = False
                    sendToggle(to, "COMMAND WELCOME", "Command Welcome Image\nGroup: All Group\nStatus: ✘", "Type: Image\nGroup: All Group", False)
                    line.settings["greet"]["join"]["groupImage"].clear()
                    
            elif texttl == 'setimage':
                line.setts["greets"]["wImage"] = True
                line.sendMode(msg, to, sender, cmd, 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            
            elif texttl == 'delimage':
                line.setts["greets"]["wImage"] = False
                if line.settings["greet"]["join"]["imagePath"] is not None:
                    line.deleteFile(line.settings["greet"]["join"]["imagePath"])
                    line.settings["greet"]["join"]["imagePath"] = None
                line.sendMode(msg, to, sender, cmd, 'Command Welcome Image successfully deleted')
                    
        elif cmd.startswith("leave"):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
            gc = line.getChats([to], False, False).chats[0]
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl.startswith("text "):
                texts = textt[5:]
                textsl = texts.lower()
                if textsl == 'list':
                    if line.settings["greet"]["leave"]["allText"]:
                        return line.sendMode(msg, to, sender, cmd, 'Group Leave Text has been activated in all groups')
                    groups = line.settings['greet']['leave']['group']
                    if groups:
                        res = '› L I S T\n'
                        no = 0
                        for group in groups:
                            no += 1
                            group = line.getChats([group], True, False).chats[0]
                            res += '\n{}. {}//{}'.format(no, group.chatName, len(group.extra.groupExtra.memberMids))
                        line.sendMode(msg, to, sender, cmd, res)
                    else:
                        line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                elif textsl.startswith('on'):
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                        targets = filter_target(sup[1], groups)
                        res = "› A D D E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target not in line.settings['greet']['leave']['group']:
                                    line.settings['greet']['leave']['group'].append(target)
                                    res += "\n{}. {} > Added".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Already".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                    elif textsl == 'on':
                        if to not in line.settings['greet']['leave']['group']:
                            line.settings['greet']['leave']['group'].append(to)
                        sendToggle(to, "COMMAND LEAVE", "Command Leave Text\nGroup: {}\nStatus: ✓".format(gc.chatName), "Type: Text\nGroup: {}".format(gc.chatName), True)
                elif textsl.startswith('off'):
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        targets = filter_target(sup[1], line.settings['greet']['leave']['group'])
                        res = "› D E L E T E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target in line.settings['greet']['leave']['group']:
                                    line.settings['greet']['leave']['group'].remove(target)
                                    res += "\n{}. {} > Deleted".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Not Found".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was deleted')
                    elif textsl == 'off':
                        if to in line.settings['greet']['leave']['group']:
                            line.settings['greet']['leave']['group'].remove(to)
                        sendToggle(to, "COMMAND LEAVE", "Command Leave Text\nGroup: {}\nStatus: ✘".format(gc.chatName), "Type: Text\nGroup: {}".format(gc.chatName), False)
                elif textsl == 'all on':
                    if not line.settings["greet"]["leave"]["allText"]:
                        line.settings["greet"]["leave"]["allText"] = True
                    sendToggle(to, "COMMAND LEAVE", "Command Leave Text\nGroup: All Group\nStatus: ✓", "Type: Text\nGroup: All Group", True)
                    line.settings["greet"]["leave"]["group"].clear()
                elif textsl == 'all off':
                    if line.settings["greet"]["leave"]["allText"]:
                        line.settings["greet"]["leave"]["allText"] = False
                    sendToggle(to, "COMMAND LEAVE", "Command Leave Text\nGroup: All Group\nStatus: ✘", "Type: Text\nGroup: All Group", False)
                    line.settings["greet"]["leave"]["group"].clear()
                else:
                    line.settings['greet']['leave']['message'] = texts
                    line.sendMode(msg, to, sender, cmd, 'The leave message was successfully changed to \'%s\'' % texts)
            
            elif texttl.startswith("sticker "):
                texts = textt[8:]
                textsl = texts.lower()
                if textsl == 'list':
                    if line.settings["greet"]["leave"]["allSticker"]:
                        return line.sendMode(msg, to, sender, cmd, 'Group Leave Sticker has been activated in all groups')
                    groups = line.settings['greet']['leave']['groupSticker']
                    if groups:
                        res = '› L I S T\n'
                        no = 0
                        for group in groups:
                            no += 1
                            group = line.getChats([group], True, False).chats[0]
                            res += '\n{}. {}//{}'.format(no, group.chatName, len(group.extra.groupExtra.memberMids))
                        line.sendMode(msg, to, sender, cmd, res)
                    else:
                        line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                elif textsl.startswith('on'):
                    if line.settings['greet']['leave']['sticker']["STKID"] == 'empty':
                        return line.sendMode(msg, to, sender, cmd, 'Sticker still empty, type \'{}Leave SetSticker\' to add sticker'.format(setKey.title()))
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                        targets = filter_target(sup[1], groups)
                        res = "› A D D E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target not in line.settings['greet']['leave']['groupSticker']:
                                    line.settings['greet']['leave']['groupSticker'].append(target)
                                    res += "\n{}. {} > Added".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Already".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                    elif textsl == 'on':
                        if to not in line.settings['greet']['leave']['groupSticker']:
                            line.settings['greet']['leave']['groupSticker'].append(to)
                        sendToggle(to, "COMMAND LEAVE", "Command Leave Sticker\nGroup: {}\nStatus: ✓".format(gc.chatName), "Type: Sticker\nGroup: {}".format(gc.chatName), True)
                elif textsl.startswith('off'):
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        targets = filter_target(sup[1], line.settings['greet']['leave']['groupSticker'])
                        res = "› D E L E T E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target in line.settings['greet']['leave']['groupSticker']:
                                    line.settings['greet']['leave']['groupSticker'].remove(target)
                                    res += "\n{}. {} > Deleted".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Not Found".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was deleted')
                    elif textsl == 'off':
                        if to in line.settings['greet']['leave']['groupSticker']:
                            line.settings['greet']['leave']['groupSticker'].remove(to)
                        sendToggle(to, "COMMAND LEAVE", "Command Leave Sticker\nGroup: {}\nStatus: ✘".format(gc.chatName), "Type: Sticker\nGroup: {}".format(gc.chatName), False)
                elif textsl == 'all on':
                    if line.settings['greet']['leave']['sticker']["STKID"] == 'empty':
                        return line.sendMode(msg, to, sender, cmd, 'Sticker still empty, type \'{}Leave SetSticker\' to add sticker'.format(setKey.title()))
                    if not line.settings["greet"]["leave"]["allSticker"]:
                        line.settings["greet"]["leave"]["allSticker"] = True
                    sendToggle(to, "COMMAND LEAVE", "Command Leave Sticker\nGroup: All Group\nStatus: ✓", "Type: Sticker\nGroup: All Group", True)
                    line.settings["greet"]["leave"]["groupSticker"].clear()
                elif textsl == 'all off':
                    if line.settings["greet"]["leave"]["allSticker"]:
                        line.settings["greet"]["leave"]["allSticker"] = False
                    sendToggle(to, "COMMAND LEAVE", "Command Leave Sticker\nGroup: All Group\nStatus: ✘", "Type: Sticker\nGroup: All Group", False)
                    line.settings["greet"]["leave"]["groupSticker"].clear()
                        
            elif texttl == 'setsticker':
                if sender == line.profile.mid:
                    line.setts["greets"]["leaveSticker"] = True
                    line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            
            elif texttl.startswith("image "):
                texts = textt[6:]
                textsl = texts.lower()
                if textsl == 'list':
                    if line.settings["greet"]["leave"]["allImage"]:
                        return line.sendMode(msg, to, sender, cmd, 'Group Leave Image has been activated in all groups')
                    groups = line.settings['greet']['leave']['groupImage']
                    if groups:
                        res = '› L I S T\n'
                        no = 0
                        for group in groups:
                            no += 1
                            group = line.getChats([group], True, False).chats[0]
                            res += '\n{}. {}//{}'.format(no, group.chatName, len(group.extra.groupExtra.memberMids))
                        line.sendMode(msg, to, sender, cmd, res)
                    else:
                        line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                elif textsl.startswith('on'):
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                        targets = filter_target(sup[1], groups)
                        res = "› A D D E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target not in line.settings['greet']['leave']['groupImage']:
                                    line.settings['greet']['leave']['groupImage'].append(target)
                                    res += "\n{}. {} > Added".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Already".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                    elif textsl == 'on':
                        if to not in line.settings['greet']['leave']['groupImage']:
                            line.settings['greet']['leave']['groupImage'].append(to)
                        sendToggle(to, "COMMAND LEAVE", "Command Leave Image\nGroup: {}\nStatus: ✓".format(gc.chatName), "Type: Image\nGroup: {}".format(gc.chatName), True)
                elif textsl.startswith('off'):
                    sup = textsl.split(" ")
                    if len(sup) >= 2:
                        targets = filter_target(sup[1], line.settings['greet']['leave']['groupImage'])
                        res = "› D E L E T E D\n"
                        no = 0
                        if targets:
                            for target in targets:
                                no += 1
                                group = line.getChats([target], True, False).chats[0]
                                if target in line.settings['greet']['leave']['groupImage']:
                                    line.settings['greet']['leave']['groupImage'].remove(target)
                                    res += "\n{}. {} > Deleted".format(no, group.chatName)
                                else:
                                    res += "\n{}. {} > Not Found".format(no, group.chatName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was deleted')
                    elif textsl == 'off':
                        if to in line.settings['greet']['leave']['groupImage']:
                            line.settings['greet']['leave']['groupImage'].remove(to)
                        sendToggle(to, "COMMAND LEAVE", "Command Leave Image\nGroup: {}\nStatus: ✘".format(gc.chatName), "Type: Image\nGroup: {}".format(gc.chatName), False)
                elif textsl == 'all on':
                    if not line.settings["greet"]["leave"]["allImage"]:
                        line.settings["greet"]["leave"]["allImage"] = True
                    sendToggle(to, "COMMAND LEAVE", "Command Leave Image\nGroup: All Group\nStatus: ✓", "Type: Image\nGroup: All Group", True)
                    line.settings["greet"]["leave"]["groupImage"].clear()
                elif textsl == 'all off':
                    if line.settings["greet"]["leave"]["allImage"]:
                        line.settings["greet"]["leave"]["allImage"] = False
                    sendToggle(to, "COMMAND LEAVE", "Command Leave Image\nGroup: All Group\nStatus: ✘", "Type: Image\nGroup: All Group", False)
                    line.settings["greet"]["leave"]["groupImage"].clear()
                    
            elif texttl == 'setimage':
                line.setts["greets"]["lImage"] = True
                line.sendMode(msg, to, sender, cmd, 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            
            elif texttl == 'delimage':
                line.setts["greets"]["lImage"] = False
                if line.settings["greet"]["leave"]["imagePath"] is not None:
                    line.deleteFile(line.settings["greet"]["leave"]["imagePath"])
                    line.settings["greet"]["leave"]["imagePath"] = None
                line.sendMode(msg, to, sender, cmd, 'Command Leave Image successfully deleted')
                
        elif cmd == 'notif on':
            line.updateSettingsAttribute(65536, 'false')
            sendToggle(to, "NOTIFIKASI LINE", "Notifications Line\nStatus: ✓", "", True)
        elif cmd == 'notif off':
            line.updateSettingsAttribute(65536, 'true')
            sendToggle(to, "Notifications LINE", "Notifications Line\nStatus: ✘", "", False)
 
        elif cmd.startswith('detectupdate on'):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
            if to not in line.settings['updateProfile']:
                line.settings['updateProfile'].append(to)
            sendToggle(to, "DETECT UPDATE PROFILE", "Detect Update Profile\nStatus: ✓", "Group: {}".format(line.getChats([to], False, False).chats[0].chatName), True)
        elif cmd.startswith('detectupdate off'):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
            if to in line.settings['updateProfile']:
                line.settings['updateProfile'].remove(to)
            sendToggle(to, "DETECT UPDATE PROFILE", "Detect Update Profile\nStatus: ✘", "Group: {}".format(line.getChats([to], False, False).chats[0].chatName), False)
                
        elif cmd.startswith('mimic'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            targets = ''
            if line.settings['mimic']['target']:
                no = 0
                for target, status in line.settings['mimic']['target'].items():
                    no += 1
                    try:
                        name = line.getContact(target).displayName
                    except TalkException:
                        name = 'Unknown'
                    targets += '\n    %i. %s//%s' % (no, name, bool_dict[status][4])
            else:
                targets += '\n    Nothing'
            res = 'Status : ' + bool_dict[line.settings['mimic']['status']][4]
            res += '\nStatus cmd: ' + bool_dict[line.settings['mimic']['cmd']][4]
            res += '\n\n› L I S T\n'
            res += targets
            res += '\n\n› C O M M A N D\n'
            res += '\n• {}Mimic'.format(setKey.title())
            res += '\n• {}Mimic <on/off>'.format(setKey.title())
            res += '\n• {}Mimic cmd <on/off>'.format(setKey.title())
            res += '\n• {}Mimic Reset'.format(setKey.title())
            res += '\n• {}Mimic Add <mention>'.format(setKey.title())
            res += '\n• {}Mimic Del <mention>'.format(setKey.title())
            if cmd == "mimic":
                line.sendMode(msg, to, sender, cmd, res)
            elif texttl == 'on':
                if not line.settings['mimic']['status']:
                    line.settings['mimic']['status'] = True
                sendToggle(to, "MIMIC USER", "Mimic User\nStatus: ✓", "", True)
            elif texttl == 'off':
                if line.settings['mimic']['status']:
                    line.settings['mimic']['status'] = False
                sendToggle(to, "MIMIC USER", "Mimic User\nStatus: ✘", "", False)
            elif texttl == 'reset':
                line.settings['mimic']['target'] = {}
                line.sendMode(msg, to, sender, cmd, 'Target mimic reset successfully')
            elif texttl.startswith('add '):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    parsed_len = len(mentions['MENTIONEES'])//20+1
                    no = 0
                    res = "╭「 Add Mimic 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                            no += 1
                            if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                if mid['M'] not in line.settings['mimic']['target']:
                                    res += '╰ %i. @! > Added\n' % (no)
                                    line.settings['mimic']['target'][mid["M"]] = True
                                else:
                                    res += '╰ %i. @! > Already\n' % (no)
                            else:
                                if mid['M'] not in line.settings['mimic']['target']:
                                    res += '├ %i. @! > Added\n' % (no)
                                    line.settings['mimic']['target'][mid["M"]] = True
                                else:
                                    res += '├ %i. @! > Already\n' % (no)
                            mids.append(mid['M'])
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
            elif texttl.startswith('del '):
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    parsed_len = len(mentions['MENTIONEES'])//20+1
                    no = 0
                    res = "╭「 Del Mimic 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                            no += 1
                            if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                if mid['M'] in line.settings['mimic']['target']:
                                    res += '╰ %i. @! > Deleted\n' % (no)
                                    del line.settings['mimic']['target'][mid["M"]]
                                else:
                                    res += '╰ %i. @! > Not in list\n' % (no)
                            else:
                                if mid['M'] in line.settings['mimic']['target']:
                                    res += '├ %i. @! > Deleted\n' % (no)
                                    del line.settings['mimic']['target'][mid["M"]]
                                else:
                                    res += '├ %i. @! > Not in list\n' % (no)
                            mids.append(mid['M'])
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
            elif texttl == 'cmd on':
                if not line.settings["mimic"]["cmd"]:
                    line.settings["mimic"]["cmd"] = True
                sendToggle(to, "MIMIC COMMAND", "Mimic Command\nStatus: ✓", "", True)
            elif texttl == 'cmd off':
                if line.settings["mimic"]["cmd"]:
                    line.settings["mimic"]["cmd"] = False
                sendToggle(to, "MIMIC COMMAND", "Mimic Command\nStatus: ✘", "", False)
                    
        elif cmd.startswith('broadcast'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            cond = textt.split(' ')
            if cmd == 'broadcast':
                res = '› T Y P E\n'
                res += '\n1 : Friends'
                res += '\n2 : Groups'
                res += '\n0 : All'
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}Broadcast'.format(setKey.title())
                res += '\n• {}Broadcast Filter'.format(setKey.title())
                res += '\n• {}Broadcast <type> <message>'.format(setKey.title())
                res += '\n• {}Broadcast 1 <amountFriends> <message>'.format(setKey.title())
                res += '\n• {}Broadcast Image <type>'.format(setKey.title())
                res += '\n• {}Broadcast Post <type>'.format(setKey.title())
                res += '\n• {}RBroadcast <amount> <message>'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
            elif cond[0] == 'filter':
                res = 'How it works?'
                res += '\n› To avoid groups from broadcast'
                res += '\n› Num = GroupList'
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}BcFilter List'.format(setKey.title())
                res += '\n• {}BcFilter Add <num>'.format(setKey.title())
                res += '\n• {}BcFilter Del <num>'.format(setKey.title())
                res += "\n\nExample multi add / del\n"
                res += "\n• BcFilter add 1,2,3-6"
                res += "\n• BcFilter del 1,2,3-6"
                line.sendMode(msg, to, sender, cmd, res)
            elif cond[0] == '1':
                if len(cond) < 3:
                    return line.sendMode(msg, to, sender, cmd, 'Broadcast failed, the message does not exist\nExample: Broadcast 1 1500 your_text_here')
                if cond[1].isdigit():
                    total = int(cond[1])
                    if total > 1500:
                        return line.sendMode(msg, to, sender, cmd, 'Broadcast failed, to avoid freeze and banned chat, bc friend max 1500 friends')
                else:
                    return line.sendMode(msg, to, sender, cmd, 'Broadcast failed, enter the number of broadcasts you want\nExample: Broadcast 1 1500 your_text_here')
                res = textt[2+len(cond[1])+1:]
                targets = line.getBcFriend(total)
                contentMetadata = {}
                if 'STICON_OWNERSHIP' in msg.contentMetadata:
                    contentMetadata.update(line.metadataFilter(msg.contentMetadata, len(setKey)+10+len(cond[1])+3, type='emoji'))
                    if "@!" in res:
                        contentMetadata.update(line.metadataFilter(contentMetadata, text=res, type='mention'))
                success = []
                for target in targets:
                    try:
                        line.sendMessage(target, res, contentMetadata)
                        success.append(target)
                    except TalkException:
                        continue
                    time.sleep(0.8)
                line.sendMode(msg, to, sender, cmd, 'Broadcast Friend\nTotal: %i friends' % len(success))
            elif cond[0] == '2':
                if len(cond) < 2:
                    return line.sendMode(msg, to, sender, cmd, 'Broadcast failed, the message does not exist yet')
                res = textt[2:]
                targets = make_list(line.getAllChatMids(True, False).memberChatMids)
                contentMetadata = {}
                if 'STICON_OWNERSHIP' in msg.contentMetadata:
                    contentMetadata.update(line.metadataFilter(msg.contentMetadata, len(setKey)+10+2, type='emoji'))
                    if "@!" in res:
                        contentMetadata.update(line.metadataFilter(contentMetadata, text=res, type='mention'))
                success = []
                for target in targets:
                    if target not in line.settings["bcFilter"]:
                        try:
                            line.sendMessage(target, res, contentMetadata)
                            success.append(target)
                        except TalkException:
                            continue
                        time.sleep(0.8)
                line.sendMode(msg, to, sender, cmd, 'Broadcast Group\nTotal: %i groups' % len(success))
            elif cond[0] == '0':
                if len(cond) < 2:
                    return line.sendMode(msg, to, sender, cmd, 'Broadcast failed, the message doesnot exist yet')
                res = textt[2:]
                targets = make_list(line.getAllChatMids(True, False).memberChatMids) + line.getBcFriend()
                contentMetadata = {}
                if 'STICON_OWNERSHIP' in msg.contentMetadata:
                    contentMetadata.update(line.metadataFilter(msg.contentMetadata, len(setKey)+10+2, type='emoji'))
                    if "@!" in res:
                        contentMetadata.update(line.metadataFilter(contentMetadata, text=res, type='mention'))
                success = []
                for target in targets:
                    if target not in line.settings["bcFilter"]:
                        try:
                            line.sendMessage(target, res, contentMetadata)
                            success.append(target)
                        except TalkException:
                            continue
                        time.sleep(0.8)
                line.sendMode(msg, to, sender, cmd, 'Broadcast Friend and Group\nTotal: %i' % len(success))
            elif cond[0] == 'image':
                if cond[1] == '1':
                    line.setts["bcImage"]["toFriend"] = True
                    res = 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                    sendToggle(to, "BROADCAST IMAGE", res, res, True)
                elif cond[1] == '2':
                    line.setts["bcImage"]["toGroup"] = True
                    res = 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                    sendToggle(to, "BROADCAST IMAGE", res, res, True)
                elif cond[1] == '0':
                    line.setts["bcImage"]["toAll"] = True
                    res = 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                    sendToggle(to, "BROADCAST IMAGE", res, res, True)
            elif cond[0] == 'post':
                if cond[1] == '1':
                    if line.settings['checkPost']:
                        return line.sendFooter(to, "To avoid spam, please deactivate first\n1. Checkpost Off\n2. VideoTL Off", reply=True)
                    if line.settings['videotl']:
                        return line.sendFooter(to, "To avoid spam, please deactivate first\n1. Checkpost Off\n2. VideoTL Off", reply=True)
                    line.setts["bcPost"]["toFriend"] = True
                    res = 'Send the post...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                    sendToggle(to, "BROADCAST POST", res, res, True)
                elif cond[1] == '2':
                    if line.settings['checkPost']:
                        return line.sendFooter(to, "To avoid spam, please deactivate first\n1. Checkpost Off\n2. VideoTL Off", reply=True)
                    if line.settings['videotl']:
                        return line.sendFooter(to, "To avoid spam, please deactivate first\n1. Checkpost Off\n2. VideoTL Off", reply=True)
                    line.setts["bcPost"]["toGroup"] = True
                    res = 'Send the post...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                    sendToggle(to, "BROADCAST POST", res, res, True)
                elif cond[1] == '0':
                    if line.settings['checkPost']:
                        return line.sendFooter(to, "To avoid spam, please deactivate first\n1. Checkpost Off\n2. VideoTL Off", reply=True)
                    if line.settings['videotl']:
                        return line.sendFooter(to, "To avoid spam, please deactivate first\n1. Checkpost Off\n2. VideoTL Off", reply=True)
                    line.setts["bcPost"]["toAll"] = True
                    res = 'Send the post...\ntype `{key}Abort` to cancel this'.format(key=setKey.title())
                    sendToggle(to, "BROADCAST POST", res, res, True)
        
        elif cmd.startswith('rbroadcast '):
            textt = removeCmd(text, setKey)
            num = textt.split(" ")[0]
            textbc = textt.replace(num + " ","")
            if num.isdigit():
                groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                targets = random.sample(groups, int(num))
                contentMetadata = {}
                if 'STICON_OWNERSHIP' in msg.contentMetadata:
                    contentMetadata.update(line.metadataFilter(msg.contentMetadata, len(setKey)+11+len(num)+1, type='emoji'))
                    if "@!" in textbc:
                        contentMetadata.update(line.metadataFilter(contentMetadata, text=textbc, type='mention'))
                success = []
                for target in targets:
                    if target not in line.settings["bcFilter"]:
                        try:
                            line.sendMessage(target, textbc, contentMetadata)
                            success.append(target)
                        except TalkException:
                            continue
                        time.sleep(0.8)
                line.sendMode(msg, to, sender, cmd, 'Broadcast Random Group\nTotal: %i groups' % len(success))
        
        elif cmd.startswith('bcfilter '):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            if texttl == 'list':
                groups = line.settings["bcFilter"]
                if groups:
                    res = '› L I S T'
                    no = 0
                    for group in groups:
                        no += 1
                        group = line.getChats([group], True, False).chats[0]
                        res += '\n{}. {}//{}'.format(no, group.chatName, len(group.extra.groupExtra.memberMids))
                    line.sendMode(msg, to, sender, cmd, res)
                else:
                    line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
            elif texttl.startswith('add '):
                sep = textt.split(' ')
                if len(sep) == 2:
                    groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                    targets = filter_target(sep[1], groups)
                    res = "› A D D E D\n"
                    no = 0
                    if targets:
                        for target in targets:
                            no += 1
                            group = line.getChats([target], True, False).chats[0]
                            if target not in line.settings["bcFilter"]:
                                line.settings["bcFilter"].append(target)
                                res += "\n{}. {} > Added".format(no, group.chatName)
                            else:
                                res += "\n{}. {} > Already".format(no, group.chatName)
                        line.sendMode(msg, to, sender, cmd, res)
                    else:
                        line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
            elif texttl.startswith('del '):
                sep = textt.split(' ')
                if len(sep) == 2:
                    targets = filter_target(sep[1], line.settings["bcFilter"])
                    res = "› D E L E T E D\n"
                    no = 0
                    if targets:
                        for target in targets:
                            no += 1
                            group = line.getChats([target], True, False).chats[0]
                            if target in line.settings["bcFilter"]:
                                line.settings["bcFilter"].remove(target)
                                res += "\n{}. {} > Deleted".format(no, group.chatName)
                            else:
                                res += "\n{}. {} > Not Found".format(no, group.chatName)
                        line.sendMode(msg, to, sender, cmd, res)
                    else:
                        line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')

        elif cmd == 'friendlist':
            friends = line.getAllContactIds()
            res = "› F R I E N D S\n"
            if friends:
                no = 0
                if len(friends) > 200:
                    parsed_len = len(friends)//200+1
                    for point in range(parsed_len):
                        for mid in friends[point*200:(point+1)*200]:
                            no += 1
                            try:
                                profile = line.getContact(mid)
                            except:
                                line.deleteContact(mid)
                                continue
                            displayNameOverridden = ""
                            if profile.displayNameOverridden:
                                displayNameOverridden = "//{}".format(profile.displayNameOverridden)
                            res += "\n%i. %s%s" % (no, profile.displayName, displayNameOverridden)
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendMode(msg, to, sender, cmd, res)
                            time.sleep(0.5)
                        res = ''
                else:
                    for mid in friends:
                        no += 1
                        try:
                            profile = line.getContact(mid)
                        except:
                            line.deleteContact(mid)
                            continue
                        displayNameOverridden = ""
                        if profile.displayNameOverridden:
                            displayNameOverridden = "//{}".format(profile.displayNameOverridden)
                        res += "\n%i. %s%s" % (no, profile.displayName, displayNameOverridden)
                    line.sendMode(msg, to, sender, cmd, res)
            else:
                line.sendMode(msg, to, sender, cmd, 'Nothing')
        
        elif cmd == 'friends':
            isi = ["Friendlist", "Friends Add @Mention/Reply", "Friends Del @Mention/Contact/Reply/<num>/mid", "Friends Rename @Mention <text>", "Friends Rename <text>"]
            res = looping_command(setKey.title(), "› C O M M A N D", isi)
            res += "\n\nNum = Friendlist"
            res += "\nYou can multiple delete friends, Type `Friends Del 1,2,3-5`"
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith('friends add'):
            friends = line.getAllContactIds()
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                parsed_len = len(mentions['MENTIONEES'])//20+1
                no = 0
                res = "╭「 Add Friends 」\n"
                for point in range(parsed_len):
                    mids = []
                    for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                        no += 1
                        if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                            if mid['M'] not in friends:
                                res += '╰ %i. @! > Added\n' % (no)
                                line.findAndAddContactsByMid(mid['M'])
                                time.sleep(0.8)
                            else:
                                res += '╰ %i. @! > Already\n' % (no)
                        else:
                            if mid['M'] not in friends:
                                res += '├ %i. @! > Added\n' % (no)
                                line.findAndAddContactsByMid(mid['M'])
                                time.sleep(0.8)
                            else:
                                res += '├ %i. @! > Already\n' % (no)
                        mids.append(mid['M'])
                    if mids:
                        if res.endswith('\n'): res = res[:-1]
                        if point != 0:
                            line.sendMention(to, res, mids)
                        else:
                            line.sendReplyMention(to, res, mids, msgIds=msg_id)
                        res = ""
            elif msg.relatedMessageId:
                data = line.getReplyMessage(to, msg.relatedMessageId)
                if data is not None:
                    res = "╭「 Add Friends 」\n"
                    if data._from not in friends:
                        res += "╰ @! > Added"
                        line.findAndAddContactsByMid(data._from)
                    else:
                        res += "╰ @! > Already"
                    line.sendMention(to, res, [data._from])
            else:
                line.sendMode(msg, to, sender, cmd, 'You can reply to the message or type `friends add @Mention`')
        
        elif cmd.startswith('friends del'):
            friends = line.getAllContactIds()
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                parsed_len = len(mentions['MENTIONEES'])//20+1
                no = 0
                res = "╭「 Del Friends 」\n"
                for point in range(parsed_len):
                    mids = []
                    for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                        no += 1
                        if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                            if mid['M'] in friends:
                                res += '╰ %i. @! > Deleted\n' % (no)
                                line.deleteContact(mid['M'])
                                time.sleep(0.8)
                            else:
                                res += '╰ %i. @! > Not in list\n' % (no)
                        else:
                            if mid['M'] in friends:
                                res += '├ %i. @! > Deleted\n' % (no)
                                line.deleteContact(mid['M'])
                                time.sleep(0.8)
                            else:
                                res += '├ %i. @! > Not in list\n' % (no)
                        mids.append(mid['M'])
                    if mids:
                        if res.endswith('\n'): res = res[:-1]
                        if point != 0:
                            line.sendMention(to, res, mids)
                        else:
                            line.sendReplyMention(to, res, mids, msgIds=msg_id)
                        res = ""
            elif len(sep) == 2:
                if sep[1].lower() == 'contact':
                    line.setts["delCon"] = True
                    res = "Send the contact...\ntype `{key}Abort` to cancel this".format(key=setKey.title())
                    sendToggle(to, "DELETE CONTACT", res, res, True)
                    return
                elif line.server.MID_REGEX.findall(sep[1]):
                    for midd in line.server.MID_REGEX.findall(sep[1]):
                        if midd in friends:
                            line.deleteContact(midd)
                        line.sendMention(to, 'Delete user from mid\nUser: @!', [midd])
                        return
                targets = filter_target(sep[1], friends)
                if targets:
                    parsed_len = len(targets)//20+1
                    no = 0
                    res = "╭「 Del Friends 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in targets[point*20:(point+1)*20]:
                            no += 1
                            if mid == targets[-1]:
                                if mid in friends:
                                    res += '╰ %i. @! > Deleted\n' % (no)
                                    line.deleteContact(mid)
                                    time.sleep(0.8)
                                else:
                                    res += '╰ %i. @! > Not in list\n' % (no)
                            else:
                                if mid in friends:
                                    res += '├ %i. @! > Deleted\n' % (no)
                                    line.deleteContact(mid)
                                    time.sleep(0.8)
                                else:
                                    res += '├ %i. @! > Not in list\n' % (no)
                            mids.append(mid)
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
            elif msg.relatedMessageId:
                data = line.getReplyMessage(to, msg.relatedMessageId)
                if data is not None:
                    res = "╭「 Del Friends 」\n"
                    if data._from in friends:
                        res += "╰ @! > Deleted"
                        line.deleteContact(data._from)
                    else:
                        res += "╰ @! > Not in list"
                    line.sendMention(to, res, [data._from])
            else:
                line.sendMode(msg, to, sender, cmd, 'You can reply to the message or type `friends del @Mention`, if using a number you can type `friends del 1,2,3-5`')
        
        elif cmd.startswith('friends rename '):
            textt = removeCmd(text, setKey)
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    profile = line.getContact(mention['M'])
                    name = text.split('@'+str(profile.displayName)+' ')
                    if len(name) == 2:
                        if mention['M'] not in line.getAllContactIds():
                            line.findAndAddContactsByMid(mention['M'])
                            time.sleep(0.8)
                        line.renameContact(mention['M'], name[1])
                        line.sendMode(msg, to, sender, cmd, 'Successfully renamed user `{}` Becomes `{}`'.format(profile.displayName, name[1]))
            elif msg.relatedMessageId:
                data = line.getReplyMessage(to, msg.relatedMessageId)
                if data is not None:
                    profile = line.getContact(data._from)
                    sep = textt.split(" ")
                    name = textt.replace(sep[0] + " ", "")
                    if data._from not in line.getAllContactIds():
                        line.findAndAddContactsByMid(data._from)
                        time.sleep(0.8)
                    line.renameContact(data._from, name)
                    line.sendMode(msg, to, sender, cmd, 'Successfully renamed user `{}` Becomes `{}`'.format(profile.displayName, name))
            else:
                line.sendMode(msg, to, sender, cmd, 'You can reply to the message or type `friends rename @Mention New_Name`')
                
        elif cmd == 'blocklist':
            friends = line.getBlockedContactIds()
            res = "› B L O C K S\n"
            if friends:
                no = 0
                if len(friends) > 200:
                    parsed_len = len(friends)//200+1
                    for point in range(parsed_len):
                        for mid in friends[point*200:(point+1)*200]:
                            no += 1
                            try:
                                profile = line.getContact(mid)
                            except:
                                line.deleteContact(mid)
                                continue
                            displayNameOverridden = ""
                            if profile.displayNameOverridden:
                                displayNameOverridden = "//{}".format(profile.displayNameOverridden)
                            res += "\n%i. %s%s" % (no, profile.displayName, displayNameOverridden)
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendMode(msg, to, sender, cmd, res)
                            time.sleep(0.5)
                        res = ''
                else:
                    for mid in friends:
                        no += 1
                        try:
                            profile = line.getContact(mid)
                        except:
                            line.deleteContact(mid)
                            continue
                        displayNameOverridden = ""
                        if profile.displayNameOverridden:
                            displayNameOverridden = "//{}".format(profile.displayNameOverridden)
                        res += "\n%i. %s%s" % (no, profile.displayName, displayNameOverridden)
                    line.sendMode(msg, to, sender, cmd, res)
            else:
                line.sendMode(msg, to, sender, cmd, 'Nothing')
        
        elif cmd == 'blocks':
            isi = ["Blocklist", "Blocks Add @Mention/Reply", "Blocks Del @Mention/Reply/<num>"]
            res = looping_command(setKey.title(), "› B L O C K S", isi)
            res += "\n\nNum = Blocklist"
            res += "\nYou can multiple delete blocked user, Type `Blocks Del 1,2,3-5`"
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith('blocks add'):
            friends = line.getBlockedContactIds()
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                parsed_len = len(mentions['MENTIONEES'])//20+1
                no = 0
                res = "╭「 Block User 」\n"
                for point in range(parsed_len):
                    mids = []
                    for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                        no += 1
                        if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                            if mid['M'] not in friends:
                                res += '╰ %i. @! > Added\n' % (no)
                                line.blockContact(mid['M'])
                                time.sleep(0.8)
                            else:
                                res += '╰ %i. @! > Already\n' % (no)
                        else:
                            if mid['M'] not in friends:
                                res += '├ %i. @! > Added\n' % (no)
                                line.blockContact(mid['M'])
                                time.sleep(0.8)
                            else:
                                res += '├ %i. @! > Already\n' % (no)
                        mids.append(mid['M'])
                    if mids:
                        if res.endswith('\n'): res = res[:-1]
                        if point != 0:
                            line.sendMention(to, res, mids)
                        else:
                            line.sendReplyMention(to, res, mids, msgIds=msg_id)
                        res = ""
            elif msg.relatedMessageId:
                data = line.getReplyMessage(to, msg.relatedMessageId)
                if data is not None:
                    res = "╭「 Block User 」\n"
                    if data._from not in friends:
                        res += "╰ @! > Added"
                        line.blockContact(data._from)
                    else:
                        res += "╰ @! > Already"
                    line.sendMention(to, res, [data._from])
            else:
                line.sendMode(msg, to, sender, cmd, 'You can reply to the message or type `blocks add @Mention`')
        
        elif cmd.startswith('blocks del'):
            friends = line.getBlockedContactIds()
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                parsed_len = len(mentions['MENTIONEES'])//20+1
                no = 0
                res = "╭「 Del Block 」\n"
                for point in range(parsed_len):
                    mids = []
                    for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                        no += 1
                        if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                            if mid['M'] in friends:
                                res += '╰ %i. @! > Deleted\n' % (no)
                                line.unblockContact(mid['M'])
                                time.sleep(0.8)
                            else:
                                res += '╰ %i. @! > Not in list\n' % (no)
                        else:
                            if mid['M'] in friends:
                                res += '├ %i. @! > Deleted\n' % (no)
                                line.unblockContact(mid['M'])
                                time.sleep(0.8)
                            else:
                                res += '├ %i. @! > Not in list\n' % (no)
                        mids.append(mid['M'])
                    if mids:
                        if res.endswith('\n'): res = res[:-1]
                        if point != 0:
                            line.sendMention(to, res, mids)
                        else:
                            line.sendReplyMention(to, res, mids, msgIds=msg_id)
                        res = ""
            elif len(sep) == 2:
                targets = filter_target(sep[1], friends)
                if targets:
                    parsed_len = len(targets)//20+1
                    no = 0
                    res = "╭「 Del Block 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in targets[point*20:(point+1)*20]:
                            no += 1
                            if mid == targets[-1]:
                                if mid in friends:
                                    res += '╰ %i. @! > Deleted\n' % (no)
                                    line.unblockContact(mid)
                                    time.sleep(0.8)
                                else:
                                    res += '╰ %i. @! > Not in list\n' % (no)
                            else:
                                if mid in friends:
                                    res += '├ %i. @! > Deleted\n' % (no)
                                    line.unblockContact(mid)
                                    time.sleep(0.8)
                                else:
                                    res += '├ %i. @! > Not in list\n' % (no)
                            mids.append(mid)
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
            elif msg.relatedMessageId:
                data = line.getReplyMessage(to, msg.relatedMessageId)
                if data is not None:
                    res = "╭「 Del Block 」\n"
                    if data._from in friends:
                        res += "╰ @! > Deleted"
                        line.unblockContact(data._from)
                    else:
                        res += "╰ @! > Not in list"
                    line.sendMention(to, res, [data._from])
            else:
                line.sendMode(msg, to, sender, cmd, 'You can reply to the message or type `blocks del @Mention`, if using a number you can type `blocks del 1,2,3-5`')
        
        elif cmd.startswith("setfaketag "):
            set = removeCmd(text, setKey)
            if set.lower() == 'sticker':
                if sender == line.profile.mid:
                    line.settings["setcommand"]["fakeTagSticker"]["status"] = True
                    line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            elif set.lower() == 'delsticker':
                line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKID"] = "180"
                line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKPKGID"] = "3"
                line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKVER"] = "100"
                line.sendMode(msg, to, sender, cmd, 'Fake Tag Sticker successfully deleted')
            else:
                line.settings["setcommand"]["faketag"] = set
                line.sendMode(msg, to, sender, cmd, 'Command fake mention successfully changed to "{}"'.format(set))

        elif cmd == line.settings["setcommand"]["faketag"].lower():
            if msg.toType == 1:
                room = line.getCompactRoom(to)
                members = [mem.mid for mem in room.contacts]
            elif msg.toType == 2:
                members = make_list(line.getChats([to], True, False).chats[0].extra.groupExtra.memberMids)
            else:
                return line.sendFooter(to, 'Use this command only for the room or group chat!')
            if members:
                line.fakeMentionSticker(to, int(line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKVER"]), int(line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKPKGID"]), int(line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKID"]), members)
        
        elif cmd.startswith('rfaketag '):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                group = line.getChats([gids[int(num)-1]], True, False).chats[0]
                members = [mem for mem in group.extra.groupExtra.memberMids]
                if members:
                    line.fakeMentionSticker(group.chatMid, int(line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKVER"]), int(line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKPKGID"]), int(line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKID"]), members)
                    line.sendMode(msg, to, sender, cmd, 'Remote Fake Tag\nto : %s' % group.chatName)

        elif cmd.startswith('mentionall '):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                group = line.getChats([gids[int(num)-1]], True, False).chats[0]
                members = [mem for mem in group.extra.groupExtra.memberMids]
                if members:
                    if line.settings["setcommand"]["mentionAllEmoji"]["productId"] is not None:
                        line.mentionMembersEmoticon(group.chatMid, line.settings["setcommand"]["mentionAllEmoji"]["productId"], members)
                    else:
                        line.mentionMembers(group.chatMid, members)
                    line.sendMode(msg, to, sender, cmd, 'Remote Mentionall\nto : %s' % group.chatName)
                
        elif cmd == line.settings["setcommand"]["mentionall"].lower():
            members = []
            if msg.toType == 1:
                room = line.getCompactRoom(to)
                members = [mem.mid for mem in room.contacts]
            elif msg.toType == 2:
                group = line.getChats([to], True, False)
                members = [mem for mem in group.chats[0].extra.groupExtra.memberMids]
            else:
                return line.sendFooter(to, 'Use this command only for the room or group chat!')
            if members:
                if line.settings["setcommand"]["mentionAllEmoji"]["productId"] is not None:
                    line.mentionMembersEmoticon(to, line.settings["setcommand"]["mentionAllEmoji"]["productId"], members, msgIds=msg_id)
                else:
                    line.mentionMembers(to, members, msgIds=msg_id)
                
        elif cmd.startswith("setmentionall "):
            set = removeCmd(text, setKey)
            if set.lower() == 'sticker':
                if sender == line.profile.mid:
                    line.settings["setcommand"]["mentionStiker"]["status"] = True
                    line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            elif set.lower() == 'delsticker':
                line.settings["setcommand"]["mentionStiker"]["stkid"] = ""
                line.sendMode(msg, to, sender, cmd, 'Mentionall Sticker successfully deleted')
            else:
                line.settings["setcommand"]["mentionall"] = set
                line.sendMode(msg, to, sender, cmd, 'Command mentionall successfully changed to "{}"'.format(set))
        
        elif cmd.startswith("setmentionemoji "):
            set = removeCmd(text, setKey)
            if 'STICON_OWNERSHIP' in msg.contentMetadata:
                if sender == line.profile.mid:
                    if len(eval(msg.contentMetadata['STICON_OWNERSHIP'])) == 1:
                        productId = eval(msg.contentMetadata['STICON_OWNERSHIP'])[0]
                        line.settings["setcommand"]["mentionAllEmoji"]["productId"] = productId
                        line.sendMode(msg, to, sender, "(emoji)", 'Set Mention Emoji\nStatus: ✓')
            elif 'EMTVER' in msg.contentMetadata:
                if msg.contentMetadata["EMTVER"] == '4':
                    for unic in line.setts["emoteFree"]:
                        if unic in text:
                            line.settings["setcommand"]["mentionAllEmoji"]["productId"] = line.setts["emoteFree"][unic]
                            line.sendMode(msg, to, sender, "(emoji)", 'Set Mention Emoji\nStatus: ✓')
            elif set.lower() == 'delemoji':
                line.settings["setcommand"]["mentionAllEmoji"]["productId"] = None
                line.sendMode(msg, to, sender, cmd, 'Mention All Emoji successfully deleted')
        
        elif cmd.startswith('call '):
            textt = removeCmd(text, setKey)
            sep = textt.split(" ")
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in deep group!!')
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                target = []
                for mention in mentions['MENTIONEES']:
                    target.append(mention['M'])
                if sep[-1].isdigit():
                    num = int(sep[-1])
                    group = line.getChats([to], True, False).chats[0]
                    parsed_len = num//15+1
                    amount = 0
                    line.acquireGroupCallRoute(to)
                    for point in range(parsed_len):
                        for var in range(0, 15):
                            if amount == num: break
                            else: amount += 1
                            try:
                                line.inviteIntoGroupCall(to, contactIds=target)
                            except:
                                return line.sendMode(msg, to, sender, cmd, 'Free Call Target Error\nCode: 20\nOnly {} successful calls'.format(amount))
                        time.sleep(1)
                    line.sendMode(msg, to, sender, cmd, 'Free Call Target\nTotal: {}\nStatus: ✓'.format(amount))

        elif cmd.startswith("rcallgroup "):
            sep = removeCmd(text, setKey)
            num = sep.split(" ")
            if len(num) == 2:
                if num[0].isdigit() and num[1].isdigit():
                    gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                    gid = gids[int(num[0])-1]
                    num = int(num[1])
                    group = line.getChats([gid], True, False).chats[0]
                    mids = make_list(group.extra.groupExtra.memberMids)
                    if line.profile.mid in mids: mids.remove(line.profile.mid)
                    parsed_len = num//15+1
                    amount = 0
                    line.acquireGroupCallRoute(gid)
                    for point in range(parsed_len):
                        for var in range(0, 15):
                            if amount == num: break
                            else: amount += 1
                            try:
                                line.inviteIntoGroupCall(gid, contactIds=mids)
                            except:
                                return line.sendMode(msg, to, sender, cmd, 'Remote Call Group Error\nCode: 20\nOnly {} successful calls at {}'.format(amount, group.chatName))
                        time.sleep(1)
                    line.sendMode(msg, to, sender, cmd, 'Remote Call Group\nTotal: {}\nGroup: {}\nStatus: ✓'.format(amount, group.chatName))
                    
        elif cmd.startswith('callgroup '):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            strnum = removeCmd(text, setKey)
            if strnum.isdigit():
                num = int(strnum)
                group = line.getChats([to], True, False).chats[0]
                mids = make_list(group.extra.groupExtra.memberMids)
                if line.profile.mid in mids: mids.remove(line.profile.mid)
                parsed_len = num//15+1
                amount = 0
                line.acquireGroupCallRoute(to)
                for point in range(parsed_len):
                    for var in range(0, 15):
                        if amount == num: break
                        else: amount += 1
                        try:
                            line.inviteIntoGroupCall(to, contactIds=mids)
                        except:
                            return line.sendMode(msg, to, sender, cmd, 'Free Call Group Error\nCode: 20\nOnly {} successful calls'.format(amount))
                    time.sleep(1)
                line.sendMode(msg, to, sender, cmd, 'Free Call Group\nTotal: {}\nStatus: ✓'.format(amount))
            
        elif cmd == 'groupinfo':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            group = line.getChats([to], True, True).chats[0]
            try:
                ccreator = group.extra.groupExtra.creator
                gcreator = line.getContact(ccreator).displayName
            except:
                ccreator = None
                gcreator = 'Not found'
            if len(group.extra.groupExtra.inviteeMids) == 0:
                pendings = 0
            else:
                pendings = len(group.extra.groupExtra.inviteeMids)
            qr = 'Close' if group.extra.groupExtra.preventedJoinByTicket else 'Open'
            if group.extra.groupExtra.preventedJoinByTicket:
                ticket = 'Not found'
            else:
                ticket = 'https://line.me/R/ti/g/' + str(line.reissueChatTicket(to).ticketId)
            created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
            path = 'https://obs.line-scdn.net' + group.picturePath
            res = "› I N F O\n"
            res += '\n• ID: ' + group.chatMid
            res += '\n• Name: ' + group.chatName
            res += '\n• Creator: ' + gcreator
            res += '\n• Created Time: ' + created
            res += '\n• Member Count: ' + str(len(group.extra.groupExtra.memberMids))
            res += '\n• Pending Count: ' + str(pendings)
            res += '\n• QR Status: ' + qr
            res += '\n• Ticket: ' + ticket
            line.sendLiffImage(to, path, line.settings["setFlag"]["icon"], " Group Picutre")
            if ccreator:
                line.sendContact(to, ccreator)
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith('groupcontact '):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                group = line.getChats([gids[int(num)-1]], True, False).chats[0]
                for mid in group.extra.groupExtra.memberMids:
                    line.sendContact(to, mid)
            
        elif cmd.startswith('groupmem '):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                group = line.getChats([gids[int(num)-1]], True, False).chats[0]
                mids = [a for a in group.extra.groupExtra.memberMids]
                if line.profile.mid in mids: mids.remove(line.profile.mid)
                parsed_len = len(mids)//20+1
                result = '𝗠𝗲𝗺𝗯𝗲𝗿𝗹𝗶𝘀𝘁\n'
                for point in range(parsed_len):
                    target = []
                    for mid in mids[point*20:(point+1)*20]:
                        result += '➡️ › @!\n'
                        if mid == mids[-1]:
                            result += '𝗧𝗼𝘁𝗮𝗹: %i 𝗠𝗲𝗺𝗯𝗲𝗿𝘀' % len(mids)
                            result += '\n𝗚𝗿𝗼𝘂𝗽: {}'.format(group.chatName)
                        target.append(mid)
                    if target:
                        if result.endswith('\n'): result = result[:-1]
                        if point == 0:
                            line.sendReplyMention(to, result, target)
                        else:
                            line.sendMention(to, result, target)
                    result = ''
        
        elif cmd.startswith('grouppend '):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                group = line.getChats([gids[int(num)-1]], False, True).chats[0]
                mids = [a for a in group.extra.groupExtra.inviteeMids]
                if not mids:
                    return line.sendFooter(to, 'Empty pending')
                if line.profile.mid in mids: mids.remove(line.profile.mid)
                parsed_len = len(mids)//20+1
                result = '𝗣𝗲𝗻𝗱𝗶𝗻𝗴𝗹𝗶𝘀𝘁\n'
                for point in range(parsed_len):
                    target = []
                    for mid in mids[point*20:(point+1)*20]:
                        result += '➡️ › @!\n'
                        if mid == mids[-1]:
                            result += '𝗧𝗼𝘁𝗮𝗹: %i 𝗠𝗲𝗺𝗯𝗲𝗿𝘀' % len(mids)
                            result += '\n𝗚𝗿𝗼𝘂𝗽: {}'.format(group.chatName)
                        target.append(mid)
                    if target:
                        if result.endswith('\n'): result = result[:-1]
                        if point == 0:
                            line.sendReplyMention(to, result, target)
                        else:
                            line.sendMention(to, result, target)
                    result = ''
            
        elif cmd.startswith('groupinfo '):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                group = line.getChats([gids[int(num)-1]], True, False).chats[0]
                try:
                    ccreator = group.extra.groupExtra.creator
                    gcreator = line.getContact(ccreator).displayName
                except:
                    ccreator = None
                    gcreator = 'Not found'
                if len(group.extra.groupExtra.inviteeMids) == 0:
                    pendings = 0
                else:
                    pendings = len(group.extra.groupExtra.inviteeMids)
                qr = 'Close' if group.extra.groupExtra.preventedJoinByTicket else 'Open'
                if group.extra.groupExtra.preventedJoinByTicket:
                    ticket = 'Not found'
                else:
                    ticket = 'https://line.me/R/ti/g/' + str(line.reissueChatTicket(gids[int(num)-1]).ticketId)
                created = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(group.createdTime) / 1000))
                path = 'https://obs.line-scdn.net' + group.picturePath
                res = "› I N F O\n"
                res += '\n• ID: ' + group.chatMid
                res += '\n• Name: ' + group.chatName
                res += '\n• Creator: ' + gcreator
                res += '\n• Created Time: ' + created
                res += '\n• Member Count: ' + str(len(group.extra.groupExtra.memberMids))
                res += '\n• Pending Count: ' + str(pendings)
                res += '\n• QR Status: ' + qr
                res += '\n• Ticket: ' + ticket
                line.sendLiffImage(to, path, line.settings["setFlag"]["icon"], " Group Picutre")
                if ccreator:
                    line.sendContact(to, ccreator)
                line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd == 'grouplist':
            gids = make_list(line.getAllChatMids(True, False).memberChatMids)
            res = "› L I S T\n"
            if gids:
                no = 0
                if len(gids) > 200:
                    parsed_len = len(gids)//200+1
                    for point in range(parsed_len):
                        for gid in gids[point*200:(point+1)*200]:
                            no += 1
                            group = line.getChats([gid], True, False).chats[0]
                            res += "\n%i. %s//%i" % (no, group.chatName, len(group.extra.groupExtra.memberMids))
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            line.sendMode(msg, to, sender, cmd, res)
                        if point != parsed_len - 1:
                            res = ''
                else:
                    for gid in gids:
                        group = line.getChats([gid], True, False).chats[0]
                        no += 1
                        res += "\n%i. %s//%i" % (no, group.chatName, len(group.extra.groupExtra.memberMids))
                    line.sendMode(msg, to, sender, cmd, res)
            else:
                line.sendMode(msg, to, sender, cmd, 'Nothing')
                    
        elif cmd.startswith('invitationlist'):
            textt = removeCmd(text, setKey)
            texttl = textt.lower()
            gids = make_list(line.getAllChatMids(False, True).invitedChatMids)
            gnames = []
            ress = []
            res = "› L I S T\n"
            if gids:
                no = 0
                if len(gids) > 200:
                    parsed_len = len(gids)//200+1
                    for point in range(parsed_len):
                        for gid in gids[point*200:(point+1)*200]:
                            no += 1
                            group = line.getChats([gid], True, False).chats[0]
                            if group.chatMid == gids[point*200]:
                                res += "\n%i. %s//%i" % (no, group.chatName, len(group.extra.groupExtra.memberMids))
                            else:
                                res += "\n%i. %s//%i" % (no, group.chatName, len(group.extra.groupExtra.memberMids))
                        if res:
                            if res.startswith('\n'): res = res[1:]
                            if point != parsed_len - 1:
                                ress.append(res)
                        if point != parsed_len - 1:
                            res = ''
                else:
                    for gid in gids:
                        group = line.getChats([gid], True, False).chats[0]
                        no += 1
                        if group.chatMid == gids[0]:
                            res += "\n%i. %s//%i" % (no, group.chatName, len(group.extra.groupExtra.memberMids))
                        else:
                            res += "\n%i. %s//%i" % (no, group.chatName, len(group.extra.groupExtra.memberMids))
                        gnames.append(group.chatName)
            else:
                res += '\n    Nothing'
            res += '\n\n› C O M M A N D\n'
            res += '\n• {}InvitationList'.format(setKey.title())
            res += '\n• {}InvitationList Accept <num/all>'.format(setKey.title())
            res += '\n• {}InvitationList Reject <num/all>'.format(setKey.title())
            ress.append(res)
            if cmd == 'invitationlist':
                for res in ress:
                    line.sendMode(msg, to, sender, cmd, res)
            elif texttl.startswith('accept '):
                texts = textt[7:].split(', ')
                accepted = []
                if not gids:
                    return line.sendFooter(to, 'There is no invite list to the group')
                for texxt in texts:
                    num = None
                    name = None
                    try:
                        num = int(texxt)
                    except ValueError:
                        name = texxt
                    if num != None:
                        if num <= len(gids) and num > 0:
                            gid = gids[num - 1]
                            group = line.getChats([gid], False, False).chats[0]
                            if group.chatMid in accepted:
                                line.sendMode(msg, to, sender, cmd, 'Already accept group %s' % group.chatName)
                                continue
                            line.acceptChatInvitation(group.chatMid)
                            accepted.append(group.chatMid)
                            line.sendMode(msg, to, cmd, 'Successfully joined the group %s' % group.chatName)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'Group invitation list you under %i' % num)
                    elif name != None:
                        if name.lower() == 'all':
                            for gid in gids:
                                if gid in accepted:
                                    continue
                                line.acceptChatInvitation(gid)
                                accepted.append(gid)
                                time.sleep(0.8)
                            line.sendMode(msg, to, sender, cmd, 'Successfully joined all invitationlist')
            elif texttl.startswith('reject '):
                texts = textt[7:].split(', ')
                rejected = []
                if not gids:
                    return line.sendFooter(to, 'There is no invite list to group')
                for texxt in texts:
                    num = None
                    name = None
                    try:
                        num = int(texxt)
                    except ValueError:
                        name = texxt
                    if num != None:
                        if num <= len(gids) and num > 0:
                            gid = gids[num - 1]
                            group = line.getChats([gid], False, False).chats[0]
                            if group.chatMid in rejected:
                                line.sendMode(msg, to, sender, cmd, 'Already reject group %s' % group.chatName)
                                continue
                            line.rejectChatInvitation(group.chatMid)
                            rejected.append(group.chatMid)
                            line.sendMode(msg, to, sender, cmd, 'Successfully cancel the invite on %s' % group.chatName)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'Group invitation list you under %i' % num)
                    elif name != None:
                        if name.lower() == 'all':
                            for gid in gids:
                                if gid in rejected:
                                    continue
                                line.rejectChatInvitation(gid)
                                rejected.append(gid)
                                time.sleep(0.8)
                            line.sendMode(msg, to, sender, cmd, 'Successfully cancel all invites group')
                    
        elif cmd == 'memberlist':
            if msg.toType == 1:
                room = line.getRoom(to)
                members = room.contacts
            elif msg.toType == 2:
                group = line.getChats([to], True, False).chats[0]
                members = [a for a in group.extra.groupExtra.memberMids]
            else:
                return line.sendFooter(to, 'Use this command only for the room or group chat!')
            if not members:
                return line.sendFooter(to, 'Member empty')
            res = "› M E M B E R S\n"
            parsed_len = len(members)//200+1
            no = 0
            for point in range(parsed_len):
                for member in members[point*200:(point+1)*200]:
                    no += 1
                    profile = line.getContact(member)
                    res += "\n%i. %s" % (no, profile.displayName)
                if res:
                    if res.startswith('\n'): res = res[1:]
                    line.sendMode(msg, to, sender, cmd, res)
                res = ''
                
        elif cmd == 'pendinglist':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            group = line.getChats([to], False, True).chats[0]
            members = [a for a in group.extra.groupExtra.inviteeMids]
            if not members:
                return line.sendFooter(to, 'Empty pending')
            res = "› P E N D I N G S\n"
            parsed_len = len(members)//200+1
            no = 0
            for point in range(parsed_len):
                for member in members[point*200:(point+1)*200]:
                    no += 1
                    try: profile = line.getContact(member)
                    except: continue
                    res += "\n%i. %s" % (no, profile.displayName)
                if res:
                    if res.startswith('\n'): res = res[1:]
                    line.sendMode(msg, to, sender, cmd, res)
                res = ''
                
        elif cmd == 'gid':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            line.sendFooter(to, '%s' % line.getChats([to], False, False).chats[0].chatMid, reply=True)
            
        elif cmd == 'gname':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            line.sendFooter(to, '%s' % line.getChats([to], False, False).chats[0].chatName, reply=True)
            
        elif cmd == 'gpict':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            line.sendLiffImage(to, 'https://obs.line-scdn.net' + line.getChats([to], False, False).chats[0].picturePath, line.settings["setFlag"]["icon"], " Group Picture")
        
        elif cmd == 'gcover':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            line.sendLiffImage(to, line.getProfileCoverURL(to), line.settings["setFlag"]["icon"], " Group Cover")
        
        elif cmd.startswith('gleave '):
            textt = removeCmd(text, setKey)
            gids = make_list(line.getAllChatMids(True, False).memberChatMids)
            targets = filter_target(textt, gids)
            if targets:
                res = "Successfully exited group:\n"
                no = 0
                if len(targets) > 2:
                    line.sendMode(msg, to, sender, cmd, 'Loading....')
                for gid in targets:
                    no += 1
                    group = line.getChats([gid], False, False).chats[0]
                    line.deleteSelfFromChat(gid)
                    res += "\n{}. {}".format(no, group.chatName)
                    time.sleep(0.8)
                line.sendMode(msg, to, sender, cmd, res)

        elif cmd.startswith('gid '):
            num = removeCmd(text, setKey)
            groups = make_list(line.getAllChatMids(True, False).memberChatMids)
            gids = filter_target(num, groups)
            if gids:
                for gid in gids:
                    line.sendMessage(to, '%s' % gid)
                    time.sleep(0.8)
            else:
                line.sendMode(msg, to, sender, cmd, "Nothing")
            
        elif cmd.startswith('gname '):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                gid = gids[int(num)-1]
                group = line.getChats([gid], False, False).chats[0]
                line.sendFooter(to, '%s' % group.chatName, reply=True)
            
        elif cmd.startswith('gpict '):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                gid = gids[int(num)-1]
                group = line.getChats([gid], False, False).chats[0]
                line.sendLiffImage(to, 'https://obs.line-scdn.net' + group.picturePath, line.settings["setFlag"]["icon"], " Group Picture")
        
        elif cmd.startswith('gcover '):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                gid = gids[int(num)-1]
                line.sendLiffImage(to, line.getProfileCoverURL(gid), line.settings["setFlag"]["icon"], " Group Cover")
            
        elif cmd == 'openqr':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            group = line.getChats([to], False, False)
            if group.chats[0].extra.groupExtra.preventedJoinByTicket == True:
                group.chats[0].extra.groupExtra.preventedJoinByTicket = False
                line.updateChat(group.chats[0], 4)
            line.sendFooter(to, 'Qr Group\nhttps://line.me/R/ti/g/{}'.format(str(line.reissueChatTicket(to).ticketId)), reply=True)
            
        elif cmd == 'closeqr':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            group = line.getChats([to], False, False)
            if group.chats[0].extra.groupExtra.preventedJoinByTicket == False:
                group.chats[0].extra.groupExtra.preventedJoinByTicket = True
                line.updateChat(group.chats[0], 4)
            
        elif cmd.startswith("openqr "):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                gid = gids[int(num)-1]
                group = line.getChats([gid], False, False).chats[0]
                if group.extra.groupExtra.preventedJoinByTicket == True:
                    group.extra.groupExtra.preventedJoinByTicket = False
                    line.updateChat(group, 4)
                line.sendFooter(to, 'Qr Group\nName: {}\nhttps://line.me/R/ti/g/{}'.format(group.chatName, str(line.reissueChatTicket(gid).ticketId)), reply=True)
            
        elif cmd.startswith("closeqr "):
            num = removeCmd(text, setKey)
            if num.isdigit():
                gids = make_list(line.getAllChatMids(True, False).memberChatMids)
                gid = gids[int(num)-1]
                group = line.getChats([gid], False, False).chats[0]
                if group.extra.groupExtra.preventedJoinByTicket == False:
                    group.extra.groupExtra.preventedJoinByTicket = True
                    line.updateChat(group, 4)
                line.sendFooter(to, 'Qr Group\nName: {}\nClosed'.format(group.chatName), reply=True)
            
        elif cmd.startswith('changegroupname '):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in deep group!!')
            group = line.getChats([to]).chats[0]
            gname = removeCmd(text, setKey)
            if len(gname) > 999:
                return line.sendMode(msg, to, sender, cmd, 'Failed to change group name, text is too long')
            group.chatName = gname
            line.updateChat(group, 1)
            line.sendMode(msg, to, sender, cmd, 'Successfully renamed group to \'%s\'' % gname)
            
        elif cmd == 'changegrouppict':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in deep group!!')
            if to not in line.settings['changeGroupPicture']:
                line.settings['changeGroupPicture'].append(to)
                line.sendMode(msg, to, sender, cmd, 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            else:
                line.sendMode(msg, to, sender, cmd, 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
                
        elif cmd == 'changegroupcover':
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in deep group!!')
            if to not in line.settings['changeGroupCover']:
                line.settings['changeGroupCover'].append(to)
                line.sendMode(msg, to, sender, cmd, 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            else:
                line.sendMode(msg, to, sender, cmd, 'Send the picture...\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
                
        elif cmd == 'getannounce':
            ann = line.getChatRoomAnnouncements(to)
            res = "› A N N O U N C E M E N T \n"
            if ann:
                for list in ann:
                    try: maker = line.getContact(list.creatorMid).displayName
                    except: maker = "Unknown"
                    res += "\n==> Creator: "+str(maker)
                    res += "\nText: "+str(list.contents.text)
                    res += "\nChat: "+str(list.contents.link)+"\n"
                line.sendFooter(to, res, reply=True)
            else: line.sendMode(msg, to, sender, cmd, 'There are no announcements in this group')
        
        elif cmd == "getcall":
            callGroup = line.getGroupCall(to)
            if callGroup.online:
                target = []
                host = callGroup.hostMids
                participant = callGroup.memberMids
                if host in participant:
                    participant.remove(host)
                if callGroup.mediaType == 1:
                    type = "=> FREE CALL GROUP"
                elif callGroup.mediaType == 2:
                    type = "=> VIDEO CALL GROUP"
                elif callGroup.mediaType == 3:
                    type = "=> LIVE GROUP"
                else:
                    type = "Unknown"
                res = type
                res += "\nHost: @!"
                res += "\nGroup: {}".format(line.getChats([to], False, False).chats[0].chatName)
                res += "\nRuntime: {}".format(humanize.naturaltime(datetime.fromtimestamp(int(callGroup.started)//1000)).title())
                res += "\n\nParticipant:"
                no = 0
                target.append(host)
                if participant:
                    for mem in participant:
                        no += 1
                        res += "\n    {}. @!".format(no)
                        target.append(mem)
                else:
                    res += "\n    Empty"
                line.sendMention(to, res, target)
            else:
                line.sendMode(msg, to, sender, cmd, "Currently no calls group/live")
        
        elif cmd.startswith('searchnote '):
            textt = removeCmd(text, setKey)
            datas = line.searchNote(to, textt)
            res = "› L I S T"
            target = []
            if datas:
                for data in datas:
                    url = 'https://line.me/R/group/home/posts/post?homeId={}&postId={}'.format(data['post']['postInfo']['homeId'], data['post']['postInfo']['postId'])
                    target.append(data['post']['userInfo']['mid'])
                    res += "\n\nCreator: @!"
                    res += "\nLike: {}".format(data['post']['postInfo']['likeCount'])
                    res += "\nComment: {}".format(data['post']['postInfo']['commentCount'])
                    res += "\nUrl: {}".format(url)
                res += "\n\nTotal: {} Note".format(len(datas))
                line.sendMention(to, res, target)
            else:
                line.sendMode(msg, to, sender, cmd, "No notes found with text `{}`".format(textt))
        
        elif cmd.startswith('createtl'):
            if cmd == 'createtl':
                isi = ["Createtl", "Createtl <num> <description>"]
                res = looping_command(setKey.title(), "› C O M M A N D", isi)
                res += "\n\nExample: Createtl 0 this is sozi"
                res += "\n\nNum = Amount of media you want to upload, if num 0, it means making a timeline without media"
                line.sendMode(msg, to, sender, cmd, res)
            elif cmd.startswith('createtl '):
                textt = removeCmd(text, setKey)
                sep = textt.split(" ")
                if len(sep) >= 2:
                    number = int(sep[0])
                    judul = textt.replace(sep[0] + " ","")
                    if number != 0:
                        if to not in line.setts["uploadTL"]:
                            line.setts["uploadTL"][to] = {
                                "total": number,
                                "description": judul,
                                "sender": sender,
                                "media": []
                            }
                        line.sendMode(msg, to, sender, cmd, 'Send {} pictur/Video\ntype `{key}Abort` to cancel this'.format(number, key=setKey.title()))
                    else:
                        post = line.createPost(judul)
                        line.sendPostToTalk(to, post["result"]["feed"]["post"]["postInfo"]["postId"])
                        
        elif cmd.startswith('createnote'):
            if cmd == 'createnote':
                isi = ["CreateNote", "CreateNote <num> <description>"]
                res = looping_command(setKey.title(), "› C O M M A N D", isi)
                res += "\n\nExample: CreateNote 0 this is acode44"
                res += "\n\nNum = Amount of media you want to upload, if num 0, it means making a note without media"
                line.sendMode(msg, to, sender, cmd, res)
            elif cmd.startswith('createnote '):
                textt = removeCmd(text, setKey)
                sep = textt.split(" ")
                if len(sep) >= 2:
                    number = int(sep[0])
                    judul = textt.replace(sep[0] + " ","")
                    if number != 0:
                        if to not in line.setts["uploadNote"]:
                            line.setts["uploadNote"][to] = {
                                "total": number,
                                "description": judul,
                                "sender": sender,
                                "media": []
                            }
                        line.sendMode(msg, to, sender, cmd, 'Send {} Image/Video\nType `{key}Abort` to cancel this'.format(number, key=setKey.title()))
                    else:
                        line.createPostGroup(to, judul)
        
        elif cmd.startswith('getnote'):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            textt = removeCmd(text, setKey)
            if cmd == 'getnote':
                data = line.getGroupPost(to)
                if 'feeds' not in data['result']: return line.sendFooter(to, 'notes is empty.')
                group = line.getChats([to], False, False).chats[0]
                res = f'Group: {group.chatName}'
                parsed_len = len(data['result']['feeds'])//20+1
                no = 0
                for point in range(parsed_len):
                    mids = []
                    for feed in data['result']['feeds'][point*20:(point+1)*20]:
                        no += 1
                        mids.append(feed['post']['userInfo']['writerMid'])
                        res += f'\n\n{no}. Creator: @!'
                        if 'text' in feed["post"]["contents"]: res += f'\nText: {feed["post"]["contents"]["text"][0:20]}'
                        else: res += '\nText: Empty'
                        if 'media' in feed["post"]["contents"]:
                            res += f'\nMedia: {len(feed["post"]["contents"]["media"])}'
                        if feed["post"]["postInfo"]["postId"] == data['result']['feeds'][-1]["post"]["postInfo"]["postId"]:
                            res += f'\n\nTotal Note: {len(data["result"]["feeds"])}'
                            res += f'\nExample:\n• GetNote <num>\n• SearchNote <query>'
                    if res.startswith('\n\n'): res = res[2:len(res)]
                    if mids:
                        line.sendReplyMention(to, res, mids, msgIds=msg_id)
                    res = ''
                    time.sleep(0.8)
            elif textt.isdigit():
                num = int(textt)
                datas = line.getGroupPost(to)
                if num <= len(datas["result"]["feeds"]):
                    data = datas["result"]["feeds"][num - 1]
                    if 'text' in data["post"]["contents"]: res = f'Text: {data["post"]["contents"]["text"]}'
                    else: res = 'Text: Empty'
                    res += "\n\nCreator: @!"
                    if 'media' in data["post"]["contents"]:
                        res += f'\nMedia: {len(data["post"]["contents"]["media"])}'
                    res += f'\nLikes: {data["post"]["postInfo"]["likeCount"]}'
                    res += f'\nComments: {data["post"]["postInfo"]["commentCount"]}'
                    res += f'\nURL: https://line.me/R/home/post?userMid={data["post"]["postInfo"]["homeId"]}&postId={data["post"]["postInfo"]["postId"]}'
                    line.sendReplyMention(to, res, [data['post']['userInfo']['writerMid']], msgIds=msg_id)
                    if 'media' in data["post"]["contents"]:
                        videos = []
                        images = []
                        for content in data["post"]["contents"]["media"]:
                            params = {'userMid': data['post']['userInfo']['writerMid'], 'oid': content['objectId']}
                            path = line.server.urlEncode(line.server.LINE_OBS_DOMAIN, '/myhome/h/download.nhn', params)
                            if content["type"] == "PHOTO":
                                images.append(path)
                            else:
                                line.sendVideoWithURL(to, path)
                        if images:
                            if len(images) >= 2:
                                line.sendMultiImageWithURL(to, images)
                            else:
                                line.sendImageWithURL(to, images[0])
                else:
                    line.sendMessage(to, f'failed to get note, this group only have {num} note')

        elif cmd.startswith("mentionnote"):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
            if cmd == 'mentionnote':
                profile = line.getProfile()
                group = line.getChats([to], True, False)
                data = [contact+'||//{}'.format(line.getContact(contact).displayName) for contact in group.chats[0].extra.groupExtra.memberMids]
                data.remove(profile.mid+'||//{}'.format(profile.displayName))
                msgas = '「 Mention Note 」'
                no = 0
                nos = 0
                for i in data:
                    no += 1
                    msgas += '\n{}. @'.format(no)
                target = []
                for i in data:
                    targets = []
                    textt = ''
                    for texttl in msgas:
                        if texttl == '@':
                            textt += str(texttl)
                            targets.append(textt.index('@'))
                            textt = textt.replace('@',' ')
                        else:
                            textt += str(texttl)
                    target.append({'type': "RECALL", 'start': targets[nos], 'end': targets[nos]+1, 'mid': str(i.split('||//')[0])})
                    nos +=1
                line.createPostGroup(to, msgas, textMeta=target)
            else:
                cmd = cmd.replace(msg.text[:12],'')
                if 'MENTION' in msg.contentMetadata != None:
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    no = 0
                    target = []
                    targets = []
                    for mention in mentionees:
                        nama = line.getContact(mention["M"]).displayName
                        target.append(str(cmd.replace('@{}'.format(nama.lower()),'==> @\n')))
                        for targ in target:
                            cmd = str(targ)
                        targetv2 = []
                        textt = ''
                        for texttl in cmd:
                            if texttl == '@':
                                textt += str(texttl)
                                targetv2.append(textt.index('@'))
                                textt = textt.replace('@',' ')
                            else:
                                textt += str(texttl)
                        targets.append({'type': "RECALL", 'start': targetv2[no], 'end': targetv2[no]+1, 'mid': str(mention["M"])})
                        no +=1
                    line.createPostGroup(to, cmd, textMeta=targets)
        
        elif cmd.startswith('addtoken '):
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                parsed_len = len(mentions['MENTIONEES'])//20+1
                no = 0
                res = "╭「 Add Token User 」\n"
                for point in range(parsed_len):
                    mids = []
                    for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                        no += 1
                        if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                            if mid['M'] not in line.settings["usertoken"]:
                                res += '╰ %i. @! > Added\n' % (no)
                                line.settings["usertoken"].append(mid['M'])
                            else:
                                res += '╰ %i. @! > Already\n' % (no)
                        else:
                            if mid['M'] not in line.settings["usertoken"]:
                                res += '├ %i. @! > Added\n' % (no)
                                line.settings["usertoken"].append(mid['M'])
                            else:
                                res += '├ %i. @! > Already\n' % (no)
                        mids.append(mid['M'])
                    if mids:
                        if res.endswith('\n'): res = res[:-1]
                        if point != 0:
                            line.sendMention(to, res, mids)
                        else:
                            line.sendReplyMention(to, res, mids, msgIds=msg_id)
                        res = ""
                            
        elif cmd.startswith('deltoken '):
            if line.settings["usertoken"]:
                if 'MENTION' in msg.contentMetadata != None:
                    mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                    parsed_len = len(mentions['MENTIONEES'])//20+1
                    no = 0
                    res = "╭「 Del Token User 」\n"
                    for point in range(parsed_len):
                        mids = []
                        for mid in mentions['MENTIONEES'][point*20:(point+1)*20]:
                            no += 1
                            if mid['M'] == mentions['MENTIONEES'][-1]["M"]:
                                if mid['M'] in line.settings["usertoken"]:
                                    res += '╰ %i. @! > Deleted\n' % (no)
                                    line.settings["usertoken"].remove(mid['M'])
                                else:
                                    res += '╰ %i. @! > Not in list\n' % (no)
                            else:
                                if mid['M'] in line.settings["usertoken"]:
                                    res += '├ %i. @! > Deleted\n' % (no)
                                    line.settings["usertoken"].remove(mid['M'])
                                else:
                                    res += '├ %i. @! > Not in list\n' % (no)
                            mids.append(mid['M'])
                        if mids:
                            if res.endswith('\n'): res = res[:-1]
                            if point != 0:
                                line.sendMention(to, res, mids)
                            else:
                                line.sendReplyMention(to, res, mids, msgIds=msg_id)
                            res = ""
                else:
                    texttl = removeCmd(text, setKey)
                    num = texttl.split(" ")
                    if num[-1].isdigit():
                        if int(num[-1]) <= len(line.settings["usertoken"]):
                            user = line.settings["usertoken"][int(num[-1]) - 1]
                            line.settings["usertoken"].remove(user)
                            line.sendReplyMention(to, 'Target: @!\nDeleted', [user], msgIds=msg_id)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'Failed to delete, total user token did not reach {} user'.format(num[-1]))
            else:
                line.sendMode(msg, to, sender, cmd, 'User token empty')

        elif cmd == 'list token':
            if line.settings["usertoken"]:
                no = 0
                parsed_len = len(line.settings["usertoken"])//20+1
                res = "╭「 User Token List 」\n"
                for point in range(parsed_len):
                    mids = []
                    for mid in line.settings["usertoken"][point*20:(point+1)*20]:
                        no += 1
                        if mid == line.settings["usertoken"][-1]:
                            res += '╰ %i. @!\n' % (no)
                        else:
                            res += '├ %i. @!\n' % (no)
                        mids.append(mid)
                    if mids:
                        if res.endswith('\n'): res = res[:-1]
                        if point != 0:
                            line.sendMention(to, res, mids)
                        else:
                            line.sendReplyMention(to, res, mids, msgIds=msg_id)
                        res = ""
            else: line.sendMode(msg, to, sender, cmd, 'User token empty')
            
        elif cmd == 'gettoken':
            res = '› O W N E R\n'
            res += '\n• {}Addtoken @Mention'.format(setKey.title())
            res += '\n• {}Deltoken @Mention/<num>'.format(setKey.title())
            res += '\n• {}List Token'.format(setKey.title())
            res += '\n\n› U S E R\n'
            res += '\n• {}Token list'.format(setKey.title())
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd == 'token list':
            res = '› T O K E N  A P P\n'
            res += '\n1. Desktopmac'
            res += '\n2. Desktopwin'
            res += '\n3. Chrome'
            res += '\n4. Iosipad'
            res += '\n'
            res += '\nExample: {}Token Desktopmac'.format(setKey.title())
            line.sendMode(msg, to, sender, cmd, res)
    #----------COMMAND KICK----------#
        elif cmd == 'kick':
            res = '› P Y T H O N + J S\n'
            res += '\n• {}{} @Mention'.format(setKey.title(), line.settings["setcommand"]["kicks"]["message"].title())
            res += '\n• {}v{} @Mention'.format(setKey.title(), line.settings["setcommand"]["kicks"]["message"].title())
            res += '\n• {}n{} <name>'.format(setKey.title(), line.settings["setcommand"]["kicks"]["message"].title())
            res += '\n• {}x{}'.format(setKey.title(), line.settings["setcommand"]["kicks"]["message"].title())
            res += '\n• {}Skill <name>'.format(setKey.title())
            res += '\n• {}Cancel <name>'.format(setKey.title())
            res += '\n• {}{} @Mention'.format(setKey.title(), line.settings["setcommand"]["invites"]["message"].title())
            res += '\n• {}n{} <name>'.format(setKey.title(), line.settings["setcommand"]["invites"]["message"].title())
            res += '\n• {}x{}'.format(setKey.title(), line.settings["setcommand"]["invites"]["message"].title())
            res += '\n• {}InviteID <idline>'.format(setKey.title())
            res += '\n• {}InviteContact'.format(setKey.title())
            res += '\n• {}reInvite @Mention/Reply'.format(setKey.title())
            res += '\n• {}setKick sticker / delSticker / <text>'.format(setKey.title())
            res += '\n• {}setInvite sticker / delSticker / <text>'.format(setKey.title())
            res += '\n• {}setTextKick <text>'.format(setKey.title())
            if line.settings['textKick'] == "": res += '\n• Text Kick: Nothing'
            else: res += '\n• Text Kick: `{}`'.format(line.settings["textKick"])
            res += '\n    Example Text Kick:'
            res += '\n    Text: `You are weird`'
            res += '\n    Cmd: Hey You are weird @Mention kick it'
            res += '\n\n› J S  O N L Y\n'
            res += '\n• {}Setkickall <text>'.format(setKey.title())
            res += '\n• {}Setcancel <text>'.format(setKey.title())
            res += '\n• Kickall = {}'.format(setKey.title()) + line.settings["setcommand"]["kickall"]
            res += '\n• Cancelall = {}'.format(setKey.title()) + line.settings["setcommand"]["cancel"]
            res += '\n\n› J S  R E M O T E\n'
            res += '\n• {}Grouplist'.format(setKey.title())
            res += '\n• {}Rkickall <num>'.format(setKey.title())
            res += '\n• {}Rcancelall <num>'.format(setKey.title())
            line.sendMode(msg, to, sender, cmd, res)
            
        elif cmd.startswith('setkickall '):
            txt = removeCmd(text, setKey)
            line.settings["setcommand"]["kickall"] = txt
            line.sendMode(msg, to, sender, cmd, 'Command kickall successfully changed to \'%s\'' % txt)
            
        elif cmd.startswith('setcancel '):
            txt = removeCmd(text, setKey)
            line.settings["setcommand"]["cancel"] = txt
            line.sendMode(msg, to, sender, cmd, 'Command cancelall successfully changed to \'%s\'' % txt)
        
        elif cmd.startswith('setkick '):
            txt = removeCmd(text, setKey)
            if txt.lower() == 'sticker':
                line.settings["setcommand"]["kicks"]["status"] = True
                line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            elif txt.lower() == 'delsticker':
                line.settings["setcommand"]["kicks"]["status"] = False
                line.settings["setcommand"]["kicks"]["stkid"] = None
                line.sendMode(msg, to, sender, cmd, 'Auto Kick by Sticker successfully deleted')
            else:
                line.settings["setcommand"]["kicks"]["status"] = False
                line.settings["setcommand"]["kicks"]["message"] = txt
                line.sendMode(msg, to, sender, cmd, 'Command kick successfully changed to \'%s\'' % txt)
        
        elif cmd.startswith('setinvite '):
            txt = removeCmd(text, setKey)
            if txt.lower() == 'sticker':
                line.settings["setcommand"]["invites"]["status"] = True
                line.sendMode(msg, to, sender, cmd, 'Send the sticker..\ntype `{key}Abort` to cancel this'.format(key=setKey.title()))
            elif txt.lower() == 'delsticker':
                line.settings["setcommand"]["invites"]["status"] = False
                line.settings["setcommand"]["invites"]["stkid"] = None
                line.sendMode(msg, to, sender, cmd, 'Auto Invite by Sticker successfully deleted')
            else:
                line.settings["setcommand"]["invites"]["status"] = False
                line.settings["setcommand"]["invites"]["message"] = txt
                line.sendMode(msg, to, sender, cmd, 'Command invite successfully changed to \'%s\'' % txt)
                
        elif cmd.startswith('settextkick '):
            txt = removeCmd(text, setKey)
            if txt == "":
                line.settings["textKick"] = ""
                line.sendMode(msg, to, sender, cmd, 'Command successfully reset')
            elif len(txt) > 5:
                line.settings["textKick"] = txt
                line.sendMode(msg, to, sender, cmd, 'Command successfully changed to \'%s\'' % txt)
            else:
                line.sendMode(msg, to, sender, cmd, 'To avoid errors, make sure the amount of text above 5')
                
        elif cmd == "safe cancelall":
            if sender == line.profile.mid:
                group = line.getChats([to], False, True).chats[0]
                if group.extra.groupExtra.inviteeMids != {}:
                    for member in group.extra.groupExtra.inviteeMids:
                        try:
                            line.cancelChatInvitation(to, [member])
                            time.sleep(0.8)
                        except TalkException as talk_error:
                            if talk_error.code == 35:
                                line.sendFooter(to, "Limit cancel", reply=True)
                                break
                            continue
        
        elif cmd == "safe kickall":
            if sender == line.profile.mid:
                group = line.getChats([to], True, False).chats[0]
                if group.extra.groupExtra.memberMids != {}:
                    for member in group.extra.groupExtra.memberMids:
                        try:
                            line.deleteOtherFromChat(to, [member])
                            time.sleep(0.8)
                        except TalkException as talk_error:
                            if talk_error.code == 35:
                                line.sendFooter(to, "Limit kick", reply=True)
                                break
                            continue

        elif cmd.startswith('{} '.format(line.settings["setcommand"]["kicks"]["message"].lower())):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in deep group!!')
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                if len(mentions['MENTIONEES']) >= 4:
                    cm = 'lib/javascript/dual.js gid={} token={} appName="{}" userAgent="{}" method=kick'.format(to, line.authToken, line.server.APP_NAME, line.server.USER_AGENT)
                    for mention in mentions['MENTIONEES']:
                        if mention['M'] in line.profile.mid or mention['M'] in sozi:
                            continue
                        elif checkAccess(mention['M']):
                            continue
                        cm += ' uid={}'.format(mention['M'])
                    print(cm)
                    success = execute_js(cm)
                else:
                    for mention in mentions['MENTIONEES']:
                        mid = mention['M']
                        if mid == line.profile.mid:
                            continue
                        try:
                            line.deleteOtherFromChat(to, [mid])
                        except TalkException as talk_error:
                            return line.sendFooter(to, 'Failed kick members, the reason is `%s`' % talk_error.reason)
                            
        elif cmd.startswith("skill "):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in deep group!!')
            name = removeCmd(text, setKey)
            if name == '' or name == " ":
                return
            group = line.getChats([to], True, True).chats[0]
            members = []
            pendings = []
            for member in group.extra.groupExtra.memberMids:
                try: contact = line.getContact(member)
                except: continue
                if contact.displayNameOverridden:
                    if name in contact.displayNameOverridden.lower():
                        members.append(member)
                if name in contact.displayName.lower():
                    if member not in members:
                        members.append(member)
            for member in group.extra.groupExtra.inviteeMids:
                try: contact = line.getContact(member)
                except: continue
                if contact.displayNameOverridden:
                    if name in contact.displayNameOverridden.lower():
                        pendings.append(member)
                if name in contact.displayName.lower():
                    if member not in pendings:
                        pendings.append(member)
            cm = ""
            cc = ""
            if members:
                cm = 'lib/javascript/dual.js gid={} token={} appName="{}" userAgent="{}" method=kick'.format(to, line.authToken, line.server.APP_NAME, line.server.USER_AGENT)
                for mid in members:
                    if mid in line.profile.mid or mid in sozi:
                        continue
                    elif checkAccess(mid):
                        continue
                    cm += ' uid={}'.format(mid)
                print(cm)
            if pendings:
                cc = 'lib/javascript/dual.js gid={} token={} appName="{}" userAgent="{}" method=cancel'.format(to, line.authToken, line.server.APP_NAME, line.server.USER_AGENT)
                for mid in pendings:
                    if mid in line.profile.mid or mid in sozi:
                        continue
                    elif checkAccess(mid):
                        continue
                    cc += ' uid={}'.format(mid)
                print(cm)
            if cc != "":
                threading.Thread(target=execute_js, args=(cc,)).start()
            if cm != "":
                threading.Thread(target=execute_js, args=(cm,)).start()
            if not members and not pendings:
                line.sendMode(msg, to, sender, cmd, "No member/pending found with name '{}'".format(name))

        elif cmd.startswith("n{} ".format(line.settings["setcommand"]["kicks"]["message"].lower())):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in deep group!!')
            name = removeCmd(text, setKey)
            if name == '' or name == " ":
                return
            group = line.getChats([to], True, False).chats[0]
            listt = []
            for member in group.extra.groupExtra.memberMids:
                contact = line.getContact(member)
                if contact.displayNameOverridden:
                    if name in contact.displayNameOverridden.lower():
                        line.deleteOtherFromChat(to, [member])
                        listt.append(member)
                        time.sleep(0.8)
                if name in contact.displayName.lower():
                    if member not in listt:
                        line.deleteOtherFromChat(to, [member])
                        listt.append(member)
                        time.sleep(0.8)
            if not listt:
                line.sendMode(msg, to, sender, cmd, "No member found by name '{}'".format(name))
                    
        elif cmd.startswith('v{} '.format(line.settings["setcommand"]["kicks"]["message"].lower())):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in deep group!!')
            group = line.getChats([to], True, False).chats[0]
            members = group.extra.groupExtra.memberMids
            friend = line.getAllContactIds()
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid == line.profile.mid:
                        continue
                    try:
                        if mid not in friend:
                            line.findAndAddContactsByMid(mid)
                            time.sleep(0.8)
                        if mid not in members:
                            line.sendMention(to, "› @! not in group", [mid])
                        else:
                            line.deleteOtherFromChat(to, [mid])
                            line.inviteIntoChat(to, [mid])
                            line.cancelChatInvitation(to, [mid])
                            time.sleep(0.8)
                    except TalkException as talk_error:
                        return line.sendFooter(to, 'Failed vultra kick members, the reason is `%s`' % talk_error.reason)
            else:
                line.sendMode(msg, to, sender, cmd, 'Failed vultra kick member, please mention user you want to kick')
                
        elif cmd == 'x{}'.format(line.settings["setcommand"]["kicks"]["message"].lower()):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in deep group!!')
            group = line.getChats([to], True, True).chats[0]
            members = group.extra.groupExtra.memberMids
            if msg.relatedMessageId is not None:
                data = line.getReplyMessage(to, msg.relatedMessageId)
                if data is not None:
                    if data._from != line.profile.mid:
                        if data._from not in members:
                            line.sendMention(to, "› @! not in group", [data._from])
                        else:
                            deleteOtherFromChat(to, [data._from])
            else:
                line.sendMode(msg, to, sender, cmd, 'you must reply the message')
                
        elif cmd.startswith('cancel '):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in deep group!!')
            name = removeCmd(text, setKey)
            if name == '' or name == " ":
                return
            group = line.getChats([to], False, True).chats[0]
            pending = group.extra.groupExtra.inviteeMids
            target = []
            for member in pending:
                try: contact = line.getContact(member)
                except: continue
                if contact.displayNameOverridden:
                    if name in contact.displayNameOverridden.lower():
                        line.cancelChatInvitation(to, [member])
                        target.append(member)
                        time.sleep(0.8)
                if name in contact.displayName.lower():
                    if member not in target:
                        line.cancelChatInvitation(to, [member])
                        target.append(member)
                        time.sleep(0.8)
            if not target:
                line.sendMode(msg, to, sender, cmd, "No pending found with name '{}'".format(name))
                
        elif cmd.startswith('{} '.format(line.settings["setcommand"]["invites"]["message"].lower())):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            group = line.getChats([to], True, True).chats[0]
            members = group.extra.groupExtra.memberMids
            pending = group.extra.groupExtra.inviteeMids
            friend = line.getAllContactIds()
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                target = []
                target2 = []
                res = "「 Invite User 」\n"
                no = 0
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid not in friend:
                        line.findAndAddContactsByMid(mid)
                        time.sleep(0.8)
                    if mid in members:
                        no += 1
                        res += '%i. @! › already joined group\n' % (no)
                        target2.append(mid)
                    elif mid in pending:
                        no += 1
                        res += '%i. @! › already invited\n' % (no)
                        target2.append(mid)
                    else:
                        target.append(mid)
                if res.endswith('\n'): res = res[:-1]
                if target2:
                    line.sendMention(to, res, target2)
                if target:
                    inviteIntoChat(to, target)
        
        elif cmd.startswith('reinvite'):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            group = line.getChats([to], True, True).chats[0]
            members = group.extra.groupExtra.memberMids
            friend = line.getAllContactIds()
            if 'MENTION' in msg.contentMetadata != None:
                mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                for mention in mentions['MENTIONEES']:
                    mid = mention['M']
                    if mid == line.profile.mid:
                        continue
                    try:
                        if mid not in friend:
                            line.findAndAddContactsByMid(mid)
                            time.sleep(0.8)
                        if mid in members:
                            line.deleteOtherFromChat(to, [mid])
                            time.sleep(0.8)
                        line.inviteIntoChat(to, [mid])
                    except TalkException as talk_error:
                        return line.sendFooter(to, 'Failed reinvite members, the reason is `%s`' % talk_error.reason)
            elif msg.relatedMessageId:
                data = line.getReplyMessage(to, msg.relatedMessageId)
                if data is not None:
                    try:
                        if data._from not in friend:
                            line.findAndAddContactsByMid(data._from)
                            time.sleep(0.8)
                        if data._from  in members:
                            line.deleteOtherFromChat(to, [data._from])
                            time.sleep(0.8)
                        line.inviteIntoChat(to, [data._from])
                    except TalkException as talk_error:
                        return line.sendFooter(to, 'Failed reinvite members, the reason is `%s`' % talk_error.reason)

        elif cmd.startswith("n{} ".format(line.settings["setcommand"]["invites"]["message"].lower())):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            group = line.getChats([to], True, True).chats[0]
            members = group.extra.groupExtra.memberMids
            pending = group.extra.groupExtra.inviteeMids
            friend = line.getAllContactIds()
            name = removeCmd(text, setKey)
            if name == '' or name == " ":
                return
            target = []
            target2 = []
            res = "「 Invite User 」\n"
            no = 0
            for teman in friend:
                try:
                    contact = line.getContact(teman)
                except:
                    line.deleteContact(teman)
                    continue
                if contact.displayNameOverridden:
                    if name in contact.displayNameOverridden.lower():
                        if teman in members:
                            no += 1
                            res += '%i. @! › already joined group\n' % (no)
                            target2.append(teman)
                        elif teman in pending:
                            no += 1
                            res += '%i. @! › already invited\n' % (no)
                            target2.append(teman)
                        else:
                            target.append(teman)
                if name in contact.displayName.lower():
                    if teman not in target:
                        if teman in members:
                            if teman not in target2:
                                no += 1
                                res += '%i. @! › already joined group\n' % (no)
                                target2.append(teman)
                        elif teman in pending:
                            if teman not in target2:
                                no += 1
                                res += '%i. @! › already invited\n' % (no)
                                target2.append(teman)
                        else:
                            target.append(teman)
            if res.endswith('\n'): res = res[:-1]
            if target2:
                line.sendMention(to, res, target2)
            if target:
                inviteIntoChat(to, target)
            elif not target and not target2:
                line.sendMode(msg, to, sender, cmd, "No user found with namea '{}'".format(name))

        elif cmd == 'x{}'.format(line.settings["setcommand"]["invites"]["message"].lower()):
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            group = line.getChats([to], True, True).chats[0]
            members = group.extra.groupExtra.memberMids
            pending = group.extra.groupExtra.inviteeMids
            friend = line.getAllContactIds()
            if msg.relatedMessageId is not None:
                data = line.getReplyMessage(to, msg.relatedMessageId)
                if data is not None:
                    if data._from != line.profile.mid:
                        if data._from not in friend:
                            line.findAndAddContactsByMid(data._from)
                            time.sleep(0.8)
                        if data._from in members:
                            line.sendMention(to, "› @! already joined group", [data._from])
                        elif data._from in pending:
                            line.sendMention(to, "› @! already invited", [data._from])
                        else:
                            inviteIntoChat(to, [data._from])
            else:
                line.sendMode(msg, to, sender, cmd, 'you must reply the message')
                
        elif cmd == line.settings["setcommand"]["kickall"].lower():
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in dalam group!!')
            if sender in line.profile.mid:
                group = make_list(line.getChats([to], True, False).chats[0].extra.groupExtra.memberMids)
                parsed_len = len(group)//140+1
                target = []
                for point in range(parsed_len):
                    cm = 'lib/javascript/dual.js gid={} token={} appName="{}" userAgent="{}" method=kick'.format(to, line.authToken, line.server.APP_NAME, line.server.USER_AGENT)
                    for g in group[point*140:(point+1)*140]:
                        if g in line.profile.mid or g in sozi:
                            continue
                        elif checkAccess(g):
                            continue
                        cm += ' uid={}'.format(g)
                    target.append(cm)
                for exe in target:
                    print(exe)
                    success = execute_js(exe)
                    time.sleep(5)
                if success:
                    line.sendMode(msg, to, sender, cmd, 'Java Script Kickall\nStatus: ✓')
                else:
                    line.sendMode(msg, to, sender, cmd, 'Java Script Kickall\nStatus: ✘')
                    
        elif cmd == line.settings["setcommand"]["cancel"].lower():
            if msg.toType != 2: return line.sendFooter(to, 'this command can only be used in group!!')
            if sender in line.profile.mid:
                group = make_list(line.getChats([to], False, True).chats[0].extra.groupExtra.inviteeMids)
                if len(group) == 0:
                    return line.sendFooter(to, 'There is no one pending members here')
                parsed_len = len(group)//10+1
                target = []
                for point in range(parsed_len):
                    cm = 'lib/javascript/dual.js gid={} token={} appName="{}" userAgent="{}" method=cancel'.format(to, line.authToken, line.server.APP_NAME, line.server.USER_AGENT)
                    for g in group[point*10:(point+1)*10]:
                        if g in line.profile.mid or g in sozi:
                            continue
                        elif checkAccess(g):
                            continue
                        cm += ' uid={}'.format(g)
                    target.append(cm)
                for exe in target:
                    print(exe)
                    success = execute_js(exe)
                    time.sleep(6)
                if success:
                    line.sendMode(msg, to, sender, cmd, 'Java Script Cancelall\nStatus: ✓')
                else:
                    line.sendMode(msg, to, sender, cmd, 'Java Script Cancelall\nStatus: ✘')
                        
        elif cmd.startswith("rkickall "):
            if sender in line.profile.mid:
                groupz = make_list(line.getAllChatMids(True, False).memberChatMids)
                sep = removeCmd(text, setKey)
                if sep.isdigit():
                    nums = int(sep)
                    groups = line.getChats([groupz[nums-1]], True, False).chats[0]
                    group = make_list(groups.extra.groupExtra.memberMids)
                    parsed_len = len(group)//140+1
                    target = []
                    for point in range(parsed_len):
                        cm = 'lib/javascript/dual.js gid={} token={} appName="{}" userAgent="{}" method=kick'.format(groups.chatMid, line.authToken, line.server.APP_NAME, line.server.USER_AGENT)
                        for g in group[point*140:(point+1)*140]:
                            if g in line.profile.mid or g in sozi:
                                continue
                            elif checkAccess(g):
                                continue
                            cm += ' uid={}'.format(g)
                        target.append(cm)
                    for exe in target:
                        print(exe)
                        success = execute_js(exe)
                        time.sleep(5)
                    if success:
                        line.sendMode(msg, to, sender, cmd, 'Java Script Kickall\nRemote Group: {}\nStatus: ✓'.format(groups.chatName))
                    else:
                        line.sendMode(msg, to, sender, cmd, 'Java Script Kickall\nRemote Group: {}\nStatus: ✘'.format(groups.chatName))

        elif cmd.startswith("rcancelall "):
            if sender in line.profile.mid:
                groupz = make_list(line.getAllChatMids(True, False).memberChatMids)
                sep = removeCmd(text, setKey)
                if sep.isdigit():
                    nums = int(sep)
                    groups = line.getChats([groupz[nums-1]], False, True).chats[0]
                    group = make_list(groups.extra.groupExtra.inviteeMids)
                    if len(group) == 0:
                        return line.sendFooter(to, 'There is no one pending members here')
                    parsed_len = len(group)//10+1
                    target = []
                    for point in range(parsed_len):
                        cm = 'lib/javascript/dual.js gid={} token={} appName="{}" userAgent="{}" method=cancel'.format(groups.chatMid, line.authToken, line.server.APP_NAME, line.server.USER_AGENT)
                        for g in group[point*10:(point+1)*10]:
                            if g in line.profile.mid or g in sozi:
                                continue
                            elif checkAccess(g):
                                continue
                            cm += ' uid={}'.format(g)
                        target.append(cm)
                    for exe in target:
                        print(exe)
                        success = execute_js(exe)
                        time.sleep(6)
                    if success:
                        line.sendMode(msg, to, sender, cmd, 'Java Script Cancelall\nRemote Group: {}\nStatus: ✓'.format(groups.chatName))
                    else:
                        line.sendMode(msg, to, sender, cmd, 'Java Script Cancelall\nRemote Group: {}\nStatus: ✘'.format(groups.chatName))

#----------DEF FOR PUBLIC COMMAND----------#
def executePublic(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey):
    if cmd == 'token list':
        if sender in line.settings["usertoken"]:
            res = '𝗧𝗼𝗸𝗲𝗻 𝗟𝗶𝘀𝘁:'
            res += '\n    1. Desktopmac'
            res += '\n    2. Desktopwin'
            res += '\n    3. Chrome'
            res += '\n    4. Iosipad'
            res += '\n'
            res += '\nexample: {}Token Desktopmac'.format(setKey.title())
            line.sendMode(msg, to, sender, cmd, res)
            
    elif cmd == 'token desktopmac':
        if sender in line.settings["usertoken"]:
            app_type = "DESKTOPMAC"
            try: line.getTokenApi(to, sender, app_type)
            except Exception as e: line.sendReplyMessage(to, str(e), msgIds=msg_id)
            
    elif cmd == 'token desktopwin':
        if sender in line.settings["usertoken"]:
            app_type = "DESKTOPWIN"
            try: line.getTokenApi(to, sender, app_type)
            except Exception as e: line.sendReplyMessage(to, str(e), msgIds=msg_id)
            
    elif cmd == 'token chrome':
        if sender in line.settings["usertoken"]:
            app_type = "CHROMEOS"
            try: line.getTokenApi(to, sender, app_type)
            except Exception as e: line.sendReplyMessage(to, str(e), msgIds=msg_id)
    
    elif cmd == 'token iosipad':
        if sender in line.settings["usertoken"]:
            app_type = "IOSIPAD"
            try: line.getTokenApi(to, sender, app_type)
            except Exception as e: line.sendReplyMessage(to, str(e), msgIds=msg_id)
            
    elif cmd == 'my point':
        if line.protect["pointMode"]["status"]:
            if sender in line.protect["pointMode"]["user"]:
                line.sendMessage(to, f'[ POINT MEMBER ]\n__________________\n𖤬 Created: {line.protect["pointMode"]["userPoint"][sender]["created"]}\n𖤬 User: {line.getContact(sender).displayName}\n𖤬 Poin: {line.protect["pointMode"]["userPoint"][sender]["points"]}')

    elif to in line.settings["publicBot"] or line.settings["allPublic"]:
        if cmd == 'speed':
            check = line.anti_spam(sender, 15, line.setts["spamPublic"])
            if check: return
            start = time.time()
            batas = line.getProfile()
            elapse = time.time() - start
            last = elapse * 1000
            line.sendMessage(to, "%s ms" % (round(last, 1)))
            line.setts["spamPublic"][sender]["time"] = time.time()
        
        elif to not in ['c325bb625cf981f92b147164e87e42280', 'c1dc8fbe66a54c6def5e55d208bc4db1a']:
            if txt == 'help':
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                isi = ["Help", "Speed", "Sider", line.settings["setcommand"]["faketag"], line.settings["setcommand"]["mentionall"], "Me"]
                profile = line.getProfile()
                if line.settings["setFlag"]["icon"] == "https://i.ibb.co/7tmGYQ1/FOOTER-ACODE44.gif":
                    if profile.pictureStatus: picture = "https://obs.line-scdn.net/" + str(profile.pictureStatus)
                    else: picture = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
                else:
                    picture = line.settings["setFlag"]["icon"]
                if line.settings["setFlag"]["name"] == 'sozibot': name = str(profile.displayName)
                else: name = line.settings["setFlag"]["name"]
                line.mainMenu(to, picture, name, setKey, line.settings["tempBackground"], line.settings["tempColor"]["text"], isi)
                line.setts["spamPublic"][sender]["time"] = time.time()
            
            elif cmd == "me":
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                profile = line.getContact(sender)
                cover = line.getProfileCoverURL(sender)
                if "/vc/" in cover: cover = cover.replace("/vc/", "/c/")
                if profile.pictureStatus: picture = "https://obs.line-scdn.net/" + str(profile.pictureStatus)
                else: picture = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
                if profile.statusMessage == "": status = "empty"
                else: status = profile.statusMessage
                data = template.sendMe(profile.mid, profile.displayName, picture, cover, status)
                line.sendLiff(to, data, mainType=False)
                line.sendContact(to, sender)
                line.setts["spamPublic"][sender]["time"] = time.time()
                
            elif cmd == line.settings["setcommand"]["faketag"].lower():
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                if msg.toType == 1:
                    room = line.getCompactRoom(to)
                    members = [mem.mid for mem in room.contacts]
                elif msg.toType == 2:
                    members = make_list(line.getChats([to], True, False).chats[0].extra.groupExtra.memberMids)
                else:
                    return line.sendFooter(to, 'Use this command only for the room or group chat!')
                if members:
                    line.fakeMentionSticker(to, int(line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKVER"]), int(line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKPKGID"]), int(line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKID"]), members)
                line.setts["spamPublic"][sender]["time"] = time.time()

            elif cmd == line.settings["setcommand"]["mentionall"].lower():
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                members = []
                if msg.toType == 1:
                    room = line.getCompactRoom(to)
                    members = [mem.mid for mem in room.contacts]
                elif msg.toType == 2:
                    group = line.getChats([to], True, False)
                    members = [mem for mem in group.chats[0].extra.groupExtra.memberMids]
                else:
                    return line.sendFooter(to, 'Use this command only for the room or group chat!')
                if members:
                    if line.settings["setcommand"]["mentionAllEmoji"]["productId"] is not None:
                        line.mentionMembersEmoticon(to, line.settings["setcommand"]["mentionAllEmoji"]["productId"], members, msgIds=msg_id)
                    else:
                        line.mentionMembers(to, members, msgIds=msg_id)
                line.setts["spamPublic"][sender]["time"] = time.time()

            elif cmd == 'sider':
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
                if msg.toType in [1, 2] and to not in line.setts["lurking"]:
                    line.setts["lurking"][to] = {
                        'status': False,
                        'time': None,
                        'members': [],
                        'reply': {
                            'status': False,
                            'message': line.settings['sider']['defaultReplyReader']
                        }
                    }
                if msg.toType in [1, 2]: res = 'Status: ' + bool_dict[line.setts["lurking"][to]['status']][4]
                if msg.toType in [1, 2]: res += '\nCyduk: ' + bool_dict[line.setts["lurking"][to]['reply']['status']][4]
                if msg.toType in [1, 2]: res += '\nCyduk Message: ' + line.setts["lurking"][to]['reply']['message']
                res += '\n\n› C O M M A N D\n'
                res += '\n• {}Sider'.format(setKey.title())
                res += '\n• {}Sider <on/off>'.format(setKey.title())
                res += '\n• {}Sider Result'.format(setKey.title())
                res += '\n• {}Sider Reset'.format(setKey.title())
                res += '\n• {}Cyduk <on/off>'.format(setKey.title())
                line.sendMode(msg, to, sender, cmd, res)
                line.setts["spamPublic"][sender]["time"] = time.time()

            elif cmd == 'sider on':
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
                if msg.toType in [1, 2] and to not in line.setts["lurking"]:
                    line.setts["lurking"][to] = {
                        'status': False,
                        'time': None,
                        'members': [],
                        'reply': {
                            'status': False,
                            'message': line.settings['sider']['defaultReplyReader']
                        }
                    }
                if not line.setts["lurking"][to]['status']:
                    line.setts["lurking"][to].update({
                        'status': True,
                        'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                        'members': []
                    })
                sendToggle(to, "CHECK READER", "Check reader activated, type '{}sider result' to see data reader".format(setKey.title()), "type '{}sider result' to view data reader".format(setKey.title()), True)
                line.setts["spamPublic"][sender]["time"] = time.time()

            elif cmd == 'sider off':
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
                if msg.toType in [1, 2] and to not in line.setts["lurking"]:
                    line.setts["lurking"][to] = {
                        'status': False,
                        'time': None,
                        'members': [],
                        'reply': {
                            'status': False,
                            'message': line.settings['sider']['defaultReplyReader']
                        }
                    }
                if line.setts["lurking"][to]['status']:
                    line.setts["lurking"][to].update({
                        'status': False,
                        'time': None,
                        'members': []
                    })
                sendToggle(to, "CHECK READER", "Check Reader disabled", "", False)
                line.setts["spamPublic"][sender]["time"] = time.time()

            elif cmd == 'sider result':
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
                if msg.toType in [1, 2] and to not in line.setts["lurking"]:
                    line.setts["lurking"][to] = {
                        'status': False,
                        'time': None,
                        'members': [],
                        'reply': {
                            'status': False,
                            'message': line.settings['sider']['defaultReplyReader']
                        }
                    }
                if not line.setts["lurking"][to]['status']:
                    line.sendMode(msg, to, sender, cmd, 'Sider not yet active, type \'{}Sider on\' first'.format(setKey.title()))
                else:
                    if not line.setts["lurking"][to]['members']:
                        line.sendMode(msg, to, sender, cmd, 'Data still empty, no one has read it yet')
                    else:
                        members = line.setts["lurking"][to]['members']
                        res = 'Check Sider'
                        if msg.toType == 2: res += '\nGroup: ' + line.getChats([to], False, False).chats[0].chatName + "\n"
                        parsed_len = len(members)//200+1
                        no = 0
                        for point in range(parsed_len):
                            for member in members[point*200:(point+1)*200]:
                                no += 1
                                try:
                                    name = line.getContact(member).displayName
                                except TalkException:
                                    name = 'Unknown'
                                if member == members[-1]:
                                    res += '\n    %i. %s' % (no, name)
                                else:
                                    res += '\n    %i. %s' % (no, name)
                            if res:
                                if res.startswith('\n'): res = res[1:]
                                line.sendReplyMessage(to, res, msgIds=msg_id)
                            res = ''
                line.setts["spamPublic"][sender]["time"] = time.time()
                
            elif cmd == 'sider reset':
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
                if msg.toType in [1, 2] and to not in line.setts["lurking"]:
                    line.setts["lurking"][to] = {
                        'status': False,
                        'time': None,
                        'members': [],
                        'reply': {
                            'status': False,
                            'message': line.settings['sider']['defaultReplyReader']
                        }
                    }
                if not line.setts["lurking"][to]['status']:
                    line.sendMode(msg, to, sender, cmd, 'Sider not yet active, type \'{}Sider on\' first'.format(setKey.title()))
                else:
                    line.setts["lurking"][to].update({
                        'status': True,
                        'time': datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d %H:%M:%S'),
                        'members': []
                    })
                    line.sendMode(msg, to, sender, cmd, 'Data sider reset successfully')
                line.setts["spamPublic"][sender]["time"] = time.time()

            elif cmd == 'cyduk on':
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
                if to not in line.setts["replyReader"]:
                    line.setts["replyReader"][to] = {
                        'listmem': [],
                        'eply': {
                            'tatus': False,
                        }
                    }
                if line.setts["replyReader"][to]['eply']['tatus']:
                    line.sendMode(msg, to, sender, cmd, "Cyduk is active, turn it off first then reactivate it")
                else:
                    line.setts["replyReader"][to]['eply']['tatus'] = True
                    line.sendFooter(to, "Start scooping...")
                line.setts["spamPublic"][sender]["time"] = time.time()

            elif cmd == 'cyduk off':
                check = line.anti_spam(sender, 15, line.setts["spamPublic"])
                if check: return
                if msg.toType not in [1, 2]: return line.sendFooter(to, 'this command can only be used in group!!')
                if to not in line.setts["replyReader"]: line.sendMode(msg, to, sender, cmd, "Cyduk is inactive, turn it on first")
                elif not line.setts["replyReader"][to]['eply']['tatus']: line.sendMode(msg, to, sender, cmd, "Cyduk is inactive, turn it on first")
                else:
                    line.setts["replyReader"][to].update({
                        'listmem': [],
                        'eply': {
                            'tatus': False,
                        }
                    })
                    line.sendFooter(to, "Stop scooping...")
                line.setts["spamPublic"][sender]["time"] = time.time()

#----------OP MESSAGE----------#
def executeOp(op):
    try:
        try: print ('\033[1;32m++ Operation : ( %i ) %s\033[0m' % (op.type, OpType._VALUES_TO_NAMES[op.type].replace('_', ' ')))
        except: print ('\033[1;32m++ Operation : ( %i )\033[0m' % (op.type))
#----------OPERATION NOTIFIED UPDATE PROFILE----------#
        if op.type == 2:
            if line.settings["updateProfile"]:
                if op.param1 in line.setts["notifCvp"]:
                    line.setts["notifCvp"].remove(op.param1)
                else:
                    gids = line.getAllChatMids(True, False).memberChatMids
                    ncvp = False
                    for gid in line.settings["updateProfile"]:
                        if gid in gids:
                            group = line.getChats([gid], True, False).chats[0]
                            if op.param1 not in ["ue1e97330bd77be02e52b9eb72a0d471c"]:
                                if op.param1 in group.extra.groupExtra.memberMids:
                                    profile = line.getContact(op.param1)
                                    res = "› U P D A T E  P R O F I L E\n"
                                    if op.param2 == '2':
                                        op3 = eval(op.param3)
                                        res += "\nUser: @!"
                                        res += "\nType: Display Name"
                                        res += "\nBefore: {}".format(op3["OLD_DISPLAY_NAME"])
                                        res += "\nAfter: {}".format(op3["DISPLAY_NAME"])
                                        line.sendMention(group.chatMid, res, [op.param1])
                                    if op.param2 == '16':
                                        res += "\nUser: @!"
                                        res += "\nType: Bio"
                                        if op.param1 in line.setts["memBackup"]:
                                            res += "\nBefore: {}".format(line.setts["memBackup"][op.param1]["bio"])
                                        res += "\nAfter: {}".format(profile.statusMessage)
                                        line.sendMention(group.chatMid, res, [op.param1])
                                    if op.param2 == '8':
                                        if not eval(op.param3):
                                            res += "\nUser: @!"
                                            res += "\nType: Display Picture"
                                            line.sendMention(group.chatMid, res, [op.param1])
                                            if profile.pictureStatus:
                                                line.sendLiffImage(group.chatMid, 'https://obs.line-scdn.net/' + profile.pictureStatus, line.settings["setFlag"]["icon"], " Display Picture", reply=True)
                                            else:
                                                line.sendLiffImage(group.chatMid, 'https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg', line.settings["setFlag"]["icon"], " Display Picture", reply=True)
                                        elif op.param1 not in line.setts["notifCvp"]:
                                            res += "\nUser: @!"
                                            res += "\nType: Display Picture Video"
                                            line.sendMention(group.chatMid, res, [op.param1])
                                            time.sleep(0.8)
                                            line.sendLiffVideo(group.chatMid, "https://obs.line-scdn.net/{}/vp".format(profile.pictureStatus), "https://obs.line-scdn.net/{}".format(profile.pictureStatus))
                                            ncvp = True
                                    if op.param1 not in line.setts["memBackup"]: line.setts["memBackup"][op.param1] = {}
                                    try: line.setts["memBackup"][op.param1]["bio"] = profile.statusMessage
                                    except: line.setts["memBackup"][op.param1]["bio"] = "Without Bio"
                                    time.sleep(1)
                    if ncvp:
                        if op.param1 not in line.setts["notifCvp"]:
                            line.setts["notifCvp"].append(op.param1)
#----------OPERATION NOTIFIED ADD----------#
        elif op.type == 5:
            if op.param2 not in line.settings["dataAdders"]:
                line.settings["dataAdders"].append(op.param1)
            if line.settings['autoBlock']['status']:
                if line.settings['autoBlock']['contentMetadata'] != {}:
                    contentMetadata = {"REPLACE": line.settings['autoBlock']['contentMetadata']['REPLACE'], "STICON_OWNERSHIP": line.settings['autoBlock']['contentMetadata']['STICON_OWNERSHIP']}
                    if '@!' in line.settings['autoBlock']['message']:
                        arrData = []
                        mentions = ast.literal_eval(line.settings['autoBlock']['contentMention']['MENTION'])
                        for mention in mentions['MENTIONEES']:
                            arrData.append({'S':mention['S'], 'E':mention['E'], 'M':op.param1})
                        contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')})
                    line.sendMessage(op.param1, line.settings['autoBlock']['message'], contentMetadata)
                elif '@!' not in line.settings['autoBlock']['message']: line.sendMessage(op.param1, line.settings['autoBlock']['message'].format(displayName=line.getContact(op.param1).displayName))
                else: line.sendMention(op.param1, line.settings['autoBlock']['message'].format(displayName=line.getContact(op.param1).displayName), [op.param1])
                line.blockContact(op.param1)
            elif line.settings['autoAdd']['image']['status']:
                if line.settings['autoAdd']['image']['path'] != "":
                    path = line.settings['autoAdd']['image']['path']
                    line.sendImage(op.param1, path)
                else:
                    profile = line.getContact(op.param1)
                    if profile.pictureStatus:
                        path = 'https://obs.line-scdn.net/' + profile.pictureStatus
                    else:
                        path = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
                    line.sendImageWithURL(op.param1, path)
            if line.settings['autoAdd']['status']:
                if not line.settings['autoBlock']['status']:
                    if line.settings['autoAdd']['reply']:
                        if line.settings['autoAdd']['contentMetadata'] != {}:
                            contentMetadata = {"REPLACE": line.settings['autoAdd']['contentMetadata']['REPLACE'], "STICON_OWNERSHIP": line.settings['autoAdd']['contentMetadata']['STICON_OWNERSHIP']}
                            if '@!' in line.settings['autoAdd']['message']:
                                arrData = []
                                mentions = ast.literal_eval(line.settings['autoAdd']['contentMention']['MENTION'])
                                for mention in mentions['MENTIONEES']:
                                    arrData.append({'S':mention['S'], 'E':mention['E'], 'M':op.param1})
                                contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')})
                            line.sendMessage(op.param1, line.settings['autoAdd']['message'], contentMetadata)
                        elif '@!' not in line.settings['autoAdd']['message']: line.sendMessage(op.param1, line.settings['autoAdd']['message'].format(displayName=line.getContact(op.param1).displayName))
                        else: line.sendMention(op.param1, line.settings['autoAdd']['message'].format(displayName=line.getContact(op.param1).displayName), [op.param1])
            if line.settings['autoAdd']['sticker']['STKID'] != "":
                if not line.settings['autoBlock']['status']:
                    line.sendSticker(op.param1, line.settings['autoAdd']['sticker']["STKVER"], line.settings['autoAdd']['sticker']["STKPKGID"], line.settings['autoAdd']['sticker']["STKID"])
#----------OPERATION NOTIFIED UNREGISTER USER----------#
        elif op.type == 33:
            if line.settings["detectResidPoint"] is not None:
                try:
                    if line.settings["detectResidPoint"].startswith('c'):
                        groups = line.getAllChatMids(True, False).memberChatMids
                        if line.settings["detectResidPoint"] not in groups:
                            line.settings["detectResidPoint"] = None
                            return
                    profile = line.getContact(op.param1)
                    res = "› U S E R  R E S I D\n"
                    res += "\nUser: @!"
                    res += "\nMid: {}".format(profile.mid)
                    res += "\nName: {}".format(profile.displayName)
                    line.sendMention(line.settings["detectResidPoint"], res, [profile.mid])
                    if profile.pictureStatus:
                        line.sendLiffImage(line.settings["detectResidPoint"], 'https://obs.line-scdn.net/' + profile.pictureStatus, line.settings["setFlag"]["icon"], " Profile Picture")
                    time.sleep(0.5)
                    line.sendContact(line.settings["detectResidPoint"], profile.mid)
                except:
                    pass
#----------OPERATION NOTIFIED UPDATE GROUP----------#
        elif op.type == 122:
            if not checkAccess(op.param2):
                if op.param3 == "4":
                    if op.param1 in line.protect["proQr"] or op.param2 in line.protect["blacklist"]:
                        deleteOtherFromChat(op.param1, [op.param2])
                        group = line.getChats([op.param1], False, False).chats[0]
                        if group.extra.groupExtra.preventedJoinByTicket == False:
                            group.extra.groupExtra.preventedJoinByTicket = True
                            line.updateChat(group, 4)
                        addBlacklist(op.param2, op.param1)
#----------OPERATION NOTIFIED INVITE INTO GROUP----------#
        elif op.type == 124:
            if line.settings['autoJoin']['kickpy'] and line.profile.mid in op.param3:
                line.acceptChatInvitation(op.param1)
                groups = line.getChats([op.param1], True, False).chats[0]
                for mem in groups.extra.groupExtra.memberMids:
                    try:
                        if checkAccess(mem) or mem == line.profile.mid or mem == sozi:
                            continue
                        line.deleteOtherFromChat(op.param1, [mem])
                        time.sleep(0.8)
                    except:
                        break

            elif line.settings['autoJoin']['kickjs'] and line.profile.mid in op.param3:
                group = make_list(line.getChats([op.param1], True, False).chats[0].extra.groupExtra.memberMids)
                parsed_len = len(group)//140+1
                target = []
                for point in range(parsed_len):
                    cm = 'lib/javascript/dual.js gid={} token={} appName="{}" userAgent="{}" method=kick'.format(op.param1, line.authToken, line.server.APP_NAME, line.server.USER_AGENT)
                    for g in group[point*140:(point+1)*140]:
                        if g in line.profile.mid or g in sozi:
                            continue
                        elif checkAccess(g):
                            continue
                        cm += ' uid={}'.format(g)
                    target.append(cm)
                line.acceptChatInvitation(op.param1)
                for exe in target:
                    print(exe)
                    success = execute_js(exe)
                    time.sleep(5)
                
            elif line.settings['autoJoin']['status'] and line.profile.mid in op.param3:
                line.acceptChatInvitation(op.param1)
                if line.settings['autoJoin']['reply']:
                    if line.settings['autoJoin']['contentMetadata'] != {}:
                        contentMetadata = {"REPLACE": line.settings['autoJoin']['contentMetadata']['REPLACE'], "STICON_OWNERSHIP": line.settings['autoJoin']['contentMetadata']['STICON_OWNERSHIP']}
                        if '@!' in line.settings['autoJoin']['message']:
                            arrData = []
                            mentions = ast.literal_eval(line.settings['autoJoin']['contentMention']['MENTION'])
                            for mention in mentions['MENTIONEES']:
                                arrData.append({'S':mention['S'], 'E':mention['E'], 'M':op.param2})
                            contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')})
                        line.sendMessage(op.param1, line.settings['autoJoin']['message'], contentMetadata)
                    elif '@!' not in line.settings['autoJoin']['message']: line.sendMode("empty", op.param1, op.param2, "AUTO JOIN GROUP", line.settings['autoJoin']['message'].format(chatName=line.getChats([op.param1], False, False).chats[0].chatName, displayName=line.getContact(op.param2).displayName))
                    else: line.sendMention(op.param1, line.settings['autoJoin']['message'].format(chatName=line.getChats([op.param1], False, False).chats[0].chatName, displayName=line.getContact(op.param2).displayName), [op.param2])
                gc = line.getChats([op.param1], False, False).chats[0]
                gc.notificationDisabled = True
                line.updateChat(gc, 8)

            elif op.param2 in line.protect["blacklist"] and line.profile.mid not in op.param3:
                if not checkAccess(op.param2):
                    if not line.settings["blmode"]:
                        if not checkProtect(op.param1):
                            return
                    invitess = op.param3.split('\x1e')
                    def addBl(invitess):
                        for ii in invitess:
                            if not checkAccess(ii):
                                addBlacklist(ii, op.param1, forceMax=True)
                    threading.Thread(target=addBl, args=(invitess,)).start()
                    if len(invitess) >= 5:
                        invites = invitess[0:5]
                    else:
                        invites = invitess
                    for invite in invites:
                        line.cancelChatInvitation(op.param1, [invite])
                    time.sleep(0.8)
                    groups = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in groups.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2], "i'll kick u cuz u has been 𝗕𝗮𝗻𝗻𝗲𝗱!!")
                    addBlacklist(op.param2, op.param1)
                    
            elif op.param1 in line.protect["proInv"] and line.profile.mid not in op.param3:
                if not checkAccess(op.param2):
                    invitess = op.param3.split('\x1e')
                    def addBl(invitess):
                        for ii in invitess:
                            if not checkAccess(ii):
                                addBlacklist(ii, op.param1)
                    threading.Thread(target=addBl, args=(invitess,)).start()
                    if len(invitess) >= 5:
                        invites = invitess[0:5]
                    else:
                        invites = invitess
                    for invite in invites:
                        line.cancelChatInvitation(op.param1, [invite])
                    time.sleep(0.8)
                    groups = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in groups.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2])
                    addBlacklist(op.param2, op.param1)
#----------OPERATION NOTIFIED LEAVE GROUP----------#
        elif op.type == 128:
            if op.param1 in line.setts["notifJoin"]:
                if op.param2 in line.setts["notifJoin"][op.param1]:
                    line.setts["notifJoin"][op.param1].remove(op.param2)
            if op.param1 not in line.setts["spamGreetLeave"]:
                line.setts["spamGreetLeave"][op.param1] = {'time': time.time(), 'floods': 0, 'ex': False}
            if time.time() - line.setts["spamGreetLeave"][op.param1]["time"] <= 10:
                line.setts["spamGreetLeave"][op.param1]["floods"] += 1
                if line.setts["spamGreetLeave"][op.param1]["floods"] >= 2: return
                line.sendLeaveMessage(op)
            else:
                line.setts["spamGreetLeave"][op.param1]["floods"] = 1
                line.sendLeaveMessage(op)
            line.setts["spamGreetLeave"][op.param1]["time"] = time.time()
                        
#----------OPERATION NOTIFIED JOIN GROUP----------#
        elif op.type == 130:
            if op.param2 in line.protect["blacklist"]:
                if not checkAccess(op.param2):
                    if not line.settings["blmode"]:
                        if not checkProtect(op.param1):
                            return
                    time.sleep(0.8)
                    group = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in group.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2], "i'll kick u cuz u has been 𝗕𝗮𝗻𝗻𝗲𝗱!!")
                    if group.extra.groupExtra.preventedJoinByTicket == False:
                        group.extra.groupExtra.preventedJoinByTicket = True
                        line.updateChat(group, 4)
                    return
            elif op.param1 not in line.setts["notifJoin"]:
                line.setts["notifJoin"][op.param1] = []
            if op.param2 not in line.setts["notifJoin"][op.param1]:
                if op.param1 not in line.setts["spamGreetWelcome"]:
                    line.setts["spamGreetWelcome"][op.param1] = {'time': time.time(), 'floods': 0, 'ex': False}
                if time.time() - line.setts["spamGreetWelcome"][op.param1]["time"] <= 10:
                    line.setts["spamGreetWelcome"][op.param1]["floods"] += 1
                    if line.setts["spamGreetWelcome"][op.param1]["floods"] >= 2: return
                    line.sendWelcomeMessage(op)
                else:
                    line.setts["spamGreetWelcome"][op.param1]["floods"] = 1
                    line.sendWelcomeMessage(op)
                line.setts["spamGreetWelcome"][op.param1]["time"] = time.time()

#----------OPERATION NOTIFIED KICKOUT GROUP----------#
        elif op.type == 133:
            if op.param1 in line.setts["notifJoin"]:
                if op.param2 in line.setts["notifJoin"][op.param1]:
                    line.setts["notifJoin"][op.param1].remove(op.param2)
            if line.profile.mid in op.param3:
                if line.settings["detectKickPoint"] is not None:
                    if line.settings["detectKickPoint"].startswith('c'):
                        groups = line.getAllChatMids(True, False).memberChatMids
                        if line.settings["detectKickPoint"] not in groups:
                            line.settings["detectKickPoint"] = None
                            return
                    profile = line.getContact(op.param2)
                    res = "you have been kicked out from group\n"
                    res += "\nUser: @!"
                    res += "\nMid: {}".format(profile.mid)
                    res += "\nGroup: {}".format(line.getChats([op.param1], False, False).chats[0].chatName)
                    line.sendMention(line.settings["detectKickPoint"], res, [profile.mid])
                    line.sendContact(line.settings["detectKickPoint"], profile.mid)
                
                if not checkAccess(op.param2):
                    addBlacklist(op.param2, op.param1)

            elif op.param2 in line.protect["blacklist"]:
                if not checkAccess(op.param2):
                    if not line.settings["blmode"]:
                        if not checkProtect(op.param1):
                            return
                    time.sleep(0.8)
                    gc = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in gc.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2], "i'll kick u cuz u has been 𝗕𝗮𝗻𝗻𝗲𝗱!!")
                            
            elif op.param3 in line.protect["assistlist"]:
                if not checkAccess(op.param2):
                    if not line.settings["backupStaff"]:
                        if not checkProtect(op.param1):
                            return
                    time.sleep(0.8)
                    gc = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in gc.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2], "u kick my staff, u got 𝗕𝗮𝗻𝗻𝗲𝗱!!")
                    addBlacklist(op.param2, op.param1)
                    gc = line.getChats([op.param1], False, True).chats[0]
                    if op.param3 not in gc.extra.groupExtra.inviteeMids:
                        inviteIntoChat(op.param1, [op.param3])
            
            elif op.param3 in line.protect["whitelist"]:
                if not checkAccess(op.param2):
                    if not line.settings["backupStaff"]:
                        if not checkProtect(op.param1):
                            return
                    time.sleep(0.8)
                    gc = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in gc.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2], "u kick my staff, u got 𝗕𝗮𝗻𝗻𝗲𝗱!!")
                    addBlacklist(op.param2, op.param1)

            elif op.param1 in line.protect["proKick"]:
                if not checkAccess(op.param2):
                    gc = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in gc.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2])
                    addBlacklist(op.param2, op.param1)
                            
#----------OPERATION NOTIFIED CANCEL GROUP----------#
        elif op.type == 126:
            if line.profile.mid in op.param3:
                if not checkAccess(op.param2):
                    addBlacklist(op.param2, op.param1)

            elif op.param2 in line.protect["blacklist"]:
                if not checkAccess(op.param2):
                    if not line.settings["blmode"]:
                        if not checkProtect(op.param1):
                            return
                    time.sleep(0.8)
                    gc = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in gc.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2], "i'll kick u cuz u has been 𝗕𝗮𝗻𝗻𝗲𝗱!!")
            
            elif op.param3 in line.protect["assistlist"]:
                if not checkAccess(op.param2):
                    if not line.settings["backupStaff"]:
                        if not checkProtect(op.param1):
                            return
                    time.sleep(0.8)
                    gc = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in gc.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2], "u cancel my staff, u got 𝗕𝗮𝗻𝗻𝗲𝗱!!")
                    addBlacklist(op.param2, op.param1)
                    gc = line.getChats([op.param1], False, True).chats[0]
                    if op.param3 not in gc.extra.groupExtra.inviteeMids:
                        inviteIntoChat(op.param1, [op.param3])
            
            elif op.param3 in line.protect["whitelist"]:
                if not checkAccess(op.param2):
                    if not line.settings["backupStaff"]:
                        if not checkProtect(op.param1):
                            return
                    time.sleep(0.8)
                    gc = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in gc.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2], "u cancel my staff, u got 𝗕𝗮𝗻𝗻𝗲𝗱!!")
                    addBlacklist(op.param2, op.param1)

            elif op.param1 in line.protect["proCancel"]:
                if not checkAccess(op.param2):
                    gc = line.getChats([op.param1], True, False).chats[0]
                    if op.param2 in gc.extra.groupExtra.memberMids:
                        deleteOtherFromChat(op.param1, [op.param2])
                    addBlacklist(op.param2, op.param1)
        elif op.type in [123, 125, 132]:
            if op.type == 123:
                line.settings["amountBackup"]["invite"] += 1
                line.settings["amountBackup"]["totalInvite"] += 1
            elif op.type == 125:
                line.settings["amountBackup"]["cancel"] += 1
                line.settings["amountBackup"]["totalCancel"] += 1
            elif op.type == 132:
                line.settings["amountBackup"]["kick"] += 1
                line.settings["amountBackup"]["totalKick"] += 1
        elif op.type == 22:
            if line.profile.mid in op.param3:
                if line.settings["autoLeave"]["status"]:
                    if line.settings["autoLeave"]["reply"]:
                        if line.settings['autoLeave']['contentMetadata'] != {}:
                            contentMetadata = {"REPLACE": line.settings['autoLeave']['contentMetadata']['REPLACE'], "STICON_OWNERSHIP": line.settings['autoLeave']['contentMetadata']['STICON_OWNERSHIP']}
                            if '@!' in line.settings['autoLeave']['message']:
                                arrData = []
                                mentions = ast.literal_eval(line.settings['autoLeave']['contentMention']['MENTION'])
                                for mention in mentions['MENTIONEES']:
                                    arrData.append({'S':mention['S'], 'E':mention['E'], 'M':op.param2})
                                contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')})
                            line.sendMessage(op.param1, line.settings['autoLeave']['message'], contentMetadata)
                        elif '@!' in line.settings["autoLeave"]["message"]: line.sendMention(op.param1, line.settings["autoLeave"]["message"], [op.param2])
                        else: line.sendMessage(op.param1, line.settings["autoLeave"]["message"])
                    line.leaveRoom(op.param1)
#----------OPERATION SEND MESSAGES----------#
        elif op.type == 25:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            to       = sender if not msg.toType and sender != line.profile.mid else receiver
            txt      = text.lower()
            cmd      = command(text)
            setKey   = line.settings['setKey']['key'] if line.settings['setKey']['status'] else ''
            if text in line.setts["tmp_text"]:
                return line.setts["tmp_text"].remove(text)
                
            if msg.toType == 0:
                if msg.contentType == 0:
                    if to in line.settings["getPc"]:
                        if '@Sozi' in text: isiText = text.replace("@Sozi","@!")
                        else: isiText = text
                        if isiText != line.settings["autoRespond"]["message"]:
                            del line.settings["getPc"][to]
                            
            if msg.contentType == 0: # Content type is text
                if txt == 'chatbot':
                    if to in line.settings['offbot'] or line.settings['offbot2']: res = 'Status: ✔︎'
                    else: res = 'Status: ✘'
                    isi = ['Mute', 'Unmute', 'Mute add <num>', 'Mute del <num>', 'Mute All <on/off>', 'Mute List']
                    res += "\n\n{}".format(looping_command(setKey.title(), "› C O M M A N D", isi))
                    isi2 = ['Mute add 1,2,3-6', 'Mute del 1,2,3-6']
                    res += "\n\n{}".format(looping_command(setKey.title(), "› Example multi add / del", isi2))
                    line.sendMode(msg, to, sender, cmd, res)
                if cmd.startswith('mute'):
                    textt = removeCmd(text, setKey)
                    texttl = textt.lower()
                    if cmd == 'mute':
                        if to not in line.settings["offbot"]:
                            line.settings["offbot"].append(to)
                            line.sendFooter(to, "Silent mode diaktifkan..")
                        else:
                            line.sendFooter(to, 'Silent mode sedang aktif..')
                    elif texttl.startswith('all '):
                        textts = texttl[4:]
                        if textts == 'on':
                            if not line.settings['offbot2']:
                                line.settings['offbot2'] = True
                            sendToggle(to, "CHAT BOT", "Chat Bot\nStatus: ✓", "", True)
                        elif textts == 'off':
                            if line.settings['offbot2']:
                                line.settings['offbot2'] = False
                            sendToggle(to, "CHAT BOT", "Chat Bot\nStatus: ✘", "", False)
                    elif texttl == 'list':
                        if line.settings['offbot2']:
                            return line.sendMode(msg, to, sender, cmd, 'Mode Mute has been activated in all groups')
                        groups = line.settings["offbot"]
                        if groups:
                            res = '› L I S T\n'
                            no = 0
                            for group in groups:
                                no += 1
                                if group.startswith('c'):
                                    group = line.getChats([group], True, False).chats[0]
                                    res += '\n{}. {}//{}'.format(no, group.chatName, len(group.extra.groupExtra.memberMids))
                                elif group.startswith('u'):
                                    res += '\n{}. {}'.format(no, line.getContact(group).displayName)
                            line.sendMode(msg, to, sender, cmd, res)
                        else:
                            line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                    elif texttl.startswith('add '):
                        sep = textt.split(' ')
                        if len(sep) == 2:
                            groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                            targets = filter_target(sep[1], groups)
                            res = "› A D D E D\n"
                            no = 0
                            if targets:
                                for target in targets:
                                    no += 1
                                    group = line.getChats([target], True, False).chats[0]
                                    if target not in line.settings["offbot"]:
                                        line.settings["offbot"].append(target)
                                        res += "\n{}. {} > Added".format(no, group.chatName)
                                    else:
                                        res += "\n{}. {} > Already".format(no, group.chatName)
                                line.sendMode(msg, to, sender, cmd, res)
                            else:
                                line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                    elif texttl.startswith('del '):
                        sep = textt.split(' ')
                        if len(sep) == 2:
                            targets = filter_target(sep[1], line.settings["offbot"])
                            res = "› D E L E T E D\n"
                            no = 0
                            if targets:
                                for target in targets:
                                    no += 1
                                    group = line.getChats([target], True, False).chats[0]
                                    if target in line.settings["offbot"]:
                                        line.settings["offbot"].remove(target)
                                        res += "\n{}. {} > Deleted".format(no, group.chatName)
                                    else:
                                        res += "\n{}. {} > Not Found".format(no, group.chatName)
                                line.sendMode(msg, to, sender, cmd, res)
                            else:
                                line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                if cmd == 'unmute':
                    if to in line.settings["offbot"]:
                        line.settings["offbot"].remove(to)
                        line.sendFooter(to, 'Silent mode dinonaktifkan..')
                    else:
                        line.sendFooter(to, 'Selfbot sedang aktif..')
                if to in line.settings["offbot"] or line.settings["offbot2"]:
                    return
                regex = re.findall(r'(https?://\S+)', text)
                share_link = []
                for link in regex:
                    if link not in share_link:
                        share_link.append(link)
                        shr = shareurl_media(to, txt, link, msg_id)
                        if shr: break
                if line.setts["detectID"]["mid"]:
                    line.mid_list(to, text, sender, 4)
                if line.setts["detectID"]["gid"]:
                    gid_regex = line.server.GID_REGEX.findall(text)
                    doneGid = []
                    for gid in gid_regex:
                        if gid not in doneGid:
                            line.sendFooter(to, str(line.getChats([gid], False, False).chats[0].chatName))
                            doneGid.append(gid)
                if txt in line.stickers:
                    line.sticker_list(to, txt, sender, 5)
                if txt in line.textsx:
                    line.text_list(to, txt, sender, msg_id, 5)
                if txt in line.protect['multi_list']:
                    line.multi_list(to, txt, sender, 10)
                if txt in line.pictures:
                    line.picture_list(to, txt, sender, msg_id, 10)
                if txt in line.audsx:
                    line.audio_list(to, txt, sender, 10)
                if txt in line.vidsx:
                    line.video_list(to, txt, sender, 10)
                if txt in line.protect['contact_list']:
                    if msg.toType == 2:
                        line.invite_list(to, txt, sender, 20)
                if line.setts["textss"]['status']:
                    name   = line.setts["textss"]['name']
                    if 'STICON_OWNERSHIP' in msg.contentMetadata:
                        getEmoji = line.metadataFilter(msg.contentMetadata, 0, type='emoji')
                        line.textsx[name] = {"message": text, "contentMetadata": getEmoji}
                        getEmoji2 = line.metadataFilter(getEmoji, len('Save successfully text\nText: %s\nRespon: ' % name), type='emoji2')
                        if "@!" in text:
                            line.textsx[name] = {"message": text, "contentMetadata": getEmoji, "contentMention": line.metadataFilter(getEmoji, text=text, type='mention')}
                            getEmoji2.update(line.metadataFilter(getEmoji, text='Save successfully text\nText: %s\nRespon: %s' % (name, text), type='mention'))
                        line.sendReplyMessage(to, 'Save successfully text\nText: %s\nRespon: %s' % (name, text), getEmoji2, msgIds=msg_id)
                    else:
                        line.textsx[name] = text
                        line.sendFooter(to, 'Save successfully text\nText: %s\nRespon: %s' % (name, text), reply=True)
                    line.setts["textss"]['status'] = False
                try:
                    executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)
                except TalkException as talk_error:
                    logError(talk_error)
                    if talk_error.code in [7, 8, 20]:
                        sys.exit(1)
                    line.sendMessage(to, '「 ERROR ✘ 」\nTalkException, Code: ' + str(talk_error.code) + '\nReason: '+ str(talk_error.reason))
                    time.sleep(3)
                except Exception as error:
                    logError(error)
                    line.sendMessage(to, '「 ERROR ✘ 」\n'+ str(error))
                    time.sleep(3)
                    
            elif msg.contentType == 1: # Content type image
                time.sleep(1)
                if line.setts["upImage"]:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/upimage.jpg')
                    data = imgBB(path)
                    line.sendFooter(to, 'Convert Image To Url\nUrl: %s' % (data["data"]["url"]), reply=True)
                    line.setts["upImage"] = False
                    line.deleteFile(path)
                elif line.setts["upBackground"]:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/upimage.jpg')
                    data = imgBB(path)
                    line.settings["tempBackground"] = data["data"]["url"]
                    line.sendFooter(to, 'Change Background Image\nUrl: %s' % (data["data"]["url"]), reply=True)
                    line.setts["upBackground"] = False
                    line.deleteFile(path)
                elif line.setts["upStory"]:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/uploadstory.bin')
                    data = line.uploadObjStory(path, 'image')
                    line.updateStory(data["obsOid"], data["xObsHash"], mediaType='image')
                    line.sendMode(msg, to, sender, "Upload Story", 'Upload Story\nStatus: ✓')
                    line.setts['upStory'] = False
                    line.deleteFile(path)
                elif line.setts["pictss"]["status"]:
                    name = line.setts["pictss"]["name"]
                    image = line.downloadObjectMsg(msg_id, saveAs="json/{}-image.bin".format(name))
                    line.pictures[name] = image
                    line.sendMode(msg, to, sender, "image", 'Save successfully gambar\nText: %s' % (name))
                    line.setts["pictss"]['status'] = False
                elif line.setts["autoAddImage"]:
                    path = line.downloadObjectMsg(msg_id, saveAs="json/autoadd-image.bin")
                    line.settings["autoAdd"]["image"]["path"] = path
                    line.sendMode(msg, to, sender, "image", 'Auto Respon Add Image saved successfully')
                    line.setts["autoAddImage"] = False
                elif line.settings["setFlag"]["status"]:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/line.jpg')
                    data = imgBB(path)
                    line.settings["setFlag"]["icon"] = data["data"]["url"]
                    line.sendFooter(to, 'Change Flag Icon\nUrl: %s' % (data["data"]["url"]), reply=True)
                    line.settings["setFlag"]["status"] = False
                    line.deleteFile(path)
                elif line.settings['changePictureProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                    line.updateProfilePicture(path)
                    line.sendMode(msg, to, sender, "image", 'Update Profile Picture\nStatus: ✓')
                    line.settings['changePictureProfile'] = False
                    line.deleteFile(path)
                elif line.settings['changeCoverProfile']:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                    line.updateProfileCover(path)
                    line.sendMode(msg, to, sender, "image", 'Update Profile Cover\nStatus: ✓')
                    line.settings['changeCoverProfile'] = False
                    line.deleteFile(path)
                elif line.settings['changeCoverVideo']["image"]:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                    res = 'Send the video...\ntype `{key}Abort` to cancel this\n\nsend pictures and videos with share/forward'.format(key=setKey.title())
                    line.settings['changeCoverVideo']["image"] = False
                    line.settings['changeCoverVideo']["video"] = True
                    line.sendMessage(to, res)
                elif to in line.settings['changeGroupPicture'] and msg.toType == 2:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/grouppicture.jpg')
                    line.updateGroupPicture(to, path)
                    line.settings['changeGroupPicture'].remove(to)
                    time.sleep(0.1)
                    line.sendMode(msg, to, sender, "image", 'Update Group Picture\nStatus: ✓')
                    line.deleteFile(path)
                elif to in line.settings['changeGroupCover'] and msg.toType == 2:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/groupcover.jpg')
                    line.updateGroupCover(to, path)
                    line.settings['changeGroupCover'].remove(to)
                    time.sleep(0.1)
                    line.sendMode(msg, to, sender, "image", 'Update Group Cover\nStatus: ✓')
                    line.deleteFile(path)
                elif to in line.setts["uploadTL"]:
                    if sender == line.setts["uploadTL"][to]["sender"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/imageTL.bin')
                        objectId = line.uploadObjHome(path, type='image', returnAs='objId', target=to)
                        line.deleteFile(path)
                        line.setts["uploadTL"][to]["media"].append({
                        	'type': 'PHOTO',
                        	'objectId': objectId
                        })
                        line.setts["uploadTL"][to]["total"] -= 1
                        if line.setts["uploadTL"][to]["total"] == 0:
                            post = line.createPostMedia(line.setts["uploadTL"][to]["description"], media=line.setts["uploadTL"][to]["media"])
                            line.sendPostToTalk(to, post["result"]["feed"]["post"]["postInfo"]["postId"])
                            del line.setts["uploadTL"][to]
                        else:
                            line.sendMessage(to, 'Send {} Image/Video\nType `{key}Abort` to cancel this'.format(line.setts["uploadTL"][to]["total"], key=setKey.title()))
                elif to in line.setts["uploadNote"]:
                    if sender == line.setts["uploadNote"][to]["sender"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/imageNote.bin')
                        objectId = line.uploadObjHome(path, type='image', returnAs='objId', target=to)
                        line.deleteFile(path)
                        line.setts["uploadNote"][to]["media"].append({
                        	'type': 'PHOTO',
                        	'objectId': objectId
                        })
                        line.setts["uploadNote"][to]["total"] -= 1
                        if line.setts["uploadNote"][to]["total"] == 0:
                            line.createPostGroupMedia(to, line.setts["uploadNote"][to]["description"], media=line.setts["uploadNote"][to]["media"])
                            del line.setts["uploadNote"][to]
                        else:
                            line.sendMessage(to, 'Send {} Image/Video\nType`{key}Abort` to cancel this'.format(line.setts["uploadNote"][to]["total"], key=setKey.title()))
                elif line.setts["bcImage"]["toFriend"]:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/bcToFriend.bin')
                    friends = line.getBcFriend()
                    line.sendFooter(to, 'Loading...')
                    success = []
                    failure = []
                    for friend in friends:
                        try:
                            line.sendImage(friend, path)
                            success.append(friend)
                        except:
                            failure.append(friend)
                            continue
                        time.sleep(0.8)
                    line.setts["bcImage"]["toFriend"] = False
                    line.sendMode(msg, to, sender, "image", 'Broadcast Image Friends\nSuccess: {}x\nFailed: {}x'.format(len(success), len(failure)))
                    line.deleteFile(path)
                elif line.setts["bcImage"]["toGroup"]:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/bcToGroup.bin')
                    groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                    line.sendFooter(to, 'Loading...')
                    success = []
                    failure = []
                    for group in groups:
                        if group not in line.settings["bcFilter"]:
                            try:
                                line.sendImage(group, path)
                                success.append(group)
                            except:
                                 failure.append(group)
                                 continue
                            time.sleep(0.8)
                    line.setts["bcImage"]["toGroup"] = False
                    line.sendMode(msg, to, sender, "image", 'Broadcast Image Group\nSuccess: {}x\nFailed: {}x'.format(len(success), len(failure)))
                    line.deleteFile(path)
                elif line.setts["bcImage"]["toAll"]:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/bcToAll.bin')
                    gogo = make_list(line.getAllChatMids(True, False).memberChatMids) + line.getBcFriend()
                    line.sendFooter(to, 'Loading...')
                    success = []
                    failure = []
                    for go in gogo:
                        if go not in line.settings["bcFilter"]:
                            try:
                                line.sendImage(go, path)
                                success.append(go)
                            except:
                                 failure.append(go)
                                 continue
                            time.sleep(0.8)
                    line.setts["bcImage"]["toAll"] = False
                    line.sendMode(msg, to, sender, "image", 'Broadcast Image All\nSuccess: {}x\nFailed: {}x'.format(len(success), len(failure)))
                    line.deleteFile(path)
                elif line.setts['greets']['wImage']:
                    path = line.downloadObjectMsg(msg_id, saveAs='json/wImage.bin')
                    line.settings['greet']['join']['imagePath'] = path
                    line.sendMode(msg, to, sender, "image", 'Set Welcome Image\nStatus: ✓')
                    line.setts['greets']['wImage'] = False
                elif line.setts['greets']['lImage']:
                    path = line.downloadObjectMsg(msg_id, saveAs='json/lImage.bin')
                    line.settings['greet']['leave']['imagePath'] = path
                    line.sendMode(msg, to, sender, "image", 'Set Leave Image\nStatus: ✓')
                    line.setts['greets']['lImage'] = False
                    
            elif msg.contentType == 2: # Content type video
                if line.settings["changevp"] == True:
                    contact = line.getProfile()
                    pict = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                    path = line.downloadFileURL(pict)
                    path1 = line.downloadObjectMsg(msg_id)
                    line.settings["changevp"] = False
                    line.updateVideoAndPictureProfile(path, path1)
                    line.sendMode(msg, to, sender, "video", 'Update Video Profile\nStatus: ✓')
                    line.deleteFile(path)
                    line.deleteFile(path1)
                elif line.settings['changeCoverVideo']["video"]:
                    pict = "tmp/cover.jpg"
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/covervideo.mp4')
                    line.updateProfileCoverVideo(pict, path)
                    line.sendMode(msg, to, sender, "video", 'Update Cover Video\nStatus: ✓')
                    line.settings['changeCoverVideo']["video"] = False
                    line.deleteFile(path)
                    line.deleteFile(pict)
                elif line.setts["upStory"]:
                    path = line.downloadObjectMsg(msg_id, saveAs='tmp/uploadstory.bin')
                    data = line.uploadObjStory(path, 'video')
                    line.updateStory(data["obsOid"], data["xObsHash"], mediaType='video')
                    line.sendMode(msg, to, sender, "Upload Story", 'Upload Story\nStatus: ✓')
                    line.setts['upStory'] = False
                    line.deleteFile(path)
                elif line.setts["vidss"]["status"]:
                    name = line.setts["vidss"]["name"]
                    video = line.downloadObjectMsg(msg_id, saveAs="tmp/{}-video.bin".format(name))
                    line.vidsx[name] = video
                    line.sendMode(msg, to, sender, "video", 'Save successfully video\nText: %s' % (name))
                    line.setts["vidss"]['status'] = False
                elif to in line.setts["uploadTL"]:
                    if sender == line.setts["uploadTL"][to]["sender"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/imageTL.bin')
                        objectId = line.uploadObjHome(path, type='video', returnAs='objId', target=to)
                        line.deleteFile(path)
                        line.setts["uploadTL"][to]["media"].append({
                        	'type': 'VIDEO',
                        	'objectId': objectId
                        })
                        line.setts["uploadTL"][to]["total"] -= 1
                        if line.setts["uploadTL"][to]["total"] == 0:
                            post = line.createPostMedia(line.setts["uploadTL"][to]["description"], media=line.setts["uploadTL"][to]["media"])
                            line.sendPostToTalk(to, post["result"]["feed"]["post"]["postInfo"]["postId"])
                            del line.setts["uploadTL"][to]
                        else:
                            line.sendMessage(to, 'Send {} Image/Video\nType `{key}Abort` to cancel this'.format(line.setts["uploadTL"][to]["total"], key=setKey.title()))
                elif to in line.setts["uploadNote"]:
                    if sender == line.setts["uploadNote"][to]["sender"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/imageNote.bin')
                        objectId = line.uploadObjHome(path, type='video', returnAs='objId', target=to)
                        line.deleteFile(path)
                        line.setts["uploadNote"][to]["media"].append({
                        	'type': 'VIDEO',
                        	'objectId': objectId
                        })
                        line.setts["uploadNote"][to]["total"] -= 1
                        if line.setts["uploadNote"][to]["total"] == 0:
                            line.createPostGroupMedia(to, line.setts["uploadNote"][to]["description"], media=line.setts["uploadNote"][to]["media"])
                            del line.setts["uploadNote"][to]
                        else:
                            line.sendMessage(to, 'Send {} Image/Video\nType `{key}Abort` to cancel this'.format(line.setts["uploadNote"][to]["total"], key=setKey.title()))
                            
            elif msg.contentType == 3: # Content type audio
                if line.setts["audss"]["status"]:
                    name = line.setts["audss"]["name"]
                    audio = line.downloadObjectMsg(msg_id, saveAs="tmp/{}-audio.bin".format(name))
                    line.audsx[name] = audio
                    line.sendMode(msg, to, sender, "audio", 'Save successfully audio\nText: %s' % (name))
                    line.setts["audss"]['status'] = False

            elif msg.contentType == 6: # Content type call group
                if msg.contentMetadata['GC_EVT_TYPE'] == 'S':
                    line.setts["detectCall"][to] = time.time()
                elif msg.contentMetadata['GC_EVT_TYPE'] == 'E':
                    if to in line.setts["detectCall"]:
                        del line.setts["detectCall"][to]
                        
            elif msg.contentType == 7: # Content type sticker
                if line.settings["setcommand"]["mentionStiker"]["stkid"] != "":
                    if msg.contentMetadata['STKID'] == line.settings["setcommand"]["mentionStiker"]["stkid"]:
                        if msg.toType == 1:
                            room = line.getCompactRoom(to)
                            members = [mem.mid for mem in room.contacts]
                        elif msg.toType == 2:
                            group = line.getChats([to], True, False)
                            members = make_list(group.chats[0].extra.groupExtra.memberMids)
                        else:
                            members = None
                        if members:
                            if line.settings["setcommand"]["mentionAllEmoji"]["productId"] is not None:
                                line.mentionMembersEmoticon(to, line.settings["setcommand"]["mentionAllEmoji"]["productId"], members, msgIds=msg_id)
                            else:
                                line.mentionMembers(to, members, msgIds=msg_id)
                if line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKID"] != "180":
                    if msg.contentMetadata['STKID'] == line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKID"]:
                        if msg.toType == 1:
                            room = line.getCompactRoom(to)
                            members = [mem.mid for mem in room.contacts]
                        elif msg.toType == 2:
                            group = line.getChats([to], True, False)
                            members = make_list(group.chats[0].extra.groupExtra.memberMids)
                        else:
                            members = None
                        if members:
                            line.fakeMentionSticker(to, int(msg.contentMetadata['STKVER']), int(msg.contentMetadata['STKPKGID']), int(msg.contentMetadata['STKID']), members)
                if line.settings['checkSticker']:
                    if not line.settings["offbot2"] and to not in line.settings["offbot"]:
                        res = 'Sticker ID: ' + msg.contentMetadata['STKID']
                        res += '\nSticker Packages ID: ' + msg.contentMetadata['STKPKGID']
                        res += '\nSticker Version: ' + msg.contentMetadata['STKVER']
                        res += '\nSticker Link: https://line.me/R/shop/detail/' + msg.contentMetadata['STKPKGID']
                        line.sendFooter(to, res, reply=True)
                if line.settings["setcommand"]["invites"]["stkid"] == msg.contentMetadata['STKID']:
                    if msg.toType == 2:
                        if msg.relatedMessageId is not None:
                            group = line.getChats([to], True, True).chats[0]
                            members = group.extra.groupExtra.memberMids
                            pending = group.extra.groupExtra.inviteeMids
                            friend = line.getAllContactIds()
                            data = line.getReplyMessage(to, msg.relatedMessageId)
                            if data is not None:
                                if data._from != line.profile.mid:
                                    if data._from not in friend:
                                        line.findAndAddContactsByMid(data._from)
                                        time.sleep(0.8)
                                    if data._from in members:
                                        line.sendMention(to, "› @! already joined group", [data._from])
                                    elif data._from in pending:
                                        line.sendMention(to, "› @! already invited", [data._from])
                                    else:
                                        inviteIntoChat(to, [data._from])
                if line.settings["setcommand"]["kicks"]["stkid"] == msg.contentMetadata['STKID']:
                    if msg.toType == 2:
                        if msg.relatedMessageId is not None:
                            group = line.getChats([to], True, True).chats[0]
                            members = group.extra.groupExtra.memberMids
                            data = line.getReplyMessage(to, msg.relatedMessageId)
                            if data is not None:
                                if data._from != line.profile.mid:
                                    if data._from not in members:
                                        line.sendMention(to, "› @! not in group", [data._from])
                                    else:
                                        deleteOtherFromChat(to, [data._from])
                elif line.settings["autoComment"]["setsticker"]:
                    line.settings["autoComment"]["sticker"] = {"STKID": msg.contentMetadata['STKID'], "STKPKGID": msg.contentMetadata['STKPKGID'], "STKVER": msg.contentMetadata['STKVER']}
                    line.settings["autoComment"]["setsticker"] = False
                    line.sendMode(msg, to, sender, "sticker", 'Save successfully sticker as auto comment\nType {key}AutoComment delSticker to remove sticker'.format(key=setKey.title()))
                elif line.setts["autoAddSticker"]:
                    line.settings["autoAdd"]["sticker"]["STKID"]  = msg.contentMetadata['STKID']
                    line.settings["autoAdd"]["sticker"]["STKPKGID"] = msg.contentMetadata['STKPKGID']
                    line.settings["autoAdd"]["sticker"]["STKVER"] = msg.contentMetadata['STKVER']
                    line.setts["autoAddSticker"] = False
                    line.sendMode(msg, to, sender, "sticker", 'Save successfully sticker as auto respon add sticker\nType {key}AutoAdd delSticker to remove sticker'.format(key=setKey.title()))
                elif line.setts["tagSticker"]:
                    line.settings["autoRespondMention"]['sticker']["STKID"]  = msg.contentMetadata['STKID']
                    line.settings["autoRespondMention"]['sticker']["STKPKGID"] = msg.contentMetadata['STKPKGID']
                    line.settings["autoRespondMention"]['sticker']["STKVER"] = msg.contentMetadata['STKVER']
                    line.setts["tagSticker"] = False
                    line.sendMode(msg, to, sender, "sticker", 'Save successfully sticker as auto respon tag sticker\nType {key}AutoRespondTag delSticker to remove sticker'.format(key=setKey.title()))
                elif line.setts["stickerss"]['status']:
                    stickerId  = msg.contentMetadata['STKID']
                    stickerPid = msg.contentMetadata['STKPKGID']
                    stickerVer = msg.contentMetadata['STKVER']
                    stickerN   = line.setts["stickerss"]['name']
                    if 'STKOPT' not in msg.contentMetadata:
                        line.stickers[stickerN] = {'STKID': stickerId, 'STKPKGID': stickerPid, 'STKVER': stickerVer}
                    else:
                        stickerOpt = msg.contentMetadata['STKOPT']
                        line.stickers[stickerN] = {'STKID': stickerId, 'STKPKGID': stickerPid, 'STKVER': stickerVer, 'STKOPT': stickerOpt}
                    line.setts["stickerss"]['status'] = False
                    line.sendMode(msg, to, sender, "sticker", 'Save successfully sticker\nText: %s' % (stickerN))
                elif line.setts["greets"]["joinSticker"]:
                    stickerId  = msg.contentMetadata['STKID']
                    stickerPid = msg.contentMetadata['STKPKGID']
                    stickerVer = msg.contentMetadata['STKVER']
                    line.settings["greet"]["join"]["sticker"]["STKID"] = stickerId
                    line.settings["greet"]["join"]["sticker"]["STKPKGID"] = stickerPid
                    line.settings['greet']['join']['sticker']["STKVER"] = stickerVer
                    line.sendMode(msg, to, sender, "sticker", 'Welcome Sticker\nStatus: ✓')
                    line.setts["greets"]["joinSticker"] = False
                elif line.setts["greets"]["leaveSticker"]:
                    stickerId  = msg.contentMetadata['STKID']
                    stickerPid = msg.contentMetadata['STKPKGID']
                    stickerVer = msg.contentMetadata['STKVER']
                    line.settings["greet"]["leave"]["sticker"]["STKID"] = stickerId
                    line.settings["greet"]["leave"]["sticker"]["STKPKGID"] = stickerPid
                    line.settings['greet']['leave']['sticker']["STKVER"] = stickerVer
                    line.sendMode(msg, to, sender, "sticker", 'Leave Sticker\nStatus: ✓')
                    line.setts["greets"]["leaveSticker"] = False
                elif line.settings["setcommand"]["mentionStiker"]["status"]:
                    stickerId  = msg.contentMetadata['STKID']
                    line.settings["setcommand"]["mentionStiker"]["stkid"] = stickerId
                    line.sendMode(msg, to, sender, "sticker", 'Mention by Sticker.\nStatus: ✓')
                    line.settings["setcommand"]["mentionStiker"]["status"] = False
                elif line.settings["setcommand"]["fakeTagSticker"]["status"]:
                    line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKID"] = msg.contentMetadata['STKID']
                    line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKPKGID"] = msg.contentMetadata['STKPKGID']
                    line.settings["setcommand"]["fakeTagSticker"]["sticker"]["STKVER"] = msg.contentMetadata['STKVER']
                    line.sendMode(msg, to, sender, "sticker", 'Fake Mention by Sticker.\nStatus: ✓')
                    line.settings["setcommand"]["fakeTagSticker"]["status"] = False
                elif line.settings["setcommand"]["kicks"]["status"]:
                    line.settings["setcommand"]["kicks"]["stkid"] = msg.contentMetadata['STKID']
                    line.sendMode(msg, to, sender, "sticker", 'Auto Kick by Sticker.\nStatus: ✓')
                    line.settings["setcommand"]["kicks"]["status"] = False
                elif line.settings["setcommand"]["invites"]["status"]:
                    line.settings["setcommand"]["invites"]["stkid"] = msg.contentMetadata['STKID']
                    line.sendMode(msg, to, sender, "sticker", 'Auto Invite by Sticker.\nStatus: ✓')
                    line.settings["setcommand"]["invites"]["status"] = False

            elif msg.contentType == 13: # Content type contact
                mid = msg.contentMetadata['mid']
                try:
                    contact = line.getContact(mid)
                except:
                    return
                if line.settings['checkContact']:
                    if not line.settings["offbot2"] and to not in line.settings["offbot"]:
                        res = 'MID: ' + mid
                        res += '\nDisplay Name: ' + str(contact.displayName)
                        if contact.displayNameOverridden: res += '\nDisplay Name Overridden: ' + str(contact.displayNameOverridden)
                        res += '\nStatus Message: ' + str(contact.statusMessage)
                        image = []
                        video = []
                        if contact.pictureStatus:
                            image.append('https://obs.line-scdn.net/' + contact.pictureStatus)
                        cover = line.getProfileCoverURL(contact.mid)
                        if "/vc/" in cover:
                            line.sendVideoWithURL(to, cover)
                        else:
                            image.append(cover)
                        if len(image) == 2:
                            line.sendMultiImageWithURL(to, image)
                        elif len(image) == 1:
                            line.sendImageWithURL(to, image[0])
                        line.sendFooter(to, res, reply=True)
                elif line.setts["inviteAlot"]["status"]:
                    if mid == line.profile.mid: return
                    name = line.setts["inviteAlot"]["name"]
                    if name not in line.protect['contact_list']:
                        line.protect['contact_list'][name] = []
                    friend = line.getAllContactIds()
                    if mid not in friend:
                        try:
                            line.findAndAddContactsByMid(mid)
                            time.sleep(3)
                        except TalkException as talk_error:
                            if talk_error.code == 35:
                                line.sendMode(msg, to, sender, cmd, 'failed to add team, your account limit add, wait for 1 hour / 24 hour')
                                line.setts["inviteAlot"]["status"] = False
                                line.setts["inviteAlot"]["name"] = ""
                                return
                    if mid in line.protect['contact_list'][name]:
                        line.sendMention(to, '╭ 「 Team Contact 」\n╰ @! > Already\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                    else:
                        line.protect['contact_list'][name].append(mid)
                        line.sendMention(to, '╭ 「 Team Contact 」\n╰ @! > Added\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                elif line.setts["invCon"]:
                    friends = line.getAllContactIds()
                    if mid not in friends:
                        line.findAndAddContactsByMid(mid)
                        time.sleep(0.8)
                    inviteIntoChat(to, [mid])
                    line.setts["invCon"] = False
                elif line.setts["delCon"]:
                    friends = line.getAllContactIds()
                    if mid not in friends:
                        line.sendMention(to, '╭ 「 Del Contact 」\n╰ @! > Not Found\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                    else:
                        line.deleteContact(mid)
                        line.sendMention(to, '╭ 「 Del Contact 」\n╰ @! > Deleted\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                elif line.setts["storyCon"]:
                    data = line.getStoryMedia(mid)
                    if data:
                        line.sendMessage(to, 'Downloading {} stories..'.format(len(data)))
                        dataImages = []
                        dataVideos = []
                        for media in data:
                            if media["type"] == "image":
                                dataImages.append(media["url"])
                            elif media["type"] == "video":
                                line.sendVideoWithURL(to, media["url"])
                        if dataImages:
                            if len(dataImages) >= 2:
                                line.sendMultiImageWithURL(to, dataImages)
                            else:
                                line.sendImageWithURL(to, dataImages[0])
                    else:
                        line.sendFooter(to, 'This user didnt upload any story')
                    line.setts["storyCon"] = False
                elif line.setts["chatCon"]["status"]:
                    line.sendMessage(mid, line.setts["chatCon"]["message"])
                    line.sendMode(msg, to, sender, "contact", 'Successfully sent message')
                    line.setts["chatCon"]["status"] = False
                elif line.setts["banContact"]:
                    if mid in line.protect["blacklist"]:
                        line.sendMention(to, '╭ 「 Ban Contact 」\n╰ @! > Already\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                    else:
                        line.protect["blacklist"].append(mid)
                        line.sendMention(to, '╭ 「 Ban Contact 」\n╰ @! > Added\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                    #line.setts["banContact"] = False
                elif line.setts["whiteContact"]:
                    if mid in line.protect["whitelist"]:
                        line.sendMention(to, '╭ 「 White Contact 」\n╰ @! > Already\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                    else:
                        line.protect["whitelist"].append(mid)
                        line.sendMention(to, '╭ 「 White Contact 」\n╰ @! > Added\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                   # line.setts["whiteContact"] = False
                elif line.setts["assContact"]:
                    if mid in line.protect["assistlist"]:
                        line.sendMention(to, '╭ 「 Assist Contact 」\n╰ @! > Already\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                    else:
                        line.protect["assistlist"].append(mid)
                        line.sendMention(to, '╭ 「 Assist Contact 」\n╰ @! > Added\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                   # line.setts["assContact"] = False
                elif line.setts["adminContact"]:
                    if mid in line.protect["adminlist"]:
                        line.sendMention(to, '╭ 「 Admin Contact 」\n╰ @! > Already\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                    else:
                        line.protect["adminlist"].append(mid)
                        line.sendMention(to, '╭ 「 Admin Contact 」\n╰ @! > Added\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                    #line.setts["adminContact"] = False
                elif line.setts["cloneContact"]:
                    line.cloneContactProfile(msg, mid, sender, to)
                    line.setts["cloneContact"] = False
                elif line.setts["coverExtraContact"]:
                    profile = line.getContact(mid)
                    datas = line.getEffect(profile.mid)
                    if datas['result']:
                        res = "User: @!"
                        res += "\nMid: {}\n".format(profile.mid)
                        no = 0
                        dataImages = []
                        dataStickers = []
                        dataText = False
                        for data in datas['result']:
                            if data["type"] == "Sticker":
                                if data["packageId"] not in dataStickers:
                                    dataStickers.append(data["packageId"])
                                    no += 1
                                    res += "\n{}. Type: {}".format(no, data["type"])
                                    res += "\n     Link: https://line.me/S/sticker/{}\n".format(data["packageId"])
                            elif data["type"] == "Link":
                                if not dataText:
                                    dataText = True
                                no += 1
                                res += "\n{}. Type: {}".format(no, data["type"])
                                res += "\n     Link: {}\n".format(data["url"])
                            elif data["type"] == "Text":
                                if not dataText:
                                    dataText = True
                                no += 1
                                res += "\n{}. Type: {}".format(no, data["type"])
                                res += "\n     Text: {}\n".format(data["text"])
                            elif data["type"] == "Image":
                                if data["url"] not in dataImages:
                                    dataImages.append(data["url"])
                        if dataStickers:
                            if res.endswith('\n'): res = res[:-1]
                            line.sendReplyMention(to, res, [profile.mid], msgIds=msg_id)
                        elif dataText:
                            if res.endswith('\n'): res = res[:-1]
                            line.sendReplyMention(to, res, [profile.mid], msgIds=msg_id)
                        if dataImages:
                            try:
                                if len(dataImages) >= 2:
                                    line.sendMultiImageWithURL(to, dataImages)
                                else:
                                    line.sendImageWithURL(to, dataImages[0])
                            except:
                                line.sendMessage(to, 'Upload image failure, try again')
                    else:
                        line.sendMode(msg, to, sender, 'CoverExtra Contact', 'This user does not use extra cover at all')
                    line.setts["coverExtraContact"] = False
                elif line.setts["lastseen"]["status"]:
                    profile = line.getContact(mid)
                    if mid in line.setts["lastseen"]["user"]:
                        res = 'Name: {}\n'.format(profile.displayName)
                        sort = sorted(line.setts["lastseen"]["user"][profile.mid])
                        parsed_len = len(sort)//20+1
                        for point in range(parsed_len):
                            for gid in sort[point*20:(point+1)*20]:
                                secs = time.time() - line.setts["lastseen"]["user"][profile.mid][gid]["time"]
                                waktu = timeChange(secs)
                                res += '\nGroup: {}'.format(line.getChats([line.setts["lastseen"]["user"][profile.mid][gid]["group"]], False, False).chats[0].chatName)
                                res += '\nLastseen {} ago\n'.format(waktu)
                            if res.startswith('\n'): res = res[1:len(res)]
                            if res.endswith('\n'): res = res[:-1]
                            line.sendMode(msg, to, sender, 'lastseen contact', res)
                            res = ''
                    else:
                        line.sendMode(msg, to, sender, 'Lastseen Contact', 'Name: {}\nData: Not Found'.format(profile.displayName))
                    line.setts["lastseen"]["status"] = False
                elif line.setts["trackCon"]:
                    profile = line.getContact(mid)
                    aa = line.getAllChatMids(True, False).memberChatMids
                    target = profile.mid
                    lacak = ""
                    num = 0
                    for gid in aa:
                        bb = line.getChats([gid], True, False).chats[0]
                        if target in bb.extra.groupExtra.memberMids:
                            num += 1
                            lacak += "\n    {}. {}".format(num, bb.chatName)
                    if lacak == "":
                        line.sendMode(msg, to, sender, 'Track Contact', 'Name: {}\nData: Not Found'.format(profile.displayName))
                        line.setts["trackCon"] = False
                    else:
                        pesan = "Nama: {}\nDia berada di group:{}".format(profile.displayName, lacak)
                        line.sendMode(msg, to, sender, 'Track Contact', pesan)
                        line.setts["trackCon"] = False

            elif msg.contentType == 16: # Content type album/note
                if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                    if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                        contact = line.getContact(sender)
                        author = contact.displayName
                    else:
                        author = msg.contentMetadata['serviceName']
                    if msg.contentMetadata['serviceType'] in ['GB', 'MH']:
                        posturl = msg.contentMetadata['postEndUrl']
                        if msg.contentMetadata['serviceType'] in ['MH']:
                            sep = posturl.replace("https://line.me/R/home/post?userMid=","").split("&postId=")
                            creat = sep[0]
                            pid = sep[1]
                        elif msg.contentMetadata['serviceType'] in ['GB']:
                            sep = posturl.replace("https://line.me/R/group/home/posts/post?homeId=","").split("&postId=")
                            creat = sender
                            pid = sep[1]
                        r = line.getPost(sep[0], pid)
                        if r is None: return
                        dataPost = r["result"]["feed"]["post"]["postInfo"]
                        if line.settings['checkPost']:
                            if not line.settings["offbot2"] and to not in line.settings["offbot"]:
                                res = '› P O S T  I N F O\n'
                                res += "\n• Like: {}".format(str(dataPost["likeCount"]))
                                res += "\n• Comment: {}".format(str(dataPost["commentCount"]))
                                if msg.contentMetadata['serviceType'] in ['MH']:
                                    res += '\n• Share: {}'.format(str(dataPost["sharedCount"]["toTalk"]))
                                res += "\n• Created: {}".format(str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(dataPost["createdTime"]) / 1000))))
                                res += '\n• Creator: ' + author
                                res += '\n• Post Link: ' + posturl
                                line.sendFooter(to, res, line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)
                        doComment = True
                        if dataPost["allowComment"]:
                            dataComment = line.listComment(sep[0], pid, limit=100)
                            for dataC in dataComment['result']['commentList']: 
                                try:
                                    if dataC['userInfo']['mid'] == line.profile.mid:
                                        doComment = False
                                        break
                                except:
                                    continue
                        if msg.contentMetadata['serviceType'] in ['MH']:
                            if doComment:
                                if line.settings['autoComment']['status']:
                                    contentMetadata = []
                                    if line.settings["autoComment"]["sticker"]: contentMetadata.append({"categoryId": "sticker", "extData": {"id": line.settings["autoComment"]["sticker"]["STKID"], "packageId": line.settings["autoComment"]["sticker"]["STKPKGID"], "packageVersion": line.settings["autoComment"]["sticker"]["STKVER"]}})
                                    if line.settings['autoComment']['contentMetadata'] != {}:
                                        contentMetadata.append(eval(str(line.settings["autoComment"]["contentMetadata"])))
                                        if '@!' in line.settings["autoComment"]["message"]:
                                            dataMention = {'recallInfos': []}
                                            for datam in line.settings["autoComment"]["contentMention"]['recallInfos']:
                                                dataMention['recallInfos'].append({'start': datam['start'], 'end': datam['end'], 'user': {'actorId': creat}})
                                            line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata, dataa=dataMention)
                                        else:
                                            line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata)
                                    elif '@!' in line.settings["autoComment"]["message"]:
                                        line.createCommentMention(sep[0], pid, line.settings['autoComment']['message'], mids=[creat], contentsList=contentMetadata)
                                    else:
                                        line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata)
                                    time.sleep(0.8)
                            if not dataPost["liked"]:
                                if line.settings["autoLike"]["status"]:
                                    line.likePost(sep[0], pid, random.choice([1001,1002,1003,1004,1005,1006]))
                        if msg.contentMetadata['serviceType'] in ['GB']:
                            if doComment:
                                if line.settings['autoComment']['note']:
                                    contentMetadata = []
                                    if line.settings["autoComment"]["sticker"]: contentMetadata.append({"categoryId": "sticker", "extData": {"id": line.settings["autoComment"]["sticker"]["STKID"], "packageId": line.settings["autoComment"]["sticker"]["STKPKGID"], "packageVersion": line.settings["autoComment"]["sticker"]["STKVER"]}})
                                    if line.settings['autoComment']['contentMetadata'] != {}:
                                        contentMetadata.append(eval(str(line.settings["autoComment"]["contentMetadata"])))
                                        if '@!' in line.settings["autoComment"]["message"]:
                                            dataMention = {'recallInfos': []}
                                            for datam in line.settings["autoComment"]["contentMention"]['recallInfos']:
                                                dataMention['recallInfos'].append({'start': datam['start'], 'end': datam['end'], 'user': {'actorId': creat}})
                                            line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata, dataa=dataMention)
                                        else:
                                            line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata)
                                    elif '@!' in line.settings["autoComment"]["message"]:
                                        line.createCommentMention(sep[0], pid, line.settings['autoComment']['message'], mids=[creat], contentsList=contentMetadata)
                                    else:
                                        line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata)
                                    time.sleep(0.8)
                            if not dataPost["liked"]:
                                if line.settings["autoLike"]["note"]:
                                    line.likePost(sep[0], pid, random.choice([1001,1002,1003,1004,1005,1006]))
                    if line.setts["bcPost"]["toFriend"] or line.setts["bcPost"]["toGroup"] or line.setts["bcPost"]["toAll"]:
                        return line.sendBroadcastPost(msg, to, sender)
                    if "mediaOid" in msg.contentMetadata:
                        if line.settings['videotl']:
                            for media in ast.literal_eval(msg.contentMetadata["previewMedias"]):
                                list = media["mediaOid"].split("|")
                                for part in list:
                                    if "oid=" in part:
                                        oid = part
                                    if "sid=" in part:
                                        sid = part.replace("sid=", "")
                                if media["mediaType"] == "V":
                                    line.sendVideoWithURL(to, "https://obs-sg.line-apps.com/myhome/"+sid+"/download.nhn?"+oid+"")
            line.settings["amountMessage"]["sent"] += 1
            line.settings["amountMessage"]["totalSent"] += 1
#----------OPERATION RECEIVE MESSAGES----------#
        elif op.type == 26:
            msg      = op.message
            text     = str(msg.text)
            msg_id   = msg.id
            receiver = msg.to
            sender   = msg._from
            cmd      = command(text)
            to       = sender if not msg.toType and sender != line.profile.mid else receiver
            txt      = text.lower()
            setKey   = line.settings['setKey']['key'] if line.settings['setKey']['status'] else ''
            if msg.toType == 0:
                if line.settings['autoRead']:
                    line.sendChatChecked(to, msg_id)
                if msg.contentType == 0:
                    if sender not in line.settings["getPc"]:
                        line.settings["getPc"][sender] = {}
                    if "message" not in line.settings["getPc"][sender]:
                        line.settings["getPc"][sender] = {"time": [], "message": []}
                    line.settings["getPc"][sender]["message"].append(text)
                    line.settings["getPc"][sender]["time"].append(time.time())
                    
            if msg.toType == 2:
                if line.settings['autoReadG']:
                    line.sendChatChecked(to, msg_id)
                if msg.contentMetadata is not None:
                    if 'MENTION' in msg.contentMetadata != None:
                        mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                        for mention in mentions['MENTIONEES']:
                            if line.profile.mid in mention['M']:
                                if line.settings["antiTag"]["status"]:
                                    if sender not in line.protect["whitelist"] and sender not in line.protect["assistlist"]:
                                        if line.settings['antiTag']['contentMetadata'] != {}:
                                            contentMetadata = {"REPLACE": line.settings['antiTag']['contentMetadata']['REPLACE'], "STICON_OWNERSHIP": line.settings['antiTag']['contentMetadata']['STICON_OWNERSHIP']}
                                            if '@!' in line.settings['antiTag']['message']:
                                                arrData = []
                                                mentions = ast.literal_eval(line.settings['antiTag']['contentMention']['MENTION'])
                                                for mention in mentions['MENTIONEES']:
                                                    arrData.append({'S':mention['S'], 'E':mention['E'], 'M':sender})
                                                contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')})
                                            line.sendReplyMessage(to, line.settings['antiTag']['message'], contentMetadata, msgIds=msg_id)
                                        elif "@!" in line.settings["antiTag"]["message"]: line.sendMention(to, line.settings["antiTag"]["message"], [sender])
                                        else: line.sendFooter(to, line.settings["antiTag"]["message"])
                                        group = line.getChats([to], True, False).chats[0]
                                        if sender in group.extra.groupExtra.memberMids:
                                            deleteOtherFromChat(to, [sender])
                                        return
                                if to not in line.setts["whoTag"]:
                                    line.setts["whoTag"][to] = {}
                                if sender not in line.setts["whoTag"][to]:
                                    line.setts["whoTag"][to][sender] = {}
                                if 'msg_id' not in line.setts["whoTag"][to][sender]:
                                    line.setts["whoTag"][to][sender]['msg_id'] = []
                                if 'timeChange' not in line.setts["whoTag"][to][sender]:
                                    line.setts["whoTag"][to][sender]['timeChange'] = []
                                line.setts["whoTag"][to][sender]['msg_id'].append(msg_id)
                                line.setts["whoTag"][to][sender]['timeChange'].append(msg.createdTime)
                                break
                if sender not in line.setts["lastseen"]["user"]: line.setts["lastseen"]["user"][sender] = {}
                line.setts["lastseen"]["user"][sender].update({to:{"mid": sender, "group": to, "time": time.time()}})

            if msg.contentType == 0: # Content type is text
                if txt == 'chatbot':
                    if sender in line.protect["adminlist"]:
                        if to in line.settings['offbot'] or line.settings['offbot2']: res = 'Status: ✔︎'
                        else: res = 'Status: ✘'
                        isi = ['Mute', 'Unmute', 'Mute add <num>', 'Mute del <num>', 'Mute All <on/off>', 'Mute List']
                        res += "\n\n{}".format(looping_command(setKey.title(), "› C O M M A N D", isi))
                        isi2 = ['Mute add 1,2,3-6', 'Mute del 1,2,3-6']
                        res += "\n\n{}".format(looping_command(setKey.title(), "› Example multi add / del", isi2))
                        line.sendMode(msg, to, sender, cmd, res)
                if cmd.startswith('mute'):
                    if sender in line.protect["adminlist"]:
                        textt = removeCmd(text, setKey)
                        texttl = textt.lower()
                        if cmd == 'mute':
                            if to not in line.settings["offbot"]:
                                line.settings["offbot"].append(to)
                                line.sendFooter(to, "Silent mode diaktifkan..")
                            else:
                                line.sendFooter(to, 'Silent mode sedang aktif..')
                        elif texttl.startswith('all '):
                            textts = texttl[4:]
                            if textts == 'on':
                                if not line.settings['offbot2']:
                                    line.settings['offbot2'] = True
                                sendToggle(to, "CHAT BOT", "Chat Bot\nStatus: ✓", "", True)
                            elif textts == 'off':
                                if line.settings['offbot2']:
                                    line.settings['offbot2'] = False
                                sendToggle(to, "CHAT BOT", "Chat Bot\nStatus: ✘", "", False)
                        elif texttl == 'list':
                            if line.settings['offbot2']:
                                return line.sendMode(msg, to, sender, cmd, 'Mode Mute has been activated in all groups')
                            groups = line.settings["offbot"]
                            if groups:
                                res = '› L I S T\n'
                                no = 0
                                for group in groups:
                                    no += 1
                                    if group.startswith('c'):
                                        group = line.getChats([group], True, False).chats[0]
                                        res += '\n{}. {}//{}'.format(no, group.chatName, len(group.extra.groupExtra.memberMids))
                                    elif group.startswith('u'):
                                        res += '\n{}. {}'.format(no, line.getContact(group).displayName)
                                line.sendMode(msg, to, sender, cmd, res)
                            else:
                                line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                        elif texttl.startswith('add '):
                            sep = textt.split(' ')
                            if len(sep) == 2:
                                groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                                targets = filter_target(sep[1], groups)
                                res = "› A D D E D\n"
                                no = 0
                                if targets:
                                    for target in targets:
                                        no += 1
                                        group = line.getChats([target], True, False).chats[0]
                                        if target not in line.settings["offbot"]:
                                            line.settings["offbot"].append(target)
                                            res += "\n{}. {} > Added".format(no, group.chatName)
                                        else:
                                            res += "\n{}. {} > Already".format(no, group.chatName)
                                    line.sendMode(msg, to, sender, cmd, res)
                                else:
                                    line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                        elif texttl.startswith('del '):
                            sep = textt.split(' ')
                            if len(sep) == 2:
                                targets = filter_target(sep[1], line.settings["offbot"])
                                res = "› D E L E T E D\n"
                                no = 0
                                if targets:
                                    for target in targets:
                                        no += 1
                                        group = line.getChats([target], True, False).chats[0]
                                        if target in line.settings["offbot"]:
                                            line.settings["offbot"].remove(target)
                                            res += "\n{}. {} > Deleted".format(no, group.chatName)
                                        else:
                                            res += "\n{}. {} > Not Found".format(no, group.chatName)
                                    line.sendMode(msg, to, sender, cmd, res)
                                else:
                                    line.sendMode(msg, to, sender, cmd, 'There\'s no group was added')
                if cmd == 'unmute':
                    if sender in line.protect["adminlist"]:
                        if to in line.settings["offbot"]:
                            line.settings["offbot"].remove(to)
                            line.sendFooter(to, 'Silent mode dinonaktifkan..')
                        else:
                            line.sendFooter(to, 'Selfbot sedang aktif..')
                if to in line.settings["offbot"] or line.settings["offbot2"]:
                    return
                regex = re.findall(r'(https?://\S+)', text)
                share_link = []
                for link in regex:
                    if link not in share_link:
                        share_link.append(link)
                        shr = shareurl_media(to, txt, link, msg_id)
                        if shr: break
                if line.setts["detectID"]["mid"]:
                    line.mid_list(to, text, sender, 4)
                if line.setts["detectID"]["gid"]:
                    gid_regex = line.server.GID_REGEX.findall(text)
                    doneGid = []
                    for gid in gid_regex:
                        if gid not in doneGid:
                            line.sendFooter(to, str(line.getChats([gid], False, False).chats[0].chatName))
                            doneGid.append(gid)
                if not lewat_list(msg.toType):
                    if txt in line.stickers:
                        line.sticker_list(to, txt, sender, 10)
                    if txt in line.textsx:
                        line.text_list(to, txt, sender, msg_id, 10)
                    if txt in line.protect['multi_list']:
                        line.multi_list(to, txt, sender, 15)
                    if txt in line.pictures:
                        line.picture_list(to, txt, sender, msg_id, 20)
                    if txt in line.audsx:
                        line.audio_list(to, txt, sender, 20)
                    if txt in line.vidsx:
                        line.video_list(to, txt, sender, 20)
                if txt in line.settings['wordban']:
                    line.sendFooter(to, 'Wordban Detected\nText: {}'.format(txt), reply=True)
                    deleteOtherFromChat(to, [sender])
                if line.setts["textss"]['status']:
                    if sender in line.protect["adminlist"]:
                        name   = line.setts["textss"]['name']
                        if 'STICON_OWNERSHIP' in msg.contentMetadata:
                            getEmoji = line.metadataFilter(msg.contentMetadata, 0, type='emoji')
                            line.textsx[name] = {"message": text, "contentMetadata": getEmoji}
                            getEmoji2 = line.metadataFilter(getEmoji, len('Save successfully text\nText: %s\nRespon: ' % name), type='emoji2')
                            if "@!" in text:
                                line.textsx[name] = {"message": text, "contentMetadata": getEmoji, "contentMention": line.metadataFilter(getEmoji, text=text, type='mention')}
                                getEmoji2.update(line.metadataFilter(getEmoji, text='Save successfully text\nText: %s\nRespon: %s' % (name, text), type='mention'))
                            line.sendReplyMessage(to, 'Save successfully text\nText: %s\nRespon: %s' % (name, text), getEmoji2, msgIds=msg_id)
                        else:
                            line.textsx[name] = text
                            line.sendFooter(to, 'Save successfully text\nText: %s\nRespon: %s' % (name, text), reply=True)
                        line.setts["textss"]['status'] = False
                if line.settings['mimic']['status']:
                    if sender in line.settings['mimic']['target'] and line.settings['mimic']['target'][sender]:
                        try:
                            line.sendMessage(to, text, msg.contentMetadata)
                            if not line.settings['mimic']['cmd']:
                                line.setts["tmp_text"].append(text)
                        except:
                            pass
                if line.settings['autoRespond']['status']:
                    if msg.toType == 0:
                        if sender not in line.setts["sleepMode_user"]:
                            if '@!' not in line.settings['autoRespond']['message']:
                                line.sendMessage(to, line.settings['autoRespond']['message'])
                            else:
                                line.sendMention(to, line.settings['autoRespond']['message'], [sender])
                            line.setts["sleepMode_user"].append(sender)
                if line.settings['autoRespondMention']['status'] or line.settings['autoRespondMention']['sticker']['STKID'] is not None:
                    if msg.contentMetadata is not None:
                        if msg.toType in [1, 2] and 'MENTION' in msg.contentMetadata.keys() and sender != line.profile.mid and msg.contentType not in [6, 7, 9]:
                            mentions = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = [mention['M'] for mention in mentions['MENTIONEES']]
                            if line.profile.mid in mentionees:
                                if sender not in line.setts["tagWar"]: line.setts["tagWar"][sender] = {'time': time.time(), 'floods': 0, 'ex': False}
                                if time.time() - line.setts["tagWar"][sender]["time"] <= 10: line.setts["tagWar"][sender]["floods"] += 1
                                else: line.setts["tagWar"][sender]["floods"] = 1
                                if line.setts["tagWar"][sender]["floods"] >= 2:
                                    return
                                if line.settings['autoRespondMention']['status']:
                                    if line.settings['autoRespondMention']['contentMetadata'] != {}:
                                        contentMetadata = {"REPLACE": line.settings['autoRespondMention']['contentMetadata']['REPLACE'], "STICON_OWNERSHIP": line.settings['autoRespondMention']['contentMetadata']['STICON_OWNERSHIP']}
                                        if '@!' in line.settings['autoRespondMention']['message']:
                                            arrData = []
                                            mentions = ast.literal_eval(line.settings['autoRespondMention']['contentMention']['MENTION'])
                                            for mention in mentions['MENTIONEES']:
                                                arrData.append({'S':mention['S'], 'E':mention['E'], 'M':sender})
                                            contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')})
                                        line.sendReplyMessage(to, line.settings['autoRespondMention']['message'], contentMetadata, msgIds=msg_id)
                                    elif '@!' not in line.settings['autoRespondMention']['message']: line.sendReplyMessage(to, line.settings['autoRespondMention']['message'], msgIds=msg_id)
                                    else: line.sendReplyMention(to, line.settings['autoRespondMention']['message'], [sender], msgIds=msg_id)
                                if line.settings['autoRespondMention']['sticker']['STKID'] is not None:
                                    if line.settings['autoRespondMention']['status']: line.sendSticker(to, line.settings['autoRespondMention']['sticker']['STKVER'], line.settings['autoRespondMention']['sticker']['STKPKGID'], line.settings['autoRespondMention']['sticker']['STKID'])
                                    else: line.sendReplySticker(to, line.settings['autoRespondMention']['sticker']['STKVER'], line.settings['autoRespondMention']['sticker']['STKPKGID'], line.settings['autoRespondMention']['sticker']['STKID'], msgIds=msg_id)
                                line.setts["tagWar"][sender]["time"] = time.time()
                if to in line.settings['detectUnsend']:
                    unsendTime = time.time()
                    line.unsend[msg_id] = {"from": sender, "text": text, "time": unsendTime}
                try:
                    if sender in line.protect["adminlist"]:
                        executeCmd(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)
                    else:
                        executePublic(msg, text, txt, cmd, msg_id, receiver, sender, to, setKey)
                except TalkException as talk_error:
                    logError(talk_error)
                    if talk_error.code in [7, 8, 20]:
                        sys.exit(1)
                    line.sendMessage(to, '「 ERROR ✘ 」\nTalkException, Code: ' + str(talk_error.code) + '\nReason: '+ str(talk_error.reason))
                    time.sleep(3)
                except Exception as error:
                    logError(error)
                    line.sendMessage(to, '「 ERROR ✘ 」\n'+ str(error))
                    time.sleep(3)
                    
            elif msg.contentType == 1: # Content type image
                time.sleep(1)
                if to in line.settings['detectUnsend']:
                    unsendTime = time.time()
                    image = line.downloadObjectMsg(msg_id, saveAs="tmp/{}-image.bin".format(time.time()))
                    line.unsend[msg_id] = {"from": sender, "image": image, "time": unsendTime}
                if line.settings["mimic"]["status"]:
                    if sender in line.settings["mimic"]["target"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/mimicImage.bin')
                        try:
                            line.sendImage(to, path)
                        except:
                            pass
                        line.deleteFile(path)
                if sender in line.protect["adminlist"]:
                    if line.setts["upImage"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/upimage.jpg')
                        data = imgBB(path)
                        line.sendFooter(to, 'Convert Image To Url\nUrl: %s' % (data["data"]["url"]), reply=True)
                        line.setts["upImage"] = False
                        line.deleteFile(path)
                    elif line.setts["upBackground"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/upimage.jpg')
                        data = imgBB(path)
                        line.settings["tempBackground"] = data["data"]["url"]
                        line.sendFooter(to, 'Change Background Image\nUrl: %s' % (data["data"]["url"]), reply=True)
                        line.setts["upBackground"] = False
                        line.deleteFile(path)
                    elif line.setts["upStory"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/uploadstory.bin')
                        data = line.uploadObjStory(path, 'image')
                        line.updateStory(data["obsOid"], data["xObsHash"], mediaType='image')
                        line.sendMode(msg, to, sender, "Upload Story", 'Upload Story\nStatus: ✓')
                        line.setts['upStory'] = False
                        line.deleteFile(path)
                    elif line.setts["pictss"]["status"]:
                        name = line.setts["pictss"]["name"]
                        image = line.downloadObjectMsg(msg_id, saveAs="json/{}-image.bin".format(name))
                        line.pictures[name] = image
                        line.sendMode(msg, to, sender, "image", 'Save successfully gambar\nText: %s' % (name))
                        line.setts["pictss"]['status'] = False
                    elif line.setts["autoAddImage"]:
                        path = line.downloadObjectMsg(msg_id, saveAs="json/autoadd-image.bin")
                        line.settings["autoAdd"]["image"]["path"] = path
                        line.sendMode(msg, to, sender, "image", 'Auto Respon Add Image set successfully')
                        line.setts["autoAddImage"] = False
                    elif line.settings["setFlag"]["status"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/line.jpg')
                        data = imgBB(path)
                        line.settings["setFlag"]["icon"] = data["data"]["url"]
                        line.sendFooter(to, 'Change Flag Icon\nUrl: %s' % (data["data"]["url"]), reply=True)
                        line.settings["setFlag"]["status"] = False
                        line.deleteFile(path)
                    elif line.settings['changePictureProfile']:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/picture.jpg')
                        line.updateProfilePicture(path)
                        line.sendMode(msg, to, sender, "image", 'Update Profile Picture\nStatus: ✓')
                        line.settings['changePictureProfile'] = False
                        line.deleteFile(path)
                    elif line.settings['changeCoverProfile']:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                        line.updateProfileCover(path)
                        line.sendMode(msg, to, sender, "image", 'Update Profile Cover\nStatus: ✓')
                        line.settings['changeCoverProfile'] = False
                        line.deleteFile(path)
                    elif line.settings['changeCoverVideo']["image"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/cover.jpg')
                        res = 'Send the video...\ntype `{key}Abort` to cancel this\n\nsend pictures and videos with share/forward'.format(key=setKey.title())
                        line.settings['changeCoverVideo']["image"] = False
                        line.settings['changeCoverVideo']["video"] = True
                        line.sendMessage(to, res)
                    elif to in line.settings['changeGroupPicture'] and msg.toType == 2:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/grouppicture.jpg')
                        line.updateGroupPicture(to, path)
                        line.settings['changeGroupPicture'].remove(to)
                        time.sleep(0.1)
                        line.sendMode(msg, to, sender, "image", 'Update Group Picture\nStatus: ✓')
                        line.deleteFile(path)
                    elif to in line.settings['changeGroupCover'] and msg.toType == 2:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/groupcover.jpg')
                        line.updateGroupCover(to, path)
                        line.settings['changeGroupCover'].remove(to)
                        time.sleep(0.1)
                        line.sendMode(msg, to, sender, "image", 'Update Group Cover\nStatus: ✓')
                        line.deleteFile(path)
                    elif to in line.setts["uploadTL"]:
                        if sender == line.setts["uploadTL"][to]["sender"]:
                            path = line.downloadObjectMsg(msg_id, saveAs='tmp/imageTL.bin')
                            objectId = line.uploadObjHome(path, type='image', returnAs='objId', target=to)
                            line.deleteFile(path)
                            line.setts["uploadTL"][to]["media"].append({
                            	'type': 'PHOTO',
                            	'objectId': objectId
                            })
                            line.setts["uploadTL"][to]["total"] -= 1
                            if line.setts["uploadTL"][to]["total"] == 0:
                                post = line.createPostMedia(line.setts["uploadTL"][to]["description"], media=line.setts["uploadTL"][to]["media"])
                                line.sendPostToTalk(to, post["result"]["feed"]["post"]["postInfo"]["postId"])
                                del line.setts["uploadTL"][to]
                            else:
                                line.sendMessage(to, 'Send {} Image/Video\nType `{key}Abort` to cancel this'.format(line.setts["uploadTL"][to]["total"], key=setKey.title()))
                    elif to in line.setts["uploadNote"]:
                        if sender == line.setts["uploadNote"][to]["sender"]:
                            path = line.downloadObjectMsg(msg_id, saveAs='tmp/imageNote.bin')
                            objectId = line.uploadObjHome(path, type='image', returnAs='objId', target=to)
                            line.deleteFile(path)
                            line.setts["uploadNote"][to]["media"].append({
                            	'type': 'PHOTO',
                            	'objectId': objectId
                            })
                            line.setts["uploadNote"][to]["total"] -= 1
                            if line.setts["uploadNote"][to]["total"] == 0:
                                line.createPostGroupMedia(to, line.setts["uploadNote"][to]["description"], media=line.setts["uploadNote"][to]["media"])
                                del line.setts["uploadNote"][to]
                            else:
                                line.sendMessage(to, 'Send {} Image/Video\nType `{key}Abort` to cancel this'.format(line.setts["uploadNote"][to]["total"], key=setKey.title()))
                    elif line.setts["bcImage"]["toFriend"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/bcToFriend.bin')
                        friends = line.getBcFriend()
                        line.sendFooter(to, 'Loading...')
                        success = []
                        failure = []
                        for friend in friends:
                            try:
                                line.sendImage(friend, path)
                                success.append(friend)
                            except:
                                failure.append(friend)
                                continue
                            time.sleep(0.8)
                        line.setts["bcImage"]["toFriend"] = False
                        line.sendMode(msg, to, sender, "image", 'Broadcast Image Friends\nSuccess: {}x\nFailed: {}x'.format(len(success), len(failure)))
                        line.deleteFile(path)
                    elif line.setts["bcImage"]["toGroup"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/bcToGroup.bin')
                        groups = make_list(line.getAllChatMids(True, False).memberChatMids)
                        line.sendFooter(to, 'Loading...')
                        success = []
                        failure = []
                        for group in groups:
                            if group not in line.settings["bcFilter"]:
                                try:
                                    line.sendImage(group, path)
                                    success.append(group)
                                except:
                                     failure.append(group)
                                     continue
                                time.sleep(0.8)
                        line.setts["bcImage"]["toGroup"] = False
                        line.sendMode(msg, to, sender, "image", 'Broadcast Image Group\nSuccess: {}x\nFailed: {}x'.format(len(success), len(failure)))
                        line.deleteFile(path)
                    elif line.setts["bcImage"]["toAll"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/bcToAll.bin')
                        gogo = make_list(line.getAllChatMids(True, False).memberChatMids) + line.getBcFriend()
                        line.sendFooter(to, 'Loading...')
                        success = []
                        failure = []
                        for go in gogo:
                            if go not in line.settings["bcFilter"]:
                                try:
                                    line.sendImage(go, path)
                                    success.append(go)
                                except:
                                     failure.append(go)
                                     continue
                                time.sleep(0.8)
                        line.setts["bcImage"]["toAll"] = False
                        line.sendMode(msg, to, sender, "image", 'Broadcast Image All\nSuccess: {}x\nFailed: {}x'.format(len(success), len(failure)))
                        line.deleteFile(path)
                    elif line.setts['greets']['wImage']:
                        path = line.downloadObjectMsg(msg_id, saveAs='json/wImage.bin')
                        line.settings['greet']['join']['imagePath'] = path
                        line.sendMode(msg, to, sender, "image", 'Set Welcome Image\nStatus: ✓')
                        line.setts['greets']['wImage'] = False
                    elif line.setts['greets']['lImage']:
                        path = line.downloadObjectMsg(msg_id, saveAs='json/lImage.bin')
                        line.settings['greet']['leave']['imagePath'] = path
                        line.sendMode(msg, to, sender, "image", 'Set Leave Image\nStatus: ✓')
                        line.setts['greets']['lImage'] = False

            elif msg.contentType == 2: # Content type video
                if to in line.settings['detectUnsend']:
                    unsendTime = time.time()
                    video = line.downloadObjectMsg(msg_id, saveAs="tmp/{}-video.bin".format(time.time()))
                    line.unsend[msg_id] = {"from": sender, "video": video, "time": unsendTime}
                if sender in line.protect["adminlist"]:
                    if line.settings["changevp"] == True:
                        contact = line.getProfile()
                        pict = "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                        path = line.downloadFileURL(pict)
                        path1 = line.downloadObjectMsg(msg_id)
                        line.settings["changevp"] = False
                        line.updateVideoAndPictureProfile(path, path1)
                        line.sendMode(msg, to, sender, "video", 'Update Video Profile\nStatus: ✓')
                        line.deleteFile(path)
                        line.deleteFile(path1)
                    elif line.settings['changeCoverVideo']["video"]:
                        pict = "tmp/cover.jpg"
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/covervideo.mp4')
                        line.updateProfileCoverVideo(pict, path)
                        line.sendMode(msg, to, sender, "video", 'Update Cover Video\nStatus: ✓')
                        line.settings['changeCoverVideo']["video"] = False
                        line.deleteFile(path)
                        line.deleteFile(pict)
                    elif line.setts["upStory"]:
                        path = line.downloadObjectMsg(msg_id, saveAs='tmp/uploadstory.bin')
                        data = line.uploadObjStory(path, 'video')
                        line.updateStory(data["obsOid"], data["xObsHash"], mediaType='video')
                        line.sendMode(msg, to, sender, "Upload Story", 'Upload Story\nStatus: ✓')
                        line.setts['upStory'] = False
                        line.deleteFile(path)
                    elif line.setts["vidss"]["status"]:
                        name = line.setts["vidss"]["name"]
                        video = line.downloadObjectMsg(msg_id, saveAs="tmp/{}-video.bin".format(name))
                        line.vidsx[name] = video
                        line.sendMode(msg, to, sender, "video", 'Save successfully video\nText: %s' % (name))
                        line.setts["vidss"]['status'] = False
                    elif to in line.setts["uploadTL"]:
                        if sender == line.setts["uploadTL"][to]["sender"]:
                            path = line.downloadObjectMsg(msg_id, saveAs='tmp/imageTL.bin')
                            objectId = line.uploadObjHome(path, type='video', returnAs='objId', target=to)
                            line.deleteFile(path)
                            line.setts["uploadTL"][to]["media"].append({
                            	'type': 'VIDEO',
                            	'objectId': objectId
                            })
                            line.setts["uploadTL"][to]["total"] -= 1
                            if line.setts["uploadTL"][to]["total"] == 0:
                                post = line.createPostMedia(line.setts["uploadTL"][to]["description"], media=line.setts["uploadTL"][to]["media"])
                                line.sendPostToTalk(to, post["result"]["feed"]["post"]["postInfo"]["postId"])
                                del line.setts["uploadTL"][to]
                            else:
                                line.sendMessage(to, 'Send {} Image/Video\nType `{key}Abort` to cancel this'.format(line.setts["uploadTL"][to]["total"], key=setKey.title()))
                    elif to in line.setts["uploadNote"]:
                        if sender == line.setts["uploadNote"][to]["sender"]:
                            path = line.downloadObjectMsg(msg_id, saveAs='tmp/imageNote.bin')
                            objectId = line.uploadObjHome(path, type='video', returnAs='objId', target=to)
                            line.deleteFile(path)
                            line.setts["uploadNote"][to]["media"].append({
                            	'type': 'VIDEO',
                            	'objectId': objectId
                            })
                            line.setts["uploadNote"][to]["total"] -= 1
                            if line.setts["uploadNote"][to]["total"] == 0:
                                line.createPostGroupMedia(to, line.setts["uploadNote"][to]["description"], media=line.setts["uploadNote"][to]["media"])
                                del line.setts["uploadNote"][to]
                            else:
                                line.sendMessage(to, 'Send {} Image/Video\nType `{key}Abort` to cancel this'.format(line.setts["uploadNote"][to]["total"], key=setKey.title()))
                                
            elif msg.contentType == 3: # Content type audio
                if sender in line.protect["adminlist"]:
                    if line.setts["audss"]["status"]:
                        name = line.setts["audss"]["name"]
                        audio = line.downloadObjectMsg(msg_id, saveAs="tmp/{}-audio.bin".format(name))
                        line.audsx[name] = audio
                        line.sendMode(msg, to, sender, "audio", 'Save successfully audio\nText: %s' % (name))
                        line.setts["audss"]['status'] = False

            elif msg.contentType == 6: # Content type call group
                if msg.toType == 2:
                    if not line.settings["offbot2"] and to not in line.settings["offbot"]:
                        group = line.getChats([to], False, False).chats[0]
                        if msg.contentMetadata['GC_EVT_TYPE'] == 'S':
                            line.setts["detectCall"][to] = time.time()
                            if line.settings['responCall']:
                                jam = pytz.timezone("Asia/Jakarta")
                                jamSek = datetime.now(tz=jam)
                                if msg.contentMetadata['GC_MEDIA_TYPE'] == 'AUDIO':
                                    res = '##---- Free Call Started ----##'
                                elif msg.contentMetadata['GC_MEDIA_TYPE'] == 'VIDEO':
                                    res = '##---- Video Call Started ----##'
                                elif msg.contentMetadata['GC_MEDIA_TYPE'] == 'LIVE':
                                    res = '##---- Live Started ----##'
                                else:
                                    res = '##---- Call Started ----##'
                                if line.settings["templateMode"]:
                                    if line.settings["tempMode"] != "footer": res += '\n\nUser: {}'.format(line.getContact(sender).displayName)
                                    else: res += '\n\nUser: @!'
                                else: res += '\n\nUser: @!'
                                res += '\nGroup: ' + str(group.chatName)
                                res += '\nDate: ' + datetime.strftime(jamSek, '%d-%m-%Y')
                                res += '\nTime: ' + datetime.strftime(jamSek, '%H:%M:%S')
                                if line.settings["templateMode"]:
                                    if line.settings["tempMode"] != "footer": line.sendMode(msg, to, sender, "call", res)
                                    else: line.sendMention(to, res, [sender])
                                else: line.sendMention(to, res, [sender])
                        elif msg.contentMetadata['GC_EVT_TYPE'] == 'E':
                            if to in line.setts["detectCall"]:
                                waktu = time.time() - line.setts["detectCall"][to]
                                durasi = timeChange(waktu)
                                del line.setts["detectCall"][to]
                            else:
                                durasi = 'Nothing'
                            if line.settings['responCall']:
                                jam = pytz.timezone("Asia/Jakarta")
                                jamSek = datetime.now(tz=jam)
                                if msg.contentMetadata['GC_MEDIA_TYPE'] == 'AUDIO':
                                    res = '##---- Free Call Ended ----##'
                                elif msg.contentMetadata['GC_MEDIA_TYPE'] == 'VIDEO':
                                    res = '##---- Video Call Ended ----##'
                                elif msg.contentMetadata['GC_MEDIA_TYPE'] == 'LIVE':
                                    res = '##---- Live Ended ----##'
                                if line.settings["templateMode"]:
                                    if line.settings["tempMode"] != "footer": res += '\n\nUser: {}'.format(line.getContact(sender).displayName)
                                    else: res += '\n\nUser: @!'
                                else: res += '\n\nUser: @!'
                                res += '\nGroup: ' + str(group.chatName)
                                res += '\nDate: ' + datetime.strftime(jamSek, '%d-%m-%Y')
                                res += '\nTime: ' + datetime.strftime(jamSek, '%H:%M:%S')
                                res += '\nDuration : ' + str(durasi)
                                if line.settings["templateMode"]:
                                    if line.settings["tempMode"] != "footer": line.sendMode(msg, to, sender, "call", res)
                                    else: line.sendMention(to, res, [sender])
                                else: line.sendMention(to, res, [sender])

            elif msg.contentType == 7: # Content type sticker
                if line.settings['checkSticker']:
                    if not line.settings["offbot2"] and to not in line.settings["offbot"]:
                        res = 'Sticker ID: ' + msg.contentMetadata['STKID']
                        res += '\nSticker Packages ID: ' + msg.contentMetadata['STKPKGID']
                        res += '\nSticker Version: ' + msg.contentMetadata['STKVER']
                        res += '\nSticker Link: https://line.me/R/shop/detail/' + msg.contentMetadata['STKPKGID']
                        line.sendFooter(to, res, reply=True)
                if to in line.settings['detectUnsend']:
                    stickerId  = msg.contentMetadata['STKID']
                    unsendTime = time.time()
                    line.unsend[msg_id] = {"from": sender, "sticker": stickerId, "time": unsendTime}
                if line.settings["mimic"]["status"]:
                    if sender in line.settings["mimic"]["target"]:
                        stickerId  = msg.contentMetadata['STKID']
                        url = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/%s/ANDROID/sticker.png' % stickerId
                        req = requests.get(url)
                        if req.status_code != 200:
                            url = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/%s/iPhone/sticker@2x.png' % stickerId
                        line.sendImageWithURL(to, url)
                        
            elif msg.contentType == 13: # Content type contact
                mid = msg.contentMetadata['mid']
                try:
                    contact = line.getContact(mid)
                except:
                    return
                if line.settings["mimic"]["status"]:
                    if sender in line.settings["mimic"]["target"]:
                        line.sendContact(to, mid)
                if sender in line.protect["adminlist"]:
                    if line.settings['checkContact']:
                        if not line.settings["offbot2"] and to not in line.settings["offbot"]:
                            res = 'MID: ' + mid
                            res += '\nDisplay Name: ' + str(contact.displayName)
                            if contact.displayNameOverridden: res += '\nDisplay Name Overridden: ' + str(contact.displayNameOverridden)
                            res += '\nStatus Message: ' + str(contact.statusMessage)
                            image = []
                            video = []
                            if contact.pictureStatus:
                                image.append('https://obs.line-scdn.net/' + contact.pictureStatus)
                            cover = line.getProfileCoverURL(contact.mid)
                            if "/vc/" in cover:
                                line.sendVideoWithURL(to, cover)
                            else:
                                image.append(cover)
                            if len(image) == 2:
                                line.sendMultiImageWithURL(to, image)
                            elif len(image) == 1:
                                line.sendImageWithURL(to, image[0])
                            line.sendFooter(to, res, reply=True)
                    elif line.setts["invCon"]:
                        friends = line.getAllContactIds()
                        if mid not in friends:
                            line.findAndAddContactsByMid(mid)
                            time.sleep(0.8)
                        inviteIntoChat(to, [mid])
                        line.setts["invCon"] = False
                    elif line.setts["delCon"]:
                        friends = line.getAllContactIds()
                        if mid not in friends:
                            line.sendMention(to, '╭ 「 Del Contact 」\n╰ @! > Not Found\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                        else:
                            line.deleteContact(mid)
                            line.sendMention(to, '╭ 「 Del Contact 」\n╰ @! > Deleted\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                    elif line.setts["storyCon"]:
                        data = line.getStoryMedia(mid)
                        if data:
                            line.sendMessage(to, 'Downloading {} stories..'.format(len(data)))
                            dataImages = []
                            dataVideos = []
                            for media in data:
                                if media["type"] == "image":
                                    dataImages.append(media["url"])
                                elif media["type"] == "video":
                                    line.sendVideoWithURL(to, media["url"])
                            if dataImages:
                                if len(dataImages) >= 2:
                                    line.sendMultiImageWithURL(to, dataImages)
                                else:
                                    line.sendImageWithURL(to, dataImages[0])
                        else:
                            line.sendFooter(to, 'This user didnt upload any story')
                        line.setts["storyCon"] = False
                    elif line.setts["chatCon"]["status"]:
                        line.sendMessage(mid, line.setts["chatCon"]["message"])
                        line.sendMode(msg, to, sender, "contact", 'Successfully sent message')
                        line.setts["chatCon"]["status"] = False
                    elif line.setts["banContact"]:
                        if mid in line.protect["blacklist"]:
                            line.sendMention(to, '╭ 「 Ban Contact 」\n╰ @! > Already\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                        else:
                            line.protect["blacklist"].append(mid)
                            line.sendMention(to, '╭ 「 Ban Contact 」\n╰ @! > Added\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                        #line.setts["banContact"] = False
                    elif line.setts["whiteContact"]:
                        if mid in line.protect["whitelist"]:
                            line.sendMention(to, '╭ 「 White Contact 」\n╰ @! > Already\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                        else:
                            line.protect["whitelist"].append(mid)
                            line.sendMention(to, '╭ 「 White Contact 」\n╰ @! > Added\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                       # line.setts["whiteContact"] = False
                    elif line.setts["assContact"]:
                        if mid in line.protect["assistlist"]:
                            line.sendMention(to, '╭ 「 Assist Contact 」\n╰ @! > Already\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                        else:
                            line.protect["assistlist"].append(mid)
                            line.sendMention(to, '╭ 「 Assist Contact 」\n╰ @! > Added\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                       # line.setts["assContact"] = False
                    elif line.setts["adminContact"]:
                        if mid in line.protect["adminlist"]:
                            line.sendMention(to, '╭ 「 Admin Contact 」\n╰ @! > Already\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                        else:
                            line.protect["adminlist"].append(mid)
                            line.sendMention(to, '╭ 「 Admin Contact 」\n╰ @! > Added\nType `{}Abort` when you\'re done'.format(setKey.title()), [mid])
                        #line.setts["adminContact"] = False
                    elif line.setts["cloneContact"]:
                        line.cloneContactProfile(msg, mid, sender, to)
                        line.setts["cloneContact"] = False
                    elif line.setts["coverExtraContact"]:
                        profile = line.getContact(mid)
                        datas = line.getEffect(profile.mid)
                        if datas['result']:
                            res = "User: @!"
                            res += "\nMid: {}\n".format(profile.mid)
                            no = 0
                            dataImages = []
                            dataStickers = []
                            dataText = False
                            for data in datas['result']:
                                if data["type"] == "Sticker":
                                    if data["packageId"] not in dataStickers:
                                        dataStickers.append(data["packageId"])
                                        no += 1
                                        res += "\n{}. Type: {}".format(no, data["type"])
                                        res += "\n     Link: https://line.me/S/sticker/{}\n".format(data["packageId"])
                                elif data["type"] == "Link":
                                    if not dataText:
                                        dataText = True
                                    no += 1
                                    res += "\n{}. Type: {}".format(no, data["type"])
                                    res += "\n     Link: {}\n".format(data["url"])
                                elif data["type"] == "Text":
                                    if not dataText:
                                        dataText = True
                                    no += 1
                                    res += "\n{}. Type: {}".format(no, data["type"])
                                    res += "\n     Text: {}\n".format(data["text"])
                                elif data["type"] == "Image":
                                    if data["url"] not in dataImages:
                                        dataImages.append(data["url"])
                            if dataStickers:
                                if res.endswith('\n'): res = res[:-1]
                                line.sendReplyMention(to, res, [profile.mid], msgIds=msg_id)
                            elif dataText:
                                if res.endswith('\n'): res = res[:-1]
                                line.sendReplyMention(to, res, [profile.mid], msgIds=msg_id)
                            if dataImages:
                                try:
                                    if len(dataImages) >= 2:
                                        line.sendMultiImageWithURL(to, dataImages)
                                    else:
                                        line.sendImageWithURL(to, dataImages[0])
                                except:
                                    line.sendMessage(to, 'Upload image failure, try again')
                        else:
                            line.sendMode(msg, to, sender, 'CoverExtra Contact', 'This user does not use extra cover at all')
                        line.setts["coverExtraContact"] = False
                    elif line.setts["lastseen"]["status"]:
                        profile = line.getContact(mid)
                        if mid in line.setts["lastseen"]["user"]:
                            res = 'Name: {}\n'.format(profile.displayName)
                            sort = sorted(line.setts["lastseen"]["user"][profile.mid])
                            parsed_len = len(sort)//20+1
                            for point in range(parsed_len):
                                for gid in sort[point*20:(point+1)*20]:
                                    secs = time.time() - line.setts["lastseen"]["user"][profile.mid][gid]["time"]
                                    waktu = timeChange(secs)
                                    res += '\nGroup: {}'.format(line.getChats([line.setts["lastseen"]["user"][profile.mid][gid]["group"]], False, False).chats[0].chatName)
                                    res += '\nLastseen {} ago\n'.format(waktu)
                                if res.startswith('\n'): res = res[1:len(res)]
                                if res.endswith('\n'): res = res[:-1]
                                line.sendMode(msg, to, sender, 'lastseen contact', res)
                                res = ''
                        else:
                            line.sendMode(msg, to, sender, 'Lastseen Contact', 'Name: {}\nData: Not Found'.format(profile.displayName))
                        line.setts["lastseen"]["status"] = False
                    elif line.setts["trackCon"]:
                        profile = line.getContact(mid)
                        aa = line.getAllChatMids(True, False).memberChatMids
                        target = profile.mid
                        lacak = ""
                        num = 0
                        for gid in aa:
                            bb = line.getChats([gid], True, False).chats[0]
                            if target in bb.extra.groupExtra.memberMids:
                                num += 1
                                lacak += "\n    {}. {}".format(num, bb.chatName)
                        if lacak == "":
                            line.sendMode(msg, to, sender, 'Track Contact', 'Name: {}\nData: Not Found'.format(profile.displayName))
                            line.setts["trackCon"] = False
                        else:
                            pesan = "Name: {}\nDia berada di group:{}".format(profile.displayName, lacak)
                            line.sendMode(msg, to, sender, 'Track Contact', pesan)
                            line.setts["trackCon"] = False

            elif msg.contentType == 16: # Content type album/note
                if msg.contentMetadata['serviceType'] in ['GB', 'NT', 'MH']:
                    if msg.contentMetadata['serviceType'] in ['GB', 'NT']:
                        contact = line.getContact(sender)
                        author = contact.displayName
                    else:
                        author = msg.contentMetadata['serviceName']
                    if msg.contentMetadata['serviceType'] in ['GB', 'MH']:
                        if line.settings["autoLike"]["reply"]:
                            if not line.settings['checkPost']:
                                if not line.settings["offbot2"] and to not in line.settings["offbot"]:
                                    if line.settings['autoLike']['contentMetadata'] != {}:
                                        contentMetadata = {"REPLACE": line.settings['autoLike']['contentMetadata']['REPLACE'], "STICON_OWNERSHIP": line.settings['autoLike']['contentMetadata']['STICON_OWNERSHIP']}
                                        if '@!' in line.settings['autoLike']['message']:
                                            arrData = []
                                            mentions = ast.literal_eval(line.settings['autoLike']['contentMention']['MENTION'])
                                            for mention in mentions['MENTIONEES']:
                                                arrData.append({'S':mention['S'], 'E':mention['E'], 'M':sender})
                                            contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')})
                                        line.sendMessage(to, line.settings['autoLike']['message'], contentMetadata)
                                    elif "@!" in line.settings["autoLike"]["message"]: line.sendMention(to, line.settings["autoLike"]["message"], [sender])
                                    else: line.sendMode(msg, to, sender, "POST TIMELINE", line.settings["autoLike"]["message"])
                        posturl = msg.contentMetadata['postEndUrl']
                        if msg.contentMetadata['serviceType'] in ['MH']:
                            sep = posturl.replace("https://line.me/R/home/post?userMid=","").split("&postId=")
                            creat = sep[0]
                            pid = sep[1]
                        elif msg.contentMetadata['serviceType'] in ['GB']:
                            sep = posturl.replace("https://line.me/R/group/home/posts/post?homeId=","").split("&postId=")
                            creat = sender
                            pid = sep[1]
                        r = line.getPost(sep[0], pid)
                        if r is None: return
                        dataPost = r["result"]["feed"]["post"]["postInfo"]
                        if line.settings['checkPost']:
                            if not line.settings["offbot2"] and to not in line.settings["offbot"]:
                                res = '› P O S T  I N F O\n'
                                res += "\n• Like: {}".format(str(dataPost["likeCount"]))
                                res += "\n• Comment: {}".format(str(dataPost["commentCount"]))
                                if msg.contentMetadata['serviceType'] in ['MH']:
                                    res += '\n• Share: {}'.format(str(dataPost["sharedCount"]["toTalk"]))
                                res += "\n• Created: {}".format(str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(dataPost["createdTime"]) / 1000))))
                                res += '\n• Creator: ' + author
                                res += '\n• Post Link: ' + posturl
                                line.sendFooter(to, res, line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)
                        doComment = True
                        if dataPost["allowComment"]:
                            dataComment = line.listComment(sep[0], pid, limit=100)
                            for dataC in dataComment['result']['commentList']: 
                                try:
                                    if dataC['userInfo']['mid'] == line.profile.mid:
                                        doComment = False
                                        break
                                except:
                                    continue
                        if msg.contentMetadata['serviceType'] in ['MH']:
                            if doComment:
                                if line.settings['autoComment']['status']:
                                    contentMetadata = []
                                    if line.settings["autoComment"]["sticker"]: contentMetadata.append({"categoryId": "sticker", "extData": {"id": line.settings["autoComment"]["sticker"]["STKID"], "packageId": line.settings["autoComment"]["sticker"]["STKPKGID"], "packageVersion": line.settings["autoComment"]["sticker"]["STKVER"]}})
                                    if line.settings['autoComment']['contentMetadata'] != {}:
                                        contentMetadata.append(eval(str(line.settings["autoComment"]["contentMetadata"])))
                                        if '@!' in line.settings["autoComment"]["message"]:
                                            dataMention = {'recallInfos': []}
                                            for datam in line.settings["autoComment"]["contentMention"]['recallInfos']:
                                                dataMention['recallInfos'].append({'start': datam['start'], 'end': datam['end'], 'user': {'actorId': creat}})
                                            line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata, dataa=dataMention)
                                        else:
                                            line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata)
                                    elif '@!' in line.settings["autoComment"]["message"]:
                                        line.createCommentMention(sep[0], pid, line.settings['autoComment']['message'], mids=[creat], contentsList=contentMetadata)
                                    else:
                                        line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata)
                                    time.sleep(0.8)
                            if not dataPost["liked"]:
                                if line.settings["autoLike"]["status"]:
                                    line.likePost(sep[0], pid, random.choice([1001,1002,1003,1004,1005,1006]))
                        if msg.contentMetadata['serviceType'] in ['GB']:
                            if doComment:
                                if line.settings['autoComment']['note']:
                                    contentMetadata = []
                                    if line.settings["autoComment"]["sticker"]: contentMetadata.append({"categoryId": "sticker", "extData": {"id": line.settings["autoComment"]["sticker"]["STKID"], "packageId": line.settings["autoComment"]["sticker"]["STKPKGID"], "packageVersion": line.settings["autoComment"]["sticker"]["STKVER"]}})
                                    if line.settings['autoComment']['contentMetadata'] != {}:
                                        contentMetadata.append(eval(str(line.settings["autoComment"]["contentMetadata"])))
                                        if '@!' in line.settings["autoComment"]["message"]:
                                            dataMention = {'recallInfos': []}
                                            for datam in line.settings["autoComment"]["contentMention"]['recallInfos']:
                                                dataMention['recallInfos'].append({'start': datam['start'], 'end': datam['end'], 'user': {'actorId': creat}})
                                            line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata, dataa=dataMention)
                                        else:
                                            line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata)
                                    elif '@!' in line.settings["autoComment"]["message"]:
                                        line.createCommentMention(sep[0], pid, line.settings['autoComment']['message'], mids=[creat], contentsList=contentMetadata)
                                    else:
                                        line.createComment(sep[0], pid, line.settings['autoComment']['message'], contentsList=contentMetadata)
                                    time.sleep(0.8)
                            if not dataPost["liked"]:
                                if line.settings["autoLike"]["note"]:
                                    line.likePost(sep[0], pid, random.choice([1001,1002,1003,1004,1005,1006]))
                    if line.setts["bcPost"]["toFriend"] or line.setts["bcPost"]["toGroup"] or line.setts["bcPost"]["toAll"]:
                        if sender in line.protect["adminlist"]:
                            return line.sendBroadcastPost(msg, to, sender)
                    if "mediaOid" in msg.contentMetadata:
                        if line.settings['videotl']:
                            for media in ast.literal_eval(msg.contentMetadata["previewMedias"]):
                                list = media["mediaOid"].split("|")
                                for part in list:
                                    if "oid=" in part:
                                        oid = part
                                    if "sid=" in part:
                                        sid = part.replace("sid=", "")
                                if media["mediaType"] == "V":
                                    line.sendVideoWithURL(to, "https://obs-sg.line-apps.com/myhome/"+sid+"/download.nhn?"+oid+"")

            elif msg.contentType == 22: # Content type flex
                if to in line.settings['detectUnsend']:
                    true = True
                    false = False
                    unsendTime = time.time()
                    flexs =  eval(msg.contentMetadata["FLEX_JSON"])
                    if flexs["type"] == "carousel": datta = {"type": "flex","altText": "UNSEND FLEX","contents": flexs}
                    else: datta = {"type": "flex","altText": "UNSEND FLEX","contents": {"type": "carousel","contents": [flexs]}}
                    line.setts["flexUnsend"][msg.id] = {"from": sender,"flex": datta, "time": unsendTime}
                    
            line.settings["amountMessage"]["receive"] += 1
#----------OPERATION SEND CHAT CHECKED----------#
        elif op.type == 40:
            if op.param1 in line.settings["getPc"]:
                del line.settings["getPc"][op.param1]
#----------OPERATION SEND CHAT REMOVED----------#
        elif op.type == 41:
            if op.param1 in line.settings["getPc"]:
                del line.settings["getPc"][op.param1]
#----------OPERATION NOTIFIED READ MESSAGES----------#
        elif op.type == 55:
            if op.param1.startswith("c"):
                group = line.getChats([op.param1], True, False).chats[0]
                if op.param2 in group.extra.groupExtra.memberMids:
                    if op.param2 in line.protect["blacklist"]:
                        if not checkAccess(op.param2):
                            if not line.settings["blmode"]:
                                if not checkProtect(op.param1):
                                    return
                            if op.param1.startswith("c"):
                                if op.param2 in group.extra.groupExtra.memberMids:
                                    if line.settings["isLimit"] is None:
                                        try:
                                            line.sendMention(op.param1, "i'll kick u @! cuz u has been 𝗕𝗮𝗻𝗻𝗲𝗱!!", [op.param2])
                                            line.deleteOtherFromChat(op.param1, [op.param2])
                                        except TalkException as talk_error:
                                            if talk_error.code == 35:
                                                line.settings["isLimit"] = time.time()+60*60*24*1
                                    elif line.settings["isLimit"] <= time.time():
                                        line.settings["isLimit"] = None
                                        line.sendMention(op.param1, "i'll kick u @! cuz u has been 𝗕𝗮𝗻𝗻𝗲𝗱!!", [op.param2])
                                        line.deleteOtherFromChat(op.param1, [op.param2])
                                return
                    if op.param1 in line.setts["lurking"]:
                        if line.setts["lurking"][op.param1]['status'] and op.param2 not in line.setts["lurking"][op.param1]['members']:
                            line.setts["lurking"][op.param1]['members'].append(op.param2)
                    if op.param1 in line.setts["replyReader"]:
                        text = line.settings['sider']["defaultReplyReader"]
                        if line.setts["replyReader"][op.param1]['eply']['tatus'] and op.param2 not in line.setts["replyReader"][op.param1]['listmem']:
                            line.setts["replyReader"][op.param1]['listmem'].append(op.param2)
                            if line.settings['sider']['contentMetadata'] != {}:
                                contentMetadata = {"REPLACE": line.settings['sider']['contentMetadata']['REPLACE'], "STICON_OWNERSHIP": line.settings['sider']['contentMetadata']['STICON_OWNERSHIP']}
                                if '@!' in text:
                                    arrData = []
                                    mentions = ast.literal_eval(line.settings['sider']['contentMention']['MENTION'])
                                    for mention in mentions['MENTIONEES']:
                                        arrData.append({'S':mention['S'], 'E':mention['E'], 'M':op.param2})
                                    contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')})
                                line.sendMessage(op.param1, text, contentMetadata)
                                time.sleep(0.5)
                            elif '@!' not in text:
                                profile = line.getContact(op.param2)
                                if profile.pictureStatus: picture = "https://obs.line-scdn.net/" + profile.pictureStatus
                                else: picture = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
                                data = template.smallTemp(profile.displayName, picture, text, 'Reader')
                                line.sendLiff(op.param1, data)
                                time.sleep(1)
                            else:
                                line.sendMention(op.param1, text.format(chatName=line.getChats([op.param1], False, False).chats[0].chatName, displayName=line.getContact(op.param2).displayName), [op.param2])
                                time.sleep(0.5)
                    if op.param1.startswith("c"):
                        try:
                            if op.param2 not in line.setts["lastseen"]["user"]: line.setts["lastseen"]["user"][op.param2] = {}
                            line.setts["lastseen"]["user"][op.param2].update({op.param1:{"mid": op.param2, "group": op.param1, "time": time.time()}})
                        except Exception as e:
                            pass
#----------OPERATION NOTIFIED UNSEND----------#
        elif op.type == 65:
            to = op.param1
            if to in line.settings["detectUnsend"]:
                sender = op.param2
                if sender in line.unsend:
                    sendTime = time.time() - line.unsend[sender]["time"]
                    sendTime = timeChange(sendTime)
                    contact = line.getContact(line.unsend[sender]["from"])
                    if "text" in line.unsend[sender]:
                        try:
                            res = '##---- Unsend Text ----##'
                            res += '\nUser: @!'
                            res += '\n\n=> {} ago'.format(sendTime)
                            res += '\nText: {}'.format(line.unsend[sender]["text"])
                            line.sendMention(to, res, [contact.mid])
                            del line.unsend[sender]
                        except:
                            del line.unsend[sender]
                    elif "image" in line.unsend[sender]:
                        try:
                            res = '##---- Unsend Image ----##'
                            res += '\nUser: @!'
                            res += '\n\n=> {} ago'.format(sendTime)
                            res += '\nImage: Below'
                            line.sendMention(to, res, [contact.mid])
                            line.sendImage(to, line.unsend[sender]['image'])
                            line.deleteFile(line.unsend[sender]['image'])
                            del line.unsend[sender]
                        except:
                            line.deleteFile(line.unsend[sender]['image'])
                            del line.unsend[sender]
                    elif "video" in line.unsend[sender]:
                        try:
                            res = '##---- Unsend Video ----##'
                            res += '\nUser: @!'
                            res += '\n\n=> {} ago'.format(sendTime)
                            res += '\nVideo: Below'
                            line.sendMention(to, res, [contact.mid])
                            line.sendVideo(to, line.unsend[sender]['video'])
                            line.deleteFile(line.unsend[sender]['video'])
                            del line.unsend[sender]
                        except:
                            line.deleteFile(line.unsend[sender]['video'])
                            del line.unsend[sender]
                    elif "sticker" in line.unsend[sender]:
                        try:
                            res = '##---- Unsend Sticker ----##'
                            res += '\nUser: @!'
                            res += '\n\n=> {} ago'.format(sendTime)
                            res += '\nSticker: Below'
                            line.sendMention(to, res, [contact.mid])
                            url = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/%s/ANDROID/sticker.png' % line.unsend[sender]["sticker"]
                            req = requests.get(url)
                            if req.status_code != 200:
                                url = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/%s/iPhone/sticker@2x.png' % line.unsend[sender]["sticker"]
                            line.sendLiffImage(to, url, line.settings["setFlag"]["icon"], ' Picture sticker')
                            del line.unsend[sender]
                        except:
                            del line.unsend[sender]
                if sender in line.setts["flexUnsend"]:
                    sendTime = time.time() - line.setts["flexUnsend"][sender]["time"]
                    sendTime = timeChange(sendTime)
                    contact = line.getContact(line.setts["flexUnsend"][sender]["from"])
                    if "flex" in line.setts["flexUnsend"][sender]:
                        try:
                            res = '##---- Unsend Flex ----##'
                            res += '\nUser: @!'
                            res += '\n\n=> {} ago'.format(sendTime)
                            res += '\nFlex: Below'
                            line.sendMention(to, res, [contact.mid])
                            line.sendLiff(to, line.setts["flexUnsend"][sender]['flex'])
                            del line.setts["flexUnsend"][sender]
                        except:
                            del line.setts["flexUnsend"][sender]
    except TalkException as talk_error:
        logError(talk_error)
        if talk_error.code in [7, 8, 20]:
            sys.exit(1)
    except KeyboardInterrupt:
        sys.exit('##---- KEYBOARD INTERRUPT -----##')
    except Exception as error:
        logError(error)
        
def restartProgram():
    print ('\033[1;32m##----- PROGRAM RESTARTED -----##\033[0m')
    python = sys.executable
    os.execl(python, python, *sys.argv)

def command(text):
    pesan = text.lower()
    if line.settings['setKey']['status']:
        if pesan.startswith(line.settings['setKey']['key']):
            cmd = pesan[len(line.settings['setKey']['key']):]
        else:
            cmd = 'Undefined command'
    else:
        cmd = text.lower()
    return cmd

def removeCmd(text, key=''):
    if key == '':
        setKey = '' if not line.settings['setKey']['status'] else line.settings['setKey']['key']
    else:
        setKey = key
    text_ = text[len(setKey):]
    sep = text_.split(' ')
    return text_[len(sep[0] + ' '):]
        
def looping_command(setkey, title='› C O M M A N D', text_list=[], show_key=True):
    res = f'{title}\n'
    for txt in text_list:
        if show_key: res += f'\n• {setkey}{txt}'
        else: res += f'\n• {txt}'
    return res

def timeChange(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weeks, days = divmod(days,7)
    months, weeks = divmod(weeks,4)
    text = ""
    if months != 0: text += "%02d month" % (months)
    if weeks != 0: text += " %02d week" % (weeks)
    if days != 0: text += " %02d day" % (days)
    if hours !=  0: text +=  " %02d hour" % (hours)
    if mins != 0: text += " %02d minute" % (mins)
    if secs != 0: text += " %02d second" % (secs)
    if text[0] == " ":
        text = text[1:]
    return text
    
def translator(to, query):
    url = requests.get("https://translate.google.com/m?sl=auto&tl={}&hl=en&q={}".format(to, query))
    soup = BeautifulSoup(url.content, "lxml")
    input = soup.find("input", {"class": "input-field"}).get("value")
    output = soup.find("div", {"class": "result-container"}).text
    return output

def imgBB(path, key=None):
    if key is None:
        key = "efce3143b17a677774976617d0805639" #sozi12andrean@gmail.com
    with open(path, "rb") as file:
        url = "https://api.imgbb.com/1/upload"
        payload = {
            "key": key,
            "image": base64.b64encode(file.read()),
        }
        data = requests.post(url, payload).json()
        return data

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def make_list(dict):
    data = list(dict)
    return data
    
def lewat_list(toType):
    lewatin = False
    if line.settings["listType"] == 1:
        if toType != 0:
            lewatin = True
    elif line.settings["listType"] == 2:
        if toType != 2:
            lewatin = True
    return lewatin

def sendToggle(to, text, text_temp_off, text2="", toggle=True):
    if line.settings["templateMode"] and line.settings["tempMode"] != "footer":
        if text2 != "": data = template.toggle_on_off2(text, text2, toggle)
        else: data = template.toggle_on_off(text, toggle)
        line.sendLiff(to, [data], mainType=False)
    else:
        line.sendFooter(to, text_temp_off, line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)

def checkAccess(user):
    statusAccess = False
    if user in line.protect["adminlist"]:
        statusAccess = True
    elif user in line.protect["assistlist"]:
        statusAccess = True
    elif user in line.protect["whitelist"]:
        statusAccess = True
    return statusAccess

def checkProtect(gid):
    statusProtect = False
    if gid in line.protect["proKick"]:
        statusProtect = True
    elif gid in line.protect["proInv"]:
        statusProtect = True
    elif gid in line.protect["proQr"]:
        statusProtect = True
    elif gid in line.protect["proCancel"]:
        statusProtect = True
    return statusProtect

def addBlacklist(user, group, forceMax=False):
    if forceMax:
        if user not in line.protect["blacklist"]:
            line.protect["blacklist"].append(user)
    elif user not in line.protect["blacklist"]:
        if not line.settings["blmode"]:
            if not checkProtect(group):
                return
        line.protect["blacklist"].append(user)

def filter_target(logics, the_list):
    target = []
    selection = Archimed(logics, range(1, len(the_list)+1)).parse()
    for num in selection:
        if num <= len(the_list):
            if the_list[num - 1] not in target:
                target.append(the_list[num - 1])
    return target

def twitterPost(to, url):
    #scrape by trojans
    URL = urllib.parse.urlparse(url)
    if(URL.netloc == "twitter.com"):
        user_id = URL.path.split("/")[1]
        tweet_id = URL.path.split("/")[3]
    Authorization = 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'
    headers = {
        'Authorization': Authorization
    }
    result = requests.post("https://api.twitter.com/1.1/guest/activate.json", headers=headers)
    token = json.loads(result.text)["guest_token"]
    headers = {
        'Authorization': Authorization,
        'x-guest-token': str(token)
    }
    result = requests.get("https://api.twitter.com/1.1/statuses/show/" + tweet_id + ".json?cards_platform=Web-12&include_cards=1&include_reply_count=1&include_user_entities=0&tweet_mode=extended", headers=headers)
    data = json.loads(result.text)
    videos = []
    images = []
    for media_index, media in enumerate(data["extended_entities"]["media"]):
        media_type = media["type"]
        if(media_type == "video" or media_type == "animated_gif"):
            variants_bitrate = []
            for variant in media["video_info"]["variants"]:
                if(variant["content_type"] == "video/mp4"):
                    variants_bitrate.append(variant["bitrate"])
                else:
                    variants_bitrate.append(-1)
            line.sendVideoWithURL(to, media["video_info"]["variants"][variants_bitrate.index(max(variants_bitrate))]["url"])
        elif(media_type == "photo"):
            images.append(media["media_url_https"] + "?name=orig")
    if images:
        if len(images) >= 2:
            line.sendMultiImageWithURL(to, images)
        else:
            line.sendImageWithURL(to, images[0])

def tiktokPost(to, _url):
    try:
        print("+++ TT DOWNLOADER")
        req = requests.session()
        get = req.get("https://ttdownloader.com")
        token = BeautifulSoup(get.text, "lxml").find("input", {"id": "token"})["value"]
        data = { "url": _url, "format": "", "token": token }
        post = req.post("https://ttdownloader.com/req/", data=data)
        video = BeautifulSoup(post.text, "lxml").findAll("a", {"class": "download-link"})
        line.sendVideoWithURL(to, str(video[0]["href"]))
    except Exception as e:
        try:
            print(e)
            print("+++ RENDY API")
            data = json.loads(requests.get("https://api.imjustgood.com/tiktokdl={}".format(_url), headers={"apikey": rendyApikey, "User-Agent": "Justgood/5.0"}).text)
            if data["status"] == 200:
                line.sendVideoWithURL(to, data["result"]["no_watermark"])
            else:
                raise Exception("Rendy API Error")
        except Exception as e:
            try:
                print(e)
                print("+++ TIKTOK DOWNLOADER")
                headers = {
                    "origin": "https://tiktok-downloader.work/",
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded"
                }
                data = { "link": _url }
                post = requests.post("https://tiktok-downloader.work/get-video", data=data, headers=headers)
                soup = BeautifulSoup(post.text, "lxml").find("a", {"class": "save-tik-tok-video-btn"})
                video = "https://tiktok-downloader.work%s" % soup.get("href").split("=")[1]
                line.sendVideoWithURL(to, video)
            except Exception as e:
                print(e)
                print("+++ TIKTOK API HERY MUSICALLYDOWN")
                params = {"apikey": eaterApikey, "url": _url}
                main = json.loads(requests.get("https://api.coursehero.store/musicallydown", params=params).text)
                if main["status"] == 200:
                    line.sendVideoWithURL(to, main["result"]["download"])
                else:
                    print("+++ TIKTOK API HERY TIKTOK")
                    main = json.loads(requests.get("https://api.coursehero.store/tiktok", params=params).text)
                    if main["status"] == 200:
                        if 'play_addr_h264' in main["result"]["aweme_detail"]["video"]:
                            line.sendVideoWithURL(to, main["result"]["aweme_detail"]["video"]["play_addr_h264"]["url_list"][0])
                        elif 'play_addr' in main["result"]["aweme_detail"]["video"]:
                            line.sendVideoWithURL(to, main["result"]["aweme_detail"]["video"]["play_addr"]["url_list"][0])
                        else:
                            print("+++ TIKTOK DOWNLOAD LOCAL")
                            HEADERS = {
                                'Connection': 'keep-alive',
                                'Pragma': 'no-cache',
                                'Cache-Control': 'no-cache',
                                'DNT': '1',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
                                'Accept': '*/*',
                                'Sec-Fetch-Site': 'same-site',
                                'Sec-Fetch-Mode': 'no-cors',
                                'Sec-Fetch-Dest': 'video',
                                'Referer': 'https://www.tiktok.com/',
                                'Accept-Language': 'en-US,en;q=0.9,bs;q=0.8,sr;q=0.7,hr;q=0.6',
                                'sec-gpc': '1',
                                'Range': 'bytes=0-',
                            }
                            _cookies = {
                                'tt_webid': '689854141086886123',
                                'tt_webid_v2': '689854141086886123'
                            }
                            response = requests.get(_url, cookies=_cookies, headers=HEADERS)
                            video_url = response.text.split('"playAddr":"')[1].split('"')[0].replace(r'\u0026', '&')
                            url = urlparse(video_url)
                            params = tuple(parse_qsl(url.query))
                            request = requests.Request(method='GET', url='{}://{}{}'.format(url.scheme, url.netloc, url.path), cookies=_cookies, headers=HEADERS, params=params)
                            prepared_request = request.prepare()
                            session = requests.Session()
                            response = session.send(request=prepared_request)
                            response.raise_for_status()
                            with open(os.path.abspath("tiktok.mp4"), 'wb') as output_file:
                                output_file.write(response.content)
                            line.sendVideo(to, "tiktok.mp4")
                            os.remove("tiktok.mp4")
                    else:
                        print("+++ TIKTOK DOWNLOAD LOCAL")
                        HEADERS = {
                            'Connection': 'keep-alive',
                            'Pragma': 'no-cache',
                            'Cache-Control': 'no-cache',
                            'DNT': '1',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
                            'Accept': '*/*',
                            'Sec-Fetch-Site': 'same-site',
                            'Sec-Fetch-Mode': 'no-cors',
                            'Sec-Fetch-Dest': 'video',
                            'Referer': 'https://www.tiktok.com/',
                            'Accept-Language': 'en-US,en;q=0.9,bs;q=0.8,sr;q=0.7,hr;q=0.6',
                            'sec-gpc': '1',
                            'Range': 'bytes=0-',
                        }
                        _cookies = {
                            'tt_webid': '689854141086886123',
                            'tt_webid_v2': '689854141086886123'
                        }
                        response = requests.get(_url, cookies=_cookies, headers=HEADERS)
                        video_url = response.text.split('"playAddr":"')[1].split('"')[0].replace(r'\u0026', '&')
                        url = urlparse(video_url)
                        params = tuple(parse_qsl(url.query))
                        request = requests.Request(method='GET', url='{}://{}{}'.format(url.scheme, url.netloc, url.path), cookies=_cookies, headers=HEADERS, params=params)
                        prepared_request = request.prepare()
                        session = requests.Session()
                        response = session.send(request=prepared_request)
                        response.raise_for_status()
                        with open(os.path.abspath("tiktok.mp4"), 'wb') as output_file:
                            output_file.write(response.content)
                        line.sendVideo(to, "tiktok.mp4")
                        os.remove("tiktok.mp4")

def nhentai(id='p'):
    ids = []
    if id == 'p':
        url = requests.get("https://nhentai.net/")
        soup = BeautifulSoup(url.content, "lxml")
        getId = soup.findAll("a", {"class": "cover"})
        for pop in getId[0:5]:
            nid = pop.get("href").split("/")[2]
            ids.append(nid)
    elif id == 'n':
        url = requests.get("https://nhentai.net/")
        soup = BeautifulSoup(url.content, "lxml")
        getId = soup.findAll("a", {"class": "cover"})
        for new in getId[5:15]:
            nid = new.get("href").split("/")[2]
            ids.append(nid)
    elif id == 'r':
        num = random.randint(360000, 367064)
        ids.append(str(num))
    else:
        ids.append(id)
    if ids:
        result = []
        for nhenID in ids:
            url = requests.get("https://nhentai.net/g/%s" % (nhenID))
            soup = BeautifulSoup(url.content, "lxml")
            data = soup.find("div", {"id": "thumbnail-container"})
            b = data.find("div", {"class": "thumbs"}).findAll("img", {"class": "lazyload"})
            idd = soup.find("h3", {"id": "gallery_id"}).text[1:]
            title = soup.find("h1", {"class": "title"}).text
            page = soup.findAll("span", {"class": "tags"})[7].text
            uploaded = soup.findAll("span", {"class": "tags"})[8].text
            keep = []
            for a in b:
                edit = a.get("data-src")[10:][:-5]
                img = "https://i.%s.jpg" % (edit)
                keep.append(img)
            result.append({
                "id": idd,
                "title": title,
                "page": page,
                "uploaded": uploaded,
                "thumb": "https://t.nhentai.net/galleries/{}/thumb.jpg".format(keep[0].split('i.nhentai.net/galleries/')[1].split('/')[0]),
                "image": keep
            })
        return result

def youtubeMp4(to, link, sendLiff=True):
    # try:
    #     print("+++ RENDY API")
    #     data = json.loads(requests.get("https://api.imjustgood.com/youtubedl={}".format(link), headers={"apikey": rendyApikey, "User-Agent": "Justgood/5.0"}).text)
    #     if data["status"] != 200:
    #         raise Exception("Rendy API Error")
    #     if sendLiff:
    #         line.sendLiffVideo(to, data['result']['videoUrl'], data['result']['thumbnail'])
    #     else:
    #         line.sendVideoWithURL(to, data['result']['videoUrl'])
    # except Exception as e:
    #     print(e)
        # print("+++ API HERY")
        # try:
        #     if 'youtube.com' in link:
        #         videoid = link.split("=")[1]
        #     elif 'youtu.be' in link:
        #         sep = link.split("/")
        #         videoid = sep[len(sep)-1]
        #     params = {"url": link}
        #     main = json.loads(requests.get("https://api.chstore.me/youtube", params=params).text)["result"]

        #     media_url = main["mp4"]
        #     if media_url == "":mp4 = main["mp4_cdn"]

        #     if sendLiff:
        #         line.sendLiffVideo(to, media_url, "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(videoid))
        #     else:
        #         line.sendVideoWithURL(to, media_url)
        print("+++ API MINZ")
        try:
            if 'youtube.com' in link:
                videoid = link.split("=")[1]
            elif 'youtu.be' in link:
                sep = link.split("/")
                videoid = sep[len(sep)-1]
            params = {"url": link}
            main = minz_api.youtubeDownload(link)["result"]
            
            media_url = main["videoUrl"]

            if sendLiff:
                line.sendLiffVideo(to, media_url, "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(videoid))
            else:
                line.sendVideoWithURL(to, media_url)
        except Exception as e:
            print(e)
            if not sendLiff:
                line.sendMessage(to, 'Error {}'.format(e))

def youtubeMp3(to, link):
    # try:
    #     print("+++ RENDY API")
    #     data = json.loads(requests.get("https://api.imjustgood.com/youtubedl={}".format(link), headers={"apikey": rendyApikey, "User-Agent": "Justgood/5.0"}).text)
    #     if data["status"] != 200:
    #         raise Exception("Rendy API Error")
    #     line.sendAudioWithURL(to, data['result']['audioUrl'])
    # except Exception as e:
    #     print(e)
        print("+++ YOUTUBE API HERY")
        try:
            params = {"url": link}
            main = json.loads(requests.get("https://api.chstore.me/youtube", params=params).text)["result"]
            try:media_url = main["mp3"][0]["mp3_url"]
            except:media_url = main["mp3_cdn"][0]["mp3_url"]

            line.sendAudioWithURL(to, media_url)
        except Exception as e:
            print(e)
            subprocess.getoutput('youtube-dl --extract-audio --audio-format mp3 --output TeamAnuBot.mp3 {}'.format(link))
            try:
                print("+++ YTDL")
                time.sleep(1)
                line.sendAudio(to, "TeamAnuBot.mp3")
                os.remove('TeamAnuBot.mp3')
            except Exception as e:
                print(e)
                line.sendMessage(to, 'Error {}'.format(e))
            
def shareurl_media(to, txt, url_ni, msg_id):
    ngebreak = False
    if 'youtubemp3' in txt or 'youtubemp4' in txt or 'smulepost' in txt or 'instapost' in txt or 'tiktokpost' in txt or 'twitterpost' in txt or 'fbpost' in txt or 'themeline' in txt or 'cocofun' in txt or 'pinterestpost' in txt or 'timelinecv' in txt:
        ngebreak = True
        return ngebreak
    if line.setts["shareurlLimit"] is not None:
        if 'instagram.com/p/' in url_ni or 'instagram.com/reel/' in url_ni or 'pin.it/' in url_ni or 'pinterest.com/pin/' in url_ni or 'youtube.com' in url_ni or 'youtu.be' in url_ni or 'smule.com/recording' in url_ni or 'smule.com/p' in url_ni or 'smule.com/c' in url_ni or 'smule.com/sing-recording' in url_ni or 'timeline.line.me/post/' in url_ni or 'tiktok.com' in url_ni or 'twitter.com' in url_ni or 'facebook.com' in url_ni or 'shop/theme' in url_ni or 'themeshop/product' in url_ni or 'sck.io/p' in url_ni or 'i.coco.fun'  in url_ni:
            if line.setts["shareurlLimit"] >= time.time():
                waktu = line.setts["shareurlLimit"]-time.time()
                timeleft = int(waktu% 60)
                line.sendReplyMessage(to, 'Failed, try again after {} seconds'.format(timeleft), msgIds=msg_id)
                ngebreak = True
                return ngebreak
            else:
                line.setts["shareurlLimit"] = None
    if line.settings["shareIG"]:
        if 'instagram.com/p/' in url_ni or 'instagram.com/reel/' in url_ni:
            main = json.loads(requests.get("https://apitrojans.xyz/instagram/post?url={}&apikey={}".format(url_ni, trojansApikey)).text)
            if main['status'] != 200:
                params = {'apikey': eaterApikey, "url": url_ni}
                main = json.loads(requests.get("https://api.coursehero.store/igpost", params=params).text)
            videos = []
            images = []
            for item in range(len(main["result"]["media"])):
                if main["result"]["media"][item]["is_video"]:
                    line.sendVideoWithURL(to, main["result"]["media"][item]["video"])
                elif 'img' in main["result"]["media"][item]:
                    images.append(main["result"]["media"][item]["img"])
                else:
                    images.append(main["result"]["media"][item]["image"])
            if images:
                if len(images) >= 2:
                    line.sendMultiImageWithURL(to, images)
                else:
                    line.sendImageWithURL(to, images[0])
            if line.setts["shareurlLimit"] is None:
                billing = int(60*1)
                line.setts["shareurlLimit"] = time.time()+billing
    if line.settings["sharePinterest"]:
        if 'pin.it/' in url_ni or 'pinterest.com/pin/' in url_ni:
            get = requests.get("https://pinterestdownloader.com/download?url=%s" % url_ni)
            soup = BeautifulSoup(get.text, "lxml")
            media = soup.findAll("a", {"class": "download_button"})
            images = []
            for data in media:
                if '.gif' in data["href"]:
                    line.sendGIFWithURL(to, data["href"])
                elif '.mp4' in data["href"]:
                    line.sendVideoWithURL(to, data["href"])
                elif '/thumbnails/' not in data['href']:
                    images.append(data['href'])
            if images:
                if len(images) >= 2:
                    line.sendMultiImageWithURL(to, images)
                else:
                    line.sendReplyImageWithURL(to, images[0], msgIds=msg_id)
            if line.setts["shareurlLimit"] is None:
                billing = int(60*1)
                line.setts["shareurlLimit"] = time.time()+billing
    if line.settings["shareYoutube"]:
        if 'youtube.com' in url_ni:
            youtubeMp4(to, url_ni, sendLiff=True)
            if line.setts["shareurlLimit"] is None:
                billing = int(60*1)
                line.setts["shareurlLimit"] = time.time()+billing
        elif 'youtu.be' in url_ni:
            youtubeMp4(to, url_ni, sendLiff=True)
            if line.setts["shareurlLimit"] is None:
                billing = int(60*1)
                line.setts["shareurlLimit"] = time.time()+billing
    if line.settings["shareSmule"]:
        if 'smule.com/recording' in url_ni or 'smule.com/p' in url_ni or 'smule.com/c' in url_ni or 'smule.com/sing-recording' in url_ni:
            params = {"apikey": eaterApikey, "url": url_ni}
            main = json.loads(requests.get("https://api.coursehero.store/smule/post", params=params).text)
            if main["result"]["performance"]["type"] == "video": line.sendVideoWithURL(to, main["result"]["performance"]["video_media_mp4_url"])
            else: line.sendAudioWithURL(to, main["result"]["performance"]["media_url"])
            if line.setts["shareurlLimit"] is None:
                billing = int(60*1)
                line.setts["shareurlLimit"] = time.time()+billing
    if line.settings["shareTimeline"]:
        if 'timeline.line.me/post/' in url_ni:
            url = requests.get(url_ni)
            soup = BeautifulSoup(url.content,"lxml")
            data = json.loads(soup.select('script[type="application/json"]')[0].string)
            data = data["postEnd"]["feed"]["post"]
            videos = []
            images = []
            for content in data["contents"]["media"]:
                if content["type"] == "PHOTO":
                    images.append("https://obs.line-scdn.net/"+content["resourceId"])
                else:
                    line.sendVideoWithURL(to, "https://obs.line-scdn.net/"+content["resourceId"])
            if images:
                if len(images) >= 2:
                    line.sendMultiImageWithURL(to, images)
                else:
                    line.sendImageWithURL(to, images[0])
            if line.setts["shareurlLimit"] is None:
                billing = int(60*1)
                line.setts["shareurlLimit"] = time.time()+billing
    if line.settings["shareTiktok"]:
        if 'tiktok.com' in url_ni:
            tiktokPost(to, url_ni)
            if line.setts["shareurlLimit"] is None:
                billing = int(60*1)
                line.setts["shareurlLimit"] = time.time()+billing
    if line.settings["shareTwitter"]:
        if 'twitter.com' in url_ni:
            if '/status/' in url_ni:
                twitterPost(to, url_ni)
                if line.setts["shareurlLimit"] is None:
                    billing = int(60*1)
                    line.setts["shareurlLimit"] = time.time()+billing
    if line.settings["shareFb"]:
        if 'facebook.com' in url_ni:
            try:
                req  = requests.post("https://www.getfvid.com/downloader", data={"url": url_ni}).text
                soup = BeautifulSoup(req, "lxml")
                data = soup.find("div", {"class": "col-md-4 btns-download"}).find_all("a")
                result = {}
                for uri in data:
                    if "HD" in  uri.text:
                        result["hd"] =  uri["href"]
                    if "Normal" in  uri.text:
                        result["normal"] =  uri["href"]
                if result:
                    if "hd" in result:
                        line.sendLiffVideo(to, result["hd"], "https://i.ibb.co/59vNQk0/d49ea7041f5c.jpg")
                    elif "normal" in result:
                        line.sendLiffVideo(to, result["normal"], "https://i.ibb.co/59vNQk0/d49ea7041f5c.jpg")
                    if line.setts["shareurlLimit"] is None:
                        billing = int(60*1)
                        line.setts["shareurlLimit"] = time.time()+billing
            except:
                pass
    if line.settings["shareTheme"]:
        if "shop/theme" in url_ni or "themeshop/product" in url_ni:
            req = requests.get(url_ni)
            data = BeautifulSoup(req.content, "lxml")
            theme_icon = json.loads(data.select('script[type="application/ld+json"]')[0].string)["image"]
            theme_android = theme_icon.split('/WEBSTORE/')[0]+'/ANDROID/theme.zip'
            line.sendMultiImageWithURL(to, [theme_icon, 'https://i.ibb.co/0MP67Pk/97ee4aec4564.jpg'])
            subprocess.getoutput("wget -O theme_android.zip {}".format(theme_android))
            line.sendFile(to, "theme_android.zip")
            line.deleteFile("theme_android.zip")
            if line.setts["shareurlLimit"] is None:
                billing = int(60*1)
                line.setts["shareurlLimit"] = time.time()+billing
    if line.settings["shareCocofun"]:
        if "i.coco.fun" in url_ni:
            #scrape by trojans
            req = requests.get(url_ni)
            soup = BeautifulSoup(req.text, "lxml")
            soup = soup.find("script", id={"appState"})
            tostr = "%s" % str(soup)
            tojson = json.loads(tostr[47:][:-9])
            data = tojson["share"]["post"]["post"]
            video_nowm = data["videos"][str(data["imgs"][0]["id"])]["urlext"]
            line.sendVideoWithURL(to, video_nowm)
            if line.setts["shareurlLimit"] is None:
                billing = int(60*1)
                line.setts["shareurlLimit"] = time.time()+billing
    return ngebreak

def deleteOtherFromChat(to, target=[], message=""):
    if line.settings["isLimit"] is None:
        try:
            if message != "": line.sendMessage(to, message)
            line.deleteOtherFromChat(to, target)
        except TalkException as talk_error:
            if talk_error.code == 35:
                line.settings["isLimit"] = time.time()+60*60*24*1
    elif line.settings["isLimit"] <= time.time():
        line.settings["isLimit"] = None
        if message != "": line.sendMessage(to, message)
        line.deleteOtherFromChat(to, target)

def inviteIntoChat(to, target=[], message=""):
    if line.settings["isLimit"] is None:
        try:
            if message != "": line.sendMessage(to, message)
            line.inviteIntoChat(to, target)
        except TalkException as talk_error:
            if talk_error.code == 35:
                line.settings["isLimit"] = time.time()+60*60*24*1
    elif line.settings["isLimit"] <= time.time():
        line.settings["isLimit"] = None
        if message != "": line.sendMessage(to, message)
        line.inviteIntoChat(to, target)
                
def check_check():
    if line.settings["autoLike"]["story"]:
        if line.settings['story_check'] is not None:
            data = line.getRecentStory()
            if data["message"] == "success":
                lastActivity = data["result"]["lastActivityTime"]
                if line.settings['story_check'] != lastActivity:
                    line.settings['story_check'] = lastActivity
                    for user in data["result"]["recentStories"]:
                        if user["mid"] != line.profile.mid:
                            if user["recentCreatedTime"] == lastActivity:
                                print('+++ CHECKING NEW STORIES')
                                dataStory = line.getStory(user["mid"])
                                if dataStory['message'] == 'success':
                                    if dataStory['result']['contents']:
                                        for media in dataStory['result']['contents']:
                                            if not media["viewReaction"]["reaction"]["liked"]:
                                                line.likeStory(media['contentId'], 1003)
                                                time.sleep(0.8)
                                                if media['contentId'] == dataStory['result']['contents'][-1]['contentId']:
                                                    if line.settings["autoComment"]["story"]["status"]:
                                                        line.commentStory(user["mid"], media['contentId'], line.settings["autoComment"]["story"]["message"])
                                break
        else:
            print('+++ SETS NEW LAST ACTIVITY STORIES')
            data = line.getRecentStory()
            line.settings['story_check'] = data["result"]["lastActivityTime"]
    if line.settings['1hour_check'] is not None:
        if line.settings['1hour_check'] <= time.time():
            print('+++ RESET 5 MINUTE DATA CHECK')
            biling = int(60*5)
            line.settings['1hour_check'] = time.time()+biling
            date = datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d')
            if date != line.settings["amountMessage"]["time"]:
                line.settings["amountMessage"]["sent"] = 0
                line.settings["amountMessage"]["time"] = date
                line.settings["amountBackup"]["invite"] = 0
                line.settings["amountBackup"]["cancel"] = 0
                line.settings["amountBackup"]["kick"] = 0
    else:
        print('+++ ADD 5 MINUTE DATA CHECK')
        biling = int(60*5)
        line.settings['1hour_check'] = time.time()+biling
        date = datetime.now(tz=pytz.timezone('Asia/Jakarta')).strftime('%Y-%m-%d')
        if date != line.settings["amountMessage"]["time"]:
            line.settings["amountMessage"]["sent"] = 0
            line.settings["amountMessage"]["time"] = date
            line.settings["amountBackup"]["invite"] = 0
            line.settings["amountBackup"]["cancel"] = 0
            line.settings["amountBackup"]["kick"] = 0

executor = ThreadPoolExecutor(max_workers=1)

def runningProgram():
    if line.settings['restartPoint'] is not None:
        try:
            line.sendFooter(line.settings['restartPoint'], 'the program has been successfully restarted', line.settings["setFlag"]["icon"], line.settings["setFlag"]["name"], reply=True)
        except TalkException:
            pass
        line.settings['restartPoint'] = None

    #DONT DELETE THIS, THIS IMPORTANT
    line.server.auth(line)
    #for publicKey in line.talk.getE2EEPublicKeys():
        #line.talk.removeE2EEPublicKey(publicKey)
        
    while True:
        try:
            task = executor.submit(check_check)
            ops = line.fetchOps(oepoll.localRev, 15, oepoll.globalRev, oepoll.individualRev)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('##---- KEYBOARD INTERRUPT -----##')
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
                executeOp(op)
                oepoll.localRev = max(op.revision, oepoll.localRev)

if __name__ == '__main__':
    runningProgram()
