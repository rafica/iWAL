# #iteration_statement
# def iteration_statement_1(s, temp, scope):
# 	scope+=1
#     s[(temp.children[1], scope)] = [temp.children[0].datatype]    
#     temp.code = temp.children[0].code +temp.children[1].code		#Check code generation step..

#     #Check that expression has data type of int.
#     if(temp.children[0].datatype=='int'):
#     	pass
#    	else:
#    		print 'type of '+temp.children[0].type+' must be int'

#translation_unit
def translation_unit_1(s, temp, scope):
	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def translation_unit_2(s, temp, scope):
	temp.code = temp.children[0].code + temp.children[1].code
	temp.datatype = temp.children[0].datatype	

#statement
def statement_1(s, temp, scope):
	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_2(s, temp, scope):
	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_3(s, temp, scope):
	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_4(s, temp, scope):
    temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_5(s, temp, scope):
    temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_6(s, temp, scope):
   	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_7(s, temp, scope):
    temp.code = temp.children[0].code
   	temp.datatype = temp.children[0].datatype	


# additive_expression:
def additive_expression_1(s, temp, scope):
	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def additive_expression_2(s, temp, scope):
	#Check if the datatype of child1 and child2 is same.
	if(temp.children[0].datatype!=temp.children[1].datatype):
		print 'Data type mismatch for '+ temp.children[0].type + ' and ' + temp.children[1].type
		temp.code = 'errorerrorerror'
		temp.datatype = 'error'
	else:
		temp.code = temp.children[0].code + ' + ' + temp.children[1].code
		temp.datatype = temp.children[0].datatype

def additive_expression_3(s, temp, scope):
    #Check if the datatype of child1 and child2 is same.
	if(temp.children[0].datatype!=temp.children[1].datatype):
		print 'Data type mismatch for '+ temp.children[0].type + ' and ' + temp.children[1].type
		temp.code = 'errorerrorerror'
		temp.datatype = 'error'		
	else:
		temp.code = temp.children[0].code + ' - ' + temp.children[1].code
		temp.datatype = temp.children[0].datatype

# constant:
def constant_1(s, temp, scope): 
   	if(type(temp.children[0])==Node):
   		print 'Error: '+ temp.children[0] + 'cannot be a Node'
   	temp.code = temp.children[0]
   	temp.datatype = 'int'

def constant_2(s, temp, scope):
    if(type(temp.children[0])==Node):
   		print 'Error: '+ temp.children[0] + 'cannot be a Node'
   	temp.code = temp.children[0]
   	temp.datatype = 'double'

def constant_3(s, temp, scope):
    if(type(temp.children[0])==Node):
   		print 'Error: '+ temp.children[0] + 'cannot be a Node'
   	temp.code = temp.children[0]
   	temp.datatype = 'string'

# expression_statement:
def expression_statement_1(s, temp, scope):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code + ';'

def expression_statement_2(s, temp, scope):
    temp.datatype = 'void'
    temp.code = ';'  