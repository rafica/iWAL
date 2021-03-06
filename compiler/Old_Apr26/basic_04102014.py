# ----------------------------------------------------------------------
# basic.py
#
# A lexer and Parser for iWAL.
# ----------------------------------------------------------------------

import sys

import ply.lex as lex
import ply.yacc as yacc

# Reserved words
reserved = (
    'AUTO', 'BREAK', 'CASE', 'CHAR', 'CONST', 'CONTINUE', 'DEFAULT', 'DO', 'DOUBLE',
    'ELSE', 'ENUM', 'EXTERN', 'FLOAT', 'FOR', 'GOTO', 'IF', 'INT', 'LONG', 'REGISTER',
    'RETURN', 'SHORT', 'SIGNED', 'SIZEOF', 'STATIC', 'STRUCT', 'SWITCH', 'TYPEDEF',
    'UNION', 'UNSIGNED', 'VOID', 'VOLATILE', 'WHILE', 'KEY', 'STRING', 'ENTER', 'REPEAT', 'UNTIL'
    )

tokens = reserved + (
    # Literals (identifier, integer constant, float constant, string constant, char const)
    'ID', 'TYPEID', 'ICONST', 'FCONST', 'SCONST', 'CCONST',

    # Operators (+,-,*,/,%,|,&,~,^,<<,>>, ||, &&, !, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'OR', 'AND', 'NOT', 'XOR', 'LSHIFT', 'RSHIFT',
    'LOR', 'LAND', 'LNOT',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    
    # Assignment (=, *=, /=, %=, +=, -=, <<=, >>=, &=, ^=, |=)
    'EQUALS', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'PLUSEQUAL', 'MINUSEQUAL',
    'LSHIFTEQUAL','RSHIFTEQUAL', 'ANDEQUAL', 'XOREQUAL', 'OREQUAL',

    # Increment/decrement (++,--)
    'PLUSPLUS', 'MINUSMINUS',

    # Structure dereference (->)
    'ARROW',

    # Conditional operator (?)
    'CONDOP',
    
    # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'SEMI', 'COLON',

    # Ellipsis (...)
    'ELLIPSIS',
    )

# Completely ignored characters
t_ignore           = ' \t\x0c'

# Newlines
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# Compute column.
# input is the input text string
# token is a token instance
def find_column(input, token):
    last_cr = input.rfind('\n',0,token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

# Operators
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_MOD              = r'%'
t_OR               = r'\|'
t_AND              = r'&'
t_NOT              = r'~'
t_XOR              = r'\^'
t_LSHIFT           = r'<<'
t_RSHIFT           = r'>>'
t_LOR              = r'\|\|'
t_LAND             = r'&&'
t_LNOT             = r'!'
t_LT               = r'<'
t_GT               = r'>'
t_LE               = r'<='
t_GE               = r'>='
t_EQ               = r'=='
t_NE               = r'!='

# Assignment operators

t_EQUALS           = r'='
t_TIMESEQUAL       = r'\*='
t_DIVEQUAL         = r'/='
t_MODEQUAL         = r'%='
t_PLUSEQUAL        = r'\+='
t_MINUSEQUAL       = r'-='
t_LSHIFTEQUAL      = r'<<='
t_RSHIFTEQUAL      = r'>>='
t_ANDEQUAL         = r'&='
t_OREQUAL          = r'\|='
t_XOREQUAL         = r'^='

# Increment/decrement
t_PLUSPLUS         = r'\+\+'
t_MINUSMINUS       = r'--'

# ->
t_ARROW            = r'->'

# ?
t_CONDOP           = r'\?'

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_PERIOD           = r'\.'
t_SEMI             = r';'
t_COLON            = r':'
t_ELLIPSIS         = r'\.\.\.'

# Identifiers and reserved words

reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"ID")
    return t

# Integer literal
t_ICONST = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FCONST = r'((\d+)(\.\d+)(e(\+|-)?(\d+))? | (\d+)e(\+|-)?(\d+))([lL]|[fF])?'

# String literal
t_SCONST = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CCONST = r'(L)?\'([^\\\n]|(\\.))*?\''

# Comments
def t_comment(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')

# Preprocessor directive (ignored)
def t_preprocessor(t):
    r'\#(.)*?\n'
    t.lexer.lineno += 1
    
def t_error(t):
    print("Illegal character %s" % repr(t.value[0]))
    t.lexer.skip(1)
    
lexer = lex.lex(optimize=1)


#######################################################################
#######################         YACC        ###########################
#######################################################################

driverNumber = 0

# translation_unit:

def p_translation_unit_1(p):
    'translation_unit : external_declaration'
    p[0] = p[1]

def p_translation_unit_2(p):
    'translation_unit : translation_unit external_declaration'
    p[0] = p[1] + ' ' + p[2]

# external_declaration:
def p_external_declaration_1(p):
    'external_declaration : function_definition'
    p[0] = p[1]

def p_external_declaration_2(p):
    'external_declaration : statement'
    p[0] = p[1]

# function_definition:
def p_function_definition_1(p):
    'function_definition : type ID LPAREN parameter_list RPAREN LBRACE statement_list RBRACE'
    p[0] = p[1]+' '+p[2]+' ( '+p[4]+ ' ) { '+p[7]+' }'

def p_function_definition_2(p):
    'function_definition : type ID LPAREN parameter_list RPAREN LBRACE RBRACE'
    p[0] = p[1]+' '+p[2]+' ( '+p[4]+ ' ) { }'

# parameter_list:
def p_parameter_list_1(p):
    'parameter_list : parameter_declaration'
    p[0] = p[1]

def p_parameter_list_2(p):
    'parameter_list : parameter_list COMMA parameter_declaration'
    p[0] = p[1] + ' , ' + p[3]

# parameter_declaration:
def p_parameter_declaration_1(p):
    'parameter_declaration : primary_expression'
    p[0] = p[1]

def p_parameter_declaration_2(p):
    'parameter_declaration : type ID'
    p[0] = p[1] + ' ' + p[2]

def p_parameter_declaration_3(p):
    'parameter_declaration : type ID EQUALS assignment_expression'
    p[0] = p[1] + ' ' + p[2] + ' = ' + p[4]

# type:
def p_type_1(p):
    'type : INT'
    p[0] = p[1]

def p_type_2(p):
    'type : DOUBLE'
    p[0] = p[1]

def p_type_3(p):
    'type : CHAR'
    p[0] = p[1]

def p_type_4(p):
    'type : STRING'
    p[0] = p[1]

def p_type_5(p):
    'type : KEY'
    p[0] = p[1]

##################### Add more types here #############

# statement:
def p_statement_1(p):
    'statement : expression_statement'
    p[0] = p[1]

def p_statement_2(p):
    'statement : compound_statement'
    p[0] = p[1]

def p_statement_3(p):
    'statement : declaration_statement'
    p[0] = p[1]

def p_statement_4(p):
    'statement : selection_statement'
    p[0] = p[1]

def p_statement_5(p):
    'statement : iteration_statement'
    p[0] = p[1]

def p_statement_6(p):
    'statement : return_statement'
    p[0] = p[1]

def p_statement_7(p):
    'statement : break_statement'
    p[0] = p[1]

# iteration_statement:
def p_iteration_statement_1(p):
    'iteration_statement : REPEAT LPAREN expression RPAREN LBRACE statement_list RBRACE'
    p[0] = 'repeat ( ' + p[3] + ' ) { ' + p[6] + ' }'

def p_iteration_statement_2(p):
    'iteration_statement : UNTIL LPAREN expression RPAREN LBRACE statement_list RBRACE'
    p[0] = 'until ( ' + p[3] + ' ) { ' + p[6] + ' }'

# selection_statement:
def p_selection_statement_1(p):
    'selection_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE'
    p[0] = 'if ( ' + p[3] + ' ) ' + p[6]

def p_selection_statement_2(p):
    'selection_statement : IF LPAREN expression RPAREN LBRACE statement RBRACE ELSE LBRACE statement_list RBRACE'
    p[0] = 'if ( ' + p[3] + ' ) { ' + p[6] + ' } ( else ) { ' + p[10] + ' }'

# declaration_statement:
def p_declaration_statement_1(p):
    'declaration_statement : type ID SEMI'
    p[0] = p[1] + ' ' + p[2] + ' ;'

def p_declaration_statement_2(p):
    'declaration_statement : type ID EQUALS assignment_expression SEMI'
    p[0] = p[1] + ' ' + p[2] + ' = ' + p[4] + ' ;'

# compound_statement:
def p_compound_statement_1(p):
    'compound_statement : LBRACE RBRACE'
    p[0] = '{ }'

def p_compound_statement_2(p):
    'compound_statement : LBRACE statement_list RBRACE'
    p[0] = '{ '+p[2]+' }'

# expression_statement:
def p_expression_statement_1(p):
    'expression_statement : expression SEMI'
    p[0] = p[1] + ';'

def p_expression_statement_2(p):
    'expression_statement : SEMI'
    p[0] = ';'

# expression:
def p_expression_1(p):
    'expression : assignment_expression'
    p[0] = p[1]

def p_expression_2(p):
    'expression : function_expression'
    p[0] = p[1]

def p_expression_3(p):
    'expression : LPAREN expression RPAREN'
    p[0] = '( ' + p[2] + ' )'

# function_expression:
def p_function_expression_1(p):
    'function_expression : ID LPAREN parameter_list RPAREN'
    if p[1]=='start':
        if not p[3]=='':
            raise Exception('Start doesnot take arguments ...')
        else:
            global driverNumber
            driverNumber+=1
            p[0] = 'WebDriver driver'+ str(driverNumber) +' = new ChromeDriver()'
            
    elif p[1]=='open':
        try:
            global driverNumber
            url = str(p[3])
            p[0] = 'driver'+ str(driverNumber) +'.get('+p[3]+')'
        except:
            raise Exception('The URL parameter passed should be a string ...')

    elif p[1]=='close':
            global driverNumber
            p[0] = 'driver'+ str(driverNumber) +'.close()'
            driverNumber = driverNumber - 1
    else:
        p[0] = p[1] + ' ( ' + p[3] + ' ) '

# assignment_expression:
def p_assignment_expression_1(p):
    'assignment_expression : ID EQUALS assignment_expression'
    p[0] = p[1] + ' = ' + p[3]

def p_assignment_expression_3(p):
    'assignment_expression : logical_OR_expression EQUALS assignment_expression'
    p[0] = p[1] + ' = ' + p[3]

def p_assignment_expression_2(p):
    'assignment_expression : logical_OR_expression'
    p[0] = p[1]

# logical_OR_expression:
def p_logical_OR_expression_1(p):
    'logical_OR_expression : logical_AND_expression'
    p[0] = p[1]
    
def p_logical_OR_expression_2(p):
    'logical_OR_expression : logical_OR_expression LOR logical_AND_expression'
    p[0] = p[1] + ' || ' + p[3]

# logical_AND_expression:
def p_logical_AND_expression_1(p):
    'logical_AND_expression : equality_expression'
    p[0] = p[1]

def p_logical_AND_expression_2(p):
    'logical_AND_expression : logical_AND_expression LAND equality_expression'
    p[0] = p[1] + ' && ' + p[3]

# equality_expression:
def p_equality_expression_1(p):
    'equality_expression : relational_expression'
    p[0] = p[1]

def p_equality_expression_2(p):
    'equality_expression : equality_expression EQ relational_expression'
    p[0] = p[1] + ' == ' + p[3]

def p_equality_expression_3(p):
    'equality_expression : equality_expression NE relational_expression'
    p[0] = p[1] + ' != ' + p[3]

# relational_expression:
def p_relational_expression_1(p):
    'relational_expression : additive_expression'
    p[0] = p[1]

def p_relational_expression_2(p):
    'relational_expression : relational_expression LT additive_expression'
    p[0] = p[1] + ' < ' + p[3]

def p_relational_expression_3(p):
    'relational_expression : relational_expression GT additive_expression'
    p[0] = p[1] + ' > ' + p[3]

def p_relational_expression_4(p):
    'relational_expression : relational_expression LE additive_expression'
    p[0] = p[1] + ' <= ' + p[3]

def p_relational_expression_5(p):
    'relational_expression : relational_expression GE additive_expression'
    p[0] = p[1] + ' >= ' + p[3]

# additive_expression:
def p_additive_expression_1(p):
    'additive_expression : multiplicative_expression'
    p[0] = p[1]

def p_additive_expression_2(p):
    'additive_expression : additive_expression PLUS multiplicative_expression'
    p[0] = p[1] + ' + ' + p[3]

def p_additive_expression_3(p):
    'additive_expression : additive_expression MINUS multiplicative_expression'
    p[0] = p[1] + ' - ' + p[3]

# multiplicative_expression:
def p_multiplicative_expression_1(p):
    'multiplicative_expression : primary_expression'
    p[0] = p[1]

def p_multiplicative_expression_2(p):
    'multiplicative_expression : multiplicative_expression TIMES primary_expression'
    p[0] = p[1] + ' * ' + p[3]

def p_multiplicative_expression_3(p):
    'multiplicative_expression : multiplicative_expression DIVIDE primary_expression'
    p[0] = p[1] + ' / ' + p[3]

# statement_list:
def p_statement_list_1(p):
    'statement_list : statement'
    p[0] = p[1]

def p_statement_list_2(p):
    'statement_list : statement_list statement'
    p[0] = p[1] + ' ' + p[2]

# primary-expression:
def p_primary_expression_1(p):
    'primary_expression : LPAREN expression RPAREN'
    p[0] = '( ' + p[2] + ' )'

def p_primary_expression_2(p):
    'primary_expression : constant'
    p[0] = p[1]

def p_primary_expression_3(p):
    'primary_expression : ID'
    p[0]= p[1]

def p_primary_expression_4(p):
    'primary_expression : reserved'
    p[0]= p[1]

def p_primary_expression_5(p):
    'primary_expression : empty'
    p[0] = p[1]

# constant:
def p_constant_1(p): 
   'constant : ICONST'
   p[0] = str(p[1])

def p_constant_2(p):
    'constant : FCONST'
    p[0] = str(p[1])

def p_constant_3(p):
    'constant : SCONST'
    p[0] = p[1]

#reserved:
def p_reserved_1(p):
    'reserved : ENTER'
    p[0] = p[1]

############################ Fill all the KEYtypes here

# return_statement:
def p_return_statement_1(p):
    'return_statement : RETURN SEMI'
    p[0] = 'return ;'

def p_return_statement_2(p):
    'return_statement : RETURN expression SEMI'
    p[0] = 'return ' + p[2] + ' ;'

# break_statement:
def p_break_statement_1(p):
    'break_statement : BREAK SEMI'
    p[0] = 'break ;'

# empty:
def p_empty(p):
    'empty : '
    p[0] = ''

# error:
def p_error(p):
    print("Whoa. We're hosed.")

##import profile
# Build the grammar

parser = yacc.yacc(method='LALR')

##profile.run("yacc.yacc(method='LALR')")

##s = 'int abc ( int x = 1 != 2 != 3, 1) { string i = "String initialization"; key k = enter; cde = def = 4 != 6 < 8 > 7 + 4 * (8); abc( (1) , 1 ); xyz = "I am a String"; if(x==1){x = 2;} else {x = 1;} return (1);} { abc = 2 || 3 && 4 == 5 <= 8 >= 7 - 3 * 1; repeat(20){ x = 1;} until(x<y) { y=y+1; break;}}'
f = open('/Users/Rafica/Documents/Github/iWAL/test.txt','r')
s = f.read()
f.close()

result = parser.parse(s)
print result
