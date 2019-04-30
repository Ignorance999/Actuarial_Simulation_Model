# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:33:14 2019

@author: User
"""
#import xml.etree.ElementTree as xmlET
import sys,os
import mUtils
from mTable import Table
from directories import gentable_test_path
#from collections import namedtuple

class GenTable(Table):
    """
    It will read data from XML file, and generate a dictionary representing a lookup table. The keys can be multi-dimensional, i.e. there may be more than 1 key column.
    """
	
   # _lsXmlAttrs=["FEATURES","KEYCOLS","HEADINGS","TYPE"]#,"BODY"]    
   # _lsXmlTypes=["str","int","str","str"]#,"BODY"]    
    def __init__(self,*args,**kwargs): #sTableDir=".",        
        #super().__init__(self,sTableName=sTableName)        
        super().__init__(*args,**kwargs)        
    def _fXMLFindChildOutputList(self,*args,**kwargs):                
        return super()._fXMLFindChildOutputList(*args,**kwargs)
    
    def _fXMLReadBody(self)->dict:      
        lsBody=self._fXMLFindChildOutputList(sChildName="BODY",
                                   sStripChars=r"[ \t]+",sSplitChars="\n")
        import re 
        #lfType=[getattr(globals()["__builtins__"],s) for s in self.TYPE]        
        #lfType=[globals()["__builtins__"][s] for s in self.TYPE]   
        lfType=[mUtils.fGetTypeFromBuiltins(s) for s in self.TYPE]        
        dTemp={}        
        for s in lsBody:
            if bool(re.search(".+",s)):
                lTemp=s.split(",")        
                #print(lTemp)
                lTemp1=[f(s) for s,f in list(zip(lTemp,lfType))]
                #print(lTemp1)
                tKey=tuple(lTemp1[self.HEADINGS.index(s)] for s in self.KEYCOLS)
                #print(tKey)
                dValue={s:lTemp1[self.HEADINGS.index(s)] for s in self.HEADINGS
                                    if s not in self.KEYCOLS}
                #print(tValue)
                dTemp.update({tKey:dValue})        
        return dTemp
    def flGetEntireColumn(self,sColName):
        lTemp=[]
        if sColName in self.KEYCOLS:
            for tTemp in self.BODY.keys():
                lTemp.append(tTemp[self.KEYCOLS.index(sColName)])
        else:
            try:
                for dTemp in self.BODY.values():
                    lTemp.append(dTemp[sColName])
            except:
                raise Exception("sColName is not a valid column name!")
        return lTemp
        
    def fReadTable(self,Key,sColName):
        """
        self.BODY is a dict
        :param Key: can be a string or a tuple containing a single element.
        :param sColName: The name of the value you are looking for.
        :return: the corresponding value in the lookup table
        """
        return self.BODY[Key][sColName]
    
    def flAllKeys(self,bAutoSimplify=True):
        lTemp=[]
        for tTemp in self.BODY.keys():
            if bAutoSimplify==True and len(self.KEYCOLS)==1:
                lTemp.append(tTemp[0])
            else:
                lTemp.append(tTemp)
        return lTemp
                
#t=GenTable(gentable_test_path)    
