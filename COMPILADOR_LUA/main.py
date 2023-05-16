from ExpressionLanguageLex import *
from ExpressionLanguageParser import *
from Visitor import *

lexer = lex.lex()

data = '''
-- Função para exibir o menu da calculadora
function exibirMenu()
    print("=== Calculadora Lua ===")
    print("Escolha a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    print("=======================")
end

-- Função para realizar a adição
function adicao(a, b)
    return a + b
end

-- Função para realizar a subtração
function subtracao(a, b)
    return a - b
end

-- Função para realizar a multiplicação
function multiplicacao(a, b)
    return a * b
end

-- Função para realizar a divisão
function divisao(a, b)
    return a / b
end

-- Função principal da calculadora
function calculadora()
    local operacao = 0
    
    while operacao ~= 5 do
        exibirMenu()
        
        -- Ler a operação escolhida
        operacao = tonumber(io.read())
        
        if operacao == 5 then
            print("Calculadora encerrada.")
            break
        end
        
        -- Ler os números
        print("Digite o primeiro número:")
        local num1 = tonumber(io.read())
        print("Digite o segundo número:")
        local num2 = tonumber(io.read())
        
        -- Realizar a operação selecionada
        if operacao == 1 then
            local resultado = adicao(num1, num2)
            print("Resultado: " .. resultado)
        elseif operacao == 2 then
            local resultado = subtracao(num1, num2)
            print("Resultado: " .. resultado)
        elseif operacao == 3 then
            local resultado = multiplicacao(num1, num2)
            print("Resultado: " .. resultado)
        elseif operacao == 4 then
            local resultado = divisao(num1, num2)
            print("Resultado: " .. resultado)
        else
            print("Operação inválida. Tente novamente.")
        end
        
        print("=======================")
    end
end

-- Iniciar a calculadora
calculadora()
'''
lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=False)
print("#realiza a analise semantica")
visitor = Visitor()

for r in result:
    r.accept(visitor)
