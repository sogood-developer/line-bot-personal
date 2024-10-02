import requests, json, threading

'''

EXAMPLE

from minzrestapi import *

api = MinzRestApi('YOUR APIKEY')
data = api.googleSearch("Naruto")
api.print_result(data)

'''

class MinzRestApi(threading.Thread):
    def __init__(self, apikey):
        super(MinzRestApi, self).__init__()
        self.base_url = "https://api.ansaragaproject.com"
        self.session = requests.Session()
        self.headers = apikey 

    def print_result(self, data):
        print(json.dumps(data, indent=4, sort_keys=True))

    def requestGet(self, path, params):
        main = self.session.get(self.base_url+path, params=params).json()
        return main

    ''' LINE FEATURE '''

    def linePrimaryCreated(self, authkey=""):
        params = {"authkey": authkey, "apikey": self.headers}
        main = self.requestGet("/authtoprimary_", params)
        return main

    def linePrimaryConvert(self, authtoken="", apptype="DESKTOPWIN"):
        params = {"authtoken": authtoken, "apptype": apptype, "apikey": self.headers}
        main = self.requestGet("/authtosecondary_", params)
        return main

    def removeE2EE(self, authtoken=""):
        params = {"authtoken": authtoken, "apikey": self.headers}
        main = self.requestGet("/removee2ee", params)
        return main

    def lineAppNameRandom(self, apptype):
        params = {"apptype": apptype, "apikey": self.headers}
        main = self.requestGet("/lineappnamerandom", params)
        return main

    def lineAppName(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/lineappname", params)
        return main

    def getContact(self, mid):
        params = {"mid": mid, "apikey": self.headers}
        main = self.requestGet("/getcontact", params)
        return main

    def sendImageWithURL(self, authtoken, to, url):
        params = {"authtoken": authtoken, "to": to, "url": url, "apikey": self.headers}
        main = self.requestGet("/sendimageurl", params)
        return main

    def sendVideoWithURL(self, authtoken, to, url):
        params = {"authtoken": authtoken, "to": to, "url": url, "apikey": self.headers}
        main = self.requestGet("/sendvideourl", params)
        return main

    def changeProfileImage(self, authtoken, msgid):
        params = {"authtoken": authtoken, "msgid": msgid, "apikey": self.headers}
        main = self.requestGet("/changeprofileimage", params)
        return main

    def changeProfileCover(self, authtoken, msgid):
        params = {"authtoken": authtoken, "msgid": msgid, "apikey": self.headers}
        main = self.requestGet("/changeprofilecover", params)
        return main

    def lineGetQr(self, apptype="DESKTOPWIN", cert=None):
        if cert:params = {"apptype": apptype, "cert": cert, "apikey": self.headers}
        else:params = {"apptype": apptype, "apikey": self.headers}
        main = self.requestGet("/getqrline", params)
        return main

    def lineGetPin(self, session):
        params = {"session": session, "apikey": self.headers}
        main = self.requestGet("/linegetpin", params)
        return main

    def lineGetAuth(self, session):
        params = {"session": session, "apikey": self.headers}
        main = self.requestGet("/linegetauth", params)
        return main

    def randomProxy(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/proxylist", params)
        return main

    ''' MEDIA FEATURE '''

    def statusApikey(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/status", params)
        return main

    def randomProxy(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/proxylist", params)
        return main

    def randomQuotesEN(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/randomquote_en", params)
        return main 

    def randomQuotesID(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/randomquote_id", params)
        return main

    def memeListGenerator(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/memelist", params)
        return main

    def generateName(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/genname", params)
        return main

    def worldNews(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/worldnews", params)
        return main

    def beritaIndonesia(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/beritaindo", params)
        return main

    def xx1MovieList(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/xx1movielist", params)
        return main

    def coronaInfo(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/coronainfo", params)
        return main

    def bmkgInfo(self):
        params = {"apikey": self.headers}
        main = self.requestGet("/bmkginfo", params)
        return main

    def instagramProfile(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/instagram", params)
        return main

    def instagramStory(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/instagramstory", params)
        return main

    def twitterProfile(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/twitter", params)
        return main

    def githubProfile(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/github", params)
        return main

    def cekResi(self, query, resi):
        params = {"query": query, "resi": resi, "apikey": self.headers}
        main = self.requestGet("/cekresi", params)
        return main

    def translator(self, query, language):
        params = {"query": query, "language": language, "apikey": self.headers}
        main = self.requestGet("/translator", params)
        return main

    def artiNama(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/artinama", params)
        return main

    def sifatNama(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/sifatnama", params)
        return main

    def kecocokanPasangan(self, nama1, nama2):
        params = {"nama1": nama1, "nama2": nama2, "apikey": self.headers}
        main = self.requestGet("/kecocokanpasangan", params)
        return main

    def mapsDirector(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/maps", params)
        return main

    def weatherInfo(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/weather", params)
        return main

    def wikipediaID(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/wikipedia_id", params)
        return main

    def wikipediaEN(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/wikipedia_en", params)
        return main

    def KBBI(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/kbbi", params)
        return main

    def lyricSearch(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/lyric", params)
        return main

    def jooxSearch(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/joox", params)
        return main

    def googleSearch(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/google", params)
        return main

    def googleImage(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/googleimg", params)
        return main

    def gifSearch(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/gif", params)
        return main

    def jadwalSholat(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/jadwalsholat", params)
        return main

    def fancyText(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/fancy", params)
        return main

    def zodiacInfo(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/zodiac", params)
        return main

    def b64Encode(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/encode", params)
        return main

    def b64Decode(self, query):
        params = {"query": query, "apikey": self.headers}
        main = self.requestGet("/decode", params)
        return main

    def tinyUrl(self, url,custom=None):
        if custom:params = {"url": url,"custom":custom, "apikey": self.headers}
        else:params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/tinyurl", params)
        return main

    def cocofunDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/cocofundl", params)
        return main

    def facebookDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/facebookdl", params)
        return main

    def tiktokDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/tiktokdl", params)
        return main

    def youtubeDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/youtubedl", params)
        return main

    def instagramDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/instagramdl", params)
        return main

    def twitterDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/twitterdl", params)
        return main

    def pinterestDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/pinterestdl", params)
        return main

    def lineVoomDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/linevoomdl", params)
        return main

    def nekopoiDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/nekopoidl", params)
        return main

    def smuleDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/smuledl", params)
        return main

    def jooxDownload(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/jooxdl", params)
        return main

    def jooxAlbum(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/jooxalbum", params)
        return main

    def jooxArtist(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/jooxartist", params)
        return main

    def jooxPlaylist(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/jooxplaylist", params)
        return main

    def screenshotWeb(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/ssweb", params)
        return main

    def zoomImage(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/zoom", params)
        return main

    def rotateImage(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/rotate", params)
        return main

    def blurImage(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/blur", params)
        return main

    def bnwImage(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/bnw", params)
        return main

    def removeBGImage(self, url):
        params = {"url": url, "apikey": self.headers}
        main = self.requestGet("/removebg", params)
        return main

    def memeGenerator(self, text1, text2, category):
        params = {"text1": text1, "text2": text2, "category": category, "apikey": self.headers}
        main = self.requestGet("/memecreate", params)
        return main

    def memeCustom(self, text1, text2, url):
        params = {"text1": text1, "text2": text2, "url": url, "apikey": self.headers}
        main = self.requestGet("/memecustom", params)
        return main

    ''' TEXT PRO '''

    def greenChrome3DText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/greenchrome3dtext", params)
        return main

    def shinyCristal3DText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/shinycristal3dtext", params)
        return main

    def cartoon3DText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/cartoon3dtext", params)
        return main

    def hologramColor3DText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/hologramcolor3dtext", params)
        return main

    def luxury3DText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/luxury3dtext", params)
        return main

    def grungeMetalic3DText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/grungemetalic3dtext", params)
        return main

    def multicolorPaint3DText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/multicolorpaint3dtext", params)
        return main

    def neonLightText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/neonlighttext", params)
        return main

    def shinyCristal3DText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/shinycristal3dtext", params)
        return main

    def typographyText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/typographytext", params)
        return main

    def partyText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/partytext", params)
        return main

    def comicText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/comictext", params)
        return main

    def goldenText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/goldentext", params)
        return main

    def blackpickLogoText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/blackpicklogotext", params)
        return main

    def transformerText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/transformertext", params)
        return main

    def lightGlowText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/lightglowtext", params)
        return main

    def haryypotterText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/harrypottertext", params)
        return main

    def quoteText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/quotetext", params)
        return main

    def bokehText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/bokehtext", params)
        return main

    def breakWallText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/breakwalltext", params)
        return main

    def iceColdText(self, text):
        params = {"apikey": self.headers, "text": text}
        main = self.requestGet("/textpro/icecoldtext", params)
        return main
