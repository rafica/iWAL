import sys, subprocess

import ply.lex as lex
import pprint

# Reserved words
reserved = (
    'BREAK', 'CHAR', 'CONST', 'CONTINUE', 'DEFAULT', 'DOUBLE',
    'ELSE', 'IF', 'INT','RETURN', 'VOID', 'KEY',
    'STRING', 'ENTER', 'REPEAT', 'UNTIL', 'BOOLEAN', 'TRUE', 'FALSE'
    )

tokens = reserved + (
    # Literals (identifier, integer constant, float constant, string constant, char const)
    'ID', 'TYPEID', 'ICONST', 'FCONST', 'SCONST', 'CCONST',

    # Operators (+,-,*,/,|, &, ||, &&, !, <, <=, >, >=, ==, !=)
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'OR', 'AND',
    'LOR', 'LAND', 'LNOT',
    'LT', 'LE', 'GT', 'GE', 'EQ', 'NE',
    
    # Assignment (=)
    'EQUALS',
    
    # Delimeters ( ) [ ] { } , . ; :
    'LPAREN', 'RPAREN',
    'LBRACKET', 'RBRACKET',
    'LBRACE', 'RBRACE',
    'COMMA', 'SEMI', 'COLON'
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
t_OR               = r'\|'
t_AND              = r'&'
t_NOT              = r'~'
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

# Delimeters
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LBRACE           = r'\{'
t_RBRACE           = r'\}'
t_COMMA            = r','
t_SEMI             = r';'
t_COLON            = r':'

# Identifiers and reserved words

reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"ID")
    return t

# Integer literal
def t_ICONST(t):
    r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'
##t_ICONST = r'(\+|-)?\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Floating literal
t_FCONST = r'((\d+)(\.\d+)(e(\+|-)?(\d+))?|(\d+)e(\+|-)?(\d+))([lL]|[fF])?'

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

def mainLex():
    lexer = lex.lex(optimize=1)
    return lexer

##lexer = lex.lex()

## For testing LEX
##f=open('test.txt')
##lines = f.readlines()
##for line in lines:
##    lexer.input(line)
##    tok = lexer.token()
##    if not tok: break      # No more input
##    print tok

