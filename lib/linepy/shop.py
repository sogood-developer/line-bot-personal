from lib.akad.ttypes import (GetProductRequest, PurchaseOrder, Locale)
import re
# -*- coding: utf-8 -*-

def loggedIn(func):
    def checkLogin(*args, **kwargs):
        if args[0].isLogin:
            return func(*args, **kwargs)
        else:
            args[0].callback.default('You must login to LINE')
    return checkLogin
    
class Shop(object):
    isLogin = False

    def __init__(self):
        self.isLogin = True
        
    @loggedIn
    def getProduct(self, packageID, language, country):
        return self.shop.getProduct(packageID, language, country)
    
    @loggedIn
    def getActivePurchases(self, start, size, language, country):
        return self.shop.getActivePurchases(start, size, language, country)
    
    @loggedIn
    def getOwnedProducts(self, sid='sticker', offset=0, limit=1000):
        shopIds = ['stickershop', 'sticonshop', 'themeshop']
        if sid == 'sticker': shopId = shopIds[0]
        elif sid == 'emoji': shopId = shopIds[1]
        elif sid == 'theme': shopId = shopIds[2]
        else: return []
        locale = Locale()
        locale.language = "EN"
        locale.country = "ID"
        return self.shop.getOwnedProducts(shopId, offset, limit, locale)

    @loggedIn
    def getProductV2(self, productId):
        productType = 1
        if re.findall("[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}", productId) != []:
            productType = 2
        else:
            if re.findall("[0-9a-f]{24}", productId) != []:
                productType = 3

        data = GetProductRequest()
        data.productType = productType
        data.productId = productId
        data.carrierCode = "510012"
        data.saveBrowsingHistory = False
        return self.shop.getProductV2(data).productDetail
    
    @loggedIn
    def placePurchaseOrderWithLineCoin(self, to, productId):
        info = self.getProductV2(productId)
        locale = Locale()
        locale.language = "EN"
        locale.country = "ID"
        data = PurchaseOrder()
        data.shopId = info.type + "shop"
        data.productId = productId
        data.recipientMid = to
        data.price = info.price
        data.enableLinePointAutoExchange = True
        data.locale = locale
        data.presentAttributes = {}
        return self.shop.placePurchaseOrderWithLineCoin(data)