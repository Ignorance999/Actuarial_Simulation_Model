doc_mResultBlock
================

Documentation
*************
1. Brief Explanation of Output

	This class's instance contains data calculated from VarNameSpace, after calling fRunModel(). 
	Its self.dfResults have 3 major dimensions, namely OutputGpInd, RangeInd, VarInd. 
	
	1. OutputGpInd: Outputformat keys, which are tuples defined in OutputFormatTable class instance.
	2. RangeInd: Values for Parameters of Variables. e.g. t=0, or t=10
	3. VarInd: Names of Variables

	
2. List of Member Variables and Methods
	0. How to Create a class instance
	
		>>> p=Process()
		>>> p.fRunModel()
		>>> varTemp=p.mVarNameSpace.aa
		>>> o=p._Output
		>>> ltOutputGpInd=o._OutputFormatTable.odOutputFormats["one"]
		[(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')),
		(('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp'))]
		>>> ltRangeInd=list(varTemp._dCache.keys())
		>>> ltRangeInd
		[(0,),
		 (1,),
		 (2,),
		 (3,),
		 ... a lot of outputs
		 (97,),
		 (98,),
		 (99,)]
		>>> lsRangeIndNames=varTemp.lsFuncArgs
		>>> lsRangeIndNames
		['t']
		>>> rb=ResultBlock( ltOutputGpInd, ltRangeInd, lsRangeIndNames)
				
	1. Functions
		1. __init__(self, ltOutputGpInd, ltRangeInd, lsRangeIndNames)
		
			>>> ltCombinedInd = list(cartesian_product(ltOutputGpInd, ltRangeInd))
			[((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (0,)),
			 ((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (1,)),
			 ((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (2,)),
			 ... a lot of outputs
			  ((('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp')), (97,)),
			 ((('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp')), (98,)),
			 ((('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp')), (99,))]
			>>> rb.dfResults
			Empty DataFrame
			Columns: []
			Index: [((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (0,)), ((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (1,)),
			... lots of outputs
			
			 
		2. fAddColumn(self, varTemp, odCURR_OUTPUT_FORMAT_CHECK_SINGLE)
		
			>>> odCURR_OUTPUT_FORMAT_CHECK_SINGLE=o._OutputFormatTable.fodOutputFormatsFromRawToCooked(odCURR_OUTPUT_FORMAT_RAW_CHECK)["one"]
			{(('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')): True,
			(('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp')): False}
			>>> varTemp=p.mVarNameSpace.aa
			>>> lResult = [varTemp._dCache[tt[1]] if odCURR_OUTPUT_FORMAT_CHECK_SINGLE[tt[0]]
                   else 0 for tt in rb.ltCombinedInd]
			>>> lResult
			[0,
			 1,
			 2,
			 3,
			 4,
			 ...lots of outputs
			 0,
			 0,
			 0,
			 0]
		
		3. fdfResultsIndToStr(self)
		
			>>> rb.dfResults.index.map(str)
			Index(['((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (0,))',
				   '((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (1,))',
				   '((('first', 'ACCUMULATION', 'ACC1'), ('second', 'CRITERIA', 'bTemp')), (2,))',
			...lots of outputs
			       '((('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp')), (97,))',
				   '((('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp')), (98,))',
				   '((('first', 'PRODUCT', 'PROD2'), ('second', 'CRITERIA', 'bTemp')), (99,))'],
				  dtype='object', length=200)
						
	2. Variables

		
3. Related Document





	
	
	
	
	
	
