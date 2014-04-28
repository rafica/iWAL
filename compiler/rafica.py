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
        if node.children[2].datatype != s[scope][node.children[0]][0]:
            print node.children[0] + 'is not '+ node.datatype
            node.code = "ERROR ERROR ERROR ERROR"
            node.datatype = "error"
        else:
            node.code = node.children[0] + "=" + children[2].code
            node.datatype = node.children[2].datatype
    return

def assignment_expression_2(s, node, scope):
    node.code = node.children[0]
    node.datatype = node.children[0].datatype
    return

def assignment_expression_3(s, node, scope):
    if node.children[0].datatype != node.children[2].datatype:
        node.code = "ERROR ERROR ERROR ERROR"
        node.datatype = "error"
        print node.children[0] +' datatypes dont match' + node.children[0].datatype +' and '+ node.children[2].datatype
    else:
        node.code = node.children[0].code + ' = ' + node.children[2].code
        node.datatype = node.children[2].datatype
    

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
    if node.children[0].datatype == node.children[2].datatype:
        node.code = node.children[0].code+ '==' + node.children[2].code
        node.datatype = "boolean"
    else:
        node.code = "ERROR ERROR ERROR ERROR"
        node.datatype = "error"
        print "datatypes "+ node.children[0].datatype +' and ' + node.children[2].datatype + ' dont match'
        


def equality_expression_3(s, node, scope):
    if node.children[0].datatype == node.children[2].datatype:
        node.code = node.children[0].code+ '!=' + node.children[2].code
        node.datatype = "boolean"
    else:
        node.code = "ERROR ERROR ERROR ERROR"
        node.datatype = "error"
        print "datatypes "+ node.children[0].datatype +' and ' + node.children[2].datatype + ' dont match'


        
    
