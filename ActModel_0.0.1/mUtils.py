# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:52:12 2019

@author: User
"""
from mVariable import Variable

def fGetTypeFromBuiltins(sType:str):
    """
    Returns the type of the variable with name sType
    """
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
	"""
	a function decorator. Used in mVarNameSpace.py. It will change fInput from a function to a Variable
	"""
    varTemp=Variable()
    varTemp.fSetfFunction(fInput,bReInitialize=True)
    #varTemp.fReInitialize()
    return varTemp
    
    