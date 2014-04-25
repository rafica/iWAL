import sys, subprocess
import ply.lex as lex
import pprint

class ilex:
                
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
        def t_NEWLINE(self,t):
            r'\n+'
            t.lexer.lineno += t.value.count("\n")

        # Compute column.
        # input is the input text string
        # token is a token instance
        def find_column(self,input, token):
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

        def t_ID(self,t):
                r'[A-Za-z_][\w_]*'
                t.type = self.reserved_map.get(t.value,'ID')
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
        def t_comment(self,t):
            r'/\*(.|\n)*?\*/'
            t.lexer.lineno += t.value.count('\n')

        # Preprocessor directive (ignored)
        def t_preprocessor(t):
            r'\#(.)*?\n'
            t.lexer.lineno += 1
            
        def t_error(t):
            print("Illegal character %s" % repr(t.value[0]))
            t.lexer.skip(1)

        def map_it(self):
                self.reserved_map = {}
                for r in self.reserved:
                        self.reserved_map[r.lower()] = r
                
        def get_lexer(self):
                return self.lexer

        def build(self):
                self.lexer = lex.lex(module=self,optimize=1)    
        
        def tok_str(self, data): 
                self.lexer.input(data) 
                tok_str = ""
                while True: 
                        tok = self.lexer.token() 
                        if not tok: 
                                break 
                tok_str += str(tok) + "\n" 
                return tok_str 
        # if __name__ == "__main__": 
        #       il = ilex()
        #       il.build() 
        #       l = il.get_lexer()
        #       f = open('../test.txt','r')
        #       lines = f.readlines()
        #       for line in lines:
        #               print il.tok_str(line) 
        #       f.close()
il = ilex()
il.map_it()
il.build() 
l = il.get_lexer()

print 'Enter string:'
while(1):
        line = raw_input()
        print il.tok_str(line)
        print'more'
        
print 'End'
##f = open('../test.txt','r')
##lines = f.readlines()
##for line in lines:
##        print il.tok_str(line) 
##f.close()
