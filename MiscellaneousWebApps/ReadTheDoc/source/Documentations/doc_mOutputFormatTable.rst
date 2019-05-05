doc_mOutputFormatTable
======================

Documentation
*************
1. Brief Explanation of OutputFormatTable
	1. This class reads data from XML files. It determines the classification of different policies, and how the policies aggregate. The ResultBlock and hence the real outputs will use information from OutputFormatTable.
	
2. List of Member Variables and Methods
	0. How to Create a class instance
	
		>>> of=OutputFormatTable(".\\test_output\\out1.txt")
		
	1. Functions
		1. __init__(self,*args,**kwargs)
		
			>>> of.__dict__
			{'_pThisModuleDir': WindowsPath('C:/Users/User/Documents/ACT/ActModel/ActModel_Curr'),
			 '_pFilePath': WindowsPath('test_output/out1.txt'),
			 '_xmlRoot': <Element 'ROOT' at 0x000000000A0F02C8>,
			 'CLASS_TYPE': 'OutputFormatTable',
			 'NAME': 'out1',
			 'BODY': OrderedDict([('one',
						   [('first', 'ACCUMULATION', 'ACC1'),
							('first', 'PRODUCT', 'PROD2'),
							('second', 'CRITERIA', 'bTemp')]),
						  ('second',
						   [('first', 'ACCUMULATION', 'ACC1'),
							('first', 'PRODUCT', 'PROD2'),
							('second', 'CRITERIA', 'bTemp')])]),
			 'odOutputFormats': OrderedDict([('one',
						   [(('first', 'ACCUMULATION', 'ACC1'),
							 ('second', 'CRITERIA', 'bTemp')),
							(('first', 'PRODUCT', 'PROD2'),
							 ('second', 'CRITERIA', 'bTemp'))]),
						  ('second',
						   [(('first', 'ACCUMULATION', 'ACC1'),
							 ('second', 'CRITERIA', 'bTemp')),
							(('first', 'PRODUCT', 'PROD2'),
							 ('second', 'CRITERIA', 'bTemp'))])]),
			 'odOutputFormatsRaw': OrderedDict([('one',
						   [('first', 'ACCUMULATION', 'ACC1'),
							('first', 'PRODUCT', 'PROD2'),
							('second', 'CRITERIA', 'bTemp')]),
						  ('second',
						   [('first', 'ACCUMULATION', 'ACC1'),
							('first', 'PRODUCT', 'PROD2'),
							('second', 'CRITERIA', 'bTemp')])])}

			
		3. _fXMLReadBody(self)
		
		4. _fCreateOutputFormats(self)
		
		>>> sKey=list(of.BODY.keys())[0]
		'one'
		>>> lTemp=list(of.BODY.values())[0]
		>>> lTemp
		[('first', 'ACCUMULATION', 'ACC1'),
		 ('first', 'PRODUCT', 'PROD2'),
		 ('second', 'CRITERIA', 'bTemp')]
		>>> dDims = {}
			for tTemp in lTemp:
				sDimName = tTemp[0]
				if sDimName in dDims:
					dDims[tTemp[0]].append(tTemp)
				else:
					dDims[tTemp[0]] = [tTemp]
		{'first': [('first', 'ACCUMULATION', 'ACC1'), ('first', 'PRODUCT', 'PROD2')],
		'second': [('second', 'CRITERIA', 'bTemp')]}
		>>> lAllDims = list(cartesian_product(
			*[autoTemp for autoTemp in dDims.values()]))
		[(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
		(('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))]
		>>> of._fCreateOutputFormats()
		OrderedDict([('one',
              [(('first', 'ACCUMULATION', 'ACC1'),
                ('second', 'CRITERIA', 'bTemp')),
               (('first', 'PRODUCT', 'PROD2'),
                ('second', 'CRITERIA', 'bTemp'))]),
             ('second',
              [(('first', 'ACCUMULATION', 'ACC1'),
                ('second', 'CRITERIA', 'bTemp')),
               (('first', 'PRODUCT', 'PROD2'),
                ('second', 'CRITERIA', 'bTemp'))])])
		
		5. fodOutputFormatsFromRawToCooked(self, dCURR_OUTPUT_FORMAT_RAW_CHECK)
		
		>>> p=Process()
		>>> dCURR_OUTPUT_FORMAT_RAW_CHECK=p.mVarNameSpace.odCURR_OUTPUT_FORMAT_RAW_CHECK()
		OrderedDict([('one',
              {('first', 'ACCUMULATION', 'ACC1'): False,
               ('first', 'PRODUCT', 'PROD2'): False,
               ('second', 'CRITERIA', 'bTemp'): True}),
             ('second',
              {('first', 'ACCUMULATION', 'ACC1'): False,
               ('first', 'PRODUCT', 'PROD2'): False,
               ('second', 'CRITERIA', 'bTemp'): True})])
		>>> sKey=list(of.odOutputFormats.keys())[0]
		>>> sKey
		'one'
		>>> lTemp=list(of.odOutputFormats.values())[0]
		>>> lTemp
		[(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
		(('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))]
		>>> dTemp = {}
            for tTemp1 in lTemp:
                bAccumulated = True
                for tTemp2 in tTemp1:
                    bAccumulated = dCURR_OUTPUT_FORMAT_RAW_CHECK[sKey][tTemp2] and bAccumulated
                dTemp[tTemp1] = bAccumulated
		{(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')): False,
		(('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp')): False}
		>>> of.fodOutputFormatsFromRawToCooked(dCURR_OUTPUT_FORMAT_RAW_CHECK)
		{'one': {(('first', 'ACCUMULATION', 'ACC1'),
		   ('second', 'CRITERIA', 'bTemp')): False,
		  (('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp')): False},
		 'second': {(('first', 'ACCUMULATION', 'ACC1'),
		   ('second', 'CRITERIA', 'bTemp')): False,
		  (('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp')): False}}
  
		... and other functions
		
	2. Variables
		1. self._pThisModuleDir
		2. self._pFilePath
		3. self._xmlRoot
		4. self.BODY 
		5. self.odOutputFormats
		5. self.odOutputFormatsRaw #ALIAS FOR self.BODY
		
3. Related Document
	Sample Code for .\\test_output\\out1.txt
	
	.. code-block:: xml	
	
		<?xml version="1.0"?>
		<ROOT>
			<CLASS_TYPE type="str" is_array="false">OutputFormatTable</CLASS_TYPE>
			<NAME type="str" is_array="false">out1</NAME>
			<BODY>
				<OUTPUT_FORMAT name="one">
					<OUTPUT_DIM name="first">
						<ACCUMULATION>
							ACC1
						</ACCUMULATION>
						<PRODUCT>
							PROD2
						</PRODUCT>
					</OUTPUT_DIM>
					<OUTPUT_DIM name="second">
						<CRITERIA>
							bTemp
						</CRITERIA>			
					</OUTPUT_DIM>
				</OUTPUT_FORMAT>
				<OUTPUT_FORMAT name="second">
					<OUTPUT_DIM name="first">
						<ACCUMULATION>
							ACC1
						</ACCUMULATION>
						<PRODUCT>
							PROD2
						</PRODUCT>
					</OUTPUT_DIM>
					<OUTPUT_DIM name="second">
						<CRITERIA>
							bTemp
						</CRITERIA>			
					</OUTPUT_DIM>
				</OUTPUT_FORMAT>
			</BODY>
		</ROOT>





	
	
	
	
	
	
