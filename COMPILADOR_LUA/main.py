from ExpressionLanguageLex import *
from ExpressionLanguageParser import *

lexer = lex.lex()

data = '''
-- Example 1: Simple program
a = 1;
-- Example 2: Block with two commands
a = 1;
b = 2;
-- Example 3: Command that assigns multiple values to multiple variables
a, b, c = 1, 2, 3;

-- Example 4: Command that returns a single value
return 1;
-- Example 5: Label definition
::mylabel::

-- Example 6: Function call using dot notation
mytable.myfunction()

-- Example 7: Assigning to a list of variables
a, b, c = 1, 2, 3;

-- Example 8: Using a table index to access a variable
mytable["mykey"] = 1;


local minhaVariavel = "Hello World!"
-- Definindo uma variável booleana
local ativo = true

-- Verificando a condição usando "if"
if ativo then
  print("O modo ativo está ligado!")
end

-- Definindo outra variável
local idade = 18

-- Verificando múltiplas condições usando "elseif"
if idade < 18 then
  x + y 
elseif idade == 18 then
  x - y
else
 x/y
end
'''
lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=True)
print ("#realiza a analise semantica")
