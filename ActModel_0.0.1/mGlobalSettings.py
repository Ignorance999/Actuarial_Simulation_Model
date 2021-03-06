# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:52:12 2019

@author: User
"""
#import pandas
import collections
import itertools
import mUtils
'''
ntGlobalSettings=collections.namedtuple("GlobalSettings",["odDimVarRanges","odOutputFormats","odReportVars"],verbose=False)\
                (odDimVarRanges=collections.OrderedDict([("t",range(0,100)),
                                                         ("k",range(3,500)),
                                                         ("s",range(4,6))]),#can also initlize using a dict
                odOutputFormats=INPUT.dAllInputs["OutputFormatTable"].BODY,
                odReportVars=INPUT.dAllInputs["ReportVarTable"].BODY)#this parameter can be customized later
'''
class GlobalSettings(object):
    def __init__(self,inputTemp):
        self._Input=inputTemp
        self.odDimVarRanges=collections.OrderedDict([("t",range(0,100)),
                                                         ("k",range(3,500)),
                                                         ("s",range(4,6))])
        
       # print(next(iter(self._Input.dAllInputs["OutputFormatTable"].values())))
        self.odOutputFormatsRaw=mUtils.fGetFirstElementOrderedDict(self._Input.dAllInputs["OutputFormatTable"]).BODY
        self.odOutputFormats=mUtils.fGetFirstElementOrderedDict(self._Input.dAllInputs["OutputFormatTable"]).odOutputFormats
        self.odReportVars=mUtils.fGetFirstElementOrderedDict(self._Input.dAllInputs["ReportVarTable"]).BODY
        
#from mInput import Input        
#g=GlobalSettings(Input())        
        
