# -*- coding: utf-8 -*-
from datetime import datetime
from .channel import Channel

import json, time, base64, requests

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.default('You want to call the function, you must login to LINE')
    return checkLogin
    
class Timeline(Channel):

    def __init__(self):
        if not self.channelId:
            self.channelId = self.server.CHANNEL_ID['LINE_TIMELINE']
        Channel.__init__(self, self.channel, self.channelId, False)
        self.tl = self.getChannelResult()
        self.dataPost = {}
        self.__loginTimeline()
        
    def __loginTimeline(self):
        self.server.setTimelineHeadersWithDict({
            'Content-Type': 'application/json',
            'User-Agent': self.server.USER_AGENT,
            'X-Line-Mid': self.profile.mid,
            'X-Line-Carrier': self.server.CARRIER,
            'X-Line-Application': self.server.APP_NAME,
            'X-Line-ChannelToken': self.tl.channelAccessToken
        })
        self.profileDetail = self.getProfileDetail()
    
    """Timeline"""

    @loggedIn
    def getFeed(self, postLimit=10, commentLimit=1, likeLimit=1, order='TIME'):
        params = {'postLimit': postLimit, 'commentLimit': commentLimit, 'likeLimit': likeLimit, 'order': order}
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/feed/list.json', params)
        r = self.server.getContent(url, headers=self.server.timelineHeaders)
        return r.json()

    @loggedIn
    def getHomeProfile(self, mid=None, postLimit=10, commentLimit=1, likeLimit=1, updateParams={}):
        if mid is None:
            mid = self.profile.mid
        params = {'homeId': mid, 'postLimit': postLimit, 'commentLimit': commentLimit, 'likeLimit': likeLimit, 'sourceType': 'LINE_PROFILE_COVER'}
        if updateParams == {}: self.dataPost = {}
        else: params.update({'postId': updateParams['result']['feeds'][-1]['post']['postInfo']['postId'], 'updatedTime': int(updateParams['result']['feeds'][-1]['post']['postInfo']['updatedTime'])})
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/post/list.json', params)
        r = self.server.getContent(url, headers=self.server.timelineHeaders)
        data = r.json()
        if 'feeds' not in data['result']:
            if self.dataPost != {}:
                return self.dataPost
            else:
                return data
        if len(data['result']['feeds']) == 10:
            if self.dataPost == {}:
                self.dataPost = data
            else:
                for feed in data['result']['feeds']:
                    self.dataPost['result']['feeds'].append(feed)
            return self.getHomeProfile(mid, updateParams=self.dataPost)
        else:
            if self.dataPost != {}:
                for feed in data['result']['feeds']:
                    self.dataPost['result']['feeds'].append(feed)
                return self.dataPost
            else:
                return data
    
    @loggedIn
    def getProfileDetail(self, mid=None, styleMediaVersion='v2', storyVersion='v6'):
        if mid is None:
            mid = self.profile.mid
        params = {
            'homeId': mid,
            'styleMediaVersion': styleMediaVersion,
            'storyVersion': storyVersion
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'x-lpv': '1',
            'x-lal': 'en_US',
            'x-lsr': 'ID',
            'x-line-bdbtemplateversion': 'v1',
            'x-line-global-config': "discover.enable=true; follow.enable=true", #why get follow count with this?
        })
        url = self.server.urlEncode(self.server.LINE_TIMELINE_HM, '/api/v1/home/profile.json', params)
        r = self.server.postContent(url, headers=hr)
        return r.json()

    @loggedIn
    def getProfileCoverDetail(self, mid=None):
        if mid is None:
            mid = self.profile.mid
        params = {
            'homeId': mid
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
        })
        url = self.server.urlEncode(self.server.LINE_TIMELINE_HM, '/api/v1/home/cover.json', params)
        r = self.server.postContent(url, headers=hr)
        return r.json()

    @loggedIn
    def updateProfileCoverById(self, objId, vobjId=None, mid=None):
        if mid is None:
            mid = self.profile.mid
        data = {
            "homeId": mid,
            "coverObjectId": objId,
            "storyShare": False,
            "meta":{} # heh
        }
        if vobjId:
            data['videoCoverObjectId'] = vobjId
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "POST",
        })
        r = self.server.postContent(self.server.LINE_TIMELINE_HM + '/api/v1/home/cover.json', headers=hr, data=json.dumps(data))
        return r.json()

    @loggedIn
    def getProfileCoverId(self, mid=None):
        if mid is None:
            mid = self.profile.mid
        home = self.getProfileCoverDetail(mid)
        return home['result']['coverObsInfo']['objectId']

    @loggedIn
    def getProfileCoverURL(self, mid=None):
        if mid is None:
            mid = self.profile.mid
        home = self.getProfileCoverDetail(mid)
        if 'videoCoverObsInfo' in home['result']:
            params = {'userid': mid, 'oid': home['result']['videoCoverObsInfo']['objectId']}
            url = self.server.urlEncode(self.server.LINE_OBS_DOMAIN, '/myhome/vc/download.nhn', params)
        else:
            params = {'userid': mid, 'oid': home['result']['coverObsInfo']['objectId']}
            url = self.server.urlEncode(self.server.LINE_OBS_DOMAIN, '/myhome/c/download.nhn', params)
        return url

    """Post"""

    @loggedIn
    def getPost(self, mid, postId):
        params = {
            'homeId': mid,
            'postId': postId,
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'x-lpv': '1',
            'x-lsr':'TW'
        })
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/post/get.json', params)
        r = self.server.postContent(url, headers=hr)
        return r.json()

    @loggedIn
    def sendPostToTalk(self, mid, postId):
        if mid is None:
            mid = self.profile.mid
        params = {'receiveMid': mid, 'postId': postId}
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v56/post/sendPostToTalk.json', params)
        r = self.server.getContent(url, headers=self.server.timelineHeaders)
        return r.json()
    
    @loggedIn
    def getPostShareLink(self, postId):
        params = {'postId': postId}
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/post/getShareLink.json', params)
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            "x-lal": "en_US"
        })
        r = self.server.getContent(url, headers=hr)
        return r.json()
    
    @loggedIn
    def getTimelineUrl(self, postId):
        params = {'homeId': postId}
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/web/getUrl.json', params)
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            "x-lal": "en_US"
        })
        r = self.server.getContent(url, headers=hr)
        return r.json()

    @loggedIn
    def createComment(self, mid, contentId, text, contentsList=[], dataa={}):
        if mid is None:
            mid = self.profile.mid
        params = {
            'homeId': mid
        }
        data = {
           "contentId" : contentId,
           "commentText" : text,
           #"secret" : False,
           "contentsList" : contentsList,
           "channelId" : self.server.CHANNEL_ID['LINE_TIMELINE']
        }
        if dataa:
            data.update(dataa)
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "POST",
            'Content-type': "application/json",
            'x-lpv': '1',
            'x-lsr':'TW'
        })
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/comment/create.json', params)
        r = self.server.postContent(url, headers=hr, json=data)
        return r.json()

    @loggedIn
    def createCommentMention(self, mid, contentId, text, mids=[], contentsList=[], dataa={}):
        if mid is None:
            mid = self.profile.mid
        params = {
            'homeId': mid
        }
        data = {
           "contentId" : contentId,
           "commentText" : text,
           #"secret" : False,
           "contentsList" : [],
           "channelId" : self.server.CHANNEL_ID['LINE_TIMELINE']
        }
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            if "recallInfos" not in data:
                data["recallInfos"] = []
            texts = text.split("@!")
            textx = ""
            unicode = ""
            for point in range(len(mids)):
                unicode += str(texts[point].encode('unicode-escape'))
                textx += str(texts[point])
                start = len(textx) if unicode == textx else len(textx) + unicode.count('U0')
                end =  12 + int(start) - 17
                arrData = {'start':start, 'end':end+6, 'user':{'actorId': mids[point]}}
                data["recallInfos"].append(arrData)
                textx += "@"
            textx += str(texts[len(mids)])
            data["commentText"] = textx
        if contentsList:
            for content in contentsList:
                data["contentsList"].append(content)
        if dataa:
            data.update(dataa)
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "POST",
            'Content-type': "application/json",
            'x-lpv': '1',
            'x-lsr':'TW'
        })
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/comment/create.json', params)
        r = self.server.postContent(url, headers=hr, json=data)
        return r.json()

    @loggedIn
    def deleteComment(self, mid, contentId, commentId):
        if mid is None:
            mid = self.profile.mid
        params = {
            'homeId': mid,
            'contentId' : contentId,
            'commentId': commentId
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'x-lpv': '1',
            'x-lsr':'TW'
        })
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/comment/delete.json', params)
        r = self.server.postContent(url, headers=hr)
        return r.json()
    
    @loggedIn
    def listComment(self, mid, contentId, limit=10):
        params = {
            'homeId': mid,
        #    'actorId': self.profile.mid,
            'contentId': contentId,
            'limit': limit
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'x-lpv': '1',
            'x-lsr':'TW'
        })
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/comment/getList.json', params)
        r = self.server.postContent(url, headers=hr)
        return r.json()

    @loggedIn
    def likePost(self, mid, contentId, likeType=1001):
        if mid is None:
            mid = self.profile.mid
        if likeType not in [1001,1002,1003,1004,1005,1006]:
            raise Exception('Invalid parameter likeType')
        params = {
            'homeId': mid
        }
        data = {
           "contentId" : contentId,
           "likeType" : str(likeType),
           "sharable" : False,
           "channelId" : self.server.CHANNEL_ID['LINE_TIMELINE']
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "POST",
            'Content-type': "application/json",
            'x-lpv': '1',
            'x-lsr':'TW'
        })
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/like/create.json', params)
        r = self.server.postContent(url, headers=hr, json=data)
        return r.json()

    @loggedIn
    def unlikePost(self, contentId):
        params = {
            'contentId': contentId,
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'x-lpv': '1',
            'x-lsr':'TW'
        })
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/like/cancel.json', params)
        r = self.server.postContent(url, headers=hr)
        return r.json()
    
    def listLike(self, mid, contentId):
        params = {
            'homeId': mid,
            'contentId': contentId
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'x-lpv': '1',
            'x-lsr':'TW'
        })
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/like/getList.json', params)
        r = self.server.postContent(url, headers=hr)
        return r.json()

    """Group Post"""
    
    @loggedIn
    def searchNote(self, mid, text):
        data = {
           "query" : text,
           "queryType" : "TEXT",
           "homeId" : mid,
           "postLimit" : 20,
           "channelId" : self.server.CHANNEL_ID['LINE_TIMELINE']
        }
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/search/note.json', {})
        r = self.server.postContent(url, headers=self.server.timelineHeaders, data=json.dumps(data))
        res = r.json()
        return res["result"]["feeds"]
    
    @loggedIn
    def createPost(self, text, holdingTime=None):
        params = {'homeId': self.profile.mid, 'sourceType': 'TIMELINE'}
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/post/create.json', params)
        payload = {'postInfo': {'readPermission': {'type': 'ALL'}}, 'sourceType': 'TIMELINE', 'contents': {'text': text}}
        if holdingTime != None:
            payload["postInfo"]["holdingTime"] = holdingTime
        data = json.dumps(payload)
        r = self.server.postContent(url, data=data, headers=self.server.timelineHeaders)
        return r.json()
    
    @loggedIn
    def createPostMedia(self, text, media=[]):
        params = {'homeId': self.profile.mid, 'sourceType': 'TIMELINE'}
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/post/create.json', params)
        payload = {'postInfo': {'readPermission': {'type': 'ALL'}}, 'sourceType': 'TIMELINE', 'contents': {'text': text, 'media': media}}
        data = json.dumps(payload)
        r = self.server.postContent(url, data=data, headers=self.server.timelineHeaders)
        return r.json()

    @loggedIn
    def createPostGroup(self, to,text, holdingTime=None, textMeta=[]):
        params = {'homeId': to, 'sourceType': 'GROUPHOME'}
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/post/create.json', params)
        payload = {'postInfo': {'readPermission': {'type': 'ALL'}}, 'sourceType': 'GROUPHOME', 'contents': {'text': text,'textMeta':textMeta}}
        if holdingTime != None:
            payload["postInfo"]["holdingTime"] = holdingTime
        data = json.dumps(payload)
        r = self.server.postContent(url, data=data, headers=self.server.timelineHeaders)
        return r.json()

    @loggedIn
    def createPostGroupMedia(self, to, text, media=[]):
        params = {'homeId': to, 'sourceType': 'GROUPHOME'}
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/post/create.json', params)
        payload = {'postInfo': {'readPermission': {'type': 'ALL'}}, 'sourceType': 'GROUPHOME', 'contents': {'text': text, 'media': media}}
        data = json.dumps(payload)
        r = self.server.postContent(url, data=data, headers=self.server.timelineHeaders)
        return r.json()
    
    @loggedIn
    def getGroupPost(self, mid, commentLimit=1, likeLimit=1, updateParams={}):
        params = {'homeId': mid, 'commentLimit': commentLimit, 'likeLimit': likeLimit, 'sourceType': 'TALKROOM'}
        if updateParams == {}: self.dataPost = {}
        else: params.update({'postId': updateParams['result']['feeds'][-1]['post']['postInfo']['postId'], 'updatedTime': int(updateParams['result']['feeds'][-1]['post']['postInfo']['updatedTime'])})
        url = self.server.urlEncode(self.server.LINE_TIMELINE_API, '/v55/post/list.json', params)
        r = self.server.getContent(url, headers=self.server.timelineHeaders)
        data = r.json()
        if 'feeds' not in data['result']:
            if self.dataPost != {}:
                return self.dataPost
            else:
                return data
        if len(data['result']['feeds']) == 10:
            if self.dataPost == {}:
                self.dataPost = data
            else:
                for feed in data['result']['feeds']:
                    self.dataPost['result']['feeds'].append(feed)
            return self.getGroupPost(mid, updateParams=self.dataPost)
        else:
            if self.dataPost != {}:
                for feed in data['result']['feeds']:
                    self.dataPost['result']['feeds'].append(feed)
                return self.dataPost
            else:
                return data

    """Group Album"""

    @loggedIn
    def getGroupAlbum(self, mid):
        params = {
            'homeId': mid,
            'sourceType': 'TALKROOM',
            'type': 'g',
            'log': None,
            'markReading': True
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "GET",
            'Content-type': "application/json",
            'x-lpv': '1', #needless
            'x-lsr':'TW', #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode(self.server.LINE_HOST_DOMAIN, '/ext/album/api/v4/albums', params)
        r = self.server.postContent(url, headers=hr)
        return r.json()

    @loggedIn
    def createGroupAlbum(self, mid, name):
        data = json.dumps({'title': name})
        params = {
            'homeId': mid,
            'sourceType': 'TALKROOM',
            'count': '1',
            'auto': False
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "POST",
            'Content-type': "application/json",
            'x-lpv': '1', #needless
            'x-lsr':'TW', #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode(self.server.LINE_HOST_DOMAIN, '/ext/album/api/v4/album', params)
        r = self.server.postContent(url, headers=hr)
        if r.status_code != 201:
            raise Exception('Create a new album failure.')
        return r.json()

    @loggedIn
    def changeGroupAlbumName(self, mid, albumId, name):
        data = json.dumps({'title': name})
        params = {'homeId': mid}
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "PUT",
            'Content-type': "application/json",
            'x-lpv': '1', #needless
            'x-lsr':'TW', #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode(self.server.LINE_HOST_DOMAIN + '/ext/album', '/api/v3/album/%s' % albumId, params)
        r = self.server.postContent(url, data=data, headers=hr)
        #r.json()['code'] == 0: success
        return r.json()
    
    @loggedIn
    def deleteGroupAlbum(self, mid, albumId):
        params = {'homeId': mid}
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'x-lhm': "DELETE",
            'Content-type': "application/json",
            'x-lpv': '1', #needless
            'x-lsr':'TW', #needless
            'x-u': '' #needless
        })
        url = self.server.urlEncode(self.server.LINE_HOST_DOMAIN + '/ext/album', '/api/v4/album/%s' % albumId, params)
        r = self.server.postContent(url, headers=hr)
        return r.json()

    @loggedIn
    def addImageToAlbum(self, mid, albumId, path):
        file = open(path, 'rb').read()
        params = {
            'oid': int(time.time()),
            'quality': '90',
            'range': len(file),
            'type': 'image'
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'Content-Type': 'image/jpeg',
            'X-Line-Mid': mid,
            'X-Line-Album': albumId,
            'x-obs-params': self.genOBSParams(params,'b64')
        })
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/album/a/upload.nhn', data=file, headers=hr)
        if r.status_code != 201:
            raise Exception('Add image to album failure.')
        return r.json()

    @loggedIn
    def getImageGroupAlbum(self, mid, albumId, objId, returnAs='path', saveAs=''):
        if saveAs == '':
            saveAs = self.genTempFile('path')
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'Content-Type': 'image/jpeg',
            'X-Line-Mid': mid,
            'X-Line-Album': albumId
        })
        params = {'ver': '1.0', 'oid': objId}
        url = self.server.urlEncode(self.server.LINE_OBS_DOMAIN, '/album/a/download.nhn', params)
        r = self.server.getContent(url, headers=hr)
        if r.status_code == 200:
            self.saveFile(saveAs, r.raw)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download image album failure.')

    """Story"""
    
    @loggedIn
    def getStory(self, mid=None):
        if mid == None:
            mid = self.profile.mid
        params = {"userMid": mid}
        url = self.server.urlEncode(self.server.LINE_HOST_DOMAIN, '/st/api/v6/story')
        result = self.server.postContent(url, data=json.dumps(params), headers=self.server.timelineHeaders).json()
        return result
    
    @loggedIn
    def getRecentStory(self):
        params = {"lastRequestTime": int(time.time()), "lastTimelineVisitTime": int(time.time())}
        result = self.server.postContent(self.server.LINE_HOST_DOMAIN + '/st/api/v6/story/recentstory/list', headers=self.server.timelineHeaders, data=json.dumps(params))
        return result.json()

    @loggedIn
    def getMidRecentStory(self):
        data = self.getRecentStory()
        result = []
        if data["message"] == "success":
            for mids in data["result"]["recentStories"]:
                media = self.getStoryMedia(mids["mid"])
                if media:
                    if mids["mid"] not in result:
                        result.append(mids["mid"])
        return result

    @loggedIn
    def getStoryMedia(self, mid=None):
        if mid == None:
            mid = self.profile.mid
        data = self.getStory(mid)
        result = []
        if data['message'] == 'success':
            if data['result']['contents']:
                for media in data['result']['contents']:
                    if media['media'][0]['mediaType'] == 'IMAGE':
                        params = {'userid': mid, 'oid': media['media'][0]['oid']}
                        url = self.server.urlEncode(self.server.LINE_OBS_DOMAIN, '/story/st/download.nhn', params)
                        result.append({
                            "type": "image",
                            "url": url
                        })
                    if media['media'][0]['mediaType'] == 'VIDEO':
                        params = {'userid': mid, 'oid': media['media'][0]['oid']}
                        url = self.server.urlEncode(self.server.LINE_OBS_DOMAIN, '/story/st/download.nhn', params)
                        result.append({
                            "type": "video",
                            "url": url
                        })
        return result

    @loggedIn
    def readStory(self, mid=None, contentId=None):
        if not isinstance(mid and contentId, str):
            raise Exception('mid and contentId is required')
        params = {"userMid": mid, "contentId": contentId, "createdTime": int(time.time()), "tsId":"", "friendType":""}
        result = self.server.postContent(self.server.LINE_HOST_DOMAIN + '/st/api/v6/story/content/read', data=json.dumps(params), headers=self.server.timelineHeaders)
        return result.json()

    @loggedIn
    def likeStory(self, contentId=None, likeType=None):
        if likeType not in [1001, 1002, 1003, 1004, 1005, 1006]:
            raise Exception ('Invalid likeType value')
        if contentId is None:
            raise Exception ('contentId is required')
        params = {"tsId": "", "contentId": contentId, "like": True, "likeType": str(likeType)}
        result = self.server.postContent(self.server.LINE_HOST_DOMAIN + '/st/api/v6/story/content/like', data=json.dumps(params), headers=self.server.timelineHeaders)
        return result.json()

    @loggedIn
    def commentStory(self, mid=None, contentId=None, text=None):
        if not isinstance(mid and contentId, str):
            raise Exception('mid and contentId is required')
        if text is None:
            text = 'Auto Comment by sozi'
        params = {"to":{"userMid": mid, "friendType": "","tsId": ""}, "contentId": contentId, "message": text}
        result = self.server.postContent(self.server.LINE_HOST_DOMAIN + '/st/api/v6/story/message/send', data=json.dumps(params), headers=self.server.timelineHeaders)
        return result.json()
        
    @loggedIn
    def updateStory(self, objId=None, obsHash=None, mediaType='image'):
        if not isinstance(objId and obsHash, str):
            raise Exception('Invalid objdId and obsHash')
        if mediaType not in ['image', 'video']:
            raise Exception('Invalid media type')
        params = {"content": {"sourceType": "USER", "contentType": "USER", "media":[{"oid": objId, "service": "story", "sid": "st", "hash": obsHash, "mediaType": mediaType.upper()}]},"shareInfo":{"shareType": "FRIEND"}}
        self.server.timelineHeaders.update({'X-Line-BDBTemplateVersion': 'v1'})
        result = self.server.postContent(self.server.LINE_HOST_DOMAIN + '/st/api/v6/story/content/create', headers = self.server.timelineHeaders, data=json.dumps(params))
        return result.json()
