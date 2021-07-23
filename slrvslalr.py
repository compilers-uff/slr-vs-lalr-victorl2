from ply.lex import lex
from ply.yacc import yacc

tokens = ('ID', 'MULT', 'EQ')
t_ID = r'id'
t_EQ = r'='
t_MULT = r'\*'
t_ignore = ' \t'


def t_error(t):
    print("Caractere '%s' inválido" % t.value[0])
    t.lexer.skip(1)

lexer = lex()

def p_expression_L_EQ_R(p):
    """
    S : L EQ R
    """

def p_expression_R(p):
    """
    S : R
    """

def p_L_MULT_R(p):
    """
    L : MULT R
    """

def p_L_ID(p):
    """
    L : ID
    """

def p_R_L(p):
    """
    R : L
    """

def p_error(p):
    print(p)


if __name__ == '__main__':
    slr_parser = yacc(method='SLR', debugfile='slr_parser.out', tabmodule='slr_parsetab')
    lalr_parser = yacc(method='LALR', debugfile='lalr_parser.out', tabmodule='lalr_parsetab')