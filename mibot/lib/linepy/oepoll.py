# -*- coding: utf-8 -*-
from lib.akad.ttypes import TalkException, ShouldSyncException
from .client import LINE
from threading import Thread
from types import *

import os, sys, time

class OEPoll(object):
    OpInterrupt = {}
    client = None
    __squareSubId = {}
    __squareSyncToken = {}

    def __init__(self, client):
        if type(client) is not LINE:
            raise Exception('You need to set LINE instance to initialize OEPoll')
        self.client = client
        self.threads = []
        self.localRev = -1
        self.globalRev = 0
        self.individualRev = 0

    def __execute(self, op, threading):
        try:
            if threading:
                _td = Thread(target=self.OpInterrupt[op.type], args=(op,))
                _td.daemon = False
                self.threads.append(_td)
            else:
                self.OpInterrupt[op.type](op)
        except Exception as e:
            self.client.log(e)

    def addOpInterruptWithDict(self, OpInterruptDict):
        self.OpInterrupt.update(OpInterruptDict)

    def addOpInterrupt(self, OperationType, DisposeFunc):
        self.OpInterrupt[OperationType] = DisposeFunc
    
    def setRevision(self, revision):
        self.client.revision = max(revision, self.client.revision)
    
    def singleTrace(self, count=1, fetchOperations=None):
        if not fetchOperations:
            fetchOperations = self.client.fetchOperation
        try:
            operations = fetchOperations(self.client.revision, count=count)
        except KeyboardInterrupt:
            sys.exit()
        except ShouldSyncException:
            self.setRevision(self.client.poll.getLastOpRevision())
            return []
        except:
            return []

        if operations is None:
            return []
        else:
            return operations

    def trace(self, threading=False, fetchOperations=None):
        if not fetchOperations:
            fetchOperations = self.client.fetchOperation
        try:
            operations = fetchOperations(self.client.revision)
        except KeyboardInterrupt:
            sys.exit()
        except ShouldSyncException:
            self.setRevision(self.client.poll.getLastOpRevision())
            return
        except:
            return
        
        for op in operations:
            if op.type in self.OpInterrupt.keys():
                self.__execute(op, threading)
            self.setRevision(op.revision)
        for thread in self.threads:
            thread.start()
        for thread in self.threads:
            thread.join()
        self.threads = []

    def singleFetchSquareChat(self, squareChatMid, limit=1):
        if squareChatMid not in self.__squareSubId:
            self.__squareSubId[squareChatMid] = 0
        if squareChatMid not in self.__squareSyncToken:
            self.__squareSyncToken[squareChatMid] = ''
        
        sqcEvents = self.client.fetchSquareChatEvents(squareChatMid, subscriptionId=self.__squareSubId[squareChatMid], syncToken=self.__squareSyncToken[squareChatMid], limit=limit, direction=1)
        self.__squareSubId[squareChatMid] = sqcEvents.subscription
        self.__squareSyncToken[squareChatMid] = sqcEvents.syncToken

        return sqcEvents.events