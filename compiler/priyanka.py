def type_1(s, temp, scope):
    temp.code = "int"
    temp.datatype = "int"
        
def type_2(s, temp, scope):
    temp.code = "double"
    temp.datatype = "double"

def type_3(s, temp, scope):
    temp.code = "char"
    temp.datatype = "char"
        
def type_4(s, temp, scope):
    temp.code = "String"
    temp.datatype = "string"        

def type_5(s, temp, scope):
    temp.code = "key"
    temp.datatype = "key"   

def type_6(s, temp, scope):
    temp.code = "boolean"
    temp.datatype = "boolean" 

def logical_OR_expression_1(s, temp, scope):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code

def logical_OR_expression_2(s, temp, scope):
    if temp.children[0].datatype == "boolean" and temp.children[1].datatype == "boolean":
        temp.datatype = "boolean"
        temp.code = temp.children[0].code +'||'+ temp.children[1].code
    else:
        print " There was an error during the production of logical OR to logical AND"
        temp.datatype = "error"
        temp.code = "error error error"
    
def expression_1(s, temp, scope):
    temp.datatype = temp.children[0].datatype
    temp.code = temp.children[0].code


def expression_3(s, temp, scope):
    temp.datatype = temp.datatype
    temp.code = '(' + temp.children[0].code + ')'

    
    
