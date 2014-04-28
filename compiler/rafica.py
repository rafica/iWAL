def found(s, var, scope):
    flag = 0
    while (scope>0):
        if scope in s:
            if var in s[scope]:
                flag = 1
                break
        scope = scope - 1
    return flag


def assignment_expression_1(s, node, scope):
    if not found(s, node.children[0], scope):
        print node.children[0] +' variable is not declared'
        node.code = "ERROR ERROR ERROR ERROR"
        node.datatype = "error"
    else:
        if node.children[1].datatype != s[scope][node.children[0]][0]:
            print node.children[0] , 'is not ', node.children[1].datatype
            node.code = "ERROR ERROR ERROR ERROR"
            node.datatype = "error"
        else:
##            print node.children[0], node.children[1].code, node.children[1].type
            node.code = node.children[0] + "=" + node.children[1].code
            node.datatype = node.children[1].datatype
    return

def assignment_expression_2(s, node, scope):
    node.code = node.children[0].code
    node.datatype = node.children[0].datatype
    return

def assignment_expression_3(s, node, scope):
    if node.children[0].datatype != node.children[1].datatype:
        node.code = "ERROR ERROR ERROR ERROR"
        node.datatype = "error"
        print node.children[0] +' datatypes dont match' + node.children[0].datatype +' and '+ node.children[1].datatype
    else:
        node.code = node.children[0].code + ' = ' + node.children[1].code
        node.datatype = node.children[1].datatype
    

def assignment_expression_4(s, node, scope):
    node.code = node.children[0].code
    node.datatype = node.children[0].datatype
    return

def external_declaration_1(s, node, scope):
    node.code = node.children[0].code
    node.datatype = node.children[0].datatype
    return

def external_declaration_2(s, node, scope):
    node.code = node.children[0].code
    node.datatype = node.children[0].datatype


def equality_expression_1(s, node, scope):
    node.code = node.children[0].code
    node.datatype = node.children[0].datatype


def equality_expression_2(s, node, scope):
    if node.children[0].datatype == node.children[1].datatype:
        node.code = node.children[0].code+ '==' + node.children[1].code
        node.datatype = "boolean"
    else:
        node.code = "ERROR ERROR ERROR ERROR"
        node.datatype = "error"
        print "datatypes "+ node.children[0].datatype +' and ' + node.children[1].datatype + ' dont match'
        


def equality_expression_3(s, node, scope):
    if node.children[0].datatype == node.children[1].datatype:
        node.code = node.children[0].code+ '!=' + node.children[1].code
        node.datatype = "boolean"
    else:
        node.code = "ERROR ERROR ERROR ERROR"
        node.datatype = "error"
        print "datatypes "+ node.children[0].datatype +' and ' + node.children[1].datatype + ' dont match'

def selection_statement_1(s, node, scope):
    if node.children[2].datatype=="boolean":
        node.code = "if("+children[0].code+"){"+children[1].code + "}"
        node.datatype = "boolean"
    else:
        node.code = 'ERRORERRORERRORERROR'
        node.datatype = 'error'


def selection_statement_2(s, node, scope):
    if node.children[2].datatype=="boolean":
        node.code = "if("+children[0].code+"){"+children[1].code + "}else{"+ children[2].code +"}"
        node.datatype = "boolean"
    else:
        node.code = 'ERRORERRORERRORERROR'
        node.datatype = 'error'
        
    
