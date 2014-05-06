
def check_type(scope, s, var):
    data_type = None
    flag = 0
    while(scope>0):
        if scope in s:
            if var in s[scope]:
                flag = 1
                data_type = s[scope][var]
        scope = scope - 1
    return [flag, data_type]

def get_parameters(param_list):
    temp = []
    param_list = param_list.strip().split(',')
    if param_list[0] == '':
        return temp
    for i in range(len(param_list)):
        param_list[i] = param_list[i].strip().split(' ')
        if len(param_list[i]) < 2:
            print 'In function definition : Parameters datatype is not passed'
        else:
            temp.append(param_list[i][0])
    return temp

def function_definition_1(s, temp, scope, type_checking_error_flag):
    scope = scope - 1
    if not scope == 1:
        print 'Line Number ',temp.lineno,': Function definition error - Out of scope bounds'
        type_checking_error_flag = 1
        temp.dataype = 'void'
        temp.code = 'ERROR ERROR ERROR'
    else:
        flag = 0
        if scope in s:
            if temp.children[1] in s[scope]:
                print 'Line Number ',temp.lineno,': Function ', temp.children[1], ' is already defined'
                type_checking_error_flag = 1
                temp.code = 'ERROR ERROR ERROR'
                flag = 1
        if not flag:
            if not scope in s:
                s[scope] = {}
            s[scope][temp.children[1]] = ['function', temp.children[0].datatype, len(temp.children[2].datatype), temp.children[2].datatype]
            temp.code = 'public static ' + temp.children[0].datatype + ' ' + temp.children[1] + '(' + temp.children[2].code + ') {\n ' + temp.children[3].code  + ' }\n'
            temp.datatype = 'void'

def function_definition_2(s, temp, scope, type_checking_error_flag):
    scope = scope - 1
    if not scope == 1:
        print 'Line Number ',temp.lineno,': Function definition error - Out of scope bounds'
        type_checking_error_flag = 1
        temp.dataype = 'void'
        temp.code = 'ERROR ERROR ERROR'
    else:
        flag = 0
        if scope in s:
            if temp.children[1] in s[scope]:
                print 'Line Number ',temp.lineno,': Function ', temp.children[1], ' is already defined'
                type_checking_error_flag = 1
                temp.code = 'ERROR ERROR ERROR'
                flag = 1
        if not flag:
            if not scope in s:
                s[scope] = {}
            s[scope][temp.children[1]] = ['function', temp.children[0].datatype, len(temp.children[2].datatype), temp.children[2].datatype]
            temp.code = 'public static ' + temp.children[0].datatype + ' ' + temp.children[1] + '(' + temp.children[2].code + ') { }\n'
            temp.datatype = 'void'

def function_expression_1(s, temp, scope, type_checking_error_flag):
    flags = check_type(scope, s, temp.children[0])
    if flags[0]==0:
        print 'Line Number ', temp.lineno, ': Function',temp.children[0] ,'not defined'
        type_checking_error_flag = 1
        temp.dataype = 'error'
        temp.code = 'ERROR ERROR ERROR'
    else:
        temp_flag = 0
        temp.datatype = flags[1][1]
        temp_params = temp.children[1].datatype
        if not len(flags[1][3])== len(temp_params):
            print 'Line Number ', temp.lineno, ': In function',temp.children[0],', the number of parameters passed are:',len(temp_params), ',', len(flags[1][3]),'expected ...'
            type_checking_error_flag = 1
            temp.code = 'ERROR ERROR ERROR'
        else:
            for i in range(len(flags[1][3])):
                if not flags[1][3][i]==temp_params[i]:
                    print 'Line Number ', temp.lineno,': In function',temp.children[0],', in parameter #', i+1, ',', flags[1][3][i], 'expected, ', temp_params[i],'given ...'
                    type_checking_error_flag = 1
                    temp.code = 'ERROR ERROR ERROR'
                    temp_flag = 1
            if not temp_flag == 1:
                temp.code = temp.children[0] + '( '+temp.children[1].code+' )'

def declaration_statement_1(s, temp, scope, type_checking_error_flag):
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Line Number ', temp.lineno, ': Variable', temp.children[1], ' is already declared'
            type_checking_error_flag = 1
        else:
            s[scope][temp.children[1]] = [temp.children[0].datatype]
    else:
        s[scope] = {}
        s[scope][temp.children[1]] = [temp.children[0].datatype]

    temp.code = temp.children[0].code + ' ' +str(temp.children[1]) + ';\n'

def declaration_statement_2(s, temp, scope, type_checking_error_flag):
    if scope in s:
        if temp.children[1] in s[scope]:
            print 'Line Number ',temp.lineno, ': Variable ', temp.children[1], ' is already declared'
            type_checking_error_flag = 1
            temp.code = 'ERROR ERROR ERROR'
        else:
            s[scope][temp.children[1]] = [temp.children[0].datatype]
    else:
        s[scope] = {}
        s[scope][temp.children[1]] = [temp.children[0].datatype]

    if not temp.children[0].datatype == temp.children[2].datatype:
        print 'Line Number ', temp.lineno, ': Error initializing the variable', temp.children[1], '.. Expecting a', temp.children[0].datatype, ' got', temp.children[2].datatype
        type_checking_error_flag = 1
        temp.code = 'ERROR ERROR ERROR'
        temp.datatype = 'void'
    else:
        temp.dataype = temp.children[0].datatype
##        print temp.children[1],  temp.children[2].code,  temp.children[2].type
        temp.code = temp.children[0].code + ' ' +str(temp.children[1]) + ' = ' + temp.children[2].code + ';\n'

def parameter_declaration_list_1(s, temp, scope, type_checking_error_flag):
    temp.datatype = [temp.children[0].datatype]
    temp.code = temp.children[0].code

def parameter_declaration_list_2(s, temp, scope, type_checking_error_flag):
    temp.datatype = temp.children[0].datatype + [temp.children[1].datatype]
    temp.code = temp.children[0].code + ',' + temp.children[1].code

def empty_1(s, temp, scope, type_checking_error_flag):
    temp.code = ''
    temp.datatype = 'void'
