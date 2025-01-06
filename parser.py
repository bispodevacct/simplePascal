import ply.yacc as yacc

from lexer import tokens
from exemplo import source

start = 'programa'

def p_empty(p):
    '''empty :'''
    pass

def p_programa(p):
    '''programa : declaracoes bloco'''

    p[0] = ('programa', p[1], p[2])

def p_bloco(p):
    '''bloco : BEGIN comando lista_com END'''

    p[0] = ('bloco', p[1], p[2], p[3], p[4])

def p_declaracoes(p):
    '''declaracoes : def_const def_tipos def_var def_rotina'''

    p[0] = ('declaracoes', p[1], p[2], p[3], p[4])

def p_def_const(p):
    '''def_const : constante def_const
                 | empty'''

    if len(p) == 3:
        p[0] = ('def_const', p[1], p[2])
    else:
        p[0] = ('def_const',)

def p_def_tipos(p):
    '''def_tipos : tipo def_tipos
                 | empty'''

    if len(p) == 3:
        p[0] = ('def_tipos', p[1], p[2])
    else:
        p[0] = ('def_tipos',)

def p_def_var(p):
    '''def_var : variavel def_var
               | empty'''

    if len(p) == 3:
        p[0] = ('def_var', p[1], p[2])
    else:
        p[0] = ('def_var',)

def p_def_rotina(p):
    '''def_rotina : rotina def_rotina
                  | empty'''

    if len(p) == 3:
        p[0] = ('def_rotina', p[1], p[2])
    else:
        p[0] = ('def_rotina',)

def p_id(p):
    '''id : ID'''

    p[0] = ('id', p[1])

def p_numero(p):
    '''numero : NUMERO'''

    p[0] = ('numero', p[1])

def p_constante(p):
    '''constante : CONST id EQUAL const_valor SEMICOLON'''

    p[0] = ('constante', p[1], p[2], p[3], p[4], p[5])

def p_const_valor(p):
    '''const_valor : CONST_VALOR
                   | exp_const'''

    p[0] = ('const_valor', p[1])

def p_tipo(p):
    '''tipo : TYPE id EQUAL tipo_dado SEMICOLON'''

    p[0] = ('tipo', p[1], p[2], p[3], p[4], p[5])

def p_variavel(p):
    '''variavel : VAR campo SEMICOLON'''

    p[0] = ('variavel', p[1], p[2], p[3])

def p_lista_id(p):
    '''lista_id : COMMA id lista_id
                | empty'''

    if len(p) == 4:
        p[0] = ('lista_id', p[1], p[2], p[3])
    else:
        p[0] = ('lista_id',)

def p_campos(p):
    '''campos : campo lista_campos'''

    p[0] = ('campos', p[1], p[2])

def p_campo(p):
    '''campo : id lista_id COLON tipo_dado'''

    p[0] = ('campo', p[1], p[2], p[3], p[4])

def p_lista_campos(p):
    '''lista_campos : SEMICOLON campo lista_campos
                    | empty'''

    if len(p) == 4:
        p[0] = ('lista_campos', p[1], p[2], p[3])
    else:
        p[0] = ('lista_campos',)

def p_tipo_dado(p):
    '''tipo_dado : INTEGER
                 | REAL
                 | CHAR
                 | BOOLEAN
                 | ARRAY LB numero RB OF tipo_dado
                 | RECORD campos END
                 | id'''

    if len(p) == 2:
        p[0] = ('tipo_dado', p[1])
    elif len(p) == 4:
        p[0] = ('tipo_dado', p[1], p[2], p[3])
    else:
        p[0] = ('tipo_dado', p[1], p[2], p[3], p[4], p[5], p[6])

def p_rotina(p):
    '''rotina : FUNCTION id param_rotina COLON tipo_dado bloco_rotina
              | PROCEDURE id param_rotina bloco_rotina'''

    if len(p) == 7:
        p[0] = ('rotina', p[1], p[2], p[3], p[4], p[5], p[6])
    else:
        p[0] = ('rotina', p[1], p[2], p[3], p[4])

def p_param_rotina(p):
    '''param_rotina : LP campos RP
                    | empty'''

    if len(p) == 4:
        p[0] = ('param_rotina', p[1], p[2], p[3])
    else:
        p[0] = ('param_rotina',)

def p_bloco_rotina(p):
    '''bloco_rotina : def_var bloco'''

    p[0] = ('bloco_rotina', p[1], p[2])

def p_lista_com(p):
    '''lista_com : SEMICOLON comando lista_com
                 | empty'''

    if len(p) == 4:
        p[0] = ('lista_com', p[1], p[2], p[3])
    else:
        p[0] = ('lista_com',)

def p_bloco_com(p):
    '''bloco_com : bloco
                 | comando'''

    p[0] = ('bloco_com', p[1])

def p_comando(p):
    '''comando : id nome atribuicao
               | WHILE exp_com DO bloco_com
               | IF exp_com THEN bloco_com else
               | FOR for DO bloco_com
               | WRITE const_valor
               | READ id nome'''

    if len(p) == 3:
        p[0] = ('comando', p[1], p[2])
    elif len(p) == 4:
        p[0] = ('comando', p[1], p[2], p[3])
    elif len(p) == 5:
        p[0] = ('comando', p[1], p[2], p[3], p[4])
    else:
        p[0] = ('comando', p[1], p[2], p[3], p[4], p[5])

def p_for(p):
    '''for : id COLONEQUAL parametro TO parametro'''

    p[0] = ('for', p[1], p[2], p[3], p[4], p[5])

def p_else(p):
    '''else : ELSE bloco_com
            | empty'''

    if len(p) == 3:
        p[0] = ('else', p[1], p[2])
    else:
        p[0] = ('else',)

def p_atribuicao(p):
    '''atribuicao : COLONEQUAL exp
                  | empty'''

    if len(p) == 3:
        p[0] = ('atribuicao', p[1], p[2])
    else:
        p[0] = ('atribuicao',)

def p_lista_param(p):
    '''lista_param : parametro COMMA lista_param
                   | parametro
                   | empty'''

    if len(p) == 4:
        p[0] = ('lista_param', p[1], p[2], p[3])
    else:
        p[0] = ('lista_param',)

def p_exp(p):
    '''exp : parametro exp_l1
           | LP parametro exp_l2'''

    if len(p) == 3:
        p[0] = ('exp', p[1], p[2])
    else:
        p[0] = ('exp', p[1], p[2], p[3])

def p_exp_l1(p):
    '''exp_l1 : op_mat exp
              | param_logico exp_logico
              | empty'''

    if len(p) == 3:
        p[0] = ('exp_l1', p[1], p[2])
    else:
        p[0] = ('exp_l1',)

def p_exp_logico(p):
    '''exp_logico : op_logico exp
                  | empty'''

    if len(p) == 3:
        p[0] = ('exp_logico', p[1], p[2])
    else:
        p[0] = ('exp_logico',)

def p_param_logico(p):
    '''param_logico : op_comp parametro
                    | empty'''

    if len(p) == 3:
        p[0] = ('param_logico', p[1], p[2])
    else:
        p[0] = ('param_logico',)

def p_exp_l2(p):
    '''exp_l2 : op_mat exp RP
              | param_logico op_logico exp RP'''

    if len(p) == 3:
        p[0] = ('exp_l2', p[1], p[2])
    else:
        p[0] = ('exp_l2', p[1], p[2], p[3])

def p_exp_const(p):
    '''exp_const : parametro exp_const_l
                 | LP parametro op_mat exp_const RP'''

    if len(p) == 2:
        p[0] = ('exp_const', p[1], p[2])
    else:
        p[0] = ('exp_const', p[1], p[2], p[3], p[4], p[5])

def p_exp_const_l(p):
    '''exp_const_l : op_mat exp_const
                   | empty'''

    if len(p) == 3:
        p[0] = ('exp_const_l', p[1], p[2])
    else:
        p[0] = ('exp_const_l',)

def p_exp_com(p):
    '''exp_com : parametro param_logico exp_com_l
               | LP parametro param_logico op_logico exp_com RP'''

    if len(p) == 4:
        p[0] = ('exp_com', p[1], p[2], p[3])
    else:
        p[0] = ('exp_com', p[1], p[2], p[3], p[4], p[5], p[6])

def p_exp_com_l(p):
    '''exp_com_l : op_logico exp_com
                 | empty'''

    if len(p) == 3:
        p[0] = ('exp_com_l', p[1], p[2])
    else:
        p[0] = ('exp_com_l',)

def p_parametro(p):
    '''parametro : id nome
                 | numero
                 | FALSE
                 | TRUE'''

    if len(p) == 3:
        p[0] = ('parametro', p[1], p[2])
    else:
        p[0] = ('parametro', p[1])

def p_op_logico(p):
    '''op_logico : AND
                 | OR'''

    p[0] = ('op_logico', p[1])

def p_op_comp(p):
    '''op_comp : GREAT
               | LESS
               | EQUALEQUAL
               | NOTEQUAL
               | GEQUAL
               | LEQUAL'''

    p[0] = ('op_comp', p[1])

def p_op_mat(p):
    '''op_mat : PLUS
              | MINUS
              | MULTIPLY
              | DIVIDE'''

    p[0] = ('op_mat', p[1])

def p_nome(p):
    '''nome : DOT id nome
            | LB parametro RB
            | LP lista_param RP
            | empty'''

    if len(p) == 4:
        p[0] = ('nome', p[1], p[2], p[3])
    else:
        p[0] = ('nome',)

parser = yacc.yacc()