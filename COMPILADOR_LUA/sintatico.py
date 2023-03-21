import ply.yacc as yacc
#import sintaxeabstrata as sa

# Definindo as regras da gramática
def p_program(p):
  ''' program : PackageClause SEMICOLON programl 
  | PackageClause SEMICOLON '''

def p_programl(p):
  ''' programl : TopLevelDecl SEMICOLON programl
  | TopLevelDecl SEMICOLON '''

def p_PackageClause(p):
  ''' PackageClause : PACKAGE ID '''

def p_IdentifierList(p):
  ''' IdentifierList : PrimaryExpr 
  | PrimaryExpr COMMA IdentifierList '''

def p_BreakStmt (p):
  ''' BreakStmt : BREAK''' 

def p_IfStmt(p):
  ''' IfStmt : IF Expression Block 
  | IF SimpleStmt SEMICOLON Expression Block
  | IF Expression Block ELSE IfStmt 
  | IF Expression Block ELSE Block
  | IF SimpleStmt SEMICOLON Expression Block ELSE IfStmt
  | IF SimpleStmt SEMICOLON Expression Block ELSE Block '''  
def p_ForStmt(p):
  ''' ForStmt : FOR Condition Block
  | FOR ForClause Block
  | FOR RangeClause Block
  | FOR Block '''

def p_Condition(p):
  ''' Condition : Expression'''

def p_ForClause(p):
  ''' ForClause : SimpleStmt SEMICOLON Condition SEMICOLON  SimpleStmt 
  | SEMICOLON SEMICOLON '''

def p_ReturnStmtm(p):
  ''' ReturnStmt : RETURN ExpressionList
  | RETURN '''

def p_error(p):
  print('Error') 
  
parser = yacc.yacc()
