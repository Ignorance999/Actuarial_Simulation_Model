"""
Created on Sat Mar 16 15:33:14 2019

@author: User
"""
from table import Table
import pandas
from io import StringIO
import re

class MPFTable(Table):
    """
    This class read data from XML file and generate a dataframe containing records for different policies.
    """
    def __init__(self,*args,**kwargs): #sTableDir=".",
        super().__init__(*args,**kwargs)
        self.iCurrMPFRowIndex=-1
        
    def _fXMLFindChildOutputList(self,*args,**kwargs):                
        return super()._fXMLFindChildOutputList(*args,**kwargs)
    
    def _fXMLReadBody(self)->pandas.DataFrame:

        sioBody=StringIO(re.sub(r"\t+","",self._xmlRoot.find("BODY").text).strip())
        self.BODY=pandas.read_csv(sioBody,sep=",",header=None,names=self.HEADINGS)
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
    
        
