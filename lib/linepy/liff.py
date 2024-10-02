# -*- coding: utf-8 -*-
from lib.akad.ttypes import (
    LiffViewRequest,
    LiffContext,
    LiffChatContext,
    LiffSquareChatContext,
    RevokeTokenRequest,
    LiffException,
    TalkException,
)
import requests, json, time

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.default('You want to call the function, you must login to LINE')
    return checkLogin

class Liff:
    isLogin = False
    liffToken = None
    liffTokens = {}
    liffBanned = {
        'status': False,
        'time': None
    }
    wait = 0

    def __init__(self):
        self.wait = time.time()
        self.isLogin = True
        self.resend = False
        self.to = None
        self.server.setLiffHeadersWithDict({
            'Authorization': '',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; Mi A1 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/69.0.3497.91 Mobile Safari/537.36 Line/10.14.3',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'X-Requested-With': 'jp.naver.self.android'
        })

    @loggedIn
    def allowLiff(self, channelId):
        # Copyright by https://github.com/RynKings
        data = {'on': ['P', 'CM'], 'off': []}
        headers = {
            'X-Line-Access': self.authToken,
            'X-Line-Application': self.server.APP_NAME,
            'X-Line-ChannelId': channelId,
            'Content-Type': 'application/json'
        }
        r = self.server.postContent(self.server.LINE_PERMISSION_API, headers=headers, data=json.dumps(data))
        return r.json()

    @loggedIn
    def issueLiffView(self, to, liffId='1657707255-WVxqmM35', revokeToken=False, isSquare=False):
        if to in self.liffTokens and not self.liffToken and not revokeToken:
            self.liffToken = self.liffTokens[to]
        else:
            if self.liffToken and revokeToken:
                try:
                    self.revokeToken(self.liffToken)
                    self.liffToken = None
                except Exception:
                    pass
            if isSquare:
                context = LiffContext(squareChat=LiffSquareChatContext(to))
            else:
                context = LiffContext(chat=LiffChatContext(to))
            liffReq = LiffViewRequest(liffId=liffId, context=context)
            try:
                liffResp = self.liff.issueLiffView(liffReq)
            except LiffException as liff_error:
                if liff_error.message == 'invalid request':
                    self.liffBanned.update({
                        'status': True,
                        'time': time.time()
                    })
                    raise Exception('issueLiffView Failed (%s)' % liff_error.message)
                elif liff_error.message == 'user consent required':
                    channelId = liff_error.payload.consentRequired.channelId
                    self.allowLiff(channelId)
                    liffResp = self.liff.issueLiffView(liffReq)
            except Exception:
                raise Exception('issueLiffView Failed (liffId is invalid or your token can\'t do this)')
            self.liffToken = liffResp.accessToken
            self.liffTokens[to] = self.liffToken
        self.to = to
        return self.liffToken
        
    @loggedIn
    def sendLiffMessage(self, message, data=None, liffToken=None, revokeToken=False):
        if liffToken:
            self.server.setLiffHeaders('Authorization', 'Bearer ' + liffToken)
        elif self.liffToken:
            self.server.setLiffHeaders('Authorization', 'Bearer ' + self.liffToken)
        else:
            raise Exception('sendLiffMessage Failed (you must issueLiffView before send)')
        if not data:
            data = {'messages': []}
            if isinstance(message, dict):
                data['messages'].append(message)
            else:
                data['messages'] = message
        # To avoid liff banned
       # waiting = self.wait - time.time()
       # if waiting > 0: time.sleep(waiting)
        r = self.server.postContent(self.server.LINE_LIFF_SEND, headers=self.server.liffHeaders, data=json.dumps(data))
     #   self.wait = time.time() + 1
        resp = r.json()
        if 'message' in resp:
            if not self.resend and self.to:
                self.resend = True
                self.issueLiffView(self.to, revokeToken=True)
                return self.sendLiffMessage(None, data=data, revokeToken=revokeToken)
        if revokeToken:
            try:
                self.revokeToken(self.liffToken)
                self.liffToken = None
            except Exception:
                pass
        self.resend = False
        self.to = None
        return resp

    @loggedIn
    def sendFlexMessage(self, flexContent, altText='Hello World', liffToken=None, revokeToken=False):
        if liffToken:
            self.server.setLiffHeaders('Authorization', 'Bearer ' + liffToken)
        elif self.liffToken:
            self.server.setLiffHeaders('Authorization', 'Bearer ' + self.liffToken)
        else:
            raise Exception('sendLiffMessage Failed (you must issueLiffView before send)')
        messages = [
            {
                'type': 'flex',
                'altText': altText,
                'contents': flexContent
            }
        ]
        data = {'messages': messages}
        # To avoid liff banned
        waiting = self.wait - time.time()
        if waiting > 0: time.sleep(waiting)
        r = self.server.postContent(self.server.LINE_LIFF_SEND, headers=self.server.liffHeaders, data=json.dumps(data))
        self.wait = time.time() + 1
        resp = r.json()
        if 'message' in resp and not self.resend and self.to:
            self.resend = True
            self.issueLiffView(self.to, revokeToken=True)
            return self.sendLiffMessage(None, data=data, revokeToken=revokeToken)
        if revokeToken:
            try:
                self.revokeToken(self.liffToken)
                self.liffToken = None
            except Exception:
                pass
        self.resend = False
        self.to = None
        return resp
    
    @loggedIn
    def sendLiff(self, to, data, mainType=True):
        if to not in self.liffTokens: self.issueLiffView(to, self.settings["arLiff"])
        if not mainType: data = {"type": "flex", "altText": "ᴬ_ᶜᴼᴰᴱ⁴⁴", "contents": {"type": "carousel", "contents": data}}
        self.server.setLiffHeaders('Authorization', 'Bearer ' + self.liffTokens[to])
        data = {'messages': [data]}
        r = self.server.postContent(self.server.LINE_LIFF_SEND, headers=self.server.liffHeaders, data=json.dumps(data))
        resp = r.json()
        if 'message' in resp:
            if resp['message'] == 'invalid receiver':
                if to.startswith('u'): self.sendMention(to, 'sendLiffMessage Failed\n(you must add @! first)', [to])
            elif resp['message'] == 'request blocked':
                print ('\033[1;32m++ Operation : ( LIMIT LIFF ) {}\033[0m'.format(self.settings["arLiff"]))
                liffId = ["1657707255-WVxqmM35", "1657710460-y83a8lNE", "1656063202-j324n1by", "1656174387-eqP4329A"]
                liffId.remove(self.settings["arLiff"])
                self.settings["arLiff"] = random.choice(liffId)
                self.issueLiffView(to, self.settings["arLiff"])
                self.server.setLiffHeaders('Authorization', 'Bearer ' + self.liffTokens[to])
                r = self.server.postContent(self.server.LINE_LIFF_SEND, headers=self.server.liffHeaders, data=json.dumps(data))
            else:
                print ('\033[1;32m++ Operation : ( LIFF ) {}\033[0m'.format(resp['message'].upper()))
                self.issueLiffView(to, self.settings["arLiff"])
                self.server.setLiffHeaders('Authorization', 'Bearer ' + self.liffTokens[to])
                r = self.server.postContent(self.server.LINE_LIFF_SEND, headers=self.server.liffHeaders, data=json.dumps(data))
        else:
            print ('\033[1;32m++ Operation : ( LIFF ) SEND LIFF MESSAGE\033[0m')
    
    @loggedIn
    def sendLiffVideo(self, to, link, preview):
        data = {
            "type": "video",
            "originalContentUrl": link,
            "previewImageUrl": preview
        }
        self.sendLiff(to, data)
    
    @loggedIn
    def sendLiffAudio(self, to, link):
        data = {
            "type": "audio",
            "originalContentUrl": link,
            "duration": 1000
        }
        self.sendLiff(to, data)
    
    @loggedIn
    def sendLiffImage(self, to, link, icon, label, reply=False):
        data = {
            "type": "image",
            "originalContentUrl": link,
            "previewImageUrl": link,
            "sentBy": {
                "label": label,
                "iconUrl": icon,
                "linkUrl": "https://line.me/ti/p/{}".format(self.generateUserTicket())
            }
        }
        self.sendLiff(to, data)
        time.sleep(0.5)

    @loggedIn
    def revokeToken(self, accessToken):
        self.server.setLiffHeaders('Authorization', '')
        self.liff.revokeToken(RevokeTokenRequest(accessToken))