doc_mMPFTable
=============

Documentation
*************
1. Brief Explanation of MPFTable
	1. This class is inherited from Table
	2. It will read XML record files. The XML files contain information for each insurance policy and asset.
	3. Other comments:
	
	It does not have key column. Basically, each row is a record for one policy. MPF stands for model point file, which is an actuarial language for “records for customers”. So in real life, you may expect there are more than 10000 rows of records, containing information different policies. There maybe more than 1 MPFTable read by the model, as these MPF Tables may be classified by different products.
	
	Currently, self.BODY is a pandas.dataframe

2. List of Member Variables and Methods
	0. How to Create a class instance
	
		>>> m=MPFTable(sFilePath=".\\MPF\\MPF(2).txt")
		
	1. Functions
		1. __init__(self,*args,**kwargs)
		
			>>> m.__dict__
			{'_pThisModuleDir': WindowsPath('C:/Users/User/Documents/ACT/ActModel/ActModel_Current'),
			 '_pFilePath': WindowsPath('MPF/MPF(2).txt'),
			 '_xmlRoot': <Element 'ROOT' at 0x000000000A1C72C8>,
			 'CLASS_TYPE': 'MPFTable',
			 'NAME': 'MPFguy',
			 'FEATURES': [''],
			 'HEADINGS': ['SONE', 'PRODUCT', 'STHIRD'],
			 'PRODUCT': 'ALL',
			 'TYPE': ['int', 'str', 'float'],
			 'BODY':       SONE PRODUCT  STHIRD
			 0  PRODuu1   PROD1       3
			 1    PROD2   PROD2       1
			 2    PROD1   PROD1       1,
			 'iCurrMPFRowIndex': -1}
			 
		2. _fXMLFindChildOutputList(self,sChildName,sType="str", bIsArray=True, #xmlRoot=None,
                            sStripChars=r"\s+",sSplitChars=",")
			
			Inherited
			
		3. _fXMLReadBody(self)
			
			>>> re.sub(r"\t+","",m._xmlRoot.find("BODY").text).strip()
			'PRODuu1,PROD1,3\nPROD2,PROD2,1\nPROD1,PROD1,1'
			>>> m._fXMLReadBody()
			      SONE PRODUCT  STHIRD
			0  PRODuu1   PROD1       3
			1    PROD2   PROD2       1
			2    PROD1   PROD1       1
		
		4. fd_sNextMPFRow(self)
		5. fd_sCurrMPFRow(self)
			>>> m.iCurrMPFRowIndex
			-1		
			>>> m.fd_sCurrMPFRow()
			'EOF'
			>>> m.fd_sNextMPFRow()
			{'SONE': 'PRODuu1', 'PRODUCT': 'PROD1', 'STHIRD': 3}
			>>> m.fd_sCurrMPFRow()
			{'SONE': 'PRODuu1', 'PRODUCT': 'PROD1', 'STHIRD': 3}
			>>> m.iCurrMPFRowIndex
			0
			>>> m.fd_sNextMPFRow()
			{'SONE': 'PROD2', 'PRODUCT': 'PROD2', 'STHIRD': 1}
			>>> m.iCurrMPFRowIndex
			1
			
		
		... and other functions
		
	2. Variables
		1. self._pThisModuleDir
		2. self._pFilePath
		3. self._xmlRoot
		4. self.BODY 	
		5. self.iCurrMPFRowIndex=-1
		
3. Related Document
	Sample Code for MPF(2).txt
	
	.. code-block:: xml	
	
		<?xml version="1.0"?>
		<ROOT>
			<CLASS_TYPE type="str" is_array="false">MPFTable</CLASS_TYPE>
			<NAME type="str" is_array="false">MPFguy</NAME>
			<FEATURES type="str">
			</FEATURES>
			<HEADINGS type="str">
			SONE,PRODUCT,STHIRD
			</HEADINGS>
			<PRODUCT type="str" is_array="false">ALL</PRODUCT>
			<TYPE type="str">
			int,str,float
			</TYPE>
			<BODY>
			PRODuu1,PROD1,3
			PROD2,PROD2,1
			PROD1,PROD1,1
			</BODY>
		</ROOT>





	
	
	
	
	
	
