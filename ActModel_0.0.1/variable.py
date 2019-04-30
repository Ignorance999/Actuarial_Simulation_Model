# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:40:33 2019

@author: User
"""
import inspect
import types

class Variable(object):
    """
    This class represent a basic unit of calculation while running the model. Its most important member variable is self._fFunction.
    """
    def __init__(self,sName="",sFunction="",sModule="",sProduct="",sAccumulation=""):
        self.sName=sName
        self.sFunction=sFunction
        self.sModule=sModule
        #dTemp={}
        #exec(self.sFunction,dTemp)
        #self._fFunction=dTemp[self.sName]
        #self.fFunction=None#types.FunctionType()
        self._fFunction=None
        self.lsFuncArgs=[]
        self._dCache={}
        self.lProduct=sProduct.split(",")
        self.lAccumulation=sAccumulation.split(",")
        
    
    def __call__(self,*args,**kwargs):        
        if self._fFunction!=None:
            sigTemp=inspect.signature(self._fFunction)
            bargTemp=sigTemp.bind(*args,**kwargs)
            bargTemp.apply_defaults()
            odArgs=bargTemp.arguments
            tParams=tuple(odArgs.values())
            if tParams==():#if this function has 0 arguments
                tParams=tuple("SINGLE_VALUE")

            if tParams in self._dCache:
                #print("use cache")
                return self._dCache[tParams]
            else:
                autoResult=self._fFunction(*args,**kwargs)
                self._dCache[tParams]=autoResult
                return autoResult
        else:
            raise Exception("call a None in variable class!")#this error is quite impossible, as function is initilized in __init__
        
    def fSetfFunction(self,mModule_fFunc,bReInitialize=False):
        if type(mModule_fFunc)==types.ModuleType:            
            exec(self.sFunction,mModule_fFunc.__dict__)
            self._fFunction=getattr(mModule_fFunc,self.sName)
        elif type(mModule_fFunc)==types.FunctionType:
            self._fFunction=mModule_fFunc
        else:
            print("gaga")
            print(type(mModule_fFunc))
            raise Exception("wrong type for mModule_fFunc")
        self.lsFuncArgs=[sKey for sKey in inspect.signature(self._fFunction).parameters.keys()]
        if bReInitialize:
            self.fReInitialize()
    
    def fReInitialize(self):
        if self.sName=="" and self._fFunction != None:
            self.sName=self._fFunction.__name__
            
   # def fSetlsFuncArgs(self):
        
