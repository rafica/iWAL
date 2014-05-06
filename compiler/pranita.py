def getTypeFromSymTable(t, symTab, curr_scope):
    flag = False
    while curr_scope > 0:
        if curr_scope in symTab:
            if t in symTab[curr_scope]:
                flag = True
                return symTab[curr_scope][t][0]
        curr_scope = curr_scope - 1    
    if(not flag):
        return False

def relational_expression_1(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code

def relational_expression_2(s, temp, scope,type_checking_error_flag):
        if temp.children[0].datatype != temp.children[1].datatype:
            print 'Line Number ', temp.lineno, ': Error, trying to compare ' , temp.children[0].datatype , ' and ' , temp.children[1].datatype , '.'
            type_checking_error_flag = 1
            temp.datatype = 'error'
            temp.code = 'errorerrorerror'
        else:
            temp.datatype = 'boolean'
            temp.code = temp.children[0].code + ' < ' + temp.children[1].code 



def relational_expression_3(s, temp, scope,type_checking_error_flag):
        if temp.children[0].datatype != temp.children[1].datatype:
            print 'Line Number ', temp.lineno, ': Error, trying to compare ' , temp.children[0].datatype , ' and ' , temp.children[1].datatype , '.'
            type_checking_error_flag = 1
            temp.datatype = 'error'
            temp.code = 'errorerrorerror'
        else:
            temp.datatype = 'boolean'
            temp.code = temp.children[0].code + ' > ' + temp.children[1].code 

   

def relational_expression_4(s, temp, scope,type_checking_error_flag):
        if temp.children[0].datatype != temp.children[1].datatype:
            print 'Line Number ',temp.lineno,': Error, trying to compare ' , temp.children[0].datatype , ' and ' , temp.children[1].datatype , '.'
            type_checking_error_flag = 1
            temp.code = 'errorerrorerror'
            temp.datatype = 'error'
        else:
            temp.datatype = 'boolean'
            temp.code = temp.children[0].code + ' <= ' + temp.children[1].code 

   
def relational_expression_5(s, temp, scope,type_checking_error_flag):
        if temp.children[0].datatype != temp.children[1].datatype:
            print 'Line Number ', temp.lineno,': Error, trying to compare ' , temp.children[0].datatype , ' and ' , temp.children[1].datatype, '.'
            type_checking_error_flag = 1
            temp.datatype = 'error'
            temp.code = 'errorerrorerror'
        else:
            temp.datatype = 'boolean'
            temp.code = temp.children[0].code + ' >= ' + temp.children[1].code 


def logical_AND_expression_1(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code


def logical_AND_expression_2(s, temp, scope,type_checking_error_flag):
    if temp.children[0].datatype == 'boolean' and temp.children[1].datatype == 'boolean':
        temp.datatype = temp.children[0].datatype
        temp.code = temp.children[0].code + ' && ' + temp.children[1].code
    else:
        print 'Line Number ', temp.lineno, ': Error, trying to AND ' + temp.children[0].datatype + ' and ' + temp.children[1].datatype + '.'
        type_checking_error_flag = 1
        temp.code = 'errorerrorerror'
        temp.datatype = 'error'
        
def primary_expression_1(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = '( ' + temp.children[0].code + ' )'


def primary_expression_2(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code


def primary_expression_3(s, temp, scope,type_checking_error_flag):
    flag = getTypeFromSymTable(temp.children[0], s, scope)
    if flag == False:
        print 'Line Number ', temp.lineno, ': Error, trying to access ' , temp.children[0] , ' but it\'s not defined.'
        type_checking_error_flag = 1
        temp.code = 'errorerrorerror'
        temp.datatype = 'error'
    else:
        temp.datatype = flag
        temp.code = temp.children[0]

def primary_expression_4(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code


def primary_expression_5(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code


def multiplicative_expression_1(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code
    

def multiplicative_expression_2(s, temp, scope,type_checking_error_flag):
    if temp.children[0].datatype != temp.children[1].datatype:
        print 'Line Number ', temp.lineno, ': Error, trying to multiply ' , temp.children[0].datatype , ' and' , temp.children[1].datatype + '.'
        type_checking_error_flag = 1
        temp.datatype = 'error'
        temp.code = 'errorerrorerror'
    else:
        temp.datatype = temp.children[0].datatype
        temp.code = temp.children[0].code + ' * ' + temp.children[1].code 
    
def multiplicative_expression_3(s, temp, scope,type_checking_error_flag):
    if temp.children[0].datatype != temp.children[1].datatype:
        print 'Line Number ',temp.lineno, ': Error, trying to divide ' , temp.children[0].datatype , ' and ' , temp.children[1].datatype , '.'
        type_checking_error_flag = 1
        temp.datatype = 'error'
        temp.code = 'errorerrorerror'
    else:
        temp.datatype = temp.children[0].datatype
        temp.code = temp.children[0].code + ' / ' + temp.children[1].code 
    

def statement_list_1(s, temp, scope,type_checking_error_flag):
	temp.datatype = 'void'
	temp.code = temp.children[0].code

def statement_list_2(s, temp, scope,type_checking_error_flag):
	temp.datatype = 'void'
	temp.code = temp.children[0].code + ' ' + temp.children[1].code

def parameter_list_1(s, temp, scope,type_checking_error_flag):
	temp.datatype = [temp.children[0].datatype]
	temp.code = temp.children[0].code

def parameter_list_2(s, temp, scope,type_checking_error_flag):
	temp.datatype = temp.children[0].datatype+[temp.children[1].datatype]
	temp.code = temp.children[0].code + ', ' + temp.children[1].code

def return_statement_1(s, temp, scope,type_checking_error_flag):
	temp.datatype = 'void'
	temp.code = 'return ;'

def return_statement_2(s, temp, scope,type_checking_error_flag):
	temp.datatype = temp.children[0].datatype
	temp.code = 'return ' + temp.children[0].code + ' ;' 

