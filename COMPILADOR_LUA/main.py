from ExpressionLanguageLex import *
from ExpressionLanguageParser import *

lexer = lex.lex()

data = '''
local a, b = 10, 20
local tabela = {nome = "João", idade = 30}

-- Definição de função
function soma(x, y)
    return x + y
end

-- Declaração de bloco de controle
if a > b then
    print("a é maior do que b")
elseif b > a then
    print("b é maior do que a")
else
    print("a e b são iguais")
end

tabela.ocupacao = "programador"

local resultado = soma(a, b)

print("O resultado da soma é:", resultado)
print("O nome é:", tabela.nome)
print("A idade é:", tabela.idade)
print("A ocupação é:", tabela.ocupacao)
'''
lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=False)
print ("#realiza a analise semantica")
