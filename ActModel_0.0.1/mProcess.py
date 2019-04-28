# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:40:33 2019

@author: User
"""
from mInput import Input
from mOutput import Output
import pprint
#import imp
import collections
import importlib
from mGlobalSettings import GlobalSettings
class Process(object):
    """

    """
    def __init__(self):
        self.dMode={"bIfRunByProd":False}#useless now
        self._Input=Input()
        self._GlobalSettings=GlobalSettings(self._Input)
        self._Output=Output(self._Input,self._GlobalSettings)
        self.odAllVariables=collections.OrderedDict()
        for scrTemp in self._Input.dAllInputs["Script"].values():
            if bool(set(scrTemp.BODY) & set(self.odAllVariables)):
                raise Exception("Repeated definition of variables!:"+ ",".join(set(scrTemp.BODY) & set(self.odAllVariables)))
            else:
                self.odAllVariables.update(scrTemp.BODY)
        
        #import imp        
        #self.mVarNameSpace=imp.new_module("VarNameSpace")
        self.mVarNameSpace=importlib.import_module("mVarNameSpace")
        for varTemp in self.odAllVariables.values(): 
           # exec(varTemp.sFunction,self.mVarNameSpace.__dict__)
           varTemp.fSetfFunction(self.mVarNameSpace)#set the function into the globals of the module
           setattr(self.mVarNameSpace,varTemp.sName,varTemp)#replace the name as a variable instead of a function
           
           #varTemp.fSetFuncGlobals(self.mVarNameSpace)
        
        setattr(self.mVarNameSpace,"INPUT",self._Input)#capital letter to show it is system variable
        setattr(self.mVarNameSpace,"OUTPUT",self._Output)
        setattr(self.mVarNameSpace,"GLOBAL_SETTINGS",self._GlobalSettings)
        
        #self.mVarNameSpace.Input2=Input()
       # self.fLoadScripts()
    
    def fRunModel(self):
        self.mVarNameSpace.fRunModel()
       
    def fPrintReport(self,sOutputFormat):
        self._Output.fPrintReport(sOutputFormat)
        
    def fPrintAllReports(self):
        self._Output.fPrintAllReports()
    #def f
p=Process()   
p.fRunModel()
p.fPrintAllReports()     
#print(type(globals()[__main__]))
# p._Output._OutputFormatTable.fodOutputFormatsFromRawToCooked(p.mVarNameSpace.odCURR_OUTPUT_FORMAT_RAW_CHECK())