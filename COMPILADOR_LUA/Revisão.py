import ply.yacc as yacc
from ExpressionLanguageLex import *

# definição de programa
def p_programa(p):
    '''programa : var_global program'''


# definição de comando
def p_comand(p):
    ''''''

# definição de bloco
def p_bloco(p):
  ''''''

# definição de estrturas de controle
def p_control_structures(p):
  '''control_strutures : control_structure control_structures'''

def p_control_structure(p):
    '''control_structure : struct_if
                         | struct_ifElse
                         | struct_while
                         | struct_for
                         | struct_forIn'''

def p_struct_while(p):
  '''struct_while : exp DO bloco END'''