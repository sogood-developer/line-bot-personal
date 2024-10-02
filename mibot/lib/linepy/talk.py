# -*- coding: utf-8 -*-
from lib.akad.ttypes import (
    Message, Location, GetAllChatMidsRequest, DeleteSelfFromChatRequest,
    DeleteOtherFromChatRequest, RejectChatInvitationRequest,
    CancelChatInvitationRequest, InviteIntoChatRequest,
    CreateChatRequest, UpdateChatRequest, GetChatsRequest,
    FindChatByTicketRequest, ReissueChatTicketRequest,
    AcceptChatInvitationByTicketRequest, AcceptChatInvitationRequest,
    ReactRequest, ReactionType, TalkException)
from random import randint
from datetime import datetime, timedelta
from lib.template import Template
import json, ntpath, time, random, requests, pytz, ast

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.default('You want to call the function, you must login to LINE')
    return checkLogin

class Talk(object):
    isLogin = False
    _messageReq = {}
    _unsendMessageReq = 0

    def __init__(self):
        self.isLogin = True

    """User"""

    @loggedIn
    def acquireEncryptedAccessToken(self, featureType=2):
        return self.talk.acquireEncryptedAccessToken(featureType)

    @loggedIn
    def getProfile(self):
        return self.talk.getProfile()

    @loggedIn
    def getSettings(self):
        return self.talk.getSettings()

    @loggedIn
    def getUserTicket(self):
        return self.talk.getUserTicket()

    @loggedIn
    def generateUserTicket(self):
        try:
            ticket = self.getUserTicket().id
        except:
            self.reissueUserTicket()
            ticket = self.getUserTicket().id
        return ticket

    @loggedIn
    def updateProfile(self, profileObject):
        return self.talk.updateProfile(0, profileObject)

    @loggedIn
    def updateSettings(self, settingObject):
        return self.talk.updateSettings(0, settingObject)

    @loggedIn
    def updateSettingsAttribute(self, attrId, value):
        return self.talk.updateSettingsAttribute(0, attrId, value)

    @loggedIn
    def updateProfileAttribute(self, attrId, value):
        return self.talk.updateProfileAttribute(0, attrId, value)

    @loggedIn
    def updateContactSetting(self, mid, flag, value):
        return self.talk.updateContactSetting(0, mid, flag, value)

    @loggedIn
    def deleteContact(self, mid):
        return self.updateContactSetting(mid, 16, 'True')

    @loggedIn
    def renameContact(self, mid, name):
        return self.updateContactSetting(mid, 2, name)

    @loggedIn
    def addToFavoriteContactMids(self, mid):
        return self.updateContactSetting(mid, 8, 'True')

    @loggedIn
    def addToHiddenContactMids(self, mid):
        return self.updateContactSetting(mid, 4, 'True')

    """Operation"""

    @loggedIn
    def fetchOps(self, localRev, count, globalRev, individualRev):
        return self.poll.fetchOps(localRev, count, globalRev, individualRev)

    @loggedIn
    def fetchOperation(self, revision, count=1):
        return self.poll.fetchOperations(revision, count)

    @loggedIn
    def getLastOpRevision(self):
        return self.poll.getLastOpRevision()

    """Message"""
    
    @loggedIn
    def sendMessage(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        if self.appType == 'CHANNELCP':
            contentMetadata.update({"AGENT_NAME": " © sozi", "AGENT_ICON": "https://media1.giphy.com/media/hNs6pybwEIjjKeZSIu/giphy.gif"})
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)
    
    @loggedIn
    def sendReplyMessage(self, to, text, contentMetadata={}, contentType=0, msgIds=None):
        msg = Message()
        msgId = None
        if msgIds is not None:
            msgId = msgIds
        else:
            for dataM in self.talk.getRecentMessagesV2(to, 5):
                if dataM.contentType in [0, 1, 2, 7]:
                    msgId = dataM.id
                    break
        if msgId is not None:
            msg.relatedMessageId = str(msgId)
            msg.relatedMessageServiceCode = 1
            msg.messageRelationType = 3
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        if self.appType == 'CHANNELCP':
            contentMetadata.update({"AGENT_NAME": " © sozi", "AGENT_ICON": "https://media1.giphy.com/media/hNs6pybwEIjjKeZSIu/giphy.gif"})
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @loggedIn
    def sendMessageObject(self, msg):
        to = msg.to
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)
    
    @loggedIn
    def sendLocation(self, to, address, latitude, longitude, phone=None, contentMetadata={}):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = "Location by Hello World"
        msg.contentType, msg.contentMetadata = 15, contentMetadata
        location = Location()
        location.address = address
        location.phone = phone
        location.latitude = float(latitude)
        location.longitude = float(longitude)
        location.title = "「 Location 」"
        msg.location = location
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)
    
    @loggedIn
    def sendReact(self, messageId, reactType):
        if reactType not in [2, 3, 4, 5, 6, 7]:
            raise Exception('Invalid reactType value')
        req = ReactRequest()
        req.messageId = messageId
        req.reactionType = ReactionType()
        req.reactionType.predefinedReactionType = reactType
        return self.talk.react(req)

    @loggedIn
    def sendMessageMusic(self, to, title=None, subText=None, url=None, iconurl=None, contentMetadata={}):
        """
        a : Android
        i : Ios
        """
        self.profile = self.getProfile()
        self.userTicket = self.generateUserTicket()
        title = title if title else 'LINE MUSIC'
        subText = subText if subText else self.profile.displayName
        url = url if url else 'line://ti/p/' + self.userTicket
        iconurl = iconurl if iconurl else 'https://obs.line-apps.com/os/p/%s' % self.profile.mid
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = title
        msg.contentType = 19
        msg.contentMetadata = {
            'text': title,
            'subText': subText,
            'a-installUrl': url,
            'i-installUrl': url,
            'a-linkUri': url,
            'i-linkUri': url,
            'linkUri': url,
            'previewUrl': iconurl,
            'type': 'mt',
            'a-packageName': 'com.spotify.music',
            'countryCode': 'JP',
            'id': 'mt000000000a6b79f9'
        }
        if contentMetadata:
            msg.contentMetadata.update(contentMetadata)
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @loggedIn
    def generateReplyMessage(self, relatedMessageId):
        msg = Message()
        msg.relatedMessageServiceCode = 1
        msg.messageRelationType = 3
        msg.relatedMessageId = str(relatedMessageId)
        return msg

    @loggedIn
    def sendMention(self, to, text="", mids=[], contentMetadata={}):
        arrData = ""
        arr = []
        mention = "@ACode44"
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            unicode = ""
            for point in range(len(mids)):
                unicode += str(texts[point].encode('unicode-escape'))
                textx += str(texts[point])
                slen = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                elen =  12 + int(slen) - 17
                arrData = {'S':str(slen), 'E':str(elen + 13), 'M':mids[point]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            raise Exception("Invalid mention position")
        contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')})
        self.sendMessage(to, textx, contentMetadata, 0)
    
    @loggedIn
    def sendReplyMention(self, to, text="", mids=[], contentMetadata={}, msgIds=None):
        arrData = ""
        arr = []
        mention = "@ACode44"
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            unicode = ""
            for point in range(len(mids)):
                unicode += str(texts[point].encode('unicode-escape'))
                textx += str(texts[point])
                slen = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                elen =  12 + int(slen) - 17
                arrData = {'S':str(slen), 'E':str(elen + 13), 'M':mids[point]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            raise Exception("Invalid mention position")
        contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')})
        self.sendReplyMessage(to, textx, contentMetadata, 0, msgIds=msgIds)
        
    @loggedIn
    def sendMentionEmot(self, to, text, productId, startcode, mids=[]):
        arrData = ""
        arr = []
        EMOT = []
        mention = "@ACode44"
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            unicode = ""
            for point in range(len(mids)):
                unicode += str(texts[point].encode('unicode-escape'))
                textx += str(texts[point])
                slen = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                elen =  12 + int(slen) - 17
                arrData = {'S':str(slen), 'E':str(elen + 13), 'M':mids[point]}
                arr.append(arrData)
                sticonId = "00"+str(startcode+point)
                if len(sticonId) == 4:
                    sticonId = sticonId.replace("0","",1)
                elif len(sticonId) == 5:
                    sticonId = sticonId.replace("0","",2)
                EMOT.append({'S':str(slen), 'E':str(elen + 13), 'productId':productId, "sticonId": sticonId, "version":1})
                textx += mention
            textx += str(texts[len(mids)])
        REPLACE = {"sticon":{"resources":EMOT}}
        contentMetadata = {
            'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),
            "REPLACE": json.dumps(REPLACE),
            "STICON_OWNERSHIP": json.dumps([productId])
        }
        self.sendMessage(to, textx, contentMetadata, 0)

    @loggedIn
    def sendReplyMentionEmot(self, to, text, productId, startcode, mids=[], msgIds=None):
        arrData = ""
        arr = []
        EMOT = []
        mention = "@ACode44"
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            unicode = ""
            for point in range(len(mids)):
                unicode += str(texts[point].encode('unicode-escape'))
                textx += str(texts[point])
                slen = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                elen =  12 + int(slen) - 17
                arrData = {'S':str(slen), 'E':str(elen + 13), 'M':mids[point]}
                arr.append(arrData)
                sticonId = "00"+str(startcode+point)
                if len(sticonId) == 4:
                    sticonId = sticonId.replace("0","",1)
                elif len(sticonId) == 5:
                    sticonId = sticonId.replace("0","",2)
                EMOT.append({'S':str(slen), 'E':str(elen + 13), 'productId':productId, "sticonId": sticonId, "version":1})
                textx += mention
            textx += str(texts[len(mids)])
        REPLACE = {"sticon":{"resources":EMOT}}
        contentMetadata = {
            'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'),
            "REPLACE": json.dumps(REPLACE),
            "STICON_OWNERSHIP": json.dumps([productId])
        }
        self.sendReplyMessage(to, textx, contentMetadata, 0, msgIds=msgIds)

    @loggedIn
    def sendFakeMentionSticker(self, to, text, stkver, stkpkgid, stkid, mids=[]):
        arrData = ""
        arr = []
        mention = "@ACode44"
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            unicode = ""
            for point in range(len(mids)):
                unicode += str(texts[point].encode('unicode-escape'))
                textx += str(texts[point])
                slen = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                elen =  12 + int(slen) - 17
                arrData = {'S':str(slen), 'E':str(elen + 13), 'M':mids[point]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            raise Exception("Invalid mention position")
        self.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}'), 'STKVER': str(stkver), 'STKPKGID': str(stkpkgid), 'STKID': str(stkid)}, 7)
    
    @loggedIn
    def sendMentionLocation(self, to, text="", mids=[]):
        arrData = ""
        arr = []
        mention = "@ACode44"
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ""
            unicode = ""
            for point in range(len(mids)):
                unicode += str(texts[point].encode('unicode-escape'))
                textx += str(texts[point])
                slen = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                elen =  12 + int(slen) - 17
                arrData = {'S':str(slen), 'E':str(elen + 13), 'M':mids[point]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            raise Exception("Invalid mention position")
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = textx
        msg.contentType = 15
        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
        location = Location()
        location.address = "Bogor Rain City"
        location.phone = None
        location.latitude = float(-6.597629)
        location.longitude = float(106.799568)
        location.title = "› BOGOR ‹"
        msg.location = location
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessage(self._messageReq[to], msg)

    @loggedIn
    def sendSticker(self, to, stickerVer, packageId, stickerId):
        contentMetadata = {
            'STKVER': stickerVer,
            'STKPKGID': packageId,
            'STKID': stickerId
        }
        return self.sendMessage(to, '', contentMetadata, 7)

    @loggedIn
    def sendReplySticker(self, to, stickerVer, packageId, stickerId, msgIds=None):
        contentMetadata = {
            'STKVER': stickerVer,
            'STKPKGID': packageId,
            'STKID': stickerId
        }
        return self.sendReplyMessage(to, '', contentMetadata, 7, msgIds=msgIds)
    
    @loggedIn
    def sendEmote(self, to, productId, sticonId):
        REPLACE = {"sticon":{"resources":[{"S": "0", "E": "7","productId":productId, "sticonId": sticonId, "version":1}]}}
        contentMetadata = {
            "REPLACE": json.dumps(REPLACE),
            "STICON_OWNERSHIP": json.dumps([productId])
        }
        return self.sendMessage(to, 'ACode44', contentMetadata, 0)

    @loggedIn
    def sendReplyEmote(self, to, productId, sticonId, msgIds=None):
        REPLACE = {"sticon":{"resources":[{"S": "0", "E": "7","productId":productId, "sticonId": sticonId, "version":1}]}}
        contentMetadata = {
            "REPLACE": json.dumps(REPLACE),
            "STICON_OWNERSHIP": json.dumps([productId])
        }
        return self.sendReplyMessage(to, 'ACode44', contentMetadata, 0, msgIds=msgIds)

    @loggedIn
    def sendContact(self, to, mid):
        contentMetadata = {'mid': mid}
        return self.sendMessage(to, '', contentMetadata, 13)
    
    def sendReplyContact(self, to, mid, msgIds=None):
        contentMetadata = {'mid': mid}
        return self.sendReplyMessage(to, '', contentMetadata, 13, msgIds=msgIds)

    @loggedIn
    def sendGift(self, to, productId, productType):
        if productType not in ['theme','sticker']:
            raise Exception('Invalid productType value')
        contentMetadata = {
            'MSGTPL': str(randint(0, 12)),
            'PRDTYPE': productType.upper(),
            'STKPKGID' if productType == 'sticker' else 'PRDID': productId
        }
        return self.sendMessage(to, '', contentMetadata, 9)

    @loggedIn
    def sendMessageAwaitCommit(self, to, text, contentMetadata={}, contentType=0):
        msg = Message()
        msg.to, msg._from = to, self.profile.mid
        msg.text = text
        msg.contentType, msg.contentMetadata = contentType, contentMetadata
        if to not in self._messageReq:
            self._messageReq[to] = -1
        self._messageReq[to] += 1
        return self.talk.sendMessageAwaitCommit(self._messageReq[to], msg)

    @loggedIn
    def unsendMessage(self, messageId):
        self._unsendMessageReq += 1
        return self.talk.unsendMessage(self._unsendMessageReq, messageId)

    @loggedIn
    def getRecentMessagesV2(self, chatId, count=1001):
    	return self.talk.getRecentMessagesV2(chatId,count)

    @loggedIn
    def requestResendMessage(self, senderMid, messageId):
        return self.talk.requestResendMessage(0, senderMid, messageId)

    @loggedIn
    def respondResendMessage(self, receiverMid, originalMessageId, resendMessage, errorCode):
        return self.talk.respondResendMessage(0, receiverMid, originalMessageId, resendMessage, errorCode)

    @loggedIn
    def removeMessage(self, messageId):
        return self.talk.removeMessage(messageId)
    
    @loggedIn
    def removeAllMessages(self, lastMessageId):
        return self.talk.removeAllMessages(0, lastMessageId)

    @loggedIn
    def removeMessageFromMyHome(self, messageId):
        return self.talk.removeMessageFromMyHome(messageId)

    @loggedIn
    def destroyMessage(self, chatId, messageId):
        return self.talk.destroyMessage(0, chatId, messageId, sessionId)
    
    @loggedIn
    def sendChatChecked(self, consumer, messageId):
        return self.talk.sendChatChecked(0, consumer, messageId)
    
    @loggedIn
    def sendChatRemoved(self, consumer, messageId):
        return self.talk.sendChatRemoved(0, consumer, messageId)

    @loggedIn
    def sendEvent(self, messageObject):
        return self.talk.sendEvent(0, messageObject)

    @loggedIn
    def getLastReadMessageIds(self, chatId):
        return self.talk.getLastReadMessageIds(0, chatId)

    @loggedIn
    def getPreviousMessagesV2WithReadCount(self, messageBoxId, endMessageId, messagesCount=50):
        return self.talk.getPreviousMessagesV2WithReadCount(messageBoxId, endMessageId, messagesCount)
    
    @loggedIn
    def mentionMembersEmoticon(self, to, productId, mids=[], msgIds=None):
        if self.profile.mid in mids: mids.remove(self.profile.mid)
        parsed_len = len(mids)//20+1
        result = '𝗠𝗲𝗻𝘁𝗶𝗼𝗻 𝗔𝗹𝗹 𝗠𝗲𝗺𝗯𝗲𝗿𝘀\n'
        for point in range(parsed_len):
            target = []
            for mid in mids[point*20:(point+1)*20]:
                result += '➡️ › @!\n'
                if mid == mids[-1]:
                    result += '𝗧𝗼𝘁𝗮𝗹: %i 𝗠𝗲𝗺𝗯𝗲𝗿𝘀' % len(mids)
                target.append(mid)
            if target:
                if result.endswith('\n'): result = result[:-1]
                startcode = 21
                if point % 2 == 0:
                    startcode = 1
                self.sendReplyMentionEmot(to, result, productId, startcode, target, msgIds=msgIds)
            result = ''
    
    @loggedIn
    def fakeMentionSticker(self, to, stkver, stkpkgid, stkid, mids=[]):
        if self.profile.mid in mids: mids.remove(self.profile.mid)
        parsed_len = len(mids)//140+1
        result = '𝗠𝗲𝗻𝘁𝗶𝗼𝗻 𝗔𝗹𝗹 𝗠𝗲𝗺𝗯𝗲𝗿𝘀\n'
        for point in range(parsed_len):
            target = []
            for mid in mids[point*140:(point+1)*140]:
                result += '➡️ › @!\n'
                if mid == mids[-1]:
                    result += '𝗧𝗼𝘁𝗮𝗹: %i 𝗠𝗲𝗺𝗯𝗲𝗿𝘀' % len(mids)
                target.append(mid)
            if target:
                if result.endswith('\n'): result = result[:-1]
                try:
                    stid = stkid + (point+1)
                    if str(stkid) == str(stid):
                        stid += 1
                    self.sendFakeMentionSticker(to, result, stkver, stkpkgid, stid, target)
                except TalkException as e:
                    if e.code == 32:
                        stid = stkid - (point+1)
                        if str(stkid) == str(stid):
                            stid -= 1
                        self.sendFakeMentionSticker(to, result, stkver, stkpkgid, stid, target)
            result = ''
    
    @loggedIn
    def mentionLocation(self, to, mids=[]):
        if self.profile.mid in mids: mids.remove(self.profile.mid)
        parsed_len = len(mids)//140+1
        result = '𝗠𝗲𝗻𝘁𝗶𝗼𝗻 𝗔𝗹𝗹 𝗠𝗲𝗺𝗯𝗲𝗿𝘀\n'
        for point in range(parsed_len):
            target = []
            for mid in mids[point*140:(point+1)*140]:
                result += '➡️ › @!\n'
                if mid == mids[-1]:
                    result += '𝗧𝗼𝘁𝗮𝗹: %i 𝗠𝗲𝗺𝗯𝗲𝗿𝘀' % len(mids)
                target.append(mid)
            if target:
                if result.endswith('\n'): result = result[:-1]
                self.sendMentionLocation(to, result, target)
            result = ''

    @loggedIn
    def mentionMembers(self, to, mids=[], msgIds=None):
        if self.profile.mid in mids: mids.remove(self.profile.mid)
        parsed_len = len(mids)//20+1
        result = '𝗠𝗲𝗻𝘁𝗶𝗼𝗻 𝗔𝗹𝗹 𝗠𝗲𝗺𝗯𝗲𝗿𝘀\n'
        for point in range(parsed_len):
            target = []
            for mid in mids[point*20:(point+1)*20]:
                result += '➡️ › @!\n'
                if mid == mids[-1]:
                    result += '𝗧𝗼𝘁𝗮𝗹: %i 𝗠𝗲𝗺𝗯𝗲𝗿𝘀' % len(mids)
                target.append(mid)
            if target:
                if result.endswith('\n'): result = result[:-1]
                self.sendReplyMention(to, result, target, msgIds=msgIds)
            result = ''
            
    @loggedIn
    def getEffect(self, mid=None):
        data = self.getProfileDetail(mid)
        res = {"result": []}
        if 'components' in data['result']['userStyleMedia']:
            for i in data['result']['userStyleMedia']['components']:
                items = {}
                if i['type'] == "STICKER":
                    items['type'] = 'Sticker'
                    items['packageId'] = i['data'][0]['sticker']['packageId']
                    items['stickerId'] = i['data'][0]['sticker']['id']
                    res['result'].append(items)
                elif i['type'] == "PFRAME" and "data" in i:
                    items['type'] = 'Image'
                    items['url'] = f'{self.server.LINE_OBS_DOMAIN}/r/{i["data"][0]["media"]["serviceName"]}/{i["data"][0]["media"]["obsNamespace"]}/{i["data"][0]["media"]["objectId"]}'
                    res['result'].append(items)
                elif i['type'] == "TEXT" and "data" in i:
                    for style in i["data"]:
                        if style["type"] == "STYLETEXT":
                            items['type'] = 'Text'
                            items["text"] = style["styleText"]["text"]
                            res['result'].append(items)
                elif i['type'] == "LINK" and "data" in i:
                    for style in i["data"]:
                        if style["type"] == "LINK":
                            items['type'] = 'Link'
                            items["url"] = f'{style["link"]["prefix"]}{style["link"]["postfix"]}'
                            res['result'].append(items)
        return res
    
    @loggedIn
    def metadataFilter(self, dataM, num=0, num2=0, text='', type='emoji'):
        if type == 'emoji' or type == 'emoji2':
            REPLACE = {"sticon":{"resources": []}}
            data_replace = eval(dataM['REPLACE'])
            for data_rep in data_replace["sticon"]["resources"]:
                if type == 'emoji':
                    REPLACE["sticon"]["resources"].append({"S": str(int(data_rep["S"])-num), "E": str(int(data_rep["E"])-num),"productId":data_rep["productId"], "sticonId": data_rep["sticonId"], "version":1})
                elif type == 'emoji2':
                    REPLACE["sticon"]["resources"].append({"S": str(int(data_rep["S"])+num), "E": str(int(data_rep["E"])+num),"productId":data_rep["productId"], "sticonId": data_rep["sticonId"], "version":1})
                else:
                    return 'invalid type'
            contentMetadata = {
                "REPLACE": json.dumps(REPLACE),
                "STICON_OWNERSHIP": dataM['STICON_OWNERSHIP']
            }
            return contentMetadata
        elif type == 'emojiComment' or type == 'emojiComment2':
            contentMetadata = {'categoryId': 'sticon', 'extData': {'sticonMetas': []}}
            data_replace = eval(dataM['REPLACE'])
            for data_rep in data_replace["sticon"]["resources"]:
                if type == 'emojiComment':
                    contentMetadata["extData"]["sticonMetas"].append({"S": str(int(data_rep["S"])-num), "E": str(int(data_rep["E"])-num),"productId":data_rep["productId"], "sticonId": data_rep["sticonId"], "version":1, "resourceType": None})
                elif type == 'emojiComment2':
                    contentMetadata["extData"]["sticonMetas"].append({"S": str(int(data_rep["S"])+num), "E": str(int(data_rep["E"])+num),"productId":data_rep["productId"], "sticonId": data_rep["sticonId"], "version":1, "resourceType": None})
                else:
                    return 'invalid type'
            return contentMetadata
        elif type == 'mention':
            arrData = []
            if "@!" in text:
                texts = text.split("@!")
                textx = ""
                unicode = ""
                unicode += str(texts[0].encode('unicode-escape'))
                textx += str(texts[0])
                slen = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                elen = int(slen) + 2
                arrData.append({'S': str(slen), 'E': str(elen), 'M': self.profile.mid})
            contentMetadata = {
                'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')
            }
            return contentMetadata
        elif type == 'mentionComment':
            if "@!" in text:
                arrData = []
                texts = text.split("@!")
                textx = ""
                unicode = ""
                unicode += str(texts[0].encode('unicode-escape'))
                textx += str(texts[0])
                start = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                end =  12 + int(start) - 17
                arrData.append({'start': start, 'end': end+7, 'user': {'actorId': self.profile.mid}})
            contentMetadata = {
                'recallInfos': arrData
            }
            return contentMetadata
        else:
            return 'invalid type'

    @loggedIn
    def getReplyMessage(self, to, msgId):
        msg = None
        datas = self.getRecentMessagesV2(to, 1001)
        for data in datas:
            if data.id == msgId:
                msg = data
                break
        return msg
    
    @loggedIn
    def getBcFriend(self, total=1500):
        data = self.getAllContactIds()
        friends = []
        friend = []
        for mid in data:
            try:
                profile = self.getContact(mid)
            except:
                self.deleteContact(mid)
                continue
            if not profile.capableBuddy:
                if mid not in friends:
                    friends.append(mid)
        for point in range(total):
            if len(friends) == 0:
                break
            midd = random.choice(friends)
            if midd not in friend:
                friends.remove(midd)
                friend.append(midd)
        return friend
    
    @loggedIn
    def getTokenApi(self, to, user, app_type):
        params = {
            'appType': app_type,
            'appVer': self.server.APP_VERSION[app_type],
            'sysName': "Sozi",
            'sysVer': self.server.SYSTEM_VERSION[app_type],
            'cert': None
        }
        self.sendMessage(to, 'Loading......')
        try:
            r = json.loads(requests.get("https://acode44.herokuapp.com/qrcode", params=params).text)
            self.sendMessage(to, 'Open this link on your LINE for smartphone in 2 minutes\n› ' + r["URL"])
        except:
            raise Exception("SQR ERROR")
        try:
            r = json.loads(requests.get(r["callbackPincode"]).text)
        except:
            raise Exception("LOGIN TIMEOUT")
        if len(r["pincode"]) == 4:
            time.sleep(1)
            self.sendMention(to, f"Pincode: {r['pincode']}\n@!", [user])
        elif params["cert"] is None:
            raise Exception("LINE 9.20.1 cant login")
        try:
            r = json.loads(requests.get(r["callbackToken"]).text)
        except:
            raise Exception("PINCODE TIMEOUT")
        self.sendMessage(to, "authtoken sent to personal chat")
        self.sendMessage(user, "AuthToken: {}".format(r["authToken"]))
        self.sendMessage(user, "Certificate: {}".format(r["certificate"]))
    
    @loggedIn
    def sendMode(self, msg, to, sender, cmd, text, textDown='© S O Z I'):
        res = ""
        if self.settings["templateMode"]:
            if self.settings["tempMode"] == "footer":
                self.sendFooter(to, text, self.settings["setFlag"]["icon"], self.settings["setFlag"]["name"], reply=True)
            else:
                if msg == "kosong": toType = "kosong"
                else: toType = msg.toType
                if toType == 0:
                    profile = self.getContact(to)
                    if profile.pictureStatus is None: pictGroup = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
                    else: pictGroup = "https://obs.line-scdn.net/" + profile.pictureStatus
                    name = profile.displayName
                elif toType == 1:
                    pictGroup = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
                    name = "Multi Chat"
                elif toType == 2 or toType == "kosong":
                    group = self.getChats([to], True, False).chats[0]
                    if group.picturePath == "": pictGroup = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
                    else: pictGroup = "https://obs.line-scdn.net" + group.picturePath
                    if self.settings["tempMode"] == "line": name = group.chatName+"({})".format(len(group.extra.groupExtra.memberMids))
                    else: name = group.chatName
                if self.settings["tempMode"] == "line":
                    profile = self.getContact(sender)
                    if profile.pictureStatus is None: pictReply = "https://i.ibb.co/zhKTF0F/d8c4a07c1032.jpg"
                    else: pictReply = "https://obs.line-scdn.net/" + profile.pictureStatus
                    nameReply = profile.displayName
                    if msg == 'kosong': msgId = "https://self.me/R/ti/p/~arshleo"
                    else: msgId = "https://self.me/R/nv/chatMsg?chatId={}&messageId={}".format(to, msg.id)
                    jam = pytz.timezone("Asia/Jakarta")
                    jamSekarang = datetime.now(tz=jam)
                    wib = datetime.strftime(jamSekarang, '%H:%M:%S').split(":")
                    data = [Template().line(text, self.settings["tempStyle"], pictGroup, pictReply, name, nameReply, cmd, msgId, wib[0], wib[1])]
                    self.sendLiff(to, data, mainType=False)
                elif self.settings["tempMode"] == "whatsapp":
                    jam = pytz.timezone("Asia/Jakarta")
                    jamSekarang = datetime.now(tz=jam)
                    wib = datetime.strftime(jamSekarang, '%H:%M:%S').split(":")
                    data = [Template().whatsapp(text, self.settings["tempStyle"], pictGroup, name, wib[0], wib[1])]
                    self.sendLiff(to, data, mainType=False)
                elif self.settings["tempMode"] == "telegram":
                    profile = self.getContact(sender)
                    if msg == 'kosong': msgId = "https://self.me/R/ti/p/~arshleo"
                    else: msgId = "https://self.me/R/nv/chatMsg?chatId={}&messageId={}".format(to, msg.id)
                    jam = pytz.timezone("Asia/Jakarta")
                    jamSekarang = datetime.now(tz=jam)
                    wib = datetime.strftime(jamSekarang, '%H:%M:%S').split(":")
                    data = [Template().telegram(text, self.settings["tempStyle"], pictGroup, name, profile.displayName, cmd, msgId, wib[0], wib[1])]
                    self.sendLiff(to, data, mainType=False)
                elif self.settings["tempMode"] == "instagram":
                    data = [Template().instagram(text, self.settings["tempStyle"], pictGroup, name)]
                    self.sendLiff(to, data, mainType=False)
        else:
            self.sendMessage(to, text)
    
    @loggedIn
    def mainMenu(self, to, picture, name, setKey, background, isi=[]):
        res = "› C O M M A N D\n\n"
        if self.settings["templateMode"]:
            if self.settings["tempMode"] == "footer":
                for point in range(len(isi)):
                    if point == 0: res += "• %s%s" % (setKey.title(), isi[point])
                    else: res += "\n• %s%s" % (setKey.title(), isi[point])
                self.sendFooter(to, res, self.settings["setFlag"]["icon"], self.settings["setFlag"]["name"], reply=True)
            else:
                if len(isi) == 6:
                    data = Template().main_menu(picture, name, setKey.title(), 'https://line.me/R/ti/p/~arshleo', text=isi[0].upper(), text2=isi[1].upper(), text3=isi[2].upper(), text4=isi[3].upper(), text5=isi[4].upper(), text6=isi[5].upper())
                    datap = {
                        "type": "flex",
                        "altText": "SOZI MAIN MENU",
                        "contents": {
                            "type": "carousel",
                            "contents": [data]
                        }
                    }
                else:
                    data = Template().old_main_menu(picture, name, setKey.title(), 'https://line.me/R/ti/p/~arshleo', text=isi[0].upper(), text2=isi[1].upper(), text3=isi[2].upper(), text4=isi[3].upper(), text5=isi[4].upper(), text6=isi[5].upper(), text7=isi[6].upper(), text8=isi[7].upper(), text9=isi[8].upper(), text10=isi[9].upper())
                    data2 = Template().old_main_menu(picture, name, setKey.title(), 'https://line.me/R/ti/p/~arshleo', text=isi[10].upper(), text2=isi[11].upper(), text3=isi[12].upper(), text4=isi[13].upper(), text5=isi[14].upper(), text6=isi[15].upper(), text7=isi[16].upper(), text8=isi[17].upper(), text9=isi[18].upper(), text10=isi[19].upper())
                    datap = {
                        "type": "flex",
                        "altText": "SOZI MAIN MENU",
                        "contents": {
                            "type": "carousel",
                            "contents": [data, data2]
                        }
                    }
                self.sendLiff(to, datap)
        else:
            for point in range(len(isi)):
                if point == 0: res += "• %s%s" % (setKey.title(), isi[point])
                else: res += "\n• %s%s" % (setKey.title(), isi[point])
            self.sendReplyMessage(to, res)

    @loggedIn
    def sendFooter(self, to, text, AGENT_ICON=None, AGENT_NAME=None, reply=False):
        if AGENT_ICON is None: AGENT_ICON = self.settings["setFlag"]["icon"]
        if AGENT_NAME is None: AGENT_NAME = self.settings["setFlag"]["name"]
        data = {
            "type": "text",
            "text": text,
            "sentBy": {
                "label": AGENT_NAME,
                "iconUrl": "https://i.ibb.co/7tmGYQ1/FOOTER-ACODE44.gif",
                "linkUrl": "https://line.me/ti/p/{}".format(self.generateUserTicket())
            }
        }
        if self.settings["templateMode"]: self.sendLiff(to, data)
        elif reply: self.sendReplyMessage(to, text)
        else: self.sendMessage(to, text)
        
    @loggedIn
    def sendLeaveMessage(self, op):
        if op.param2 not in self.protect["blacklist"]:
            if op.param1 in self.settings['greet']['leave']['group'] or self.settings['greet']['leave']['allText']:
            
                if '@!' not in self.settings['greet']['leave']['message']:
                    self.sendMode("kosong", op.param1, op.param2, "NOTIFIED LEAVE GROUP", self.settings['greet']['leave']['message'].format(chatName=self.getChats([op.param1], False, False).chats[0].chatName, displayName=self.getContact(op.param2).displayName))
                else:
                    self.sendMention(op.param1, self.settings['greet']['leave']['message'].format(chatName=self.getChats([op.param1], False, False).chats[0].chatName, displayName=self.getContact(op.param2).displayName), [op.param2])
                    
            if op.param1 in self.settings['greet']['leave']['groupSticker'] or self.settings['greet']['leave']['allSticker']:
                if self.settings['greet']['leave']['sticker']["STKID"] != 'kosong':
                    try:
                        self.sendSticker(op.param1, self.settings['greet']['leave']['sticker']["STKVER"], self.settings['greet']['leave']['sticker']["STKPKGID"], self.settings['greet']['leave']['sticker']["STKID"])
                    except:
                        pass
    
            if op.param1 in self.settings['greet']['leave']['groupImage'] or self.settings['greet']['leave']['allImage']:
                if self.settings['greet']['leave']['imagePath'] is None:
                    profile = self.getContact(op.param2)
                    if profile.pictureStatus:
                        self.sendImageWithURL(op.param1, 'https://obs.line-scdn.net/' + profile.pictureStatus)
                else:
                    self.sendImage(op.param1, self.settings['greet']['leave']['imagePath'])
                    
    @loggedIn
    def sendWelcomeMessage(self, op):
        if op.param2 not in self.protect["blacklist"]:
            if op.param1 in self.settings['greet']['join']['group'] or self.settings['greet']['join']['allText']:
                if '@!' not in self.settings['greet']['join']['message']:
                    self.sendMode("kosong", op.param1, op.param2, "NOTIFIED ACCEPT GROUP", self.settings['greet']['join']['message'].format(chatName=self.getChats([op.param1], False, False).chats[0].chatName, displayName=self.getContact(op.param2).displayName))
                else:
                    self.sendMention(op.param1, self.settings['greet']['join']['message'].format(chatName=self.getChats([op.param1], False, False).chats[0].chatName, displayName=self.getContact(op.param2).displayName), [op.param2])
                    
            if op.param1 in self.settings['greet']['join']['groupSticker'] or self.settings['greet']['join']['allSticker']:
                if self.settings['greet']['join']['sticker']["STKID"] != 'kosong':
                    try:
                        self.sendSticker(op.param1, self.settings['greet']['join']['sticker']["STKVER"], self.settings['greet']['join']['sticker']["STKPKGID"], self.settings['greet']['join']['sticker']["STKID"])
                    except:
                        pass
        
            if op.param1 in self.settings['greet']['join']['groupImage'] or self.settings['greet']['join']['allImage']:
                if self.settings['greet']['join']['imagePath'] is None:
                    profile = self.getContact(op.param2)
                    if profile.pictureStatus:
                        self.sendImageWithURL(op.param1, 'https://obs.line-scdn.net/' + profile.pictureStatus)
                else:
                    self.sendImage(op.param1, self.settings['greet']['join']['imagePath'])
        self.setts["notifJoin"][op.param1].append(op.param2)
    
    @loggedIn
    def sendBroadcastPost(self, msg, to, sender):
        if self.setts["bcPost"]["toFriend"]:
            if msg.contentMetadata['serviceType'] == 'MH':
                friends = self.getBcFriend()
                id = msg.contentMetadata['postEndUrl'].split("postId=")[1]
                self.sendFooter(to, 'Loading...')
                success = []
                for friend in friends:
                    self.sendPostToTalk(friend, id)
                    success.append(friend)
                    time.sleep(0.8)
                self.setts["bcPost"]["toFriend"] = False
                self.sendMode(msg, to, sender, "Broadcast Post", 'Broadcast Post Friend\nSuccess: {}x'.format(len(success)))
        elif self.setts["bcPost"]["toGroup"]:
            if msg.contentMetadata['serviceType'] == 'MH':
                groups = self.getAllChatMids(True, False).memberChatMids
                id = msg.contentMetadata['postEndUrl'].split("postId=")[1]
                self.sendFooter(to, 'Loading...')
                success = []
                for group in groups:
                    if group not in self.settings["bcFilter"]:
                        self.sendPostToTalk(group, id)
                        success.append(group)
                        time.sleep(0.8)
                self.setts["bcPost"]["toGroup"] = False
                self.sendMode(msg, to, sender, "Broadcast Post", 'Broadcast Post Group\nSuccess: {}x'.format(len(success)))
        elif self.setts["bcPost"]["toAll"]:
            if msg.contentMetadata['serviceType'] == 'MH':
                gogo = make_list(self.getAllChatMids(True, False).memberChatMids) + self.getBcFriend()
                id = msg.contentMetadata['postEndUrl'].split("postId=")[1]
                self.sendFooter(to, 'Loading...')
                success = []
                for gog in gogo:
                    if gog not in self.settings["bcFilter"]:
                        self.sendPostToTalk(gog, id)
                        success.append(gog)
                        time.sleep(0.8)
                self.setts["bcPost"]["toAll"] = False
                self.sendMode(msg, to, sender, "Broadcast Post", 'Broadcast Post All\nSuccess: {}x'.format(len(success)))
    
    @loggedIn
    def anti_spam(self, sender, sec, data):
        if sender not in data:
            data[sender] = {'time': time.time(), 'floods': 0, 'ex': False}
        if time.time() - data[sender]["time"] <= sec: data[sender]["floods"] += 1
        else: data[sender]["floods"] = 1
        if data[sender]["floods"] >= 2: return True
        return False
    
    @loggedIn
    def invite_list(self, to, txt, sender, sec):
        check = self.anti_spam(sender, sec, self.setts["spamCList"])
        if check: return
        friends = self.getAllContactIds()
        groups = self.getChats([to]).chats[0]
        target = []
        for mid in self.protect['contact_list'][txt]:
            if mid not in friends:
                try:
                    self.findAndAddContactsByMid(mid)
                    time.sleep(5)
                except TalkException as talk_error:
                    if talk_error.code in [3, 35]:
                        if talk_error.code == 3:
                            self.protect['contact_list'][txt].remove(mid)
                        continue
            if mid in groups.extra.groupExtra.memberMids or mid in groups.extra.groupExtra.inviteeMids:
                continue
            if mid not in target:
                target.append(mid)
        if target:
            total = 500 - len(groups.extra.groupExtra.memberMids) - len(groups.extra.groupExtra.inviteeMids)
            if total != 0: self.inviteIntoChat(to, target[0:total])
            else: self.sendMessage(to, 'MEMBER & PENDING IS FULL')
        self.setts["spamCList"][sender]["time"] = time.time()
    
    @loggedIn
    def text_list(self, to, txt, sender, msg_id, sec):
        check = self.anti_spam(sender, sec, self.setts["spamText"])
        if check: return
        elif 'contentMetadata' in self.textsx[txt]:
            contentMetadata = {"REPLACE": self.textsx[txt]['contentMetadata']['REPLACE'], "STICON_OWNERSHIP": self.textsx[txt]['contentMetadata']['STICON_OWNERSHIP']}
            if '@!' in self.textsx[txt]['message']:
                arrData = []
                mentions = ast.literal_eval(self.textsx[txt]['contentMention']['MENTION'])
                for mention in mentions['MENTIONEES']:
                    arrData.append({'S':mention['S'], 'E':mention['E'], 'M':sender})
                contentMetadata.update({'MENTION': str('{"MENTIONEES":' + json.dumps(arrData) + '}')})
            self.sendReplyMessage(to, self.textsx[txt]['message'], contentMetadata, msgIds=msg_id)
        elif '@!' not in self.textsx[txt]: self.sendReplyMessage(to, self.textsx[txt], msgIds=msg_id)
        else: self.sendReplyMention(to, self.textsx[txt], [sender], msgIds=msg_id)
        self.setts["spamText"][sender]["time"] = time.time()

    @loggedIn
    def mid_list(self, to, text, sender, sec):
        check = self.anti_spam(sender, sec, self.setts["spamText"])
        if check: return
        mid_regex = self.server.MID_REGEX.findall(text)
        doneMid = []
        for mid in mid_regex:
            if mid not in doneMid:
                try: self.sendContact(to, mid)
                except: pass
                doneMid.append(mid)
        self.setts["spamText"][sender]["time"] = time.time()

    @loggedIn
    def multi_list(self, to, txt, sender, sec):
        check = self.anti_spam(sender, sec, self.setts["spamMulti"])
        if check: return
        for mul in self.protect['multi_list'][txt]:
            if mul['type'] == 'text': self.sendMessage(to, mul['text'])
            elif mul['type'] == 'image': self.sendImage(to, mul['path'])
            elif mul['type'] == 'video': self.sendVideo(to, mul['path'])
            elif mul['type'] == 'audio': self.sendAudio(to, mul['path'])
            elif mul['type'] == 'contact': self.sendContact(to, mul['mid'])
        self.setts["spamMulti"][sender]["time"] = time.time()
    
    @loggedIn
    def picture_list(self, to, txt, sender, msg_id, sec):
        check = self.anti_spam(sender, sec, self.setts["spamImage"])
        if check: return
        self.sendReplyImage(to, self.pictures[txt], msgIds=msg_id)
        self.setts["spamImage"][sender]["time"] = time.time()
        
    @loggedIn
    def audio_list(self, to, txt, sender, sec):
        check = self.anti_spam(sender, sec, self.setts["spamAudio"])
        if check: return
        self.sendAudio(to, self.audsx[txt])
        self.setts["spamAudio"][sender]["time"] = time.time()
    
    @loggedIn
    def video_list(self, to, txt, sender, sec):
        check = self.anti_spam(sender, sec, self.setts["spamVideo"])
        if check: return
        self.sendVideo(to, self.vidsx[txt])
        self.setts["spamVideo"][sender]["time"] = time.time()
    
    @loggedIn
    def sticker_list(self, to, txt, sender, sec):
        if self.settings['stickertemplate']:
            if sender not in self.setts["spamBigSticker"]:
                self.setts["spamBigSticker"][sender] = {'time': time.time(), 'floods': 0, 'banned': None}
            if self.setts["spamBigSticker"][sender]["banned"] is not None:
                if self.setts["spamBigSticker"][sender]["banned"] >= time.time(): return
                else: self.setts["spamBigSticker"][sender]["banned"] = None
            if time.time() - self.setts["spamBigSticker"][sender]["time"] <= sec:
                self.setts["spamBigSticker"][sender]["floods"] += 1
                if self.setts["spamBigSticker"][sender]["floods"] >= 3:
                    if self.setts["spamBigSticker"][sender]["banned"] is None:
                        biling = int(60*60*1)
                        self.setts["spamBigSticker"][sender]["banned"] = time.time()+biling
                    return
                self.sendBigSticker(to, self.stickers[txt])
            else:
                self.setts["spamBigSticker"][sender]["floods"] = 0
                self.sendBigSticker(to, self.stickers[txt])
            self.setts["spamBigSticker"][sender]["time"] = time.time()
        else:
            try:
                stid = self.stickers[txt]['STKID']
                stpk = self.stickers[txt]['STKPKGID']
                stv = self.stickers[txt]['STKVER']
                if sender not in self.setts["spamBigSticker"]:
                    self.setts["spamBigSticker"][sender] = {'time': time.time(), 'floods': 0, 'banned': None}
                if self.setts["spamBigSticker"][sender]["banned"] is not None:
                    if self.setts["spamBigSticker"][sender]["banned"] >= time.time(): return
                    else: self.setts["spamBigSticker"][sender]["banned"] = None
                if time.time() - self.setts["spamBigSticker"][sender]["time"] <= sec:
                    self.setts["spamBigSticker"][sender]["floods"] += 1
                    if self.setts["spamBigSticker"][sender]["floods"] >= 3:
                        if self.setts["spamBigSticker"][sender]["banned"] is None:
                            biling = int(60*60*1)
                            self.setts["spamBigSticker"][sender]["banned"] = time.time()+biling
                        return
                    self.sendSticker(to, stv, stpk, stid)
                else:
                    self.setts["spamBigSticker"][sender]["floods"] = 0
                    self.sendSticker(to, stv, stpk, stid)
                self.setts["spamBigSticker"][sender]["time"] = time.time()
            except TalkException as e:
                if e.code == 32:
                    if sender not in self.setts["spamBigSticker"]:
                        self.setts["spamBigSticker"][sender] = {'time': time.time(), 'floods': 0, 'banned': None}
                    if self.setts["spamBigSticker"][sender]["banned"] is not None:
                        if self.setts["spamBigSticker"][sender]["banned"] >= time.time(): return
                        else: self.setts["spamBigSticker"][sender]["banned"] = None
                    if time.time() - self.setts["spamBigSticker"][sender]["time"] <= sec:
                        self.setts["spamBigSticker"][sender]["floods"] += 1
                        if self.setts["spamBigSticker"][sender]["floods"] >= 3:
                            if self.setts["spamBigSticker"][sender]["banned"] is None:
                                biling = int(60*60*1)
                                self.setts["spamBigSticker"][sender]["banned"] = time.time()+biling
                            return
                        self.sendBigSticker(to, self.stickers[txt])
                    else:
                        self.setts["spamBigSticker"][sender]["floods"] = 0
                        self.sendBigSticker(to, self.stickers[txt])
                    self.setts["spamBigSticker"][sender]["time"] = time.time()

    """Object"""
        
    @loggedIn
    def sendImage(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 1).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectId)

    @loggedIn
    def sendImageWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendImage(to, path)
    
    @loggedIn
    def sendReplyImage(self, to, path, msgIds=None):
        objectId = self.sendReplyMessage(to=to, text=None, contentType = 1, msgIds=msgIds).id
        return self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=objectId)

    @loggedIn
    def sendReplyImageWithURL(self, to, url, msgIds=None):
        path = self.downloadFileURL(url, 'path')
        return self.sendReplyImage(to, path, msgIds=msgIds)
    
    @loggedIn
    def sendMultiImage(self, to, paths):
        objectId = self.sendMessage(to=to, text=None, contentType = 1).id
        for path in paths:
            id_nya = self.sendMessage(to=to, text=None, contentMetadata={'GID': objectId}, contentType = 1).id
            upload = self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=id_nya)
            time.sleep(0.3)
            if path == path[-1]:
                return upload

    @loggedIn
    def sendMultiImageWithURL(self, to, urls):
        paths = []
        for url in urls:
            path = self.downloadFileURL(url, 'path')
            paths.append(path)
            time.sleep(0.3)
        return self.sendMultiImage(to, paths)
        
    @loggedIn
    def sendReplyMultiImage(self, to, paths):
        objectId = self.sendMessage(to=to, text=None, contentType = 1).id
        for path in paths:
            if path == paths[0]: id_nya = self.sendReplyMessage(to=to, text=None, contentMetadata={'GID': objectId}, contentType = 1).id
            else: id_nya = self.sendMessage(to=to, text=None, contentMetadata={'GID': objectId}, contentType = 1).id
            upload = self.uploadObjTalk(path=path, type='image', returnAs='bool', objId=id_nya)
            time.sleep(0.3)
            if path == path[-1]:
                return upload

    @loggedIn
    def sendReplyMultiImageWithURL(self, to, urls):
        paths = []
        for url in urls:
            path = self.downloadFileURL(url, 'path')
            paths.append(path)
            time.sleep(0.3)
        return self.sendReplyMultiImage(to, paths)

    @loggedIn
    def sendGIF(self, to, path):
        return self.uploadObjTalk(path=path, type='gif', returnAs='bool', to=to)

    @loggedIn
    def sendGIFWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendGIF(to, path)
        
    @loggedIn
    def sendVideo(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'VIDLEN': '60000','DURATION': '60000'}, contentType = 2).id
        return self.uploadObjTalk(path=path, type='video', returnAs='bool', objId=objectId)

    @loggedIn
    def sendVideoWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendVideo(to, path)
    
    @loggedIn
    def sendReplyVideo(self, to, path, msgIds=None):
        objectId = self.sendReplyMessage(to=to, text=None, contentMetadata={'VIDLEN': '60000','DURATION': '60000'}, contentType = 2, msgIds=msgIds).id
        return self.uploadObjTalk(path=path, type='video', returnAs='bool', objId=objectId)

    @loggedIn
    def sendReplyVideoWithURL(self, to, url, msgIds=None):
        path = self.downloadFileURL(url, 'path')
        return self.sendReplyVideo(to, path, msgIds=msgIds)
        
    @loggedIn
    def sendAudio(self, to, path):
        objectId = self.sendMessage(to=to, text=None, contentType = 3).id
        return self.uploadObjTalk(path=path, type='audio', returnAs='bool', objId=objectId)

    @loggedIn
    def sendAudioWithURL(self, to, url):
        path = self.downloadFileURL(url, 'path')
        return self.sendAudio(to, path)
    
    @loggedIn
    def sendReplyAudio(self, to, path, msgIds=None):
        objectId = self.sendReplyMessage(to=to, text=None, contentType = 3, msgIds=msgIds).id
        return self.uploadObjTalk(path=path, type='audio', returnAs='bool', objId=objectId)

    @loggedIn
    def sendReplyAudioWithURL(self, to, url, msgIds=None):
        path = self.downloadFileURL(url, 'path')
        return self.sendReplyAudio(to, path, msgIds=msgIds)

    @loggedIn
    def sendFile(self, to, path, file_name=''):
        if file_name == '':
            file_name = ntpath.basename(path)
        file_size = len(open(path, 'rb').read())
        objectId = self.sendMessage(to=to, text=None, contentMetadata={'FILE_NAME': str(file_name),'FILE_SIZE': str(file_size)}, contentType = 14).id
        return self.uploadObjTalk(path=path, type='file', returnAs='bool', objId=objectId, name=file_name)

    @loggedIn
    def sendFileWithURL(self, to, url, fileName=''):
        path = self.downloadFileURL(url, 'path')
        return self.sendFile(to, path, fileName)

    """Contact"""

    @loggedIn
    def deleteAccount(self):
        return self.talk.unregisterUserAndDevice()
        
    @loggedIn
    def registerUserid(self, id):
        return self.talk.registerUserid(0, id)
        
    @loggedIn
    def blockContact(self, mid):
        return self.talk.blockContact(0, mid)

    @loggedIn
    def unblockContact(self, mid):
        return self.talk.unblockContact(0, mid)

    @loggedIn
    def findAndAddContactByMetaTag(self, userid, reference):
        return self.talk.findAndAddContactByMetaTag(0, userid, reference)

    #@loggedIn
    #def findAndAddContactsByMid(self, mid):
        #return self.talk.findAndAddContactsByMid(0, mid, 0, '')

    @loggedIn
    def findAndAddContactsByEmail(self, emails=[]):
        return self.talk.findAndAddContactsByEmail(0, emails)

    @loggedIn
    def findAndAddContactsByUserid(self, userid):
        return self.talk.findAndAddContactsByUserid(0, userid)

    @loggedIn
    def findContactsByUserid(self, userid):
        return self.talk.findContactByUserid(userid)

    @loggedIn
    def findContactByTicket(self, ticketId):
        return self.talk.findContactByUserTicket(ticketId)

    @loggedIn
    def getAllContactIds(self):
        return self.talk.getAllContactIds()

    @loggedIn
    def getBlockedContactIds(self):
        return self.talk.getBlockedContactIds()

    @loggedIn
    def getContact(self, mid):
        return self.talk.getContact(mid)

    @loggedIn
    def getContacts(self, midlist):
        return self.talk.getContacts(midlist)

    @loggedIn
    def getFavoriteMids(self):
        return self.talk.getFavoriteMids()

    @loggedIn
    def getHiddenContactMids(self):
        return self.talk.getHiddenContactMids()

    @loggedIn
    def tryFriendRequest(self, midOrEMid, friendRequestParams, method=1):
        return self.talk.tryFriendRequest(midOrEMid, method, friendRequestParams)

    @loggedIn
    def makeUserAddMyselfAsContact(self, contactOwnerMid):
        return self.talk.makeUserAddMyselfAsContact(contactOwnerMid)

    @loggedIn
    def getContactWithFriendRequestStatus(self, id):
        return self.talk.getContactWithFriendRequestStatus(id)

    @loggedIn
    def reissueUserTicket(self, expirationTime=100, maxUseCount=100):
        return self.talk.reissueUserTicket(expirationTime, maxUseCount)
    
    @loggedIn
    def cloneContactProfile(self, msg, mid, sender, to):
        if not self.setts["backupProfile"]:
            return self.sendMode(msg, to, sender, "clone", 'Failed to clone profile, type `Backup` first')
        contact = self.getContact(mid)
        profile = self.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        if contact.pictureStatus:
            pict = self.downloadFileURL("http://dl.profile.line-cdn.net/" + contact.pictureStatus)
            self.updateProfilePicture(pict)
        home = self.getProfileCoverDetail(mid)
        if 'videoCoverObsInfo' in home['result']:
            self.updateProfileCoverById(home['result']['coverObsInfo']['objectId'], home['result']['videoCoverObsInfo']['objectId'])
        else:
            self.updateProfileCoverById(home['result']['coverObsInfo']['objectId'])
        self.updateProfile(profile)
        self.sendMode(msg, to, sender, "clone", 'Succeed clone profile')
    
    @loggedIn
    def backupProfile(self, msg, sender, to):
        profile = self.getContact(self.profile.mid)
        try:
            self.settings['myProfile']['displayName'] = profile.displayName
            self.settings['myProfile']['statusMessage'] = profile.statusMessage
            self.settings['myProfile']['coverId'] = self.profileDetail['result']['coverObsInfo']['objectId']
            if 'videoCoverObsInfo' in self.profileDetail['result']: self.settings['myProfile']['coverVideoId'] = self.profileDetail['result']['videoCoverObsInfo']['objectId']
            pict = "http://dl.profile.line-cdn.net/" + profile.pictureStatus
            self.downloadFileURL(pict, returnAs='path', saveAs='tmp/picture.bin')
            self.setts["backupProfile"] = True
            self.sendMode(msg, to, sender, "backup", 'Succeed backup profile')
        except Exception as e:
            self.sendMode(msg, to, sender, "backup", 'Failed backup profile, cause: {}'.format(e))
    
    @loggedIn
    def restoreProfile(self, msg, sender, to):
        if not self.setts["backupProfile"]:
            return self.sendMode(msg, to, sender, "clone", 'Failed to restore profile, type `Backup` first')
        profile = self.getProfile()
        try:
            profile.displayName = self.settings['myProfile']['displayName']
            profile.statusMessage = self.settings['myProfile']['statusMessage']
            self.updateProfilePicture('tmp/picture.bin')
            time.sleep(0.5)
            if 'coverVideoId' in self.settings['myProfile']:
                self.updateProfileCoverById(self.settings['myProfile']['coverId'], self.settings['myProfile']['coverVideoId'])
                self.settings['myProfile']['coverVideoId'] = self.profileDetail['result']['videoCoverObsInfo']['objectId']
            else:
                self.updateProfileCoverById(self.settings['myProfile']['coverId'])
            self.settings['myProfile']['coverId'] = self.profileDetail['result']['coverObsInfo']['objectId']
            self.updateProfile(profile)
            self.sendMode(msg, to, sender, "restore", 'Succes restore profile')
        except Exception as e:
            self.sendMode(msg, to, sender, "restore", 'Failed to restore profile, cause: {}'.format(e))
            
    """Group"""
    
    @loggedIn
    def getChatRoomAnnouncementsBulk(self, chatRoomMids):
        return self.talk.getChatRoomAnnouncementsBulk(chatRoomMids)

    @loggedIn
    def getChatRoomAnnouncements(self, chatRoomMid):
        return self.talk.getChatRoomAnnouncements(chatRoomMid)

    @loggedIn
    def createChatRoomAnnouncement(self, chatRoomMid, type, contents):
        return self.talk.createChatRoomAnnouncement(0, chatRoomMid, type, contents)

    @loggedIn
    def removeChatRoomAnnouncement(self, chatRoomMid, announcementSeq):
        return self.talk.removeChatRoomAnnouncement(0, chatRoomMid, announcementSeq)

    @loggedIn
    def getGroupWithoutMembers(self, groupId):
        return self.talk.getGroupWithoutMembers(groupId)
    
    @loggedIn
    def findChatByTicket(self, ticketId):
        return self.talk.findChatByTicket(FindChatByTicketRequest(ticketId))

    @loggedIn
    def findGroupByTicket(self, ticketId):
        return self.talk.findGroupByTicket(ticketId)
        
    @loggedIn
    def acceptChatInvitation(self, chatMid):
        return self.talk.acceptChatInvitation(AcceptChatInvitationRequest(0,chatMid))

    @loggedIn
    def acceptGroupInvitation(self, groupId):
        return self.talk.acceptGroupInvitation(0, groupId)
        
    @loggedIn
    def acceptChatInvitationByTicket(self, chatMid, ticketId):
        return self.talk.acceptChatInvitationByTicket(AcceptChatInvitationByTicketRequest(0,chatMid,ticketId))

    @loggedIn
    def acceptGroupInvitationByTicket(self, groupId, ticketId):
        return self.talk.acceptGroupInvitationByTicket(0, groupId, ticketId)

    @loggedIn
    def cancelChatInvitation(self, chatMid, targetUserMids=[]):
        return self.talk.cancelChatInvitation(CancelChatInvitationRequest(0,chatMid,targetUserMids))
        
    @loggedIn
    def cancelGroupInvitation(self, groupId, contactIds):
        return self.talk.cancelGroupInvitation(0, groupId, contactIds)
    
    @loggedIn
    def createChat(self, name, targetUserMids=[]):
        return self.talk.createChat(CreateChatRequest(0,0,name,targetUserMids,""))
        
    @loggedIn
    def createGroup(self, name, midlist):
        return self.talk.createGroup(0, name, midlist)
    
    @loggedIn
    def getChats(self, chatMids=[], withMembers=True, withInvitees=True):
        return self.talk.getChats(GetChatsRequest(chatMids,withMembers,withInvitees))
        
    @loggedIn
    def getGroup(self, groupId):
        return self.talk.getGroup(groupId)

    @loggedIn
    def getGroups(self, groupIds):
        return self.talk.getGroups(groupIds)

    @loggedIn
    def getGroupsV2(self, groupIds):
        return self.talk.getGroupsV2(groupIds)

    @loggedIn
    def getCompactGroup(self, groupId):
        return self.talk.getCompactGroup(groupId)

    @loggedIn
    def getCompactRoom(self, roomId):
        return self.talk.getCompactRoom(roomId)

    @loggedIn
    def getGroupIdsByName(self, groupName):
        gname = []
        gids = self.getAllChatMids(True, False)
        for gid in gids.memberChatMids:
            group = self.getChats([gid], False, False).chats[0]
            if groupName in group.chatName:
                gname.append(group.chatMid)
        return gname

    @loggedIn
    def getAllChatMids(self, groupJoined=True, invitation=True):
        return self.talk.getAllChatMids(GetAllChatMidsRequest(groupJoined, invitation), 0)
        
    @loggedIn
    def getGroupIdsInvited(self):
        return self.talk.getGroupIdsInvited()

    @loggedIn
    def getGroupIdsJoined(self):
        return self.talk.getGroupIdsJoined()

    @loggedIn
    def updateGroupPreferenceAttribute(self, groupMid, updatedAttrs):
        return self.talk.updateGroupPreferenceAttribute(0, groupMid, updatedAttrs)

    @loggedIn
    def inviteIntoChat(self, chatMid, targetUserMids=[]):
        return self.talk.inviteIntoChat(InviteIntoChatRequest(0,chatMid,targetUserMids))

    @loggedIn
    def inviteIntoGroup(self, groupId, midlist):
        return self.talk.inviteIntoGroup(0, groupId, midlist)
        
    @loggedIn
    def deleteOtherFromChat(self, chatMid, targetUserMids=[]):
        return self.talk.deleteOtherFromChat(DeleteOtherFromChatRequest(0,chatMid,targetUserMids))

    @loggedIn
    def kickoutFromGroup(self, groupId, midlist):
        return self.talk.kickoutFromGroup(0, groupId, midlist)

    @loggedIn
    def deleteSelfFromChat(self, chatMid):
        return self.talk.deleteSelfFromChat(DeleteSelfFromChatRequest(0,chatMid))
        
    @loggedIn
    def leaveGroup(self, groupId):
        return self.talk.leaveGroup(0, groupId)

    @loggedIn
    def rejectChatInvitation(self, chatMid):
        return self.talk.rejectChatInvitation(RejectChatInvitationRequest(0,chatMid))
        
    @loggedIn
    def rejectGroupInvitation(self, groupId):
        return self.talk.rejectGroupInvitation(0, groupId)

    @loggedIn
    def reissueChatTicket(self, chatMid):
        return self.talk.reissueChatTicket(ReissueChatTicketRequest(0,chatMid))
        
    @loggedIn
    def reissueGroupTicket(self, groupId):
        return self.talk.reissueGroupTicket(groupId)

    @loggedIn
    def updateChat(self, chat, updatedAttribute):
        return self.talk.updateChat(UpdateChatRequest(0,chat,updatedAttribute))
        
    @loggedIn
    def updateGroup(self, groupObject):
        return self.talk.updateGroup(0, groupObject)

    """Room"""

    @loggedIn
    def createRoom(self, midlist):
        return self.talk.createRoom(0, midlist)

    @loggedIn
    def getRoom(self, roomId):
        return self.talk.getRoom(roomId)

    @loggedIn
    def inviteIntoRoom(self, roomId, midlist):
        return self.talk.inviteIntoRoom(0, roomId, midlist)

    @loggedIn
    def leaveRoom(self, roomId):
        return self.talk.leaveRoom(0, roomId)

    """Call"""
        
    @loggedIn
    def acquireCallTalkRoute(self, to):
        return self.talk.acquireCallRoute(to)
    
    """Report"""

    @loggedIn
    def reportSpam(self, chatMid, memberMids=[], spammerReasons=[], senderMids=[], spamMessageIds=[], spamMessages=[]):
        return self.talk.reportSpam(chatMid, memberMids, spammerReasons, senderMids, spamMessageIds, spamMessages)
        
    @loggedIn
    def reportSpammer(self, spammerMid, spammerReasons=[], spamMessageIds=[]):
        return self.talk.reportSpammer(spammerMid, spammerReasons, spamMessageIds)
