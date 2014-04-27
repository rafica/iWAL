# lextab.py. This file automatically created by PLY (version 3.4). Don't edit!
_tabversion   = '3.4'
_lextokens    = {'VOID': 1, 'LBRACKET': 1, 'MINUS': 1, 'RPAREN': 1, 'LONG': 1, 'PLUS': 1, 'ELLIPSIS': 1, 'GT': 1, 'RBRACE': 1, 'ENUM': 1, 'PERIOD': 1, 'GE': 1, 'ICONST': 1, 'ENTER': 1, 'DOUBLE': 1, 'MINUSEQUAL': 1, 'TIMESEQUAL': 1, 'OR': 1, 'SHORT': 1, 'RETURN': 1, 'RSHIFTEQUAL': 1, 'STATIC': 1, 'SIZEOF': 1, 'FCONST': 1, 'UNSIGNED': 1, 'UNION': 1, 'COLON': 1, 'REPEAT': 1, 'DIVIDE': 1, 'FOR': 1, 'PLUSPLUS': 1, 'EQUALS': 1, 'ELSE': 1, 'EQ': 1, 'UNTIL': 1, 'AND': 1, 'TYPEID': 1, 'LBRACE': 1, 'INT': 1, 'SIGNED': 1, 'CONTINUE': 1, 'NOT': 1, 'OREQUAL': 1, 'MOD': 1, 'RSHIFT': 1, 'DEFAULT': 1, 'CHAR': 1, 'WHILE': 1, 'DIVEQUAL': 1, 'EXTERN': 1, 'CASE': 1, 'LAND': 1, 'REGISTER': 1, 'MODEQUAL': 1, 'NE': 1, 'SCONST': 1, 'SWITCH': 1, 'PLUSEQUAL': 1, 'BREAK': 1, 'VOLATILE': 1, 'KEY': 1, 'ANDEQUAL': 1, 'DO': 1, 'LNOT': 1, 'CONST': 1, 'LOR': 1, 'LSHIFT': 1, 'GOTO': 1, 'LE': 1, 'SEMI': 1, 'LT': 1, 'COMMA': 1, 'CCONST': 1, 'TYPEDEF': 1, 'XOR': 1, 'STRING': 1, 'AUTO': 1, 'TIMES': 1, 'LPAREN': 1, 'MINUSMINUS': 1, 'ID': 1, 'IF': 1, 'STRUCT': 1, 'FLOAT': 1, 'XOREQUAL': 1, 'LSHIFTEQUAL': 1, 'RBRACKET': 1}
_lexreflags   = 0
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_NEWLINE>\\n+)|(?P<t_ID>[A-Za-z_][\\w_]*)|(?P<t_comment>/\\*(.|\\n)*?\\*/)|(?P<t_preprocessor>\\#(.)*?\\n)|(?P<t_FCONST>((\\d+)(\\.\\d+)(e(\\+|-)?(\\d+))? | (\\d+)e(\\+|-)?(\\d+))([lL]|[fF])?)|(?P<t_ICONST>\\d+([uU]|[lL]|[uU][lL]|[lL][uU])?)|(?P<t_CCONST>(L)?\\\'([^\\\\\\n]|(\\\\.))*?\\\')|(?P<t_SCONST>\\"([^\\\\\\n]|(\\\\.))*?\\")|(?P<t_ELLIPSIS>\\.\\.\\.)|(?P<t_PLUSPLUS>\\+\\+)|(?P<t_LOR>\\|\\|)|(?P<t_OREQUAL>\\|=)|(?P<t_PLUSEQUAL>\\+=)|(?P<t_RSHIFTEQUAL>>>=)|(?P<t_TIMESEQUAL>\\*=)|(?P<t_LSHIFTEQUAL><<=)|(?P<t_RBRACE>\\})|(?P<t_XOREQUAL>^=)|(?P<t_NE>!=)|(?P<t_PLUS>\\+)|(?P<t_MINUSMINUS>--)|(?P<t_OR>\\|)|(?P<t_LBRACE>\\{)|(?P<t_PERIOD>\\.)|(?P<t_DIVEQUAL>/=)|(?P<t_XOR>\\^)|(?P<t_TIMES>\\*)|(?P<t_RBRACKET>\\])|(?P<t_LBRACKET>\\[)|(?P<t_GE>>=)|(?P<t_RPAREN>\\))|(?P<t_LAND>&&)|(?P<t_LSHIFT><<)|(?P<t_LE><=)|(?P<t_RSHIFT>>>)|(?P<t_ANDEQUAL>&=)|(?P<t_MINUSEQUAL>-=)|(?P<t_MODEQUAL>%=)|(?P<t_LPAREN>\\()|(?P<t_EQ>==)|(?P<t_DIVIDE>/)|(?P<t_AND>&)|(?P<t_SEMI>;)|(?P<t_MINUS>-)|(?P<t_MOD>%)|(?P<t_EQUALS>=)|(?P<t_GT>>)|(?P<t_NOT>~)|(?P<t_COMMA>,)|(?P<t_LT><)|(?P<t_COLON>:)|(?P<t_LNOT>!)', [None, ('t_NEWLINE', 'NEWLINE'), ('t_ID', 'ID'), ('t_comment', 'comment'), None, ('t_preprocessor', 'preprocessor'), None, (None, 'FCONST'), None, None, None, None, None, None, None, None, None, None, (None, 'ICONST'), None, (None, 'CCONST'), None, None, None, (None, 'SCONST'), None, None, (None, 'ELLIPSIS'), (None, 'PLUSPLUS'), (None, 'LOR'), (None, 'OREQUAL'), (None, 'PLUSEQUAL'), (None, 'RSHIFTEQUAL'), (None, 'TIMESEQUAL'), (None, 'LSHIFTEQUAL'), (None, 'RBRACE'), (None, 'XOREQUAL'), (None, 'NE'), (None, 'PLUS'), (None, 'MINUSMINUS'), (None, 'OR'), (None, 'LBRACE'), (None, 'PERIOD'), (None, 'DIVEQUAL'), (None, 'XOR'), (None, 'TIMES'), (None, 'RBRACKET'), (None, 'LBRACKET'), (None, 'GE'), (None, 'RPAREN'), (None, 'LAND'), (None, 'LSHIFT'), (None, 'LE'), (None, 'RSHIFT'), (None, 'ANDEQUAL'), (None, 'MINUSEQUAL'), (None, 'MODEQUAL'), (None, 'LPAREN'), (None, 'EQ'), (None, 'DIVIDE'), (None, 'AND'), (None, 'SEMI'), (None, 'MINUS'), (None, 'MOD'), (None, 'EQUALS'), (None, 'GT'), (None, 'NOT'), (None, 'COMMA'), (None, 'LT'), (None, 'COLON'), (None, 'LNOT')])]}
_lexstateignore = {'INITIAL': ' \t\x0c'}
_lexstateerrorf = {'INITIAL': 't_error'}
