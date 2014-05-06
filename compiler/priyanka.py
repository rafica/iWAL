def type_1(s, temp, scope,type_checking_error_flag):
    temp.code = "int"
    temp.datatype = "int"
        
def type_2(s, temp, scope,type_checking_error_flag):
    temp.code = "double"
    temp.datatype = "double"

def type_3(s, temp, scope,type_checking_error_flag):
    temp.code = "char"
    temp.datatype = "char"
        
def type_4(s, temp, scope,type_checking_error_flag):
    temp.code = "String"
    temp.datatype = "string"        

def type_5(s, temp, scope,type_checking_error_flag):
    temp.code = "key"
    temp.datatype = "key"   

def type_6(s, temp, scope,type_checking_error_flag):
    temp.code = "boolean"
    temp.datatype = "boolean" 

def logical_OR_expression_1(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code

def logical_OR_expression_2(s, temp, scope,type_checking_error_flag):
    if temp.children[0].datatype == "boolean" and temp.children[1].datatype == "boolean":
        temp.datatype = "boolean"
        temp.code = temp.children[0].code +'||'+ temp.children[1].code
    else:
        print 'Line Number ', temp.lineno, ': Data type mismatch. ',temp.children[0].type,' of type ',temp.children[0].datatype,'but ',temp.children[1].type, ' of type ',temp.children[1].datatype,'.'
        type_checking_error_flag = 1
        temp.datatype = "error"
        temp.code = "error error error"
        
def expression_1(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code

def expression_3(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.datatype
    temp.code = '(' + temp.children[0].code + ')'

def equality_expression_1(s, temp, scope,type_checking_error_flag):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code               
        
def equality_expression_2(s, temp, scope,type_checking_error_flag):
    if temp.children[0].datatype == temp.children[1].datatype:
        temp.datatype = "boolean"
        temp.code = temp.children[0].code + '==' + temp.children[0].code
    else:
        print 'Line Number ', temp.lineno, ': Data type mismatch. ',temp.children[0].type,' of type ',temp.children[0].datatype,'but ',temp.children[1].type, ' of type ',temp.children[1].datatype,'.'
        type_checking_error_flag = 1
        temp.datatype = "error"
        temp.code = "error error error"

def equality_expression_3(s, temp, scope,type_checking_error_flag):
    if temp.children[0].datatype == temp.children[1].datatype:
        temp.datatype = "boolean"
        temp.code = temp.children[0].code + '!=' + temp.children[0].code
    else:
        print 'Line Number ', temp.lineno, ': Data type mismatch. ',temp.children[0].type,' of type ',temp.children[0].datatype,'but ',temp.children[1].type, ' of type ',temp.children[1].datatype,'.'
        type_checking_error_flag = 1
        temp.datatype = "error"
        temp.code = "error error error"
    
def break_statement_1(s, temp, scope,type_checking_error_flag):
    temp.datatype = "void"
    temp.code = 'break ;'     
    
    


    
