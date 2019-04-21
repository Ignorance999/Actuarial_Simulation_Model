# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:40:33 2019

@author: User
"""
from pathlib import Path
import xml.etree.ElementTree as xmlET
from mInputPrototype import InputPrototype
from mVariable import Variable

class Script(InputPrototype):
    #TODO: add all available possible tags for script.txt
    def __init__(self,*args,**kwargs):
       #self.BODY is dict of Variable
       self.dVariables={}#ALIAS FOR SELF.BODY
       super().__init__(*args,**kwargs)
       
       #self._lxmlVars=[]
       #self._lVariables=[]
        
        
    def _fXMLReadBody(self)->dict:
        #self.BODY is dict of Variable
        dTemp={}
        for xmlVar in self._xmlRoot.find("BODY").findall("VARIABLE"):  
          #  sFunction=xmlVar.find("FUNCTION").text
           # iPosStart=sFunction.find("def ")
            #sSpaceBuffer=sFunction[0:iPosStart].trim()
            #sFunction1
            #print("gg:"+sFunction1)
            #print()
            varTemp=Variable(sName=xmlVar.attrib["name"],
                             sFunction=xmlVar.find("FUNCTION").text.strip(),
                             sModule=self.NAME,
                             sProduct=xmlVar.find("PRODUCT").text if xmlVar.find("PRODUCT")!=None else"",
                             sAccumulation=xmlVar.find("ACCUMULATION").text if xmlVar.find("ACCUMULATION")!=None else"")
            dTemp[varTemp.sName]=varTemp
        self.BODY=dTemp
        self.dVariables=self.BODY
        return self.BODY
        
            #varTemp.fFunction=
            #TODO: check the structure of script is correct
            