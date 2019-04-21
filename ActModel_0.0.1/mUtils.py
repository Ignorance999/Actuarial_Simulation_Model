# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:52:12 2019

@author: User
"""
from mVariable import Variable
def fGetTypeFromBuiltins(sType:str):
    #used in both mTable and mGenTable
    try:
        return globals()["__builtins__"][sType]
    except:
        return getattr(globals()["__builtins__"],sType)
    #finally:
     #   raise Exception ("fGetTypeFromBuiltins Error")        
    
def fGetFirstElementOrderedDict(odTemp):
    return next(iter(odTemp.values()))


def fdecCreateVariable(fInput):
    varTemp=Variable()
    varTemp.fSetfFunction(fInput,bReInitialize=True)
    #varTemp.fReInitialize()
    return varTemp
    
    