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
import collections
#import pandas
'''
        from pathlib import Path
        import xml.etree.ElementTree as xmlET
      import re 
      '''
class ReportVarTable(Table):
	"""
	This class reads data from XML files. It contains several groups of variables. 
	"""
	
    def __init__(self,*args,**kwargs): #sTableDir=".",        
        #super().__init__(self,sTableName=sTableName)   
        self.odReportVars=collections.OrderedDict()#ALIAS FOR SELF.BODY
        super().__init__(*args,**kwargs)
        
        
    def _fXMLFindChildOutputList(self,*args,**kwargs):                
        return super()._fXMLFindChildOutputList(*args,**kwargs)
    
    def _fXMLReadBody(self):
        odTemp=collections.OrderedDict()
        for xmlVar in self._xmlRoot.find("BODY").findall("REPORT_VARS"): 
            lAccumVal=xmlVar.text.strip().split(",")
            odTemp[xmlVar.attrib["name"]]=lAccumVal        
        self.BODY=odTemp
        self.odReportVars=self.BODY
        return self.BODY
    
    
#a=ReportVarTable(".\\test_output\\REPORTVAR.txt")