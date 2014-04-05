# ----------------------------------------------------------------------
# ilex.py
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
    'UNION', 'UNSIGNED', 'VOID', 'VOLATILE', 'WHILE'
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
    pass

def p_external_declaration_2(p):
    'external_declaration : statement'
    p[0] = p[1]

# function_definition:
def p_function_definition_1(p):
    'function_definition : type ID LPAREN primary_expression RPAREN LBRACE statement_list RBRACE'
    p[0] = p[1]+' '+p[2]+' ( '+p[4]+ ' ) { '+p[7]+' }'
    pass

def p_function_definition_2(p):
    'function_definition : type ID LPAREN primary_expression RPAREN LBRACE RBRACE'
    p[0] = p[1]+' '+p[2]+' ( '+p[4]+ ' ) { }'
    pass

# type:
def p_type_1(p):
    'type : INT'
    p[0] = p[1]

##################### Add more types here #############

# statement:
def p_statement_1(p):
    'statement : expression_statement'
    p[0] = p[1]
    pass

def p_statement_2(p):
    'statement : compound_statement'
    p[0] = p[1]
    pass

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

# assignment_expression:
def p_assignment_expression_1(p):
    'assignment_expression : ID EQUALS primary_expression'
    p[0] = p[1] + ' = ' + p[3]
    
def p_assignment_expression_2(p):
    'assignment_expression : logical_OR_expression'
    p[0] = p[1]

# logical_OR_expression:
##def p_logical_OR_expression_1(p):
##    'logical_OR_expression : logical_OR_expression LOR primary_expression'
##    p[0] = p[1] + ' || ' + p[3]

def p_logical_OR_expression_2(p):
    'logical_OR_expression : primary_expression'
    p[0] = p[1]

# compound_statement:
def p_compound_statement_1(p):
    'compound_statement : LBRACE RBRACE'
    p[0] = '{ }'

def p_compound_statement_2(p):
    'compound_statement : LBRACE statement_list RBRACE'
    p[0] = '{ '+p[2]+' }'

# statement_list:
def p_statement_list_1(p):
    'statement_list : statement'
    p[0] = p[1]

def p_statement_list_2(p):
    'statement_list : statement_list statement'
    p[0] = p[1] + ' ' + p[2]

# primary-expression:
def p_primary_expression_1(p):
    'primary_expression : constant'
    p[0] = p[1]
    pass

def p_primary_expression_2(p):
    'primary_expression : empty'
    p[0] = p[1]
    pass

# constant:
def p_constant(p): 
   'constant : ICONST'
   p[0] = str(p[1])
   pass

def p_empty(t):
    'empty : '
    p[0] = ''
    pass

def p_error(t):
    print("Whoa. We're hosed")

##import profile
# Build the grammar

parser = yacc.yacc(method='LALR')

##profile.run("yacc.yacc(method='LALR')")

s = 'int abc ( 1 ) { abc=2; } { abc=2; }'
##f = open('/Users/nithin/Desktop/Spring_2014/PLT/project/compiler/hello.txt','r')
##s = f.read()
##f.close()

result = parser.parse(s)
print result
