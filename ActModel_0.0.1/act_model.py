# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:39:33 2019

@author: User
"""
import mInput
import mOutput
import mProcess
class ActModel:    
    def __init__(self):
        self._Input=mInput.Input()
        self._Output=mOutput.Output()
        self._Process=mProcess.Process()
        print(self._Input.__dict__)
    
    
    