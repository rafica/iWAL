#iteration_statement
def iteration_statement_1(s, temp, scope):
        i = 1
        while(('loop'+i) in s[scope]):
                i=i+1
        #loopi is the variable name to use.
        temp.code = 'for (int loop' + i + ' = 0; loop' + i + ' <' + temp.children[0].code + ' ; loop' + i + '++){\n' + temp.children[1].code + '\n}'
        temp.datatype = 'void'
        s[scope]['loop'+i] = ['int']
        if(temp.children[0].datatype!='int'):
                print 'type of '+ temp.children[0].type+' must be int!'

def iteration_statement_2(s, temp, scope):
    # 'iteration_statement : UNTIL LPAREN expression RPAREN LBRACE statement_list RBRACE'
    temp.code = 'while (' + temp.children[0].code + '){\n' + temp.children[1].code + '\n}'
    temp.datatype = 'void'
    if(temp.children[0].datatype!='boolean'):
    	print 'type of '+ temp.children[0].type + 'must be boolean!'

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

def statement_8(s, temp, scope):
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
   	if(type(temp.children[0])=='Node'):
   		print 'Error: '+ temp.children[0] + 'cannot be a Node'
   	temp.code = temp.children[0]
   	temp.datatype = 'int'

def constant_2(s, temp, scope):
        if(type(temp.children[0])=='Node'):
   		print 'Error: '+ temp.children[0] + 'cannot be a Node'
   	temp.code = temp.children[0]
   	temp.datatype = 'double'

def constant_3(s, temp, scope):
        if(type(temp.children[0])=='Node'):
   		print 'Error: '+ temp.children[0] + 'cannot be a Node'
   	temp.code = temp.children[0]
   	temp.datatype = 'string'

# expression_statement:
def expression_statement_1(s, temp, scope):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code + ';\n'

def expression_statement_2(s, temp, scope):
    temp.datatype = 'void'
    temp.code = ';\n'  

# function_expression

def function_expression_1(s, temp, scope):
    # 'function_expression : ID LPAREN parameter_list RPAREN'
    # p[0] = Node('function_expression_1',[p[1],p[3]])
    temp.datatype = s[scope][temp.children[0]][1]	#Assign the return type of function to the data type of temp.
    temp.code = temp.children[0].type + '(' + temp.children[1].code + ');'
    if(temp.children[0].type not in s[scope]):
    	print 'Function undefined!'
        temp.code = 'ERROR ERROR ERROR'
    elif(s[scope][temp.children[0]][0]!='function'):
    	print 'It\'s not a function!'
    	temp.code = 'ERROR ERROR ERROR'
    elif(s[scope][temp.children[0]][2]!=len(s[scope][temp.children[0]][3])):
    	print 'Function ' + temp.children[0].type + ' accepts '+ s[scope][temp.children[0]][2] + ' arguments. ' + len(s[scope][temp.children[0]][3]) + 'given.'
        temp.code = 'ERROR ERROR ERROR'

    variables = temp.children[1].code.strip().split(',')
    for var in variables:
    	[flag, data_type] = check_type(scope, s, )
    	if(flag==0):
    		print 'Parameter variable ' + var + ' does not exist in scope.'
                temp.code = 'ERROR ERROR ERROR'


# parameter_declaration:
def parameter_declaration_1(s, temp, scope):
    # 'parameter_declaration : primary_expression'
    # # p[0] = p[1]
    # p[0] = Node('parameter_declaration_1',[p[1]])
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code

def parameter_declaration_2(s, temp, scope):
    temp.datatype = temp.children[0].datatype
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Variable', temp.children[1], 'is declared again here ...'
            temp.code = 'ERROR ERROR ERROR'
            temp.datatype = 'void'
        else:
            s[scope][temp.children[1]] = [temp.children[0].datatype]
    else:
        s[scope] = {}
        s[scope][temp.children[1]] = [temp.children[0].datatype]
    temp.code = temp.children[0].code + ' ' +str(temp.children[1])


def parameter_declaration_3(s, temp, scope):
    # 'parameter_declaration : type ID EQUALS assignment_expression'
    # # p[0] = p[1] + ' ' + p[2] + ' = ' + p[4]
    # p[0] = Node('parameter_declaration_3',[[p[2],p[1]],p[4]],p[3])
    temp.datatype = temp.children[0].datatype
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Variable', temp.children[1], 'is declared again here ...'
        else:
            s[scope][temp.children[1]] = [temp.children[0].datatype]
    else:
        s[scope] = {}
        s[scope][temp.children[1]] = [temp.children[0].datatype]
        temp.code = ''

    if not temp.children[0].datatype == temp.children[2].datatype:
        print 'Error initializing the variable', temp.children[1], '.. Expecting a', temp.children[0].datatype, ' got', temp.children[2].datatype
        temp.code = 'ERROR ERROR ERROR'
        temp.datatype = 'void'
    else:
        temp.dataype = temp.children[0].datatype
        temp.code = temp.children[0].code + ' ' +str(temp.children[1]) + ' = ' + temp.children[2].code + ';\n'

#This function checks if the variable 'var' exists in the symbol table or not.
def check_type(scope, s, var):
    data_type = None
    flag = 0
    while(scope>0):
        if scope in s:
            if var in s[scope]:
                flag = 1
                data_type = s[scope][var][0]
        scope = scope - 1
    return [flag, data_type]
