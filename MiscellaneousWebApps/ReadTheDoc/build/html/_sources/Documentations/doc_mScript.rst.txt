doc_mScript
=============

Documentation
*************
1. Brief Explanation of Script
	1. This class is inherited from InputPrototype
	2. It will read XML script files. The XML files contain variables that are components of models.
	3. Other comments:
	
	These scripts (eg .\script\ Script2.txt) containing definitions for different functions that will dependent on each other. Each variable in the script will be stored as a Variable class instance.
	

2. List of Member Variables and Methods
	0. How to Create a class instance
	
		>>> s=Script(sFilePath=".\\script\\Script2.txt")
		
	1. Functions
		1. __init__(self,*args,**kwargs)
		
			>>> s.__dict__
			{'dVariables': {'aa': <mVariable.Variable at 0xa201470>,
			  'bb': <mVariable.Variable at 0xa201668>,
			  'CC': <mVariable.Variable at 0xa2017b8>},
			 '_pThisModuleDir': WindowsPath('C:/Users/User/Documents/ACT/ActModel/ActModel_Current'),
			 '_pFilePath': WindowsPath('script/Script2.txt'),
			 '_xmlRoot': <Element 'ROOT' at 0x000000000A1DDE58>,
			 'CLASS_TYPE': 'Script',
			 'NAME': 'oneguy',
			 'FEATURES': [''],
			 'BODY': {'aa': <mVariable.Variable at 0xa201470>,
			  'bb': <mVariable.Variable at 0xa201668>,
			  'CC': <mVariable.Variable at 0xa2017b8>}}
			 
		2. _fXMLFindChildOutputList(self,sChildName,sType="str", bIsArray=True, #xmlRoot=None,
                            sStripChars=r"\s+",sSplitChars=",")
			
			Inherited
			
		3. _fXMLReadBody(self)
			
			>>> s._fXMLReadBody()
			{'aa': <mVariable.Variable at 0xa2073c8>,
			'bb': <mVariable.Variable at 0xa207400>,
			'CC': <mVariable.Variable at 0xa207438>}
		
		... and other functions
		
	2. Variables
		1. self._pThisModuleDir
		2. self._pFilePath
		3. self._xmlRoot
		4. self.BODY 	
		
3. Related Document
	Sample Code for Script2.txt
	
	.. code-block:: xml	
		<?xml version="1.0"?>
		<ROOT>
			<CLASS_TYPE type="str" is_array="false">Script</CLASS_TYPE>
			<NAME type="str" is_array="false">oneguy</NAME>
			<FEATURES type="str">
			</FEATURES>
			<BODY>
				<VARIABLE name="aa">
					<PRODUCT>PROD1</PRODUCT>
					<ACCUMULATION>ACC1</ACCUMULATION>
					<FUNCTION>
					def aa(t):
						return t
					</FUNCTION>
				</VARIABLE>
				<VARIABLE name="bb">
					<PRODUCT>PROD2</PRODUCT>
					<ACCUMULATION>ALL</ACCUMULATION>
					<FUNCTION>
					def bb(t,k):
						return aa(t)*k
					</FUNCTION>
				</VARIABLE>
				<VARIABLE name="CC">
					<PRODUCT>PROD2,PROD3</PRODUCT>
					<FUNCTION>
					def CC():
						return aa(1)+1
					</FUNCTION>
				</VARIABLE>
			</BODY>
		</ROOT>





	
	
	
	
	
	
