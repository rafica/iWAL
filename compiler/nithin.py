
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

def get_parameters(param_list):
    temp = []
    param_list = param_list.strip().split(',')
    if param_list == '':
        return temp
    for i in range(len(param_list)):
        param_list[i] = param_list[i].strip().split(' ')
        if len(param_list[i]) < 2:
            print 'In function definition : Parameters datatype is not passed'
        else:
            temp.append(param_list[i][0])
    return temp

def function_definition_1(s, temp, scope):
    scope = scope - 1
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Variable', temp.children[1], 'is declared again here ...'
            temp.code = 'ERROR ERROR ERROR'
        else:
            params = get_parameters(temp.children[2].code)
            s[scope][temp.children[1]] = ['function', temp.children[0].datatype, len(params), params]
            temp.code = 'public static ' + temp.children[0].datatype + ' ' + temp.children[1] + '(' + temp.children[2].code + ') { ' + temp.children[3].code  + ' }'

def function_definition_2(s, temp, scope):
    scope = scope - 1
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Variable', temp.children[1], 'is declared again here ...'
            temp.code = 'ERROR ERROR ERROR'
        else:
            params = get_parameters(temp.children[2].code)
            s[scope][temp.children[1]] = ['function', temp.children[0].datatype, len(params), params]
            temp.code = 'public static ' + temp.children[0].datatype + ' ' + temp.children[1] + '(' + temp.children[2].code + ') { }'
 
def declaration_statement_1(s, temp, scope):
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Variable', temp.children[1], 'is declared again here ...'
        else:
            s[scope][temp.children[1]] = [temp.children[0].datatype]
    else:
        s[scope] = {}
        s[scope][temp.children[1]] = [temp.children[0].datatype]

    temp.code = temp.children[0].code + ' ' +str(temp.children[1]) + ';\n'

def declaration_statement_2(s, temp, scope):
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Variable', temp.children[1], 'is declared again here ...'
            temp.code = 'ERROR ERROR ERROR'
        else:
            s[scope][temp.children[1]] = [temp.children[0].datatype]
    else:
        s[scope] = {}
        s[scope][temp.children[1]] = [temp.children[0].datatype]

    if not temp.children[0].datatype == temp.children[2].datatype:
        print 'Error initializing the variable', temp.children[1], '.. Expecting a', temp.children[0].datatype, ' got', temp.children[2].datatype
        temp.code = 'ERROR ERROR ERROR'
        temp.datatype = 'void'
    else:
        temp.dataype = temp.children[0].datatype
        temp.code = temp.children[0].code + ' ' +str(temp.children[1]) + ' = ' + temp.children[2].code + ';\n'
