import ply.yacc as yacc
from ilexer import *

#######################################################################
#######################         YACC        ###########################
#######################################################################

class Node(object):
    def __init__(self, type, children=None,parent=None, token=None):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = []
        self.parent = parent
        self.token = token

    def __str__(self):
        return self.traverse(1)

##    def traverse(self):
##        print self.type
##
##        for children

    def traverse(self, i):
        s = self.type
        indent = "\n" + i*' |'
        if self.parent != None:
            if isinstance(self.parent, Node):
                print "Node"
                s += indent + self.leaf.traverse(i+1)
            else:
                s += indent + str(self.parent)

        for children in self.children:
            if type(children)==Node:
                s += indent + children.traverse(i+1)
##            else:
##                print s
        return s

# translation_unit:
def p_translation_unit_1(p):
    'translation_unit : external_declaration'
    # p[0] = p[1]
    p[0] = Node('translation_unit_1', [p[1]])

def p_translation_unit_2(p):
    'translation_unit : translation_unit external_declaration'
    # p[0] = p[1] + ' ' + p[2]
    p[0] = Node('translation_unit_2', [p[1],p[2]])

# external_declaration:
def p_external_declaration_1(p):
    'external_declaration : function_definition'
    # p[0] = p[1]
    p[0] = Node('external_declaration_1', [p[1]])

def p_external_declaration_2(p):
    'external_declaration : statement'
    # p[0] = p[1]
    p[0] = Node('external_declaration_2', [p[1]])
# function_definition:
def p_function_definition_1(p):
    'function_definition : type ID LPAREN parameter_list RPAREN LBRACE statement_list RBRACE'
    # p[0] = p[1]+' '+p[2]+' ( '+p[4]+ ' ) { '+p[7]+' }'
    p[0] = Node('function_definition_1', [p[1],p[4],p[7]],p[2])

def p_function_definition_2(p):
    'function_definition : type ID LPAREN parameter_list RPAREN LBRACE RBRACE'
    # p[0] = p[1]+' '+p[2]+' ( '+p[4]+ ' ) { }'
    p[0] = Node('function_definition_2',[p[1],p[4]],p[2])

# parameter_list:
def p_parameter_list_1(p):
    'parameter_list : parameter_declaration'
    # p[0] = p[1]
    p[0] = Node('parameter_list_1',[p[1]])

def p_parameter_list_2(p):
    'parameter_list : parameter_list COMMA parameter_declaration'
    # p[0] = p[1] + ' , ' + p[3]
    p[0] = Node('parameter_list_2',[p[1],p[3]])

# parameter_declaration:
def p_parameter_declaration_1(p):
    'parameter_declaration : primary_expression'
    # p[0] = p[1]
    p[0] = Node('paramemter_declaration_1',[p[1]])

def p_parameter_declaration_2(p):
    'parameter_declaration : type ID'
    # p[0] = p[1] + ' ' + p[2]
    p[0] = Node('parameter_declaration_2',[p[1],p[2]])

def p_parameter_declaration_3(p):
    'parameter_declaration : type ID EQUALS assignment_expression'
    # p[0] = p[1] + ' ' + p[2] + ' = ' + p[4]
    p[0] = Node('parameter_declaration_3',[[p[2],p[1]],p[4]],p[3])

# type:
def p_type_1(p):
    'type : INT'
    # p[0] = p[1]
    p[0] = Node('type_1',[p[1]])

def p_type_2(p):
    'type : DOUBLE'
    # p[0] = p[1]
    p[0] = Node('type_2',[p[1]])

def p_type_3(p):
    'type : CHAR'
    # p[0] = p[1]
    p[0] = Node('type_3',[p[1]])

def p_type_4(p):
    'type : STRING'
    # p[0] = 'String'       #CHECK..
    p[0] = Node('type_4',[p[1]])

def p_type_5(p):        #Optional..can remove.
    'type : KEY'
    # p[0] = p[1]
    p[0] = Node('type_5',[p[1]])

##################### Add more types here #############

# statement:
def p_statement_1(p):
    'statement : expression_statement'
    # p[0] = p[1]
    p[0] = Node('statement_1',[p[1]])

def p_statement_2(p):
    'statement : compound_statement'
    # p[0] = p[1]
    p[0] = Node('statement_2',[p[1]])

def p_statement_3(p):
    'statement : declaration_statement'
    # p[0] = p[1]
    p[0] = Node('statement_3',[p[1]])

def p_statement_4(p):
    'statement : selection_statement'
    # p[0] = p[1]
    p[0] = Node('statement_4',[p[1]])

def p_statement_5(p):
    'statement : iteration_statement'
    # p[0] = p[1]
    p[0] = Node('statement_5',[p[1]])

def p_statement_6(p):
    'statement : return_statement'
    # p[0] = p[1]
    p[0] = Node('statement_6',[p[1]])

def p_statement_7(p):
    'statement : break_statement'
    # p[0] = p[1]
    p[0] = Node('statement_7',[p[1]])

# iteration_statement:
def p_iteration_statement_1(p):
    'iteration_statement : REPEAT LPAREN expression RPAREN LBRACE statement_list RBRACE'
    ## p[0] = 'repeat ( ' + p[3] + ' ) { ' + p[6] + ' }'
    # p[0] = 'for(int repeatNumber'+str(repeatNumber)+'=0, repeatNumber'+str(repeatNumber)+'<'+p[3]+', repeatNumber'+str(repeatNumber)+'++) { '+p[6]+'}'
    p[0] = Node('iteration_statement_1',[p[3],p[6]])

def p_iteration_statement_2(p):
    'iteration_statement : UNTIL LPAREN expression RPAREN LBRACE statement_list RBRACE'
    # p[0] = 'until ( ' + p[3] + ' ) { ' + p[6] + ' }'
    p[0] = Node('iteration_statement_2',[p[3],p[6]])

# selection_statement:
def p_selection_statement_1(p):
    'selection_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE'
    # p[0] = 'if ( ' + p[3] + ' ) ' + p[6]
    p[0] = Node('selection_statement_1',[p[3],p[6]])

def p_selection_statement_2(p):
    'selection_statement : IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE LBRACE statement_list RBRACE'
    # p[0] = 'if ( ' + p[3] + ' ) { ' + p[6] + ' } ( else ) { ' + p[10] + ' }'
    p[0] = Node('selection_statement_2',[p[3],p[6],p[10]])        #CHECK

# declaration_statement:
def p_declaration_statement_1(p):
    'declaration_statement : type ID SEMI'
    # p[0] = p[1] + ' ' + p[2] + ' ;'
    p[0] = Node('declaration_statement_1',[p[1],p[2]])

def p_declaration_statement_2(p):
    'declaration_statement : type ID EQUALS assignment_expression SEMI'
    p[0] = Node('declaration_statement_2',[p[1],Node('EqualTo',[p[2],p[4]],p[3])])

# compound_statement:
def p_compound_statement_1(p):
    'compound_statement : LBRACE RBRACE'
    # p[0] = '{ }'
    p[0] = Node('compound_statement_1',[p[1],p[2]])

def p_compound_statement_2(p):
    'compound_statement : LBRACE statement_list RBRACE'
    # p[0] = '{ '+p[2]+' }'
    p[0] = Node('compound_statement_2',[p[1],p[2],p[3]])

# expression_statement:
def p_expression_statement_1(p):
    'expression_statement : expression SEMI'
    # p[0] = p[1] + ';'
    p[0] = Node('expression_statement_1',[p[1]])

def p_expression_statement_2(p):
    'expression_statement : SEMI'
    # p[0] = ';'
    p[0] = Node('expression_statement_2',[p[1]])    #CHECK

# expression:
def p_expression_1(p):
    'expression : assignment_expression'
    # p[0] = p[1]
    p[0] = Node('expression_1',[p[1]])

def p_expression_2(p):
    'expression : function_expression'
    # p[0] = p[1]
    p[0] = Node('expression_2',[p[1]])

def p_expression_3(p):
    'expression : LPAREN expression RPAREN'
    # p[0] = '( ' + p[2] + ' )'
    p[0] = Node('expression_3',[p[2]])

# function_expression:
def p_function_expression_1(p):
    'function_expression : ID LPAREN parameter_list RPAREN'
    p[0] = Node('function_expression_1',[p[1],p[3]])

# assignment_expression:
def p_assignment_expression_1(p):
    'assignment_expression : ID EQUALS assignment_expression'
    # p[0] = p[1] + ' = ' + p[3]
    p[0] = Node('assignment_expression_1',[p[1],p[3]],p[2])

def p_assignment_expression_3(p):
    'assignment_expression : logical_OR_expression EQUALS assignment_expression'
    # p[0] = p[1] + ' = ' + p[3]
    p[0] = Node('assignment_expression_2',[p[1],p[3]],p[2])

def p_assignment_expression_2(p):
    'assignment_expression : logical_OR_expression'
    # p[0] = p[1]
    p[0] = Node('assignment_expression_3',[p[1]])

# logical_OR_expression:
def p_logical_OR_expression_1(p):
    'logical_OR_expression : logical_AND_expression'
    # p[0] = p[1]
    p[0] = Node('logical_OR_expression_1',[p[1]])
    
def p_logical_OR_expression_2(p):
    'logical_OR_expression : logical_OR_expression LOR logical_AND_expression'
    # p[0] = p[1] + ' || ' + p[3]
    p[0] = Node('logical_OR_expression_2',[p[1],p[3]],p[2])

# logical_AND_expression:
def p_logical_AND_expression_1(p):
    'logical_AND_expression : equality_expression'
    # p[0] = p[1]
    p[0] = Node('logical_AND_expression_1',[p[1]])

def p_logical_AND_expression_2(p):
    'logical_AND_expression : logical_AND_expression LAND equality_expression'
    # p[0] = p[1] + ' && ' + p[3]
    p[0] = Node('logical_AND_expression_2',[p[1],p[3]],p[2])

# equality_expression:
def p_equality_expression_1(p):
    'equality_expression : relational_expression'
    # p[0] = p[1]
    p[0] = Node('equality_expression_1',[p[1]])

def p_equality_expression_2(p):
    'equality_expression : equality_expression EQ relational_expression'
    # p[0] = p[1] + ' == ' + p[3]
    p[0] = Node('equality_expression_2',[p[1],p[3]],p[2])

def p_equality_expression_3(p):
    'equality_expression : equality_expression NE relational_expression'
    # p[0] = p[1] + ' != ' + p[3]
    p[0] = Node('equality_expression_3',[p[1],p[3]],p[2])

# relational_expression:
def p_relational_expression_1(p):
    'relational_expression : additive_expression'
    # p[0] = p[1]
    p[0] = Node('relational_expression_1',[p[1]])

def p_relational_expression_2(p):
    'relational_expression : relational_expression LT additive_expression'
    # p[0] = p[1] + ' < ' + p[3]
    p[0] = Node('relational_expression_2',[p[1],p[3]],p[2])

def p_relational_expression_3(p):
    'relational_expression : relational_expression GT additive_expression'
    # p[0] = p[1] + ' > ' + p[3]
    p[0] = Node('relational_expression_3',[p[1],p[3]],p[2])

def p_relational_expression_4(p):
    'relational_expression : relational_expression LE additive_expression'
    # p[0] = p[1] + ' <= ' + p[3]
    p[0] = Node('relational_expression_4',[p[1],p[3]],p[2])

def p_relational_expression_5(p):
    'relational_expression : relational_expression GE additive_expression'
    # p[0] = p[1] + ' >= ' + p[3]
    p[0] = Node('relational_expression_5',[p[1],p[3]],p[2])

# additive_expression:
def p_additive_expression_1(p):
    'additive_expression : multiplicative_expression'
    # p[0] = p[1]
    p[0] = Node('additive_expression_1',[p[1]])

def p_additive_expression_2(p):
    'additive_expression : additive_expression PLUS multiplicative_expression'
    # p[0] = p[1] + ' + ' + p[3]
    p[0] = Node('additive_expression_2',[p[1],p[3]],p[2])

def p_additive_expression_3(p):
    'additive_expression : additive_expression MINUS multiplicative_expression'
    # p[0] = p[1] + ' - ' + p[3]
    p[0] = Node('additive_expression_3',[p[1],p[3]],p[2])

# multiplicative_expression:
def p_multiplicative_expression_1(p):
    'multiplicative_expression : primary_expression'
    # p[0] = p[1]
    p[0] = Node('multiplicative_expression_1',[p[1]])

def p_multiplicative_expression_2(p):
    'multiplicative_expression : multiplicative_expression TIMES primary_expression'
    # p[0] = p[1] + ' * ' + p[3]
    p[0] = Node('multiplicative_expression_2',[p[1],p[3]],p[2])

def p_multiplicative_expression_3(p):
    'multiplicative_expression : multiplicative_expression DIVIDE primary_expression'
    # p[0] = p[1] + ' / ' + p[3]
    p[0] = Node('multiplicative_expression_3',[p[1],p[3]],p[2])

# statement_list:
def p_statement_list_1(p):
    'statement_list : statement'
    # p[0] = p[1]
    p[0] = Node('statement_list_1',[p[1]])

def p_statement_list_2(p):
    'statement_list : statement_list statement'
    # p[0] = p[1] + ' ' + p[2]
    p[0] = Node('statement_list_2',[p[1],p[2]])        #CHECK

# primary-expression:
def p_primary_expression_1(p):
    'primary_expression : LPAREN expression RPAREN'
    # p[0] = '( ' + p[2] + ' )'
    p[0] = Node('primary_expression_1',[p[2]])

def p_primary_expression_2(p):
    'primary_expression : constant'
    # p[0] = p[1]
    p[0] = Node('primary_expression_2',[p[1]])

def p_primary_expression_3(p):
    'primary_expression : ID'
    # p[0]= p[1]
    p[0]= Node('primary_expression_3',[p[1]])

def p_primary_expression_4(p):
    'primary_expression : reserved'
    # p[0]= p[1]
    p[0]= Node('primary_expression_4',[p[1]])

def p_primary_expression_5(p):
    'primary_expression : empty'
    # p[0] = p[1]
    p[0] = Node('primary_expression_5',[p[1]])

# constant:
def p_constant_1(p): 
   'constant : ICONST'
   # p[0] = str(p[1])
   p[0] = Node('constant_1',[p[1]])

def p_constant_2(p):
    'constant : FCONST'
    # p[0] = str(p[1])
    p[0] = Node('constant_2',[p[1]])

def p_constant_3(p):
    'constant : SCONST'
    # p[0] = p[1]
    p[0] = Node('constant_3',[p[1]])

#reserved:
def p_reserved_1(p):
    'reserved : ENTER'
    # p[0] = p[1]
    p[0] = Node('reserved_1',[p[1]])

############################ Fill all the KEYtypes here

# return_statement:
def p_return_statement_1(p):
    'return_statement : RETURN SEMI'
    # p[0] = 'return ;'
    p[0] = Node('return_statement_1',[p[1]])

def p_return_statement_2(p):
    'return_statement : RETURN expression SEMI'
    # p[0] = 'return ' + p[2] + ' ;'
    p[0] = Node('return_statement_2',[p[2]])

# break_statement:
def p_break_statement_1(p):
    'break_statement : BREAK SEMI'
    # p[0] = 'break ;'
    p[0] = Node('break_statement_1',[p[1]])

# empty:
def p_empty(p):
    'empty : '
    # p[0] = ''
    p[0] = Node('empty_1')

# error:
def p_error(p):
    print("Whoa. We're hosed.")

def mainYacc():
    mainLex()
    parser = yacc.yacc(method='LALR')
    f = open('../test.txt','r')
    s = f.read()
    f.close()
    result = parser.parse(s)
    return result

result = mainYacc()
result.traverse(-1)
