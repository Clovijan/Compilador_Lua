import ply.yacc as yacc
from ExpressionLanguageLex import *

def p_program(p):
  '''program : comands
             | var_global program
             | function
             | local_function
             | comands program
             | function program
             | local_function program'''

def p_var_global(p):
  '''var : NAME ATRIB exp_16'''

def p_function(p):
  '''function : FUNCTION signature comands END '''
  
def p_local_function(p):
  '''local_function : LOCAL FUNCTION signature comands END'''
  
def p_signature(p):
  '''signature : ID LPAREN sigparam RPAREN'''
  
def p_sigparam(p):
  '''sigparam : ID
              | n_sigparam'''

def p_n_sigparam(p):
  '''n_sigparam : ID COMMA sigparam'''

def p_comands(p):
  '''comands : comand
             | comand comands'''

def p_comand(p):
  '''comand : comand_1
            | comand_2'''
    
def p_comand_1(p):
  '''comand_1 : IF list_exp THEN comand_1  ELSE comand_1 END 
              | IF list_exp THEN comands ELSE comands END
              | IF list_exp THEN comand_1 ELSE comands END
              | IF list_exp THEN comands ELSE comand_1 END
              | other_comand'''
  
#def p_elseif(p):
#  '''elseif : ELSEIF list_exp THEN comands
#            | '''
  
def p_other_comand(p):
  '''other_comand : WHILE list_exp DO comands END
                  | fordo END
                  | forin END
                  | exp
                  | RETURN exp
                  | BREAK'''

def p_comand_2(p):
  '''comand_2 : IF list_exp THEN comands END
              | IF list_exp THEN comand_1 ELSE comand_2 END
              | IF list_exp THEN comands ELSE comand_2 END'''

def p_fordo(p):
  '''fordo : FOR exp DO comands'''

def p_forin(p):
  '''forin : FOR exp IN comands'''

def p_list_exp(p):
  '''list_exp : exp COMMA list_exp
              | exp list_exp
              | paren_list_exp COMMA list_exp
              | exp 
              | paren_list_exp
              | paren_list_exp list_exp'''

def p_paren_exp(p):
  '''paren_list_exp : LPAREN exp RPAREN'''
 
def p_call(p):
  '''call : ID paren_list_exp
          | ID LPAREN RPAREN'''

#FALTA algo na definição dos arrays
def p_array(p):
  '''array : ID EQUAL LKEY exp RKEY
           | ID EQUAL LKEY RKEY
           | ID LCOCHETE ID RCOCHETE EQUAL exp'''

def p_exp(p):
    '''exp : exp ASSIGN exp_1
           | exp_1'''
          
def p_exp_1(p):
  '''exp_1 : exp_1 OR exp_2
           | exp_1 BITWISE_OR exp_2
           | exp_2'''
   
def p_exp_2(p): 
  '''exp_2 : exp_2 AND exp_3
           | exp_2 BITWISE_AND exp_3
           | exp_3'''
  
def p_exp_3(p):
  '''exp_3 : exp_3 BITWISE_EXC_OR exp_4
           | exp_4'''

def p_exp_4(p):
  '''exp_4 : exp_4 LESS_THAN exp_5
           | exp_4 BIGGER_THAN exp_5
           | exp_4 BIGGER_EQUAL exp_5
           | exp_4 LESS_EQUAL exp_5
           | exp_4 DIF exp_5
           | exp_4 EQUAL exp_5
           | exp_5'''

def p_exp_5(p):
  '''exp_5 : exp_5 CONCATENATION exp_6
           | exp_6'''

def p_exp_6(p):
  '''exp_6 : exp_6 SUB exp_7
           | exp_7'''

def p_exp_7(p):
  '''exp_7 : exp_7 SUM exp_8
           | exp_8'''

def p_exp_8(p):
  '''exp_8 : exp_8 MODULE exp_9
            | exp_9'''

def p_exp_9(p):
  '''exp_9 : exp_9 DIV exp_10
            | exp_10'''
  
def p_exp_10(p):
  '''exp_10 : exp_10 DIV_INT exp_11
            | exp_11'''

def p_exp_11(p):
  '''exp_11 : exp_11 MULT exp_12
            | exp_12'''

def p_exp_12(p):
  '''exp_12 : exp_12 NOT exp_13
            | exp_13'''

def p_exp_13(p):
  '''exp_13 : DENIAL exp_13
            | UNARY_BITWISE_NOT exp_13
            | LENGHT exp_13
            | exp_14'''
  
def p_exp_14(p):
  '''exp_14 : exp_14 POW exp_15
            | exp_15'''
  
def p_exp_15(p):
  '''exp_15 : exp_15 COMMA exp_16
            | exp_15 DOT exp_16
            | LOCAL exp_15
            | call
            | array
            | exp_16'''

def p_exp_16(p):
  '''exp_16 : NUMBER 
            | STRING 
            | ID
            | NIL
            | TRUE
            | FALSE'''
            
def p_error(p):
    print("Erro Sintático") 
         