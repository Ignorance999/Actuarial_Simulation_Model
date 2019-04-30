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


class Table(InputPrototype):
	"""
	Base Class for all Tables
	"""