doc_mOutput
=============

Documentation
*************
1. Brief Explanation of Output
	1. This class controls the output of the model. It contains ResultBlocks, which are multi-dimensional dataframes. It also can print results into excel files.
	2. This class instances are created by Process instance

	
2. List of Member Variables and Methods
	0. How to Create a class instance
	
		>>> p=Process()
		>>> o=p._Output
		
	1. Functions
		1. __init__(self,sName="",sFunction="",sModule="",sProduct="",sAccumulation="")
		
			>>> o.__dict__
			{'_Input': <input.Input at 0xa06bfd0>,
			 '_GlobalSettings': <global_settings.GlobalSettings at 0xa075048>,
			 '_OutputFormatTable': <output_format_table.OutputFormatTable at 0xa0889b0>,
			 'ddReports': {'one': {}, 'second': {}}}
			 
		2. fRecordPolResults(self, varTemp, odCURR_OUTPUT_FORMAT_RAW_CHECK)
		
			>>> p.fRunModel()
			>>> vn=p.mVarNameSpace
			>>> varTemp=vn.aa  #an instance of Variable
			>>> varTemp.__dict__
			{'sName': 'aa',
			 'sFunction': 'def aa(t):\n\t\t\t\treturn t',
			 'sModule': 'oneguy',
			 '_fFunction': <function var_name_space.aa(t)>,
			 'lsFuncArgs': ['t'],
			 '_dCache': {(0,): 0,
			  (1,): 1,
			  (2,): 2,
			  (3,): 3,
			  ... many outputs
			  (97,): 97,
			  (98,): 98,
			  (99,): 99},
			 'lProduct': ['PROD1'],
			 'lAccumulation': ['ACC1'],
			 'bRerunEveryTime': False}
			>>> odCURR_OUTPUT_FORMAT_RAW_CHECK=vn.odCURR_OUTPUT_FORMAT_RAW_CHECK()
			>>> odCURR_OUTPUT_FORMAT_RAW_CHECK
			OrderedDict([('one',
              {('first', 'ACCUMULATION', 'ACC1'): True,
               ('first', 'PRODUCT', 'PROD2'): False,
               ('second', 'CRITERIA', 'bTemp'): True}),
             ('second',
              {('first', 'ACCUMULATION', 'ACC1'): True,
               ('first', 'PRODUCT', 'PROD2'): False,
               ('second', 'CRITERIA', 'bTemp'): True})])
			>>> tFuncArgs = tuple(varTemp.lsFuncArgs)
			>>> tFuncArgs
			('t',)
			>>> list(o._OutputFormatTable.odOutputFormats["one"])
			[(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
			(('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))]
			>>> from result_block import ResultBlock
			>>> ResultBlockTemp=ResultBlock(list(o._OutputFormatTable.odOutputFormats["one"]),
                                                       list(varTemp._dCache.keys()), varTemp.lsFuncArgs)
			For more behaviour about ResultBlock, you can read the documentation for ResultBlock
		
		3. fPrintReport(self, sOutputFormat)
			
			The function that print the ResultBlocks to excel filedate
			
			>>> o.fPrintReport("one") # should after execution of p.fRunModel()
			
			Sample output of excel file "one.xlsx":
			
			.. csv-table::
			    :header: " ", "aa"
			    :widths: 100, 10
				
				"((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (0,))",0
				"((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (1,))",1
				"((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (2,))",2
			

		
	2. Variables

		
3. Related Document





	
	
	
	
	
	
