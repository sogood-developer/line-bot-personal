# -*- coding: utf-8 -*-
from lib.linepy import *
from art import *
from lib.akad.ttypes import OpType, MediaType, ContentType, ApplicationType, TalkException, ErrorCode, ShouldSyncException
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from threading import Thread
from urllib.parse import urlencode, quote
from pathlib import Path
from lib.template import Template
from lib.archimed import Archimed
from youtubesearchpython import SearchVideos
from lib.nulis import tulis
from Naked.toolshed.shell import execute_js
from collections.abc import Iterable
from pytube import YouTube
import time, random, sys, json, codecs, re, os, shutil, requests, ast, pytz, atexit, traceback, base64, pafy, timeago, math, argparse

try:
    if __modified__ != 'Zero Cool':
        sys.exit('++ Error : Please use lib linepy-modified, you can find it on github')
except Exception as e:
    sys.exit('++ Error : Please use lib linepy-modified, you can find it on github')
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def update_non_existing_inplace(original_dict, to_add):
    for key, value in original_dict.items():
        if key not in to_add:
            to_add[key] = value
        if type(value) == dict:
            for k, v in value.items():
                if k not in to_add[key]:
                    to_add[key][k] = v
    original_dict.update(to_add)
    return original_dict

class SafeDict(dict):
    def __missing__(self, key):
        return '{' + key + '}'
