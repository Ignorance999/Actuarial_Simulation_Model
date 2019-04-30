# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:52:12 2019

"""
from itertools import product as cartesian_product
import pandas
class ResultBlock(object):
    '''
	This class's instance contains data calculated from VarNameSpace, after calling fRunModel(). 
	Its self.dfResults have 3 major dimensions, namely OutputGpInd, RangeInd, VarInd. 
	OutputGpInd: Outputformat keys, which are tuples defined in OutputFormatTable class instance.
	RangeInd: Values for Parameters of Variables. e.g. t=0, or t=10
	VarInd: Names of Variables
    '''
    
    def __init__(self,ltOutputGpInd,ltRangeInd,lsRangeIndNames): 
        self.ltOutputGpInd=ltOutputGpInd#Outputformattable->odOutputFormats
        self.ltRangeInd=ltRangeInd
        self.lsRangeIndNames=lsRangeIndNames
        self.ltCombinedInd=list(cartesian_product(ltOutputGpInd,ltRangeInd))

        indexTemp=pandas.MultiIndex.from_tuples(self.ltCombinedInd)
        
        self.dfResults=pandas.DataFrame(index=indexTemp)
        
        
    def fAddRow(self,dResultForPol):
        pass
    
    def fAddColumn(self,varTemp,odCURR_OUTPUT_FORMAT_CHECK_SINGLE):
		#TODO:change this name later
        #print([dVarCache[tt[1]] for tt in self.ltCombinedInd])
        #print([odCURR_OUTPUT_FORMAT_CHECK_SINGLE[tt[0]] for tt in self.ltCombinedInd])
        lResult=[varTemp._dCache[tt[1]] if odCURR_OUTPUT_FORMAT_CHECK_SINGLE[tt[0]] else 0 for tt in self.ltCombinedInd]
        self.dfResults[varTemp.sName]=lResult

        
    def fdfResultsIndToStr(self):
        dfTemp=self.dfResults.copy(deep=True)
        dfTemp.index=self.dfResults.index.map(str)
        return dfTemp
