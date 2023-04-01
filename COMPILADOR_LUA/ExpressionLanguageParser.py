import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa
import Visitor as vis
import SemanticVisitor as sv


# definição de trecho
def p_program(p):
    '''program : block'''


# definição de bloco
def p_block(p):
    '''block : command
             | command command_ret'''


# definição de comando
def p_command(p):
    '''command : COMMA
               | list_vars ATRIB list_exps
               | call_function
               | rotulo
               | BREAK
               | GOTO NAME
               | DO block END
               | struct_while
               | struct_repeat
               | struct_if_Else
               | struct_for
               | struct_for_in
               | function
               | local_function
               | local_var'''


# definição de comandoret
def p_ret_command(p):
    '''ret_command : RETURN LCOLCH list_exps RCOLCH
                   | RETURN LCOLCH list_exps RCOLCH COMMA'''


# definição de comandret
def p_command_ret(p):
    '''command_ret : RETURN
                 | RETURN list_exps
                 | RETURN list_exps COMMA'''


# definição de rótulo
def p_rotulo(p):
    '''rotulo : DUALCOLON NAME DUALCOLON'''


# definicao de nomefuncao
def name_fuction(p):
    '''name_function : NAME
                     | NAME DOT NAME
                     | NAME COLON NAME'''


# definição de listavars
def p_list_vars(p):
    '''list_vars : var 
                 | var SEMICOLON list_vars'''


# definição de var
def p_var(p):
    '''var : NAME 
           | prefix_exp LCOLCH exp RCOLCH
           | prefix_exp DOT NAME'''


# definição de listanomes
def p_list_names(p):
    '''list_names: NAME 
                 | NAME COMMA list_names'''


# definição de listaexps
def p_list_exps(p):
    '''list_exps : exp 
                 | exp COMMA list_exps'''


# definição de exp
def p_exp(p):
    '''exp: NIL
          | FALSE
          | TRUE
          | NUMBER
          | CADEIA
          | VARARGS
          | def_function
          | exp_prefix
          | construct_table
          | exp op_bin exp
          | op_unaria exp'''


# definição de expprefixo
def p_exp_prefix(p):
    '''exp_prefix : VAR 
                  | call_function
                  | LPAREN exp RPAREN'''


# definição de chamadafuncao
def p_call_function(p):
    '''call_function: exp_prefix args
                    | exp_prefix COLON NAME args'''


# definição de args
def p_args(p):
    ''' args : LPAREN list_exp RPAREN
              | construct_table
              | cadeia'''


# definição de deffunção
def p_def_function(p):
    '''def_function : FUNCTION body_function'''


# definição de corpofunção
def p_body_function(p):
    '''body_function : LPAREN list_pars RPAREN block END'''


# definição de listapars
def p_list_pars(p):
    '''list_pars : list_names COMMA VARARGS
                 | VARARGS
                 | list_names'''


# definição de construtortabela
def p_construct_table(p):
    '''construct_table : LBRACE list_fields RBRACE'''


# definição de listadecampos
def p_list_fields(p):
    '''list_fields : field LBRACE separator_fields field RPARECE
                   | separator_fields'''


# definição de campo
def p_field(p):
    '''field : LCOLCH exp RCOLCH ATRIB exp
             | NAME ATRIB exp
             | exp'''


# definição de separadordecampos
def p_separator_fields(p):
    '''separator_fields : COMMA
                        | SEMICOLON'''


# definição de variável local
def p_local_var(p):
    '''local_var : LOCAL list_names ATRIB list_exp'''


# definição de opbin
def p_op_bin(p):
    ''' op_bin : PLUS
               | MINUS
               | TIMES
               | DIVIDE
               | EXPO 
               | PERCENTUAL
               | CONCAT
               | LT
               | LTEQUALS
               | GT
               | GTEQUALS
               | EQUALS
               | DIF
               | AND
               | OR'''


# definição de opunária
def p_op_unary(p):
    '''op_unary : MINUS
                | not
                | TAG'''


# definicao de função
def p_function(p):
    '''function : FUNCTION name_function body_function'''


# definicao de if
def p_if(p):
    '''if : IF exp THEN block else_ifs else END'''


def p_else_ifs(p):
    '''else_ifs : else_ifs else_if
              | else_if'''


def p_else_if(p):
    '''else_if : ELSEIF exp THEN block'''


def p_else(p):
    '''else : ELSE block'''


# definicao de while
def p_struct_while(p):
    '''struct_while : WHILE exp DO block END'''


# definicao de for
def p_struct_for(p):
    '''struct_for : FOR NAME ATRIB exp COMMA exp DO block END
                  | FOR NAME ATRIB exp COMMA exp COMMA exp DO block END'''


# definicao de forin
def p_struct_for_in(p):
    '''struct_for_in : FOR list_names IN listExp DO block END'''


# definição de repeat
def p_struct_repeat(p):
    '''struct_repeat : REPEAT block UNTIL exp'''


# definicao de funcao local
def p_local_function(p):
    '''local_function : FUCTION name_function body_function'''

# definicao de error
def p_error(p):
    print("Syntax error in input!")


# REFERÊNCIAS (NO FINAL DO MANUAL TEM A DEFINIÇÃO DE TUDO)
# LINK DO MANUAL : https://www.lua.org/manual/5.2/pt/manual.html
