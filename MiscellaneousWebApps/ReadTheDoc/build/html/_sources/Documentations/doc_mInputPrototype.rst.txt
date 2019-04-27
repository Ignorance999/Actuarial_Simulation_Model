doc_mInputPrototype
===================

Documentation
*************
1. Brief Explanation of InputPrototype
	1. This class is the abstract parent class for all Tables and Scripts.
	2. It will read XML files. These XML files are source files containing assumptions and records of the model.
2. List of Member Variables and Methods
	0. How to Create a class instance
	
		>>> i=InputPrototype()
		
	1. Functions
		1. __init__(self,sFilePath=".\\test_input\\Table.txt")
		
			>>> i.__dict__
			{'_pThisModuleDir': None,
			 '_pFilePath': WindowsPath('test_input/Table.txt'),
			 '_xmlRoot': <Element 'ROOT' at 0x0000000009D9F638>,
			 'CLASS_TYPE': 'GenTable',
			 'NAME': 'oneguffy',
			 'FEATURES': [''],
			 'KEYCOLS': ['SONE', 'SSECOND'],
			 'HEADINGS': ['SONE', 'SSECOND', 'STHIRD'],
			 'TYPE': ['int', 'str', 'float'],
			 'BODY': None}
			>>> i._xmlRoot
			<Element 'ROOT' at 0x0000000009D9F638>
			>>> [j for j in i._xmlRoot]
			[<Element 'CLASS_TYPE' at 0x0000000009D9F688>,
			 <Element 'NAME' at 0x0000000009D9F6D8>,
			 <Element 'FEATURES' at 0x0000000009D9F728>,
			 <Element 'KEYCOLS' at 0x0000000009D9F778>,
			 <Element 'HEADINGS' at 0x0000000009D9F7C8>,
			 <Element 'TYPE' at 0x0000000009D9F818>,
			 <Element 'BODY' at 0x0000000009D9F868>]
			 
		2. _fXMLFindChildOutputList(self,sChildName,sType="str", bIsArray=True, #xmlRoot=None,
                            sStripChars=r"\s+",sSplitChars=",")			
			
			>>> bIsArray=[]
			>>>	for xmlChild in i._xmlRoot:
			>>>		if xmlChild.tag != "BODY":
			>>>			if "is_array" in xmlChild.attrib:
			>>>				bIsArray=False if (xmlChild.attrib["is_array"].lower()=="false") else True
			>>>			else:
			>>>				bIsArray=True
			>>>		bIsArray.append(bIsArray)
			>>>	bIsArray
			[False, False, True, True, True, True, True]
			>>> [j for j in i._xmlRoot][0].attrib["type"]
			'str'
	
		3. _fXMLReadBody(self)
		4. __str__(self)
		5. fcGetClassType(cls,sFilePath=".\\Table.txt")
			This is a class method. 
	2. Variables
		1. self._pThisModuleDir
		2. self._pFilePath
		3. self._xmlRoot
		4. self.BODY 			
3. Related Document
	Sample Code for Table.txt
	
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



	
	
	
	
	
	
