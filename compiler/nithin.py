
def function_definition_1(s, temp, scope):
    pass

def declaration_statement_1(s, temp, scope):
    s[(temp.children[1], scope)] = [temp.children[0].datatype]
    temp.code = temp.children[0].code + ' ' +str(temp.children[1]) + ';\n'
    return scope

##def declaration_statement_2(s, temp, scope):
##    s[(temp.children[1], scope)] = 
