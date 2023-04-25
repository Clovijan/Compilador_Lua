import ply.yacc as yacc
from ExpressionLanguageLex import *

precedence = (('left', 'OR'), ('left', 'AND'), ('left', 'GT', 'LT', 'GTEQUALS',
                                                'LTEQUALS', 'EQUALS', 'DIF'),
              ('left', 'CONCAT'), ('left', 'PLUS', 'MINUS'),
              ('left', 'PERCENTUAL', 'TIMES',
               'DIVIDE'), ('left', 'NOT', 'TAG'), ('left', 'EXPO'))


# definição de trecho
def p_program(p):
    '''program : block'''


# definição de bloco
def p_block(p):
    '''block : command
             | command command_ret'''


# definição de comando
def p_command(p):
    '''command : SEMICOLON
               | list_vars ATRIB list_exps
               | call_function
               | rotulo
               | BREAK
               | GOTO NAME
               | DO block END
               | struct_while
               | struct_repeat
               | if
               | struct_for
               | struct_for_in
               | def_function
               | local_var'''


# definição de comandret
def p_command_ret(p):
    '''command_ret : RETURN
                   | RETURN list_exps
                   | RETURN list_exps SEMICOLON'''


# definição de rótulo
def p_rotulo(p):
    '''rotulo : DUALCOLON NAME DUALCOLON'''


# definicao de nomefuncao
def p_name_function(p):
    '''name_function : NAME
                     | NAME DOT NAME
                     | NAME COLON NAME'''


# definição de listavars
def p_list_vars(p):
    '''list_vars : var COMMA var'''


# definição de var
def p_var(p):
    '''var : NAME 
           | prefix_exp LCOLCH exp RCOLCH
           | prefix_exp DOT NAME'''


def p_prefix_exp(p):
    ''' prefix_exp : var
                   | call_function 
                   | LPAREN exp RPAREN'''


# definição de listanomes
def p_list_names(p):
    '''list_names : NAME COMMA list_names
                  | NAME'''


# definição de listaexps
def p_list_exps(p):
    '''list_exps : exp COMMA list_exps
                 | exp'''


# definição de exp
def p_exp(p):
    '''exp : NIL
           | FALSE
           | TRUE
           | NUMBER
           | STRING
           | VARARGS
           | def_function
           | exp_prefix
           | construct_table
           | exp op_bin exp
           | exp op_unary exp'''


# definição de expprefixo
def p_exp_prefix(p):
    '''exp_prefix : VAR 
                  | call_function
                  | LPAREN exp RPAREN'''


# definição de chamadafuncao
def p_call_function(p):
    '''call_function : exp_prefix args
                     | exp_prefix COLON NAME args'''


# definição de args
def p_args(p):
    ''' args : LPAREN list_exps RPAREN
             | construct_table'''


# definição de deffunção
def p_def_function(p):
    '''def_function : function 
                    | local_function'''


# definição de corpofunção
def p_body_function(p):
    '''body_function : LPAREN list_pars RPAREN block END'''


# definição de listapars
def p_list_pars(p):
    '''list_pars : list_names COMMA VARARGS
                 | VARARGS'''


# definição de construtortabela
def p_construct_table(p):
    '''construct_table : LBRACE list_fields RBRACE
                       | LBRACE RBRACE'''


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
                 | LOCAL NAME ATRIB exp'''


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
                | NOT
                | TAG'''


# definicao de função
def p_function(p):
    '''function : FUNCTION body_function'''


# definicao de if
def p_if(p):
    '''if : IF exp THEN block END
          | IF exp THEN else
          | IF exp THEN block else_ifs'''


def p_else_ifs(p):
    '''else_ifs : else_if else_ifs 
                | else_if '''


def p_else_if(p):
    '''else_if : ELSEIF exp THEN block 
               | else'''


def p_else(p):
    '''else : ELSE block END'''


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


# definicao de funcao local
def p_local_function(p):
    '''local_function : LOCAL FUNCTION name_function body_function'''


# definicao de error
def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: {p.value}")
    else:
        print("Erro de sintaxe: fim de entrada inesperado")


# REFERÊNCIAS (NO FINAL DO MANUAL TEM A DEFINIÇÃO DE TUDO)
# LINK DO MANUAL : https://www.lua.org/manual/5.2/pt/manual.html
