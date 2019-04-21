# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:33:14 2019

@author: User
"""
#import xml.etree.ElementTree as xmlET
import sys,os
import re  
from pathlib import Path
import xml.etree.ElementTree as xmlET
import mUtils
import pprint
from mInputPrototype import InputPrototype

#heading tbl
'''
        from pathlib import Path
        import xml.etree.ElementTree as xmlET
      import re 
      '''
class Table(InputPrototype):
   # lscAllTableTypes=["MPFTable","GenTable","ScenTable","ProdTable"]#no key gen table as it is abstract table
    #TODO: add all available possible tags for table.txt
    
    
   # _lsXmlAttrs=["FEATURES","KEYCOLS","HEADINGS","TYPE"]#,"BODY"]    
   # _lsXmlTypes=["str","int","str","str"]#,"BODY"]   
    '''   
    def __init__(self,*args,**kwargs): #sTableDir=".",
        return super().__init__(*args,**kwargs)
        
    def _fXMLFindChildOutputList(self,*args,**kwargs):
        return super()._fXMLFindChildOutputList(*args,**kwargs)
    
    def _fXMLReadBody(self):
        #print("gg1")
        pass
    def __str__(self):
        return super().__str__()
    
   
    @classmethod
    def fcGetClassType(cls,*args,**kwargs):
        return super().fcGetClassType(*args,**kwargs)
'''
    
#t=Table()    