# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:40:33 2019

@author: User
"""
from input_prototype import InputPrototype
from variable import Variable


class Script(InputPrototype):
    """
    This class will read the scripts and turn them into a dict containing Variables.
    """

    def __init__(self, *args, **kwargs):
        # self.BODY is dict of Variable
        self.dVariables = {}  # ALIAS FOR SELF.BODY
        super().__init__(*args, **kwargs)

    def _fXMLReadBody(self) -> dict:
        """
        self.BODY is dict of Variables
        """
        dTemp = {}
        for xmlVar in self._xmlRoot.find("BODY").findall("VARIABLE"):

            varTemp = Variable(sName=xmlVar.attrib["name"],
                               sFunction=xmlVar.find("FUNCTION").text.strip(),
                               sModule=self.NAME,
                               sProduct=xmlVar.find("PRODUCT").text if xmlVar.find(
                                   "PRODUCT") != None else"",
                               sAccumulation=xmlVar.find("ACCUMULATION").text if xmlVar.find("ACCUMULATION") != None else"")
            dTemp[varTemp.sName] = varTemp
        self.BODY = dTemp
        self.dVariables = self.BODY
        return self.BODY
