# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:39:33 2019

@author: User
"""
from input import Input
from output import Output
from process import Process


class ActModel:
    def __init__(self):
        self._Input = Input()
        self._Output = Output()
        self._Process = Process()
        print(self._Input.__dict__)
