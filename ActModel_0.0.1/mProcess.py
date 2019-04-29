# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:40:33 2019

@author: User
"""
from mInput import Input
from mOutput import Output
import pprint
import collections
import importlib
from mGlobalSettings import GlobalSettings
class Process(object):
    """
	This class is to manage all the internal calculations of this model. 
	It contains Input, GlobalSettings, VarNameSpace and Output class instance.
    """
    def __init__(self):
        self.dMode={"bIfRunByProd":False}#useless now, this "bIfRunByProd" indicator is for later use.
        self._Input=Input()
        self._GlobalSettings=GlobalSettings(self._Input)
        self._Output=Output(self._Input,self._GlobalSettings)
        self.odAllVariables=collections.OrderedDict() # a member variable containing Variable class instances.
        for scrTemp in self._Input.dAllInputs["Script"].values():
            if bool(set(scrTemp.BODY) & set(self.odAllVariables)):
                raise Exception("Repeated definition of variables!:"+ ",".join(set(scrTemp.BODY) & set(self.odAllVariables)))
            else:
                self.odAllVariables.update(scrTemp.BODY)
        
        self.mVarNameSpace=importlib.import_module("mVarNameSpace")
        for varTemp in self.odAllVariables.values():
           varTemp.fSetfFunction(self.mVarNameSpace)#load the function into the globals of the module
           setattr(self.mVarNameSpace,varTemp.sName,varTemp)#replace the name as a Variable instead of a function           

        setattr(self.mVarNameSpace,"INPUT",self._Input)
        setattr(self.mVarNameSpace,"OUTPUT",self._Output)
        setattr(self.mVarNameSpace,"GLOBAL_SETTINGS",self._GlobalSettings)
        
    
    def fRunModel(self):
        """
        This function is called to run the entire model (to calculate the specified Variables in mVarNameSpace)
        """
        self.mVarNameSpace.fRunModel()
       
    def fPrintReport(self,sOutputFormat):
        """
        Print report using the specified name of OutputFormat 
        """
        self._Output.fPrintReport(sOutputFormat)
        
    def fPrintAllReports(self):
        self._Output.fPrintAllReports()

p=Process()   
p.fRunModel()
p.fPrintAllReports()     
