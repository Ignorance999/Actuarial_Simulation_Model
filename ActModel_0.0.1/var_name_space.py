# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:52:12 2019

@author: User
"""
import itertools
import collections
from mUtils import fdecCreateVariable    
import mUtils

INPUT=None
GLOBAL_SETTINGS=None
OUTPUT=None
"""
This module is the namespace for model calculation. Variables, Input, GlobalSettings and Output class instances will be loaded here for running the model. It will also generate the results and pass them to Output.
"""

'''
GLOBAL_SETTINGS=collections.namedtuple("GlobalSettings",["odDimVarRanges","odOutputFormats","odReportVars"],verbose=False)\
                (odDimVarRanges=collections.OrderedDict([("t",range(0,100)),
                                                         ("k",range(3,500)),
                                                         ("s",range(4,6))]),#can also initlize using a dict
                odOutputFormats=INPUT.dAllInputs["OutputFormatTable"].BODY,
                odReportVars=INPUT.dAllInputs["ReportVarTable"].BODY)#this parameter can be customized later
'''
def fRunModel():
    odVarRanges=GLOBAL_SETTINGS.odDimVarRanges
    lsVars=GLOBAL_SETTINGS.odReportVars["ok"]
    dNEXT_POLICY()#test only
    '''even slower than following method
    lDimVarsAllProds=list(itertools.product(*[autoTemp for autoTemp in odSettings.values()]))    
    for tTemp in lDimVarsAllProds:
        for sVar in lsVars:
            dArgs={}
            for iInd,sArg in enumerate(globals()[sVar].lsFuncArgs):
                dArgs[sArg]=tTemp[iInd]
            globals()[sVar](**dArgs)
    '''  
    for sVar in lsVars:
        odTemp=collections.OrderedDict({sKey:odVarRanges[sKey] for sKey in globals()[sVar].lsFuncArgs})
        lDimVarsAllProds=list(itertools.product(*[autoTemp for autoTemp in odTemp.values()]))    
        dArgs={}
        for tTemp in lDimVarsAllProds:
            for iInd,sArg in enumerate(odTemp.keys()):
                dArgs[sArg]=tTemp[iInd]
            globals()[sVar](**dArgs)
        OUTPUT.fRecordPolResults(globals()[sVar],odCURR_OUTPUT_FORMAT_RAW_CHECK())
    
@fdecCreateVariable    
def odCURR_OUTPUT_FORMAT_RAW_CHECK():
    #TODO: a bit hard to understand,more explanation later
    odAllDimsCheck=collections.OrderedDict()
    for sKey,lValue in GLOBAL_SETTINGS.odOutputFormatsRaw.items():
        dTemp={}
        bTemp=False
        for tTemp in lValue:
            sType=tTemp[1]
            sName=tTemp[2]
            #print("sName:" +sName)
            if sType=="ACCUMULATION":
                bTemp=mUtils.fGetFirstElementOrderedDict(INPUT.dAllInputs["AccumTable"]).fCheckProdInAccum(sCURR_PRODUCT(),sName)
            elif sType=="PRODUCT":
                bTemp=(sCURR_PRODUCT()==sName)
            elif sType=="CRITERIA":
                bTemp=globals()[sName]()
            else:
                raise Exception("error sType for mVarNameSpace!")
            dTemp[tTemp]=bTemp
        odAllDimsCheck[sKey]=dTemp
    return odAllDimsCheck
                    
                    
                
@fdecCreateVariable    
def dCURR_POLICY():
    return INPUT.fd_sCurrMPFRow()	

@fdecCreateVariable    
def sCURR_PRODUCT():
    if dCURR_POLICY!="EOF":
        sMPFProd=INPUT.fd_sCurrInput("MPFTable").PRODUCT
        if sMPFProd!="ALL": 
            sProd=sMPFProd										
        else:
            sProd=dCURR_POLICY()["PRODUCT"]
        if sProd in INPUT.dKeyGenTables["ProdTable"].flAllKeys():
            return sProd
        else:
            raise Exception("in Buildins,dCURR_PRODUCT:"+sProd+ " is not a valid product")	
    else:
        return "EOF"
    
@fdecCreateVariable    
def dNEXT_POLICY():
    return INPUT.fd_sNextMPFRow()
#def aa(t):
#    return t+20

