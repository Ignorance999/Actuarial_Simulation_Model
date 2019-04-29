# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:33:14 2019

@author: User
"""
import sys,os
import mUtils
from mGenTable import GenTable

class KeyGenTable(GenTable):
    """
    This class will only allow one pre-determined key column for the table.
    """    
    def __init__(self,sRestriction=None,*args,**kwargs): 
		
		#sTableDir=".",        
        #super().__init__(self,sTableName=sTableName)
          
        super().__init__(*args,**kwargs)
        self._sRestriction=sRestriction
        #self.fSetRestriction(sRestriction)
    
    #def fSetRestriction(self,sRestriction=None):
    #    self.sRestriction=sRestriction
        #TODO: self.keycols cannot be 0, show this checking in mGenTable
        #TODO: KEYCOLS should not have repeated values, should check this
        if len(self.KEYCOLS)>1 or (self._sRestriction!=None and self.KEYCOLS[0]!=self._sRestriction):            
            raise Exception("KeyGenTable's self._srestriction is not equal to KEYCOLS")
    
    def fReadTable(self,Key,sColName):
        """
        self.BODY is a dict, generated from inherited self._fXMLReadBody
        :param Key: can be a string or a tuple containing a single element.
        :param sColName: The name of the value you are looking for.
        :return: the corresponding value in the lookup table
        """  
        if type(Key)=="str":
            Key=tuple(Key)
        return self.BODY[Key][sColName]
