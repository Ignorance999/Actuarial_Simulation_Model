"""
Created on Sat Mar 16 12:40:33 2019

@author: User
"""

from table import Table
from MPF_table import MPFTable
from gen_table import GenTable
from keygen_table import KeyGenTable
from script import Script
from accum_table import AccumTable
from report_var_table import ReportVarTable
from output_format_table import OutputFormatTable
from pathlib import Path
from collections import OrderedDict
import directories as dirs
import os


class Input():
    """
        This class will manage all the inputs. It contains all the Tables and Scripts. During its initilization, these Tables and Scripts are loaded.
    """

    # do not count key gen tables as their unique property
    lscMultiInputTypes = ["MPFTable", "GenTable", "Script"]
    lscSingleInputTypes = ["AccumTable", "ReportVarTable", "OutputFormatTable"]
    dscRestrictionsToKeyGen = {"ProdTable": "PRODUCT",
                               "ScenTable": "SCEN_ID",
                               "GlobalTable": "RUN_NUM"}

    def __init__(self, dsMultiInputDirs={"GenTable": dirs.test_input_dir,
                                         "MPFTable": dirs.mpf_dir,
                                         "Script": dirs.script_dir},
                 dsSingleInputDirs={"AccumTable": dirs.test_output_dir,
                                    "ReportVarTable": dirs.report_var_test_path,
                                    "OutputFormatTable": dirs.output_format_test_path},  # "KeyGenTable":".\\Prod\\"
                 dsKeyGenTablesDirs={
                 "ProdTable": dirs.prod_table_path,
                 "ScenTable": dirs.scen_table_path,
                 "GlobalTable": dirs.global_table_path}):
        """

        :param dsMultiInputDirs:
        :param dsSingleInputDirs:
        :param dsKeyGenTablesDirs:
        """
        try:
            self._pThisModuleDir = Path(__file__).parent
        except NameError:
            #Console Mode
            self._pThisModuleDir=None

        dsAllInputsDirs={**dsMultiInputDirs,**dsSingleInputDirs}
        self._dpAllInputsDirs={sKey:Path(sVal) for sKey,sVal in dsAllInputsDirs.items()}
        self._dpKeyGenTablesDirs={sKey:Path(sVal) for sKey,sVal in dsKeyGenTablesDirs.items()}
       # self._pMPFTableDir=Path(sMPFTableDir)
       # self._pScriptDir=Path(sScriptDir)
        self.dAllInputs={}
        for sInputType in Input.lscMultiInputTypes:
            self.dAllInputs[sInputType] = self.fodLoadAllInputs(
                sInputType, str(self._dpAllInputsDirs[sInputType]))

        self.dKeyGenTables = {}

        for sName in dsKeyGenTablesDirs.keys():
            odTemp = self.fodLoadAllInputs("KeyGenTable",
                                           str(self._dpKeyGenTablesDirs[sName]),
                                           bIfOnlyOneFile=True,
                                           sRestriction=Input.dscRestrictionsToKeyGen[sName])
            self.dKeyGenTables[sName] = list(odTemp.values())[0]
        self.dAllInputs["KeyGenTable"] = self.dKeyGenTables

        for sInputType in Input.lscSingleInputTypes:
            self.dAllInputs[sInputType] = self.fodLoadAllInputs(sInputType,
                                                                str(
                                                                    self._dpAllInputsDirs[sInputType]),
                                                                bIfOnlyOneFile=True)

        self.diCurrInput = {}
        for sInputType in Input.lscMultiInputTypes:
            self.diCurrInput[sInputType] = -1

    def fodLoadAllInputs(self, sInputType, sAllInputDir, bIfOnlyOneFile=False, *args_to_input, **kwargs_to_input) -> OrderedDict:
        """
        Called from __init__. It is to load specified tables/scripts from sAllInputDir
        :param sInputType: the class of the table. e.g. GenTable
        :param sAllInputDir: the file/folder address of the table(s)
        :param bIfOnlyOneFile: if the address of file represents only one XML file.
        :param args_to_input: this argument is transferred to the __init__ function of sInputType class
        :param kwargs_to_input: this argument is transferred to the __init__ function of sInputType class
        :return: odTemp: an OrderedDict containing different instances with the type sInputType
        """
        pAllInputDir = Path(sAllInputDir)

        odTemp = OrderedDict()
        if bIfOnlyOneFile and not sAllInputDir.endswith(".txt"):
            raise Exception("KeyGenTable must has only one instance!")
        txt_pattern = os.path.join(".", "**", "*.txt")
        lpFilePaths = [pAllInputDir] if sAllInputDir.endswith(
            ".txt") else pAllInputDir.glob(txt_pattern)
        for pFilePath in lpFilePaths:
            sTableType = Table.fcGetClassType(str(pFilePath))
            if sTableType == sInputType:
                fTableType = globals()[sInputType]
                tblTemp = fTableType(sFilePath=str(
                    pFilePath), *args_to_input, **kwargs_to_input)
                if tblTemp.NAME not in odTemp:
                    odTemp[tblTemp.NAME] = tblTemp
                else:
                    raise Exception(
                        "Reload files with the same name!:" + str(pFilePath))
            else:
                raise Exception("File Type not correct:" +
                                str(pFilePath)+"\n not equal to:\n "+sInputType)
        return odTemp

    def __str__(self):
        sTemp = ""
        for odTemp in self.dAllInputs.values():
            for tblTemp in odTemp.values():
                sTemp = sTemp+tblTemp.__str__()
        return sTemp

    # not yet finished

    def fd_sNextInput(self, sInputType):
        self.diCurrInput[sInputType] = self.diCurrInput[sInputType]+1
        return self.fd_sCurrInput(sInputType)

    def fd_sCurrInput(self, sInputType):
        i = self.diCurrInput[sInputType]
        if i >= 0 and i <= len(self.dAllInputs[sInputType])-1:
            return list(self.dAllInputs[sInputType].values())[i]
        else:
            self.diCurrInput[sInputType] = -1
            return "EOF"

    def fd_sNextMPFRow(self):
        """
        move the pointer of policy records to next record (controlled by diCurrInput["MPFTable"] and mpfCurr.fd_sNextMPFRow())
        :param self:
        :return: a dictionary representing a policy record
        """
        if self.diCurrInput["MPFTable"] == -1:
            mpfCurr = self.fd_sNextInput("MPFTable")
        else:
            mpfCurr = self.fd_sCurrInput("MPFTable")
        d_sResultTemp = mpfCurr.fd_sNextMPFRow()
        if d_sResultTemp == "EOF":
            if self.fd_sNextInput("MPFTable") == "EOF":
                return "EOF"
            else:
                return self.fd_sNextMPFRow()
        else:
            return d_sResultTemp

    def fd_sCurrMPFRow(self):
        return self.fd_sCurrInput("MPFTable").fd_sCurrMPFRow() if self.fd_sCurrInput("MPFTable") != "EOF" else "EOF"