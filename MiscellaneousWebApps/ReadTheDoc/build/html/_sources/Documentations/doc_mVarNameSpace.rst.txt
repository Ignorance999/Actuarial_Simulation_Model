doc_mVarNameSpace
=============

Documentation
*************
1. Brief Explanation of VarNameSpace
	1. It is created from Process instance
	2. It is a Module
	3. Other comments:
	
	This module is the namespace for model calculation. Variables, Input, GlobalSettings and Output class instances will be loaded here for running the model. It will also generate the results and pass them to Output.
	
2. List of Variables and Methods contained in this module
	0. How to Create a class instance
	
		>>> p=Process() 
		>>> vn=p.mVarNameSpace
		
	1. Functions
		1. __init__(self,sName="",sFunction="",sModule="",sProduct="",sAccumulation="")
		
		>>> vn.__dict__
		... Omit many useless lines
		'fdecCreateVariable': <function mUtils.fdecCreateVariable(fInput)>,
		'mUtils': <module 'mUtils' from 'C:\\Users\\User\\Documents\\ACT\\ActModel\\ActModel_Curr\\mUtils.py'>,
		'INPUT': <__main__.Input at 0xa013940>,
		'GLOBAL_SETTINGS': <mGlobalSettings.GlobalSettings at 0xa029ef0>,
		'OUTPUT': <mOutput.Output at 0xa02ef98>,
		'fRunModel': <function mVarNameSpace.fRunModel()>,
		'odCURR_OUTPUT_FORMAT_RAW_CHECK': <mVariable.Variable at 0x9f6f6d8>,
		'dCURR_POLICY': <mVariable.Variable at 0x9f6f630>,
		'sCURR_PRODUCT': <mVariable.Variable at 0x9f6f358>,
		'dNEXT_POLICY': <mVariable.Variable at 0x9f6f710>,
		'aa1': <mVariable.Variable at 0xa021550>,
		'bb1': <mVariable.Variable at 0xa021cc0>,
		'aa': <mVariable.Variable at 0xa029320>,
		'bb': <mVariable.Variable at 0xa029518>,
		'CC': <mVariable.Variable at 0xa029668>,
		'bTemp': <mVariable.Variable at 0xa029860>,
		'bTemp2': <mVariable.Variable at 0xa029cc0>}
					 
		2. dCURR_POLICY()
		
		>>> vn.dCURR_POLICY()
		'EOF'
			
		3. sCURR_PRODUCT()
		
		>>> vn.sCURR_PRODUCT()
		'EOF'
		
		4. dNEXT_POLICY()
		
		>>> vn.dNEXT_POLICY()
		{'SONE': 'PRODuu1', 'PRODUCT': 'PROD1', 'STHIRD': 3}
		>>> vn.dNEXT_POLICY()
		{'SONE': 'PROD2', 'PRODUCT': 'PROD2', 'STHIRD': 1}
		
		5. odCURR_OUTPUT_FORMAT_RAW_CHECK()
		
		>>> vn.odCURR_OUTPUT_FORMAT_RAW_CHECK()
		OrderedDict([('one',
              {('first', 'ACCUMULATION', 'ACC1'): False,
               ('first', 'PRODUCT', 'PROD2'): True,
               ('second', 'CRITERIA', 'bTemp'): True}),
             ('second',
              {('first', 'ACCUMULATION', 'ACC1'): False,
               ('first', 'PRODUCT', 'PROD2'): True,
               ('second', 'CRITERIA', 'bTemp'): True})])
			   
		6. fRunModel()
		
		>>> odVarRanges = vn.GLOBAL_SETTINGS.odDimVarRanges
		>>> odVarRanges
		OrderedDict([('t', range(0, 100)), ('k', range(3, 500)), ('s', range(4, 6))])
		>>> lsVars = vn.GLOBAL_SETTINGS.odReportVars["ok"]
		>>> lsVars
		vn.GLOBAL_SETTINGS.odReportVars["ok"]
		['aa', 'bb', 'CC']
		>>> vn.dNEXT_POLICY()
		{'SONE': 'PROD1', 'PRODUCT': 'PROD1', 'STHIRD': 1} # the third record is shown because the first 2 are already shown during testing of dNEXT_POLICY()
		>>> odTemps=[OrderedDict({sKey: odVarRanges[sKey] for sKey in vn.__dict__[sVar].lsFuncArgs}) for sVar in lsVars]
		>>> odTemps
		[OrderedDict([('t', range(0, 100))]),
		 OrderedDict([('t', range(0, 100)), ('k', range(3, 500))]),
		 OrderedDict()]
		>>> odTemp=odTemp[0]
		>>> from itertools import product as cartesian_product
		>>> lDimVarsAllProds = list(cartesian_product(
            *[autoTemp for autoTemp in odTemp.values()]))
		>>> lDimVarsAllProds
		[(0,),
		 (1,),
		 (2,),
		 (3,),
		 ...many outputs
		 (93,),
		 (94,),
		 (95,),
		 (96,),
		 (97,),
		 (98,),
		 (99,)]
		>>> dArgs = {}
		>>> for tTemp in lDimVarsAllProds:
				for iInd, sArg in enumerate(odTemp.keys()):
					dArgs[sArg] = tTemp[iInd]
		>>> dArgs
		{'t': 99}
		
		... and other functions
		
	2. Variables

		
3. Related Document





	
	
	
	
	
	
