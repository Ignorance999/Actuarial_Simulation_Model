doc_mReportVarTable
=============

Documentation
*************
1. Brief Explanation of ReportVarTable
	1. This class reads data from XML files. It contains several groups of variables. 
	
2. List of Member Variables and Methods
	0. How to Create a class instance
	
		>>> r=ReportVarTable(".\\test_output\\REPORTVAR.txt")
		
	1. Functions
		1. __init__(self,*args,**kwargs)
		
			>>> r.__dict__
			{'odReportVars': OrderedDict([('ok', ['aa', 'bb', 'CC'])]),
			 '_pThisModuleDir': WindowsPath('C:/Users/User/Documents/ACT/ActModel/ActModel_Curr'),
			 '_pFilePath': WindowsPath('test_output/REPORTVAR.txt'),
			 '_xmlRoot': <Element 'ROOT' at 0x000000000A0E6D18>,
			 'CLASS_TYPE': 'ReportVarTable',
			 'NAME': 'report1',
			 'BODY': OrderedDict([('ok', ['aa', 'bb', 'CC'])])}

			
		3. _fXMLReadBody(self)
			
			
		
		... and other functions
		
	2. Variables
		1. self._pThisModuleDir
		2. self._pFilePath
		3. self._xmlRoot
		4. self.BODY 	
		5. self.odReportVars #ALIAS FOR self.BODY
		
3. Related Document
	Sample Code for .\\test_output\\REPORTVAR.txt
	
	.. code-block:: xml	
	
		<?xml version="1.0"?>
		<ROOT>
			<CLASS_TYPE type="str" is_array="false">ReportVarTable</CLASS_TYPE>
			<NAME type="str" is_array="false">report1</NAME>
			<BODY>
				<REPORT_VARS name="ok">
					aa,bb,CC
				</REPORT_VARS>
			</BODY>
		</ROOT>





	
	
	
	
	
	
