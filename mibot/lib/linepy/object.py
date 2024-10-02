# -*- coding: utf-8 -*-
from datetime import datetime
import json, time, ntpath, random, os, hashlib

def genObjectId():
    random.seed = (os.urandom(1024))
    return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(32))

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.default('You want to call the function, you must login to LINE')
    return checkLogin
    
class Object(object):

    def __init__(self):
        if self.isLogin == True:
            self.log("[%s] : Login success" % self.profile.displayName)

    """Group"""

    @loggedIn
    def updateGroupPicture(self, groupId, path):
        files = {'file': open(path, 'rb')}
        data = {'params': self.genOBSParams({'oid': groupId,'type': 'image'})}
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/g/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Update group picture failure.')
        return True
    
    @loggedIn
    def updateGroupCover(self, to, path, returnAs='bool'):
        if returnAs not in ['objId','bool']:
            raise Exception('Invalid returnAs value')
        objId = genObjectId()
        self.uploadObjCover(path, type='image', returnAs='bool', objId=objId, mid=to)
        self.updateProfileCoverById(objId, mid=to)
        if returnAs == 'objId':
            return objId
        elif returnAs == 'bool':
            return True

    """Personalize"""

    @loggedIn
    def updateProfilePicture(self, path, type='p'):
        hstr = 'ACode44_%s' % int(time.time() * 1000)
        file_name = hashlib.md5(hstr.encode()).hexdigest()
        files = {'file': open(path, 'rb')}
        params = {
            'name': file_name,
            'quality': '100',
            'type': 'image',
            'ver': '2.0'
        }
        if type == 'vp':
            params.update({'cat': 'vp.mp4'})
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/r/talk/p/' + self.profile.mid, headers=self.server.Headers, data={'params': json.dumps(params)}, files=files)
        if r.status_code != 201:
            raise Exception(f"update Profile Image failure. Receive statue code: {r.status_code}")
        return True
        
    @loggedIn
    def updateProfileVideoPicture(self, path):
        try:
            from ffmpy import FFmpeg
            files = {'file': open(path, 'rb')}
            hstr = 'ACode44_%s' % int(time.time() * 1000)
            file_name = hashlib.md5(hstr.encode()).hexdigest()
            params = {
                'name': file_name,
                'quality': '100',
                'type': 'video',
                'ver': '2.0',
                'cat': 'vp.mp4'
            }
            r_vp = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/r/talk/vp/' + self.profile.mid, headers=self.server.Headers, data={'params': json.dumps(params)}, files=files)
            if r_vp.status_code != 201:
                raise Exception(f"update Profile Video failure. Receive statue code: {r.status_code}")
            path_p = self.genTempFile('path')
            ff = FFmpeg(inputs={'%s' % path: None}, outputs={'%s' % path_p: ['-ss', '00:00:2', '-vframes', '1']})
            ff.run()
            self.updateProfilePicture(path_p, 'vp')
        except:
            raise Exception('You should install FFmpeg and ffmpy from pypi')

    @loggedIn
    def updateVideoAndPictureProfile(self, path_p, path, returnAs='bool'):
        if returnAs not in ['bool']:
            raise Exception('Invalid returnAs value')
        files = {'file': open(path, 'rb')}
        hstr = 'ACode44_%s' % int(time.time() * 1000)
        file_name = hashlib.md5(hstr.encode()).hexdigest()
        params = {
            'name': file_name,
            'quality': '100',
            'type': 'video',
            'ver': '2.0',
            'cat': 'vp.mp4'
        }
        r_vp = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/r/talk/vp/' + self.profile.mid, headers=self.server.Headers, data={'params': json.dumps(params)}, files=files)
        if r_vp.status_code != 201:
            raise Exception(f"update Profile Video failure. Receive statue code: {r.status_code}")
        self.updateProfilePicture(path_p, 'vp')
        if returnAs == 'bool':
            return True
            
    @loggedIn
    def updateProfileCover(self, path, returnAs='bool'):
        if returnAs not in ['objId','bool']:
            raise Exception('Invalid returnAs value')
        objId = genObjectId()
        self.uploadObjCover(path, type='image', returnAs='bool', objId=objId)
        self.updateProfileCoverById(objId)
        if returnAs == 'objId':
            return objId
        elif returnAs == 'bool':
            return True

    @loggedIn
    def updateProfileCoverVideo(self, path, path_v, returnAs='bool'):
        if returnAs not in ['objId','bool']:
            raise Exception('Invalid returnAs value')
        objId = genObjectId()
        self.uploadObjCover(path, type='image', returnAs='bool', objId=objId)
        self.uploadObjCover(path_v, type='video', returnAs='bool', objId=objId)
        self.updateProfileCoverById(objId, objId)
        if returnAs == 'objId':
            return objId
        elif returnAs == 'bool':
            return True
    
    """Object"""

    @loggedIn
    def uploadObjCover(self, path, type='image', returnAs='bool', objId=None, mid=None):
        if returnAs not in ['objId','bool']:
            raise Exception('Invalid returnAs value')
        if type not in ['image','video']:
            raise Exception('Invalid type value')
        if type == 'image':
            contentType = 'image/png'
            url = '/r/myhome/c/'
        elif type == 'video':
            contentType = 'video/mp4'
            url = '/r/myhome/vc/'
        if not objId:
            objId = genObjectId()
        if not mid:
            mid = self.profile.mid
        file = open(path, 'rb').read()
        params = {
           "name": path,
           "oid": objId,
           "type": '%s' % str(type),
           "userid": mid,
           "ver": "2.0"
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            "X-Line-PostShare":  "false",
            "X-Line-StoryShare":"false",
            "x-line-signup-region": "ID",
            "Content-Length": str(len(file)),
            "content-type": contentType,
            "x-obs-params": self.genOBSParams(params,'b64')
        })
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + url + objId, headers=hr, data=file)
        if r.status_code != 201:
            raise Exception('Upload cover failure.')
        if returnAs == 'objId':
            return objId
        elif returnAs == 'bool':
            return True
    
    @loggedIn
    def uploadObjStory(self, path, type='image', objId=None):
        if type not in ['image','video']:
            raise Exception('Invalid type value')
        if type == 'image':
            contentType = 'image/jpeg'
        elif type == 'video':
            contentType = 'video/mp4'
        if not objId:
            objId  = genObjectId()
        files = open(path, 'rb').read()
        params = {
            'name': '%s' % str(time.time()*1000),
            'userid': '%s' % self.profile.mid,
            'oid': '%s' % str(objId),
            'type': type,
            'ver': '2.0'
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'Content-Type': contentType,
            'Content-Length': str(len(files)),
            'x-obs-params': self.genOBSParams(params,'b64')
        })
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/story/st/upload.nhn', headers=hr, data=files)
        if r.status_code != 201:
            raise Exception('Upload object story failure.')
        result = {'obsOid': r.headers['x-obs-oid'], 'xObsHash': r.headers['x-obs-hash']}
        return result

    @loggedIn
    def uploadObjSquare(self, squareChatMid, path, type='image', returnAs='bool', name=None):
        if returnAs not in ['bool']:
            raise Exception('Invalid returnAs value')
        if type not in ['image','gif','video','audio','file']:
            raise Exception('Invalid type value')
        try:
            import magic
        except ImportError:
            raise Exception('You must install python-magic from pip')
        mime = magic.Magic(mime=True)
        contentType = mime.from_file(path)
        data = open(path, 'rb').read()
        params = {
            'name': '%s' % str(time.time()*1000),
            'oid': 'reqseq',
            'reqseq': '%s' % str(self.revision),
            'tomid': '%s' % str(squareChatMid),
            'type': '%s' % str(type),
            'ver': '1.0'
        }
        if type == 'video':
            params.update({'duration': '60000'})
        elif type == 'audio':
            params.update({'duration': '60000'})
        elif type == 'gif':
            params.update({'type': 'image', 'cat': 'original'})
        elif type == 'file':
            params.update({'name': name})
        headers = self.server.additionalHeaders(self.server.Headers, {
            'Content-Type': contentType,
            'Content-Length': str(len(data)),
            'x-obs-params': self.genOBSParams(params,'b64'),
            'X-Line-Access': self.squareObsToken
        })
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/r/g2/m/reqseq', data=data, headers=headers)
        if r.status_code != 201:
            raise Exception('Upload %s failure.' % type)
        if returnAs == 'bool':
            return True

    @loggedIn
    def uploadObjTalk(self, path, type='image', returnAs='bool', objId=None, to=None, name=None):
        if returnAs not in ['objId','bool']:
            raise Exception('Invalid returnAs value')
        if type not in ['image','gif','video','audio','file']:
            raise Exception('Invalid type value')
        headers=None
        files = {'file': open(path, 'rb')}
        if type == 'image' or type == 'video' or type == 'audio' or type == 'file':
            e_p = self.server.LINE_OBS_DOMAIN + '/talk/m/upload.nhn'
            data = {'params': self.genOBSParams({'oid': objId,'size': len(open(path, 'rb').read()),'type': type, 'name': name})}
        elif type == 'gif':
            e_p = self.server.LINE_OBS_DOMAIN + '/r/talk/m/reqseq'
            files = None
            data = open(path, 'rb').read()
            params = {
                'name': '%s' % str(time.time()*1000),
                'oid': 'reqseq',
                'reqseq': '%s' % str(self.revision),
                'tomid': '%s' % str(to),
                'cat': 'original',
                'type': 'image',
                'ver': '1.0'
            }
            headers = self.server.additionalHeaders(self.server.Headers, {
                'Content-Type': 'image/gif',
                'Content-Length': str(len(data)),
                'x-obs-params': self.genOBSParams(params,'b64')
            })
        r = self.server.postContent(e_p, data=data, headers=headers, files=files)
        if r.status_code != 201:
            raise Exception('Upload %s failure.' % type)
        if returnAs == 'objId':
            return objId
        elif returnAs == 'bool':
            return True

    @loggedIn
    def uploadObjHome(self, path, type='image', returnAs='bool', objId=None, target=None):
        if returnAs not in ['objId','bool']:
            raise Exception('Invalid returnAs value')
        if type not in ['image','video']:
            raise Exception('Invalid type value')
        if type == 'image':
            contentType = 'image/jpeg'
        elif type == 'video':
            contentType = 'video/mp4'
        if not objId:
            objId  = genObjectId()
        if not target:
            target = self.profile.mid
        files = open(path, 'rb').read()
        params = {
            'name': '%s' % str(time.time()*1000),
            'userid': '%s' % target,
            'oid': '%s' % str(objId),
            'type': type,
            'ver': '2.0'
        }
        hr = self.server.additionalHeaders(self.server.timelineHeaders, {
            'Content-Type': contentType,
            'Content-Length': str(len(files)),
            'x-obs-params': self.genOBSParams(params,'b64')
        })
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/r/myhome/h/' + objId, headers=hr, data=files)
        if r.status_code != 201:
            raise Exception('Upload object home failure.')
        if returnAs == 'objId':
            return objId
        elif returnAs == 'bool':
            return True

    @loggedIn
    def downloadObjectMsg(self, messageId, returnAs='path', saveAs=''):
        if saveAs == '':
            saveAs = self.genTempFile('path')
        if returnAs not in ['path','bool','bin']:
            raise Exception('Invalid returnAs value')
        params = {'oid': messageId}
        url = self.server.urlEncode(self.server.LINE_OBS_DOMAIN, '/talk/m/download.nhn', params)
        r = self.server.getContent(url)
        if r.status_code == 200:
            self.saveFile(saveAs, r.raw)
            if returnAs == 'path':
                return saveAs
            elif returnAs == 'bool':
                return True
            elif returnAs == 'bin':
                return r.raw
        else:
            raise Exception('Download object failure.')

    @loggedIn
    def forwardObjectMsg(self, to, msgId, contentType='image'):
        if contentType not in ['image','video','audio']:
            raise Exception('Type not valid.')
        data = self.genOBSParams({'name': f'{int(time.time())}', 'tomid': to,'oid': 'reqseq','reqseq': self.revision,'type': contentType,'copyFrom': '/talk/m/%s' % msgId})
        r = self.server.postContent(self.server.LINE_OBS_DOMAIN + '/talk/m/copy.nhn', data=data, headers=self.server.timelineHeaders)
        if r.status_code != 200:
            raise Exception('Forward object failure.')
        return True
