"""
Created on Sat Mar 16 12:40:33 2019

@author: User
"""
from result_block import ResultBlock
from utils import fGetFirstElementOrderedDict
import re
import pandas


class Output():
    """
        This class controls the output of the model. It contains ResultBlocks, which are multi-dimensional dataframes. It also can print results into excel files.
    """

    def __init__(self, inputTemp, globalsettingsTemp):
        self._Input = inputTemp
        self._GlobalSettings = globalsettingsTemp
        self._OutputFormatTable = fGetFirstElementOrderedDict(
            self._Input.dAllInputs["OutputFormatTable"])
        self.ddReports = {}  # key is outputformat names
        for s in self._OutputFormatTable.odOutputFormats.keys():
            self.ddReports[s] = {}
        # key is range tuple

    def fRecordPolResults(self, varTemp, odCURR_OUTPUT_FORMAT_RAW_CHECK):
        """
                Called from mVarNameSpace.fRunModel. Use ResultBlocks to record the results of the model.
        :param varTemp:
        :param odCURR_OUTPUT_FORMAT_RAW_CHECK:
        :return:
        """
        tFuncArgs = tuple(varTemp.lsFuncArgs)

        for sKey, dResultBlocks in self.ddReports.items():
            if tFuncArgs not in dResultBlocks.keys():
                dResultBlocks[tFuncArgs] = ResultBlock(list(self._OutputFormatTable.odOutputFormats[sKey]),
                                                       list(varTemp._dCache.keys()), varTemp.lsFuncArgs)
            dResultBlocks[tFuncArgs].fAddColumn(varTemp,
                                                self._OutputFormatTable.fodOutputFormatsFromRawToCooked(odCURR_OUTPUT_FORMAT_RAW_CHECK)[sKey])

    def fPrintReport(self, sOutputFormat):
        """
                Generate excel files from ResultBlocks
        :param sOutputFormat:
        :return:
        """
        writer = pandas.ExcelWriter(sOutputFormat+".xlsx")
        for resultblockTemp in self.ddReports[sOutputFormat].values():
            resultblockTemp.fdfResultsIndToStr().to_excel(writer, sheet_name=re.sub(
                "[\[\]]", "#", str(resultblockTemp.lsRangeIndNames)))
        writer.save()

    def fPrintAllReports(self):
        for sKey in self.ddReports.keys():
            self.fPrintReport(sKey)
