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

def p_add_op(p):
  ''' add_op : PLUS
  | MINUS'''

def p_mul_op(p):
  ''' mul_op : TIMES
  | DIVIDE
  | MODULE 
  | LSHIFT
  | RSHIFT '''
  
def p_comando(p):
  ''' comando ::= listavars EQUALS listaexps ''' 
  
def p_listavars(p):
  ''' listavars ::= var LBRACE COMMA var RBRACE '''

def p_listaexps(p):
  ''' listaexps ::= exp LBRACE COMMA exp RBRACE '''  

def p_var(p):
  ''' var ::= var  '''

def p_Declaration(p):
  ''' Declaration : ConstDecl  
  | VarDecl '''   

def p_VarDecl(p):
  ''' VarDecl : VAR VarSpec 
  | LPAREN VarDecll RPAREN 
  | LPAREN RPAREN '''

def p_VarDecll(p):
  ''' VarDecll : VarSpec SEMICOLON VarDecll
  | VarSpec SEMICOLON '''

def p_VarSpec(p):
  ''' VarSpec : IdentifierList Type
  | IdentifierList Type EQ ExpressionList
  | EQ ExpressionList '''  
  
def p_PrimaryExpr(p):
  ''' PrimaryExpr : Literal
  | ID
  | LPAREN Expression RPAREN
  | ID LCOLCH Expression RCOLCH
  | ID Arguments '''

def p_Expression(p):
  #''' Expression : IF '''
  ''' Expression : Expression binary_op Expression1
  | Expression1 '''

def p_Expression1(p):
  ''' Expression1 : UnaryExpr '''  

def p_Arguments(p):
  ''' Arguments : LPAREN ExpressionList RPAREN
  | LPAREN Type RPAREN 
  | LPAREN TYPE COMMA ExpressionList RPAREN
  | LPAREN RPAREN '''    

def p_Literal(p):
  ''' Literal : NUMBER
  | STRING
  | TRUE
  | FALSE '''  

def p_trecho(p):
  ''' trecho ::= bloco '''
  
def p_bloco(p):
  ''' bloco :: LBRACE StatementList RBRACE 
  | LBRACE RBRACE''' 
 
def p_error(p):
  print('Error') 
  
parser = yacc.yacc()
