import os
import shutil
from ply.lex import lex
from ply.yacc import yacc


tokens = ('id', 'MULT', 'EQ')

t_EQ = r'='
t_MULT = r'\*'
t_ignore = '\t'

def t_error(t):
    print("Caractere '%s' inválido" % t.value[0])
    t.lexer.skip(1)

def p_equality(p):
    """
    S : L EQ R
    """
    return p

def p_initial_simple_transform(p):
    """
    S : R
    """
    return p

def p_multiplication(p):
    """
    L : MULT R
    """
    return p

def p_define_id(p):
    """
    L : id
    """
    return p

def p_simple_transform(p):
    """
    R : L
    """
    return p

def p_error(p):
    print(f"Erro de sintaxe: {p.value!r}")

# gerando parsers SLR e LALR e salvando saidas na pasta outputs
if __name__ == '__main__':
    # gerando parsers SLR e LALR
    yacc(method='SLR', debugfile='slr_parser.out', tabmodule='slr_parsetab')
    yacc(method='LALR', debugfile='lalr_parser.out', tabmodule='lalr_parsetab')

    # criando pasta de outputs
    output_folder = "outputs"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # movendo os arquivos gerados para pasta outputs
    output_files = ["slr_parser.out", "lalr_parser.out", "slr_parsetab.py","lalr_parsetab.py"]
    for file in output_files:
        shutil.move(file, f"{output_folder}/{file}")
 
