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

#heading tbl
'''
        from pathlib import Path
        import xml.etree.ElementTree as xmlET
      import re 
      '''
class InputPrototype(object):
   # _lsXmlAttrs=["FEATURES","KEYCOLS","HEADINGS","TYPE"]#,"BODY"]    
   # _lsXmlTypes=["str","int","str","str"]#,"BODY"]    
    def __init__(self,sFilePath=".\\Table.txt"): #sTableDir=".",
        #KEYCOL STARTS AT 0
        #from pathlib import Path
        # import xml.etree.ElementTree as xmlET
        self._pThisModuleDir = Path(__file__).parent
        #print(self._sThisModuleDir)
        #print(fileDir)
        #self._pTableDir = (self._pThisModuleDir/sTableDir).resolve()
        #print(self._sTableDir)        
        self._pFilePath=Path(sFilePath)  
        self._xmlRoot = xmlET.parse(self._pFilePath).getroot()
        for xmlChild in self._xmlRoot:#list(zip(Table._lsXmlAttrs,Table._lsXmlTypes)):
            if xmlChild.tag != "BODY":
                #print(xmlChild.tag)
               # print(xmlChild.attrib["type"])
                if "is_array" in xmlChild.attrib:
                    bIsArray=False if (xmlChild.attrib["is_array"].lower()=="false") else True
                else:
                    bIsArray=True
                self.__setattr__(xmlChild.tag,
                             self._fXMLFindChildOutputList(sChildName=xmlChild.tag,
                                                          sType=xmlChild.attrib["type"],
                                                          bIsArray=bIsArray)) 
        self.BODY=self._fXMLReadBody() 
        
    def _fXMLFindChildOutputList(self,sChildName,sType="str", bIsArray=True, #xmlRoot=None,
                            sStripChars=r"\s+",sSplitChars=","):
        sTemp=self._xmlRoot.find(sChildName).text 
        #fType=globals()["__builtins__"][sType]
        fType=mUtils.fGetTypeFromBuiltins(sType)
        if bIsArray:
            lsTemp=sTemp.split(sSplitChars)
            lsTemp1=[re.sub(sStripChars,"",s) for s in lsTemp]           
            lTemp=list(map(fType,lsTemp1))
            return lTemp
        else:
            Temp=fType(sTemp)
            return Temp
    
    def _fXMLReadBody(self):
        #print("gg1")
        pass
    def __str__(self):
        return str(pprint.pprint(self.__dict__))
    
    #lscAllTableTypes=["MPFTable","GenTable"]
    #TODO:change this to static method? maybe?
    @classmethod
    def fcGetClassType(cls,sFilePath=".\\Table.txt"):
        pFilePath=Path(sFilePath)  
        xmlRoot = xmlET.parse(pFilePath).getroot()
        sTableType=xmlRoot.find("CLASS_TYPE").text
        return sTableType

    
#t=Table()    