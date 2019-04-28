# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 12:40:33 2019

@author: User
"""
from mResultBlock import ResultBlock 
import mUtils
import re
import pandas
class Output():
    """

    """
    def __init__(self,inputTemp,globalsettingsTemp):
        self._Input=inputTemp
        self._GlobalSettings=globalsettingsTemp
        self._OutputFormatTable=mUtils.fGetFirstElementOrderedDict(self._Input.dAllInputs["OutputFormatTable"])
        self.ddReports={}#key is outputformat names
        for s in self._OutputFormatTable.odOutputFormats.keys():
            self.ddReports[s]={}
        #key is range tuple
        
    def fRecordPolResults(self,varTemp,odCURR_OUTPUT_FORMAT_RAW_CHECK):
        """

        :param varTemp:
        :param odCURR_OUTPUT_FORMAT_RAW_CHECK:
        :return:
        """
        tFuncArgs=tuple(varTemp.lsFuncArgs)
        
        #for skey,dCURR_OUTPUT_FORMAT_RAW in odCURR_OUTPUT_FORMAT_RAW_CHECK:
            
        #odCURR_OUTPUT_FORMAT_CHECK
        for sKey,dResultBlocks in self.ddReports.items():  
            if tFuncArgs not in dResultBlocks.keys():
                dResultBlocks[tFuncArgs]=ResultBlock(list(self._OutputFormatTable.odOutputFormats[sKey]),
                                                        list(varTemp._dCache.keys()),varTemp.lsFuncArgs)
            dResultBlocks[tFuncArgs].fAddColumn(varTemp,
                                 self._OutputFormatTable.fodOutputFormatsFromRawToCooked(odCURR_OUTPUT_FORMAT_RAW_CHECK)[sKey])     
            
        
    def fPrintReport(self,sOutputFormat):
        """

        :param sOutputFormat:
        :return:
        """
        #for sKey,dResultBlocks in self.ddReports.items():
        writer=pandas.ExcelWriter(sOutputFormat+".xlsx")
        for resultblockTemp in self.ddReports[sOutputFormat].values():
            resultblockTemp.fdfResultsIndToStr().to_excel(writer,sheet_name=re.sub("[\[\]]","#",str(resultblockTemp.lsRangeIndNames)))
        writer.save()
        
    def fPrintAllReports(self):
        for sKey in self.ddReports.keys():
            self.fPrintReport(sKey)
            