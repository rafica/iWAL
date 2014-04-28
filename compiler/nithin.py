
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

def function_definition_1(s, temp, scope):
    print 'Not supposed to come here ...'
    pass

def declaration_statement_1(s, temp, scope):
    flag = 0
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Variable', temp.children[1], 'is declared again here ...'
            flag = 1
    if not flag:
        s[scope][temp.children[1]] = [temp.children[0].datatype]

    temp.code = temp.children[0].code + ' ' +str(temp.children[1])

##    if (temp.children[1], scope) in s:
##        print 'Variable', temp.children[1], 'is declared again here ...'
##    s[(temp.children[1], scope)] = [temp.children[0].datatype]
##    temp.code = temp.children[0].code + ' ' +str(temp.children[1])

def declaration_statement_2(s, temp, scope):
    print 'Not supposed to be called for now ...'
##    flag = 0
##    if scope in s:
##        if temp.children[1] in s[scope]:
##            print 'Variable', temp.children[1], 'is declared again here ...'
##            flag = 1
##    if not flag:
##        
##        s[(temp.children[1], scope)] = [temp.children[0].datatype]
##    temp.code = temp.children[0].code + ' ' +str(temp.children[1])
