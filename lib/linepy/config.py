# -*- coding: utf-8 -*-
from lib.akad.ttypes import ApplicationType
import re, random, os

def randomSysname():
    random.seed = (os.urandom(1024))
    return ''.join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(6))
    
class Config(object):
    LINE_HOST_DOMAIN            = 'https://legy-jp-addr.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://legy-jp-addr.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://legy-jp-addr.line.naver.jp/mh'
    LINE_TIMELINE_HM            = 'https://legy-jp-addr.line.naver.jp/hm'
    LINE_LIFF_SEND              = 'https://api.line.me/message/v3/share'
    LINE_PERMISSION_API         = 'https://access.line.me/dialog/api/permissions'

    LINE_LOGIN_REQUEST_V1       = "/acct/lgn/sq/v1"
    LINE_LOGIN_CHECK_V1         = "/acct/lp/lgn/sq/v1"
    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'
    
    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/TSHOP4'

    CHANNEL_ID = {
        'LINE_ACODE': '1655208881',
        'LINE_TROJANS': '1638870522',
        'LINE_TIMELINE': '1341209850',
        'LINE_TRANSLATE': '1627632136',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }
    
    desktopmac_app_version = ["7.7.0", "7.8.0", "7.8.1", "7.9.0", "7.10.1"]
    desktopwin_app_version = ["7.7.0", "7.8.0", "7.8.1", "7.9.0", "7.10.1"]
    chromeos_app_version = ["2.4.2", "2.4.3", "2.4.4", "2.4.5", "2.4.6", "2.4.7"]
    
    APP_VERSION = {
        'IOS': '11.12.0',
        'IOSIPAD': '11.12.0',
        'ANDROID': '11.13.2',
        'ANDROIDLITE': '2.17.0',
        'CHANNELCP': '2.15.0',
        'DESKTOPWIN': "8.6.0.3277",
        'DESKTOPMAC': random.choice(desktopmac_app_version),
        'CHROMEOS': random.choice(chromeos_app_version),
        'DEFAULT': '11.9.0'
    }

    SYSTEM_VERSION = {
        'IOS': '14.4.2',
        'IOSIPAD': '14.4.2',
        'ANDROID': '8.1.0',
        'ANDROIDLITE': '11',
        'CHANNELCP': '9',
        'DESKTOPWIN': '10.0',
        'DESKTOPMAC': random.choice(["10.15.7", "11.2.3"]),
        'CHROMEOS': '89.0.4',
        'DEFAULT': '14.2'
    }

    APP_TYPE    = 'DESKTOPMAC'
    APP_VER     = APP_VERSION[APP_TYPE] if APP_TYPE in APP_VERSION else APP_VERSION['DEFAULT']
    CARRIER     = '51010, 0-13'
    SYSTEM_NAME = 'WINDOWS'
    SYSTEM_VER  = SYSTEM_VERSION[APP_TYPE] if APP_TYPE in SYSTEM_VERSION else SYSTEM_VERSION['DEFAULT']
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    URL_REGEX   = re.compile(r'^(?:http|ftp)s?://' r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' r'localhost|' r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' r'(?::\d+)?' r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    MID_REGEX   = re.compile(r'u\w{32}')
    GID_REGEX   = re.compile(r'c\w{32}')
    RID_REGEX   = re.compile(r'r\w{32}')
    ALLIDS_REGEX= re.compile(r'(?:u\w{32}|c\w{32}|r\w{32})')

    def __init__(self, appType=None):
        if appType:
            fix_sysname = {"DESKTOPWIN": "WINDOWS", "DESKTOPMAC": "MAC"}
            self.APP_TYPE = appType
            self.SYSTEM_NAME = fix_sysname[appType]
        self.APP_VER = self.APP_VERSION[self.APP_TYPE] if self.APP_TYPE in self.APP_VERSION else self.APP_VERSION['DEFAULT']
        self.SYSTEM_VER  = self.SYSTEM_VERSION[self.APP_TYPE] if self.APP_TYPE in self.SYSTEM_VERSION else self.SYSTEM_VERSION['DEFAULT']
        self.APP_NAME = '%s\t%s\t%s\t%s' % (self.APP_TYPE, self.APP_VER, self.SYSTEM_NAME, self.SYSTEM_VER)
        if self.APP_TYPE == 'CHROMEOS':
            self.USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
        elif self.APP_TYPE == 'ANDROIDLITE':
            self.USER_AGENT = 'LLA/%s Nexus 5X %s' % (self.APP_VER, self.SYSTEM_VER)
        else:
            self.USER_AGENT = 'Line/%s %s %s' % (self.APP_VER, self.SYSTEM_NAME+"-"+randomSysname(), self.SYSTEM_VER)
