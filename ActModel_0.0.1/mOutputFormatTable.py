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
import itertools
#import pandas
'''
        from pathlib import Path
        import xml.etree.ElementTree as xmlET
      import re 
      '''
class OutputFormatTable(Table):
	"""
	This class reads data from XML files. It determines the classification of different policies, and how the policies aggregate. The ResultBlock and hence the real outputs will use information from OutputFormatTable.
	"""
   # _lsXmlAttrs=["FEATURES","KEYCOLS","HEADINGS","TYPE"]#,"BODY"]    
   # _lsXmlTypes=["str","int","str","str"]#,"BODY"]    
    def __init__(self,*args,**kwargs): #sTableDir=".",        
        #super().__init__(self,sTableName=sTableName)   
        #self.dAccumulations={}        
        super().__init__(*args,**kwargs)
        #self.odOutputFormatsRaw=mUtils.fGetFirstElementOrderedDict(self._Input.dAllInputs["OutputFormatTable"]).BODY
        self.odOutputFormats=self._fCreateOutputFormats()
        self.odOutputFormatsRaw=self.BODY #alias for BODY
        '''
        {'one': [(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
                 (('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))],
        'second': [(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
                    (('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))]}
        '''
        
    def _fXMLFindChildOutputList(self,*args,**kwargs):                
        return super()._fXMLFindChildOutputList(*args,**kwargs)
    
    def _fXMLReadBody(self):
        odTemp=collections.OrderedDict()
        for xmlTemp1 in self._xmlRoot.find("BODY").findall("OUTPUT_FORMAT"):
            lTemp=[]
            for xmlTemp2 in xmlTemp1.findall("OUTPUT_DIM"):
                for xmlTemp3 in xmlTemp2:
                    tTemp=(xmlTemp2.attrib["name"],xmlTemp3.tag,xmlTemp3.text.strip())#tag is accumulation/product, text.strip is its value,eg PROD1
                    lTemp.append(tTemp)
            odTemp[xmlTemp1.attrib["name"]]=lTemp                   
        self.BODY=odTemp
        return self.BODY
    
    def _fCreateOutputFormats(self):
        '''        
         'BODY': OrderedDict([('one',
               [('first', 'ACCUMULATION', 'ACC1'),
                ('first', 'PRODUCT', 'PROD2'),
                ('second', 'CRITERIA', 'bTemp')]),
              ('second',
               [('first', 'ACCUMULATION', 'ACC1'),
                ('first', 'PRODUCT', 'PROD2'),
                ('second', 'CRITERIA', 'bTemp')])])}
        '''  
        odAllDims=collections.OrderedDict()
        for sKey,lTemp in self.BODY.items():
            dDims={}            
            for tTemp in lTemp:
                sDimName=tTemp[0]
                if sDimName in dDims:
                    dDims[tTemp[0]].append(tTemp)    
                else:
                    dDims[tTemp[0]]=[tTemp]
                '''{'first': [('first', 'ACCUMULATION', 'ACC1'), ('first', 'PRODUCT', 'PROD2')],
                    'second': [('second', 'CRITERIA', 'bTemp')]}'''    
                lAllDims=list(itertools.product(*[autoTemp for autoTemp in dDims.values()]))
                '''[(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
                    (('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))]'''
            odAllDims[sKey]=lAllDims  
                    #self.dOutputFormats=dAllDims
        '''
        {'one': [(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
                 (('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))],
        'second': [(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
                    (('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))]}
        '''
        return odAllDims              

    def fodOutputFormatsFromRawToCooked(self,dCURR_OUTPUT_FORMAT_RAW_CHECK):
        '''
        self.odOutputFormats:
        {'one': [(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
                 (('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))],
        'second': [(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
                    (('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))]}
        dCURR_OUTPUT_FORMAT_CHECK:
        
        '''
        '''
        dCURR_OUTPUT_FORMAT_CHECK:
        {'one': {('first', 'ACCUMULATION', 'ACC1'): True,
  ('first', 'PRODUCT', 'PROD2'): False,
  ('second', 'CRITERIA', 'bTemp'): False},
 'second': {('first', 'ACCUMULATION', 'ACC1'): True,
  ('first', 'PRODUCT', 'PROD2'): False,
  ('second', 'CRITERIA', 'bTemp'): False}}
        '''
        dAllTemp={}
        for sKey,lTemp in self.odOutputFormats.items():
            dTemp={}
            for tTemp1 in lTemp:
                bAccumulated=True
                for tTemp2 in tTemp1:
                    bAccumulated=dCURR_OUTPUT_FORMAT_RAW_CHECK[sKey][tTemp2] and bAccumulated
                dTemp[tTemp1]=bAccumulated
            dAllTemp[sKey]=dTemp                    
        return dAllTemp        
    
#a=OutputFormatTable(".\\test_output\\out1.txt")