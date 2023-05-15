import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa

precedence = (('left', 'OR'), ('left', 'AND'), ('left', 'GT', 'LT', 'GTEQUALS',
                                                'LTEQUALS', 'EQUALS', 'DIF'),
              ('left', 'CONCAT'), ('left', 'PLUS', 'MINUS'),
              ('left', 'PERCENTUAL', 'TIMES',
               'DIVIDE'), ('left', 'NOT', 'TAG'), ('left', 'EXPO'))


# definição de trecho
def p_program(p):
    '''program : block
               | function 
               | function program'''
    if (p[1] == 'block'):
        p[0] = sa.ProgramConcrete(p[1])
    elif (p[1] == 'function'):
        p[0] = sa.ProgramConcrete(p[1])
    elif (len(p) == 3):
        p[0] = sa.ProgramConcrete2(p[1], p[2])


# definição de bloco
def p_block(p):
    '''block : command
             | command block'''
    if (p[1] == 1):
        p[0] = sa.BlockConcrete(p[1])
    if (p[1] == 2):
        p[0] = BlockConcrete2(p[1], p[2])


# definição de comando
def p_command(p):
    '''command : list_vars ATRIB list_exps
               | call_function
               | rotulo
               | BREAK
               | DO block END
               | struct_while
               | struct_repeat
               | if
               | struct_for
               | struct_for_in
               | LOCAL list_vars ATRIB list_exps
               | command_ret'''

    if (p[1] == 'list_vars'):
        p[0] = CommandAtrib(p[1], p[3])
    elif (p[1] == 'call_function'):
        p[0] = CommandCallFunction(p[1])
    elif (p[1] == 'rotulo'):
        p[0] = CommandRotulo(p[1])
    elif (p[1] == 'break'):
        p[0] = CommandBreak(p[1])
    elif (len(p) == 3):
        p[0] = CommandDoBlockEnd(p[3])
    elif (p[1] == 'struct_while'):
        p[0] = CommandStructWhile(p[1])
    elif (p[1] == 'struct_repeat'):
        p[0] = CommandStructRepeat(p[1])
    elif (p[1] == 'if'):
        p[0] = CommandIf(p[1])
    elif (p[1] == 'struct_for'):
        p[0] = CommandStructFor(p[1])
    elif (p[1] == 'struct_for_in'):
        p[0] = CommandStructForIn(p[1])
    elif (len(p) == 5):
        p[0] = CommandLocalListVarsAtribListExps(p[2], p[4], p[5])


# definição de comandret
def p_command_ret(p):
    '''command_ret : RETURN SEMICOLON
                   | RETURN list_exps
                   | RETURN list_exps SEMICOLON '''
    if (p[2] == 'semicolon'):
        p[0] = CommandReturn(None)
    elif (p[1] == 'return'):
        p[0] = CommandReturnListExps(p[2])
    elif (len(p) == 3):
        p[0] = CommandReturnListExpsSemicolon(p[2])


# definição de rótulo
def p_rotulo(p):
    '''rotulo : DUALCOLON NAME DUALCOLON'''
    p[0] = ExpRotulo(p[1], p[2], p[3])


# definicao de nomefuncao
def p_name_function(p):
    '''name_function : NAME
                     | NAME COLON NAME'''
    if (len(p) == 1):
        p[0] = ExpNameFunction1(p[1])
    else:
        p[0] = ExpNameFunction(p[1], p[2], p[3])


# definição de listavars
def p_list_vars(p):
    '''list_vars : var 
                 | var COMMA list_vars'''
    if (len(p) == 1):
        p[0] = ListvarsConcrete1(p[1])
    else:
        p[0] = ListvarConcrete2(p[1], p[3])


# definição de var
def p_var(p):
    '''var : NAME 
           | prefix_exp LCOLCH exp RCOLCH'''
    if (len(p) == 1):
        p[0] = VarConcrete1(p[1])
    else:
        p[0] = VarConcrete2(p[1], p[3])


# definição de prefixexp
def p_prefix_exp(p):
    ''' prefix_exp : var
                  | call_function '''
    if (p[1] == 'var'):
        p[0] = PrefixExpVar(p[1])
    if (p[1] == 'call_function'):
        p[0] = PrefixExpCallFunction(p[1])


# definição de listanomes
def p_list_names(p):
    '''list_names : list_names COMMA NAME  
                  | NAME'''
    if (len(p) == 3):
        p[0] = ListNamesConcrete1(p[1], p[3])
    else:
        p[0] = ListNamesConcrete2(p[1])


# definição de listaexps
def p_list_exps(p):
    '''list_exps : exp COMMA list_exps
                 | exp'''
    if (len(p) == 3):
        p[0] = ListExpsConcrete1(p[1], p[3])
    else:
        p[0] = ListExpsConcrete2(p[1])


# definição de exp (professor pediu para substituir nil por nan)
def p_exp(p):
    '''exp : NIL 
           | FALSE
           | TRUE 
           | NUMBER
           | STRING 
           | VARARGS 
           | def_function 
           | prefix_exp
           | TAG exp
           | MINUS exp
           | NOT exp
           | exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp DIVIDE exp
           | exp EXPO exp
           | exp PERCENTUAL exp
           | exp CONCAT exp
           | exp LT exp
           | exp LTEQUALS exp
           | exp GT exp
           | exp GTEQUALS exp
           | exp EQUALS exp
           | exp DIF exp
           | exp AND exp
           | exp OR exp'''

    if (p[1] == 'nil'):
        p[0] = sa.ExpNil([1])
    elif (p[1] == 'true' or p[1] == 'false'):
        p[0] = sa.BooleanExp(p[1])
    elif (p[1] == 'number'):
        p[0] = sa.ExpNumber([1])
    elif (p[1] == 'string'):
        p[0] = sa.ExpString([1])
    elif (p[1] == 'varargs'):
        p[0] = sa.ExpVarargs([1])
    elif (p[1] == 'def_function'):
        p[0] = sa.ExpDefFunction([1])
    elif (p[1] == 'prefix_exp'):
        p[0] = sa.ExpPrefixExp([1])
    elif (p[1] == 'tag'):
        p[0] = sa.ExpTag([2])
    elif (p[1] == 'minus'):
        p[0] = sa.ExpMinus([2])
    elif (p[1] == 'not'):
        p[0] = sa.ExpNot([2])
#  elif (p[2] == 'PLUS'):
#       p[0] = ExpPlus([1], p[3]) PAREI AQUI....12/05/2023
    elif (len(p) == 3):
        p[0] = sa.ExpMinus([1], p[3])
    elif (p[2] == 'times'):
        p[0] = ExpTimes([1], p[3])
    elif (p[2] == 'divide'):
        p[0] = ExpDivide([1], p[3])
    elif (p[2] == 'expo'):
        p[0] = ExpExpo([1], p[3])
    elif (p[2] == 'percentual'):
        p[0] = ExpPercentual([1], p[3])
    elif (p[2] == 'concat'):
        p[0] = ExpConcat([1], p[3])
    elif (p[2] == 'lt'):
        p[0] = ExpLt([1], p[3])
    elif (p[2] == 'ltequals'):
        p[0] = ExpLtEquals([1], p[3])
    elif (p[2] == 'gt'):
        p[0] = ExpGt([1], p[3])
    elif (p[2] == 'gtequals'):
        p[0] = ExpGtEqual([1], p[3])
    elif (p[2] == 'equals'):
        p[0] = ExpEquals([1], p[3])
    elif (p[2] == 'dif'):
        p[0] = ExpDif([1], p[3])
    elif (p[2] == 'and'):
        p[0] = ExpAnd([1], p[3])
    elif (p[2] == 'or'):
        p[0] = ExpOr([1], p[3])


# definição de chamadafuncao
def p_call_function(p):
    '''call_function : prefix_exp args'''
    p[0] = CallFunctionConcrete(p[2])


# definição de args
def p_args(p):
    ''' args : LPAREN list_exps RPAREN
             | LPAREN RPAREN'''
    if (len(p) == 4):
        p[0] = ExpArgs1(p[2])
    elif (len(p) == 3):
        p[0] = ExpArgs2(p[1], p[2])


# definição de deffunção
def p_def_function(p):
    '''def_function : function'''


# definição de corpofunção
def p_body_function(p):
    '''body_function : LPAREN list_pars RPAREN block END'''


# definição de listapars
def p_list_pars(p):
    '''list_pars : list_names
                 | list_names COMMA VARARGS
                 | VARARGS'''


# definição de listadecampos
def p_list_fields(p):
    '''list_fields : field 
                   | field separator_fields list_fields
                   | field_empty
                   | field_empty separator_fields list_fields'''


# definição de campo vazio
def p_field_empty(p):
    '''field_empty : LCOLCH exp RCOLCH
                   | NAME'''


# definição de campo
def p_field(p):
    '''field : LCOLCH exp RCOLCH ATRIB exp
             | NAME ATRIB exp '''


# definição de sepcampos
def p_separator_fields(p):
    '''separator_fields : COMMA
                        | SEMICOLON'''


# definição de variável local
def p_local_var(p):
    '''local_var : LOCAL list_names ATRIB list_exps
                 | LOCAL list_names
                 | LOCAL NAME ATRIB exp'''


# definicao de função
def p_function(p):
    '''function : FUNCTION name_function body_function'''


# definicao de if
def p_if(p):
    '''if : IF exp THEN block END
          | IF exp THEN block else1
          | IF exp THEN block else_if else1'''


def p_else_if(p):
    '''else_if : ELSEIF exp THEN block
               | ELSEIF exp THEN block else_if'''


def p_else(p):
    '''else1 : ELSE block END'''


# definicao de while
def p_struct_while(p):
    '''struct_while : WHILE exp DO block END'''


# definicao de for
def p_struct_for(p):
    '''struct_for : FOR NAME ATRIB exp COMMA exp DO block END
                  | FOR NAME ATRIB exp COMMA exp COMMA exp DO block END'''


# definicao de forin
def p_struct_for_in(p):
    '''struct_for_in : FOR list_names IN list_exps DO block END'''


# definição de repeat
def p_struct_repeat(p):
    '''struct_repeat : REPEAT block UNTIL exp'''


# definicao de error
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: {p.value}")
    else:
        print("Erro de sintaxe: fim de entrada inesperado")


# REFERÊNCIAS (NO FINAL DO MANUAL TEM A DEFINIÇÃO DE TUDO)
# LINK DO MANUAL : https://www.lua.org/manual/5.2/pt/manual.html
