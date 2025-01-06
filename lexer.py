import ply.lex as lex

# Tokens
reserved = {
    'begin':        'BEGIN',
    # 'end':          'END',
    'const':        'CONST',
    'type':         'TYPE',
    'var':          'VAR',
    'integer':      'INTEGER',
    'real':         'REAL',
    'char':         'CHAR',
    'boolean':      'BOOLEAN',
    'array':        'ARRAY',
    'of':           'OF',
    'record':       'RECORD',
    'function':     'FUNCTION',
    'procedure':    'PROCEDURE',
    'while':        'WHILE',
    'do':           'DO',
    'if':           'IF',
    'then':         'THEN',
    'for':          'FOR',
    'write':        'WRITE',
    'read':         'READ',
    'to':           'TO',
    'else':         'ELSE',
    'false':        'FALSE',
    'true':         'TRUE',
    'and':          'AND',
    'or':           'OR'
}

tokens = [
    'ID',
    'NUMERO',
    'CONST_VALOR',
    'EQUAL',
    'SEMICOLON',
    'COLON',
    'LB',
    'RB',
    'LP',
    'RP',
    'COLONEQUAL',
    'COMMA',
    'GREAT',
    'LESS',
    'EQUALEQUAL',
    'NOTEQUAL',
    'GEQUAL',
    'LEQUAL',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'DOT',
    'END'
] + list(reserved.values())

# t_ID =          r'([a-z]|[A-Z])+\d*'
# t_NUMERO =      r'\d+(\.\d+)?'
# t_CONST_VALOR = r'"\w*(\s|\w)*"'
t_EQUAL =       r'='
t_SEMICOLON =   r';'
t_COLON =       r':'
t_LB =          r'\['
t_RB =          r'\]'
t_LP =          r'\('
t_RP =          r'\)'
t_COLONEQUAL =  r':='
t_COMMA =       r','
t_GREAT =       r'>'
t_LESS =        r'<'
t_EQUALEQUAL =  r'=='
t_NOTEQUAL =    r'!='
t_GEQUAL =      r'>='
t_LEQUAL =      r'<='
t_PLUS =        r'\+'
t_MINUS =       r'-'
t_MULTIPLY =    r'\*'
t_DIVIDE =      r'/'
t_DOT =         r'\.'

t_ignore =      ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
    r'([a-z]|[A-Z])+\d*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.type = reserved.get(t.value,'NUMERO')    # Check for reserved words
    return t

def t_CONST_VALOR(t):
    r'"\w*(\s|\w)*"'
    t.type = reserved.get(t.value,'CONST_VALOR')    # Check for reserved words
    return t

def t_END(t):
    r'end'
    t.type = reserved.get(t.value,'END')    # Check for reserved words
    return t

def t_error(t):
    print(f'Illegal character {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()