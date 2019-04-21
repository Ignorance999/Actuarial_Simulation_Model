# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:52:12 2019

@author: User
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
        
        '''
        ltSepCombInd=[]
        for t in ltCombinedInd:
            lTemp=[]
            for t2 in t:
                lTemp.extend(t2)
            ltSepCombInd.append(tuple(lTemp))
        '''
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
'''        
a=[((10,20),(30,40)),
   ((10,40),(30,40))]        
b=[(1,2),
    (3,4)]
r=ResultBlock(a,b,["haha","ff","ee"])
#r.fAddRow()
#r.fAddRow({1:11,2:22,3:33})
print(r.dfResults)
s=r.dfResults
s["e"]=(1,2,3,4)
s.loc[(10,20),(30,40),1,2]#slower
s.loc[((10,20),(30,40),1,2)]#much faster
'''
#p._Output.ddReports["one"][('t',)].dfResults