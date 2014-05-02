def getTypeFromSymTable(symTab, t , curr_scope):
	flag = False
	while curr_scope > 0:
                if curr_scope in symTab:
                        if t in symTab[curr_scope]:
                                flag = True
                                return symTab[curr_scope][t][0]
                curr_scope = curr_scope - 1    
 	if(not flag):
                return None


def assignment_expression_1(s, node, scope):
    temp = getTypeFromSymTable(s, node.children[0], scope)
    if not temp:
        print node.children[0] +' variable is not declared'
        node.code = "ERROR ERROR ERROR ERROR"
        node.datatype = "error"
    else:
##        if not (node.children[1].datatype == s[temp][node.children[0]][0]):
        if not (node.children[1].datatype == temp):
            print node.children[0] + 'is not '+ node.datatype
            node.code = "ERROR ERROR ERROR ERROR"
            node.datatype = "error"
        else:
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
    if node.children[0].datatype=="boolean":
        node.code = "if("+node.children[0].code+"){"+node.children[1].code + "}"
        node.datatype = "boolean"
    else:
        node.code = 'ERRORERRORERRORERROR'
        node.datatype = 'error'


def selection_statement_2(s, node, scope):
    if node.children[0].datatype=="boolean":
        node.code = "if("+node.children[0].code+"){"+node.children[1].code + "}else{"+ node.children[2].code +"}"
        node.datatype = "boolean"
    else:
        node.code = 'ERRORERRORERRORERROR'
        node.datatype = 'error'

def compound_statement_1(s, node, scope):
        node.code = "{}"
        node.datatype = "void"

def compound_statement_2(s, node, scope):
        node.code = "{"+ node.children[1] + "}"
        node.datatype = "void"

        
        
