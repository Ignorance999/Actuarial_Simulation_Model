# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:33:14 2019

@author: User
"""
from directories import accumm_test_path
from table import Table
'''
        from pathlib import Path
        import xml.etree.ElementTree as xmlET
      import re 
      '''


class AccumTable(Table):
    """
    This class reads data from XML files. It contains several groups of product names. An accumulation means a group of products. 
    """

    def __init__(self, *args, **kwargs):
        self.dAccumulations = {}  # ALIAS FOR SELF.BODY
        super().__init__(*args, **kwargs)

    def _fXMLFindChildOutputList(self, *args, **kwargs):
        return super()._fXMLFindChildOutputList(*args, **kwargs)

    def _fXMLReadBody(self):
        dTemp = {}
        for xmlVar in self._xmlRoot.find("BODY").findall("ACCUMULATION"):
            lAccumVal = xmlVar.text.strip().split(",")
            dTemp[xmlVar.attrib["name"]] = lAccumVal
        self.BODY = dTemp
        self.dAccumulations = self.BODY
        return self.BODY

    def fCheckProdInAccum(self, s_lProd, sAccum):
        lAccum = self.BODY[sAccum]
        if type(s_lProd) == str:
            return s_lProd in lAccum
        elif type(s_lProd) == list:
            return set(s_lProd).issubset(lAccum)
        else:
            raise Exception("Error for AccumTable! s_lProd can only be s or l")
