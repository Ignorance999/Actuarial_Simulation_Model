# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:52:12 2019

"""
import pandas
import itertools
class ResultBlock(object):
    '''
    OutputGpInd, RangeInd, VarInd
    '''
    
    def __init__(self,ltOutputGpInd,ltRangeInd,lsRangeIndNames): 
        self.ltOutputGpInd=ltOutputGpInd#Outputformattable->odOutputFormats
        self.ltRangeInd=ltRangeInd
        self.lsRangeIndNames=lsRangeIndNames
        self.ltCombinedInd=list(itertools.product(ltOutputGpInd,ltRangeInd))

        indexTemp=pandas.MultiIndex.from_tuples(self.ltCombinedInd)
        
        self.dfResults=pandas.DataFrame(index=indexTemp)
        
        
    def fAddRow(self,dResultForPol):
        pass
        #srTemp=pandas.Series(dResultForPol,index="ff")
        #self.dfResults=self.dfResults.append(dResultForPol,ignore_index=True)
    
    def fAddColumn(self,varTemp,odCURR_OUTPUT_FORMAT_CHECK_SINGLE):#change this name later
        #print([dVarCache[tt[1]] for tt in self.ltCombinedInd])
        #print([odCURR_OUTPUT_FORMAT_CHECK_SINGLE[tt[0]] for tt in self.ltCombinedInd])
        lResult=[varTemp._dCache[tt[1]] if odCURR_OUTPUT_FORMAT_CHECK_SINGLE[tt[0]] else 0 for tt in self.ltCombinedInd]
        self.dfResults[varTemp.sName]=lResult
        #print(lResult)
        
    def fdfResultsIndToStr(self):
        dfTemp=self.dfResults.copy(deep=True)
        dfTemp.index=self.dfResults.index.map(str)
        return dfTemp
