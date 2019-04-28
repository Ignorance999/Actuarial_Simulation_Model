# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:33:14 2019

@author: User
"""
#import xml.etree.ElementTree as xmlET
import sys,os
from mTable import Table
import pandas as pandas
from io import StringIO
import re
#import pandas
'''
        from pathlib import Path
        import xml.etree.ElementTree as xmlET
      import re 
      '''
class MPFTable(Table):
   # _lsXmlAttrs=["FEATURES","KEYCOLS","HEADINGS","TYPE"]#,"BODY"]    
   # _lsXmlTypes=["str","int","str","str"]#,"BODY"]    
    def __init__(self,*args,**kwargs): #sTableDir=".",        
        #super().__init__(self,sTableName=sTableName)        
        super().__init__(*args,**kwargs)
        self.iCurrMPFRowIndex=-1
        
    def _fXMLFindChildOutputList(self,*args,**kwargs):                
        return super()._fXMLFindChildOutputList(*args,**kwargs)
    
    def _fXMLReadBody(self)->pandas.DataFrame:
        #self.BODY is dataframe
        
        #import pandas        
        # from io import StringIO
       # print("gg")
        sioBody=StringIO(re.sub(r"\t+","",self._xmlRoot.find("BODY").text).strip())
        self.BODY=pandas.read_csv(sioBody,sep=",",header=None,names=self.HEADINGS)
        #print(self.BODY)
        return self.BODY
    
    
    #@staticmethod
    #TODO: may try using itertools later
    def fd_sNextMPFRow(self):
        self.iCurrMPFRowIndex=self.iCurrMPFRowIndex+1
        return self.fd_sCurrMPFRow()

    def fd_sCurrMPFRow(self):
        if self.iCurrMPFRowIndex>=0 and self.iCurrMPFRowIndex<=self.BODY.shape[0]-1:
            return dict(self.BODY.iloc[self.iCurrMPFRowIndex])
        else:
            self.iCurrMPFRowIndex=-1
            return "EOF"
    
    #def fd_sNextMPFRow(self):
    #    return next(self.BODY.iterrows())
        
#w=MPFTable(sFilePath=".\\MPF\\MPF.txt")    