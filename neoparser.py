import ply.yacc as yacc

from lexer import tokens

start = 'programa'

def p_programa(p):
    '''programa : bloco'''

    p[0] = ('programa', p[1])

def p_bloco(p):
    '''bloco : BEGIN comando END'''

    p[0] = ('bloco', p[1], p[2], p[3])

def p_comando(p):
    '''comando : WRITE const_valor'''
    
    p[0] = ('comando', p[1], p[2])

def p_const_valor(p):
    '''const_valor : CONST_VALOR'''

    p[0] = ('const_valor', p[1])

parser = yacc.yacc()