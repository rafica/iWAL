import unittest
import sys

from cStringIO import StringIO
from itertools import izip

sys.path.append('..')
import ilexer

class Testing_iLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = ilexer.mainLex()
    def test_tokens(self):
        """
        Checks the correctness of single tokens
        """
        cases = {'a_iden45' : 'ID',
        #'$%flawed' : 'ID',
        '4yetanother_' : 'ID',
        '+' : 'PLUS',
        '-' : 'MINUS',
        '*' : 'TIMES',         
        '/' : 'DIVIDE',
        '|' : 'OR',
        '&' : 'AND',
        '||': 'LOR',
        '&&': 'LAND',
        '!':  'LNOT',
        '<':  'LT',
        '<=': 'LE',
        '>':  'GT',
        '>=': 'GE',
        '==': 'EQ',
        '!=': 'NE',
        '=':'EQUALS',
        '(' : 'LPAREN',
        ')' : 'RPAREN',
        '[' : 'LBRACKET',
        ']' : 'RBRACKET',
        '{' : 'LBRACE',
        '}' : 'RBRACE',
        ',' : 'COMMA',
        ';' : 'SEMICOLON',
        ';' : 'SEMI',         
        ':' : 'COLON',
        'This check !! %%%3#;.5553@@LLO WORLD':'STRING',
        #'// This is an iWAL comment !!' : 'COMMENT',
        '/* This is a block iWAL comment !! \*/' : 'COMMENT'}
        self.assert_tokens_eq(cases)
        
    def assert_tokens_eq(self, cases):
        """
        Takes in dictionary of value inputs and checks for type and
        value
        correctness of the LexToken output
        """
        for key, val in cases.iteritems():
            self.lexer.input(str(key))
            token = self.lexer.token()
            self.assertEqual(key, token.value)
            self.assertEqual(val, token.type)
    def test_msgenroll(self):
        """
        Checks the correctness of msgenroll program
        """
        progfile = open('msgenroll.txt', 'r')
        expfile = open('msgenroll_lexoutput.txt', 'r')
        self.assert_prog(progfile, expfile)
    
     
    def assert_prog(self, progfile, expfile):
        """
        Takes in an iWAL programming file and expected output file and
        checks for
        correctness
        """
        lines = progfile.readlines()
        for line in lines:
            self.lexer.input(line)
            tokens = ""
            tok = self.lexer.token()
            if not tok:
                break
            tokens += str(tok) + "\n"
            StringIO(tokens)
        for t, o in izip(tokens, expfile):
            self.assertEqual(t, o)
            
##if __name__ == "__main__":
##    unittest.main(verbosity=2)
            
suite = unittest.TestLoader().loadTestsFromTestCase(Testing_iLexer)
unittest.TextTestRunner(verbosity=2).run(suite)


