doc_mGenTable
===================

Documentation
*************
1. Brief Explanation of GenTable
	1. This class is inherited from Table
	2. It will read XML lookup files. 
	3. Other comments
	This name is from my software, which may be changed in the future. It will read XML in “test_input” folder. Currently, it will recognize those columns that can be regarded as “keys” and other columns as “values”. The “BODY” member is a dictionary. I am thinking of changing this self.BODY to pandas.dataframe instead.
	
2. List of Member Variables and Methods
	0. How to Create a class instance
	
		>>> g=GenTable()
		
	1. Functions
		1. __init__(self,*args,**kwargs)
		
			>>> g.__dict__
			{'_pThisModuleDir': WindowsPath('C:/Users/User/Documents/ACT/ActModel/ActModel_Current'),
			 '_pFilePath': WindowsPath('test_input/Table.txt'),
			 '_xmlRoot': <Element 'ROOT' at 0x0000000009EA96D8>,
			 'CLASS_TYPE': 'GenTable',
			 'NAME': 'oneguffy',
			 'FEATURES': [''],
			 'KEYCOLS': ['SONE', 'SSECOND'],
			 'HEADINGS': ['SONE', 'SSECOND', 'STHIRD'],
			 'TYPE': ['int', 'str', 'float'],
			 'BODY': {(1, 'H'): {'STHIRD': 3.0},
			  (3, 'F'): {'STHIRD': 1.0},
			  (4, 'D'): {'STHIRD': 1.0}}}
			>>> g._xmlRoot
			<Element 'ROOT' at 0x0000000009EA96D8>
			>>> [j for j in g._xmlRoot]
			[<Element 'CLASS_TYPE' at 0x0000000009EB8458>,
			 <Element 'NAME' at 0x0000000009EB8548>,
			 <Element 'FEATURES' at 0x0000000009EB8598>,
			 <Element 'KEYCOLS' at 0x0000000009EB85E8>,
			 <Element 'HEADINGS' at 0x0000000009EB8638>,
			 <Element 'TYPE' at 0x0000000009EB8688>,
			 <Element 'BODY' at 0x0000000009EB86D8>]
			 
		2. _fXMLFindChildOutputList(self,sChildName,sType="str", bIsArray=True, #xmlRoot=None,
                            sStripChars=r"\s+",sSplitChars=",")
			Inherited
			
		3. _fXMLReadBody(self)
			
			>>> g._fXMLReadBody()
			{(1, 'H'): {'STHIRD': 3.0},
			 (3, 'F'): {'STHIRD': 1.0},
			 (4, 'D'): {'STHIRD': 1.0}}
			>>> lsBody=g._fXMLFindChildOutputList(sChildName="BODY",
                           sStripChars=r"[ \t]+",sSplitChars="\n")
			>>> lsBody
			['', '1,H,3', '3,F,1', '4,D,1', '']
		
		4. flGetEntireColumn(self,sColName)
			
			>>> g.flGetEntireColumn("SONE")
			[1, 3, 4]
		
		5. fReadTable(self,Key,sColName)
		6. flAllKeys(self,bAutoSimplify=True)
		
			>>> g.flAllKeys()
			[(1, 'H'), (3, 'F'), (4, 'D')]
			
			If bAutoSimplify is True and there are only one KEYCOLS, then the elements of the list returned by flAllKeys() will not be tuples. For the current case shown, the keys are tuples.

	2. Variables
		1. self._pThisModuleDir
		2. self._pFilePath
		3. self._xmlRoot
		4. self.BODY 			
3. Related Document
	Sample Code for Table.txt(same as that related to mInputPrototype)
	
	.. code-block:: xml	
	
		<?xml version="1.0"?>
		<ROOT>
			<CLASS_TYPE type="str" is_array="false">GenTable</CLASS_TYPE>
			<NAME type="str" is_array="false">oneguffy</NAME>
			<FEATURES type="str">
			</FEATURES>
			<KEYCOLS type="str">
			SONE,SSECOND
			</KEYCOLS>
			<HEADINGS type="str">
			SONE,SSECOND,STHIRD
			</HEADINGS>
			<TYPE type="str">
			int,str,float
			</TYPE>
			<BODY>
			1,H,3
			3,F,1
			4,D,1
			</BODY>
		</ROOT>



	
	
	
	
	
	
