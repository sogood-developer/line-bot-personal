# -*- coding: utf-8 -*-
from lib.akad.ttypes import Message
from .auth import Auth
from .models import Models
from .talk import Talk
from .square import Square
from .call import Call
from .timeline import Timeline
from .server import Server
from .liff import Liff
from .shop import Shop
from .callback import Callback
import livejson

class LINE(Auth, Models, Talk, Square, Call, Timeline, Liff, Shop):

    def __init__(self, idOrAuthToken=None, passwd=None, **kwargs):
        """
        :param idOrAuthToken: Login email, token. Default: None
        :param passwd: Login password. Default: None
        :param kwargs: See below
        :Keyword Arguments:
            - **certificate**: Line certificate after email login. Default: None
            - **systemName**: System name when first login. Default: None
            - **appType**: Application type to login. Default: None
            - **appName**: Application name to login. Default: None
            - **showQr**: Print out qr code. Default: False
            - **channelId**: Channel ID to login Timeline. Default: None
            - **keepLoggedIn**: Keep logged in if succesfull login. Default: True
            - **customThrift**: Increase speed thrift with custom thrift. Default: False
            - **callback**: Use custom callback.
        :return:
        """
        self.certificate = kwargs.pop('certificate', None)
        self.systemName = kwargs.pop('systemName', None)
        self.appType = kwargs.pop('appType', None)
        self.appName = kwargs.pop('appName', None)
        self.showQr = kwargs.pop('showQr', False)
        self.channelId = kwargs.pop('channelId', None)
        self.keepLoggedIn = kwargs.pop('keepLoggedIn', True)
        self.customThrift = kwargs.pop('customThrift', True)
        self.ignoreSquare = kwargs.pop('ignoreSquare', True)
        callback = kwargs.pop("callback", None)
        Auth.__init__(self)
        if callback and callable(callback):
            self.callback = Callback(callback)
        if not (idOrAuthToken or idOrAuthToken and passwd):
            self.loginWithQrCode()
        if idOrAuthToken and passwd:
            self.loginWithCredential(idOrAuthToken, passwd)
        elif idOrAuthToken and not passwd:
            self.loginWithAuthToken(idOrAuthToken)
        self.__initAll()

    def __initAll(self):

        self.profile    = self.talk.getProfile()
        
        self.settings = livejson.File('json/setting.json', True, False, 4)
        self.stickers = livejson.File('json/sticker.json', True, False, 4)
        self.unsend = livejson.File('json/unsend.json', True, False, 4)
        self.pictures = livejson.File('json/picture.json', True, False, 4)
        self.textsx = livejson.File('json/text.json', True, False, 4)
        self.audsx = livejson.File('json/audio.json', True, False, 4)
        self.vidsx = livejson.File('json/video.json', True, False, 4)
        self.protect = livejson.File('json/protect.json', True, False, 4)
            
        self.setts = {
            "lastseen": {
                "status": False,
                "user": {}
            },
            "inviteAlot": {
                "status": False,
                "name": ""
            },
            "chatCon": {
                "status": False,
                "message": ""
            },
            "audss": {
                "status": False,
                "name": ""
            },
            "vidss": {
                "status": False,
                "name": ""
            },
            "pictss": {
                "status": False,
                "name": ""
            },
            "stickerss": {
                "status": False,
                "name": ""
            },
            "textss": {
                "status": False,
                "name": ""
            },
            "bcImage": {
                "toFriend": False,
                "toGroup": False,
                "toAll": False
            },
            "bcPost": {
                "toFriend": False,
                "toGroup": False,
                "toAll": False
            },
            "greets": {
                "joinSticker": False,
                "leaveSticker": False,
                "lImage": False,
                "wImage": False
            },
            "detectID": {
                "mid": False,
                "gid": False
            },
            "flexUnsend": {},
            "lurking": {},
            "replyReader": {},
            "floods": {},
            "memBackup": {},
            "whoTag": {},
            "tagWar": {},
            "spamPublic": {},
            "spamText": {},
            "spamMulti": {},
            "spamCList": {},
            "spamImage": {},
            "spamVideo": {},
            "spamAudio": {},
            "spamBigSticker": {},
            "spamGreetLeave": {},
            "spamGreetWelcome": {},
            "detectCall": {},
            "notifJoin": {},
            "uploadNote": {},
            "uploadTL": {},
            "emoteFree": {
                '\U00102902': '5ac21b4f031a6752fb806d59',
                '\U00102801': '5ac21ae3040ab15980c9b440',
                '\U00102702': '5ac21a8c040ab15980c9b43f',
                '\U00102604': '5ac21a13031a6752fb806d57',
                '\U00100c02': '5ac21f52040ab15980c9b445',
                '\U00100902': '5ac21d59031a6752fb806d5d',
                '\U00100802': '5ac21cc5031a6752fb806d5c',
                '\U00100b03': '5ac21ef5031a6752fb806d5e',
                '\U00100503': '5ac21a18040ab15980c9b43e',
                '\U00100a02': '5ac21e6c040ab15980c9b444',
                '\U00100303': '5ac21184040ab15980c9b43a',
                '\U00100202': '5ac1de17040ab15980c9b438',
                '\U00100404': '5ac21542031a6752fb806d55',
                '\U00101002': '5ac2211e031a6752fb806d61',
                '\U00100e03': '5ac2206d031a6752fb806d5f',
                '\U00101102': '5ac2216f040ab15980c9b448',
                '\U00100706': '5ac21c46040ab15980c9b442',
                '\U00101901': '5ac22775040ab15980c9b44c',
                '\U00101701': '5ac223c6040ab15980c9b44a'
            },
            "backupTemp": {
                "backgroundImage": "https://i.ibb.co/T0RJmNM/BACKGROUND-ACODE44.png",
                "color": {
                    "background": "#3b3c3673",
                    "text": "#FFFFFF",
                    "border": "#777b7e"
                }
            },
            "sleepMode_user": [],
            "tmp_text": [],
            "offbot": [],
            "postComment": [],
            "notifCvp": [],
            "backupProfile": False,
            "shareurlLimit": None,
            "trackCon": False,
            "invCon": False,
            "delCon": False,
            "storyCon": False,
            "upImage": False,
            "autoAddImage": False,
            "autoAddSticker": False,
            "tagSticker": False,
            "upBackground": False,
            "upStory": False,
            "banContact": False,
            "whiteContact": False,
            "adminContact": False,
            "assContact": False,
            "cloneContact": False,
            "coverExtraContact": False
        }
        
        Models.__init__(self)
        Talk.__init__(self)
        Square.__init__(self)
        Call.__init__(self)
        if self.appType != "CHANNELCP":
            Timeline.__init__(self)
        Liff.__init__(self)
        Shop.__init__(self)
