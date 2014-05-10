# lextab.py. This file automatically created by PLY (version 3.4). Don't edit!
_tabversion   = '3.4'
_lextokens    = {'LNOT': 1, 'CONST': 1, 'DEFAULT': 1, 'VOID': 1, 'CHAR': 1, 'LOR': 1, 'GT': 1, 'RETURN': 1, 'TRUE': 1, 'MINUS': 1, 'DIVIDE': 1, 'LAND': 1, 'RPAREN': 1, 'FCONST': 1, 'SEMI': 1, 'COLON': 1, 'NE': 1, 'SCONST': 1, 'UNTIL': 1, 'LT': 1, 'BOOLEAN': 1, 'PLUS': 1, 'COMMA': 1, 'CCONST': 1, 'REPEAT': 1, 'STRING': 1, 'EQUALS': 1, 'RBRACE': 1, 'ELSE': 1, 'GE': 1, 'LE': 1, 'ICONST': 1, 'LPAREN': 1, 'ENTER': 1, 'TIMES': 1, 'EQ': 1, 'ID': 1, 'IF': 1, 'AND': 1, 'TYPEID': 1, 'LBRACE': 1, 'FALSE': 1, 'INT': 1, 'DOUBLE': 1, 'BREAK': 1, 'CONTINUE': 1, 'KEY': 1, 'RBRACKET': 1, 'LBRACKET': 1, 'OR': 1}
_lexreflags   = 0
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_NEWLINE>\\n+)|(?P<t_ID>[A-Za-z_][\\w_]*)|(?P<t_ICONST>\\d+([uU]|[lL]|[uU][lL]|[lL][uU])?)|(?P<t_comment>/\\*(.|\\n)*?\\*/)|(?P<t_preprocessor>\\#(.)*?\\n)|(?P<t_FCONST>((\\d+)(\\.\\d+)(e(\\+|-)?(\\d+))?|(\\d+)e(\\+|-)?(\\d+))([lL]|[fF])?)|(?P<t_CCONST>(L)?\\\'([^\\\\\\n]|(\\\\.))*?\\\')|(?P<t_SCONST>\\"([^\\\\\\n]|(\\\\.))*?\\")|(?P<t_LOR>\\|\\|)|(?P<t_OR>\\|)|(?P<t_LE><=)|(?P<t_LBRACKET>\\[)|(?P<t_NE>!=)|(?P<t_RBRACE>\\})|(?P<t_LPAREN>\\()|(?P<t_LBRACE>\\{)|(?P<t_TIMES>\\*)|(?P<t_RBRACKET>\\])|(?P<t_GE>>=)|(?P<t_RPAREN>\\))|(?P<t_LAND>&&)|(?P<t_EQ>==)|(?P<t_PLUS>\\+)|(?P<t_AND>&)|(?P<t_NOT>~)|(?P<t_COMMA>,)|(?P<t_DIVIDE>/)|(?P<t_LT><)|(?P<t_SEMI>;)|(?P<t_MINUS>-)|(?P<t_COLON>:)|(?P<t_EQUALS>=)|(?P<t_LNOT>!)|(?P<t_GT>>)', [None, ('t_NEWLINE', 'NEWLINE'), ('t_ID', 'ID'), ('t_ICONST', 'ICONST'), None, ('t_comment', 'comment'), None, ('t_preprocessor', 'preprocessor'), None, (None, 'FCONST'), None, None, None, None, None, None, None, None, None, None, (None, 'CCONST'), None, None, None, (None, 'SCONST'), None, None, (None, 'LOR'), (None, 'OR'), (None, 'LE'), (None, 'LBRACKET'), (None, 'NE'), (None, 'RBRACE'), (None, 'LPAREN'), (None, 'LBRACE'), (None, 'TIMES'), (None, 'RBRACKET'), (None, 'GE'), (None, 'RPAREN'), (None, 'LAND'), (None, 'EQ'), (None, 'PLUS'), (None, 'AND'), (None, 'NOT'), (None, 'COMMA'), (None, 'DIVIDE'), (None, 'LT'), (None, 'SEMI'), (None, 'MINUS'), (None, 'COLON'), (None, 'EQUALS'), (None, 'LNOT'), (None, 'GT')])]}
_lexstateignore = {'INITIAL': ' \t\x0c'}
_lexstateerrorf = {'INITIAL': 't_error'}
