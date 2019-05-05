doc_mInput
=============

Documentation
*************
1. Brief Explanation of Input
	1. Created by Process instance
	2. Other comments:
	
	This class will manage all the inputs. It contains all the Tables and Scripts. During its initilization, these Tables and Scripts are loaded.

2. List of Member Variables and Methods
	0. How to Create a class instance
	
		>>> i=Input()	
		
	1. Functions
		1. __init__(self,dsMultiInputDirs={"GenTable":".\\test_input\\"........

		
			>>> import pprint
			>>> pprint.pprint(i.__dict__)
			{'_dpAllInputsDirs': {'AccumTable': WindowsPath('test_output/accum.txt'),
						  'GenTable': WindowsPath('test_input'),
						  'MPFTable': WindowsPath('MPF'),
						  'OutputFormatTable': WindowsPath('test_output/out1.txt'),
						  'ReportVarTable': WindowsPath('test_output/REPORTVAR.txt'),
						  'Script': WindowsPath('script')},
			 '_dpKeyGenTablesDirs': {'GlobalTable': WindowsPath('Prod/GLOBAL.txt'),
									 'ProdTable': WindowsPath('Prod/PROD.txt'),
									 'ScenTable': WindowsPath('Prod/scen.txt')},
			 '_pThisModuleDir': None,
			 'dAllInputs': {'AccumTable': OrderedDict([('Accum1',
														<mAccumTable.AccumTable object at 0x0000000009F48C18>)]),
							'GenTable': OrderedDict([('oneguy',
													  <mGenTable.GenTable object at 0x0000000009F29DA0>),
													 ('oneguffy',
													  <mGenTable.GenTable object at 0x0000000009F34EF0>)]),
							'KeyGenTable': {'GlobalTable': <mKeyGenTable.KeyGenTable object at 0x0000000009F48C88>,
											'ProdTable': <mKeyGenTable.KeyGenTable object at 0x0000000009F34DD8>,
											'ScenTable': <mKeyGenTable.KeyGenTable object at 0x0000000009F29978>},
							'MPFTable': OrderedDict([('MPFguy',
													  <mMPFTable.MPFTable object at 0x0000000009F29E80>),
													 ('MPFgu3y',
													  <mMPFTable.MPFTable object at 0x0000000009F29F28>)]),
							'OutputFormatTable': OrderedDict([('out1',
															   <mOutputFormatTable.OutputFormatTable object at 0x0000000009F47BA8>)]),
							'ReportVarTable': OrderedDict([('report1',
															<mReportVarTable.ReportVarTable object at 0x0000000009F477B8>)]),
							'Script': OrderedDict([('oneguy333',
													<mScript.Script object at 0x0000000009F29B00>),
												   ('oneguy',
													<mScript.Script object at 0x0000000009F3B588>),
												   ('OUTPUT_CRITERIA',
													<mScript.Script object at 0x0000000009F3BE10>)])},
			 'dKeyGenTables': {'GlobalTable': <mKeyGenTable.KeyGenTable object at 0x0000000009F48C88>,
							   'ProdTable': <mKeyGenTable.KeyGenTable object at 0x0000000009F34DD8>,
							   'ScenTable': <mKeyGenTable.KeyGenTable object at 0x0000000009F29978>},
			 'diCurrInput': {'GenTable': -1, 'MPFTable': -1, 'Script': -1}}
			 
		2. fd_sCurrInput(self,sInputType)
		
			>>> i.lscMultiInputTypes
			['MPFTable', 'GenTable', 'Script']
			>>> [i.fd_sCurrInput(s) for s in i.lscMultiInputTypes]
			['EOF', 'EOF', 'EOF']
			
		3. fd_sNextInput(self,sInputType)
		
			>>> [i.fd_sNextInput(s) for s in i.lscMultiInputTypes]
			[<mMPFTable.MPFTable at 0x9f929e8>,
			 <mGenTable.GenTable at 0x9f92dd8>,
			 <mScript.Script at 0x9f92e10>] 		
		
		4. fd_sCurrMPFRow(self)
		
			>>> i=Input() #reset everything
			>>> i.fd_sCurrMPFRow()
			'EOF'
			
		5. fd_sNextMPFRow(self)
		
			>>> i.fd_sNextMPFRow()
			{'SONE': 'PRODuu1', 'PRODUCT': 'PROD1', 'STHIRD': 3}
			>>> i.fd_sNextMPFRow()
			{'SONE': 'PROD2', 'PRODUCT': 'PROD2', 'STHIRD': 1}
			>>> i.fd_sNextMPFRow()
			{'SONE': 'PROD1', 'PRODUCT': 'PROD1', 'STHIRD': 1}
			>>> i.fd_sNextMPFRow()
			{'SONE': 11, 'SSECOND': 'H1', 'STHIRD': 31}
			>>> i.fd_sNextMPFRow()
			{'SONE': 31, 'SSECOND': 'F1', 'STHIRD': 11}
			>>> i.fd_sNextMPFRow()
			{'SONE': 41, 'SSECOND': 'D1', 'STHIRD': 11}
			>>> i.fd_sNextMPFRow()
			'EOF'
			
			
	2. Variables

		
3. Related Document






	
	
	
	
	
	
