doc_mVariable
=============

Documentation
*************
1. Brief Explanation of Variable
	1. It is generated upon reading XML script files.
	2. This class instances are included in Script::BODY
	2. Other comments:
	
	This class will hold definitions for variables. During initialization, they only contain strings for their function definitions (self.sFunction). Later “self. fSetfFunction” will be called and Variable::_fFunction will contain a real function definition. Variable class can be called, and have caches to store any calculated values. 

	I think calling a user-defined class may not be efficient in terms of computation time. We may need to think of a new way to store caches and compute quickly.

2. List of Member Variables and Methods
	0. How to Create a class instance
	
		>>> s=Script(sFilePath=".\\script\\Script2.txt")
		>>> v=s.BODY["aa"] 'take the Variable named "aa" as an example
		
	1. Functions
		1. __init__(self,sName="",sFunction="",sModule="",sProduct="",sAccumulation="")
		
			>>> v.__dict__
			{'sName': 'aa',
			 'sFunction': 'def aa(t):\n\t\t\t\treturn t',
			 'sModule': 'oneguy',
			 '_fFunction': None,
			 'lsFuncArgs': [],
			 '_dCache': {},
			 'lProduct': ['PROD1'],
			 'lAccumulation': ['ACC1']}
			 
		2. fSetfFunction(self,mModule_fFunc,bReInitialize=False)
			>>> import imp
			>>> module = imp.new_module("haha")
			>>> print(v._fFunction)
			None
			>>> v.fSetfFunction(module,False)
			>>> v._fFunction
			<function haha.aa(t)>
			>>> v._fFunction(23)
			23
			
		3. fReInitialize(self)
		
			TODO: explain this later
		
		... and other functions
		
	2. Variables

		
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





	
	
	
	
	
	
