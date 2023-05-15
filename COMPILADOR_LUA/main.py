from ExpressionLanguageLex import *
from ExpressionLanguageParser import *
from Visitor import *

lexer = lex.lex()

data = '''
print("hello")
'''
lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=False)
print("#realiza a analise semantica")
visitor = Visitor()
  
for r in result:
  r.accept(visitor)
