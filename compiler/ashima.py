plus_operands_allowed={'int','double','string'}
minus_operands_allowed={'int','double'}

#iteration_statement
def iteration_statement_1(s, temp, scope,type_checking_error_flag):
        i = scope
##        temp_flag = check_type_loop(scope, s, 'loop'+str(i))
##        while(temp_flag[0]==1):
##                i=i+1
##                temp_flag = check_type_loop(scope, s, 'loop'+str(i))
        #loopi is the variable name to use.
        temp.code = 'for (int loop' + str(i) + ' = 0; loop' + str(i) + ' <' + temp.children[0].code + ' ; loop' + str(i) + '++){\n' + temp.children[1].code + '\n}\n'
        temp.datatype = 'void'
        if not scope in s:
                s[scope] = {}
        s[scope]['loop'+str(i)] = ['int']
        if(temp.children[0].datatype!='int'):
                print 'Line Number ', temp.lineno, ': Type of ',temp.children[0].type,' must be int.'
                type_checking_error_flag = 1

def iteration_statement_2(s, temp, scope,type_checking_error_flag):
    # 'iteration_statement : UNTIL LPAREN expression RPAREN LBRACE statement_list RBRACE'
    temp.code = 'while (' + temp.children[0].code + '){\n' + temp.children[1].code + '\n}'
    temp.datatype = 'void'
    if(temp.children[0].datatype!='boolean'):
    	print 'Line Number ', temp.lineno, ': Type of ',temp.children[0].type ,'must be boolean.'
    	type_checking_error_flag = 1

#translation_unit
def translation_unit_1(s, temp, scope,type_checking_error_flag):
	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype

def translation_unit_2(s, temp, scope,type_checking_error_flag):
	temp.code = temp.children[0].code + temp.children[1].code
	temp.datatype = temp.children[0].datatype	

#statement
def statement_1(s, temp, scope,type_checking_error_flag):
	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_2(s, temp, scope,type_checking_error_flag):
	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_3(s, temp, scope,type_checking_error_flag):
	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_4(s, temp, scope,type_checking_error_flag):
        temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_5(s, temp, scope,type_checking_error_flag):
        temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_6(s, temp, scope,type_checking_error_flag):
   	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def statement_7(s, temp, scope,type_checking_error_flag):
        temp.code = temp.children[0].code
   	temp.datatype = temp.children[0].datatype	

def statement_8(s, temp, scope,type_checking_error_flag):
        temp.code = temp.children[0].code
   	temp.datatype = temp.children[0].datatype	


# additive_expression:
def additive_expression_1(s, temp, scope,type_checking_error_flag):
	temp.code = temp.children[0].code
	temp.datatype = temp.children[0].datatype	

def additive_expression_2(s, temp, scope,type_checking_error_flag):
	#Check if the datatype of child1 and child2 is same.
        #Check if the datatype of left and right operand is acceptable for operator +.
        if(temp.children[0].datatype not in plus_operands_allowed or temp.children[1].datatype not in plus_operands_allowed):
                print 'Error: Trying to add ',temp.children[0].datatype,' and ',temp.children[1].datatype
                temp.code = 'errorerrorerror'
		temp.datatype = 'error'
	elif(temp.children[0].datatype!=temp.children[1].datatype):
		print 'Line Number ', temp.lineno, ': Data type mismatch. Left operand is ',temp.children[0].datatype,' and right operand is ',temp.children[1].datatype,'.'
                type_checking_error_flag = 1
		temp.code = 'errorerrorerror'
		temp.datatype = 'error'
	else:
		temp.code = temp.children[0].code + ' + ' + temp.children[1].code
		temp.datatype = temp.children[0].datatype

def additive_expression_3(s, temp, scope,type_checking_error_flag):
    #Check if the datatype of child1 and child2 is same.
        if(temp.children[0].datatype not in minus_operands_allowed or temp.children[1].datatype not in minus_operands_allowed):
                print 'Error: Trying to subtract ',temp.children[1].datatype,' from ',temp.children[0].datatype
                temp.code = 'errorerrorerror'
		temp.datatype = 'error'
	elif(temp.children[0].datatype!=temp.children[1].datatype):
		print 'Line Number ', temp.lineno, ': Data type mismatch. Left operand is ',temp.children[0].datatype,' and right operand is ',temp.children[1].datatype,'.'
                type_checking_error_flag = 1
		temp.code = 'errorerrorerror'
		temp.datatype = 'error'
	else:
		temp.code = temp.children[0].code + ' - ' + temp.children[1].code
		temp.datatype = temp.children[0].datatype

# constant:
def constant_1(s, temp, scope,type_checking_error_flag): 
   	if(type(temp.children[0])=='Node'):
   		print 'Line Number ', temp.lineno, ': ',temp.children[0],' cannot be a Node.'
                type_checking_error_flag = 1
   	temp.code = temp.children[0]
   	temp.datatype = 'int'

def constant_2(s, temp, scope,type_checking_error_flag):
        if(type(temp.children[0])=='Node'):
   		print 'Line Number ', temp.lineno, ': ',temp.children[0],' cannot be a Node.'
   		type_checking_error_flag = 1
   	temp.code = temp.children[0]
   	temp.datatype = 'double'

def constant_3(s, temp, scope,type_checking_error_flag):
        if(type(temp.children[0])=='Node'):
   		print 'Line Number ', temp.lineno, ': ',temp.children[0],' cannot be a Node.'
   		type_checking_error_flag = 1
   	temp.code = temp.children[0]
   	temp.datatype = 'string'

def constant_5(s, temp, scope,type_checking_error_flag):
        if(type(temp.children[0])=='Node'):
   		print 'Line Number ', temp.lineno, ': ',temp.children[0],' cannot be a Node.'
   		type_checking_error_flag = 1
   	temp.code = temp.children[0]
   	temp.datatype = 'boolean'

# expression_statement:
def expression_statement_1(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code + ';\n'

def expression_statement_2(s, temp, scope,type_checking_error_flag):
    temp.datatype = 'void'
    temp.code = ';\n'  

# parameter_declaration:
def parameter_declaration_1(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Line Number ', temp.lineno, ': Variable', temp.children[1], ' is declared again here.'
            type_checking_error_flag = 1
            temp.code = 'ERROR ERROR ERROR'
            temp.datatype = 'void'
        else:
            s[scope][temp.children[1]] = [temp.children[0].datatype]
    else:
        s[scope] = {}
        s[scope][temp.children[1]] = [temp.children[0].datatype]
    temp.code = temp.children[0].code + ' ' +str(temp.children[1])


def parameter_declaration_2(s, temp, scope,type_checking_error_flag):
    # 'parameter_declaration : type ID EQUALS assignment_expression'
    # # p[0] = p[1] + ' ' + p[2] + ' = ' + p[4]
    # p[0] = Node('parameter_declaration_3',[[p[2],p[1]],p[4]],p[3])
    temp.datatype = temp.children[0].datatype
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Line Number ', temp.lineno, ': Variable', temp.children[1], ' is declared again here.'
        else:
            s[scope][temp.children[1]] = [temp.children[0].datatype]
    else:
        s[scope] = {}
        s[scope][temp.children[1]] = [temp.children[0].datatype]
        temp.code = ''

    if not temp.children[0].datatype == temp.children[2].datatype:
        print 'Line Number ', temp.lineno, ': Cannot initialize ', temp.children[1], '. Expecting a ', temp.children[0].datatype, ' but got a ', temp.children[2].datatype
        type_checking_error_flag = 1
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

##def check_type_loop(scope, s, var):
##    ls = s.keys()
##    max_scope = max(ls)
##    return check_type(max_scope, s, var)
