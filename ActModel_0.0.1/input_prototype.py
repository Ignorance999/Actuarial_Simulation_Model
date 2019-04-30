# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:33:14 2019

@author: User
"""
import re
from pathlib import Path
import xml.etree.ElementTree as xmlET
from utils import fGetTypeFromBuiltins
import pprint
from directories import test_input_table_path, default_table_path

class InputPrototype(object):
    """
    The abstract parent class for all Tables and Scripts
    Reads XML files - source files containing assumptions and records of the model

    Attributes:
        _pThisModuleDir
        _xmlRoot
        BODY
    """

   # _lsXmlAttrs=["FEATURES","KEYCOLS","HEADINGS","TYPE"]#,"BODY"]
   # _lsXmlTypes=["str","int","str","str"]#,"BODY"]

    def __init__(self,sFilePath=test_input_table_path):
        try:
            self._pThisModuleDir = Path(__file__).parent
        except NameError:
            #Console Mode
            self._pThisModuleDir=None


        self._pFilePath=Path(sFilePath)
        self._xmlRoot = xmlET.parse(str(self._pFilePath)).getroot()# grabbing xml file to use as root
		# setting self._fXMLFindChildOutputList with xml values from xml root
        for xmlChild in self._xmlRoot:
            if xmlChild.tag != "BODY":
                if "is_array" in xmlChild.attrib:
                    bIsArray=False if (xmlChild.attrib["is_array"].lower()=="false") else True
                else:
                    bIsArray=True
                self.__setattr__(xmlChild.tag,
                             self._fXMLFindChildOutputList(sChildName=xmlChild.tag,
                                                          sType=xmlChild.attrib["type"],
                                                          bIsArray=bIsArray))
        self.BODY=self._fXMLReadBody()

    def _fXMLFindChildOutputList(self,sChildName,sType="str", bIsArray=True,
                            sStripChars=r"\s+",sSplitChars=","):
        """
        Returns xml children grabbed from xmlRoot and cleaned with mUtils.fGetTypeFromBuiltins()
        :param sChildName: the child to grab from xml root
        :param sType: type of the child, defaults to "str"
        :param bIsArray: boolean value indiciating if child is array
        :param sStripChars: characters to strip from each element in xml
        :param sSplitChars: characters to split xml elements
        :return: Temp, a list of the types of the objects contained in xml file
        """
        sTemp=self._xmlRoot.find(sChildName).text
        fType = fGetTypeFromBuiltins(sType)
        if bIsArray:
            lsTemp=sTemp.split(sSplitChars)
            lsTemp1=[re.sub(sStripChars,"",s) for s in lsTemp]
            lTemp=list(map(fType,lsTemp1))
            return lTemp
        else:
            Temp=fType(sTemp)
            return Temp

    def _fXMLReadBody(self):
        pass
    def __str__(self):
        return str(pprint.pprint(self.__dict__))

    #lscAllTableTypes=["MPFTable","GenTable"]
    #TODO:change this to static method? maybe?
    @classmethod
    def fcGetClassType(cls,sFilePath=default_table_path):
        pFilePath=Path(sFilePath)
        xmlRoot = xmlET.parse(str(pFilePath)).getroot()
        sTableType=xmlRoot.find("CLASS_TYPE").text
        return sTableType


#t=Table()
