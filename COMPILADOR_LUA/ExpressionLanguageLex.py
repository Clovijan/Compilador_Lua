import ply.lex as lex

reserved = {
    'break': 'BREAK', 
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'for' : 'FOR',
    'and' : 'AND',
    'do': 'DO',
    'end':'END',
    'if' : 'IF',
    'goto':'GOTO',
    'true' : 'TRUE',
    'false': 'FALSE',
    'function' : 'FUNCTION',
    'in':'IN',
    'local': 'LOCAL',
    'nil': 'NIL',
    'not': 'NOT',
    'or': 'OR',
    'repeat': 'REPEAT',
    'local': 'LOCAL',
    'return': 'RETURN',
    'then': 'THEN',
    'until': 'UNTIL',
    'while': 'WHILE'
 }
# Lista de tokens
tokens = [
    'NAME',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'EQUALS',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
    'COLON',
    'DOT',
    'VARARGS',
    'UNTIL',
    'LOCAL',
 
 ] + list(reserved.values()) 

# Regras de expressões regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_SEMICOLON = r';'
t_COLON = r':'
t_DOT = r'\.'
t_VARARGS = r'\.\.\.'

# Nomes e números
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'NAME')
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# Ignorar comentários
def t_COMMENT(t):
    r'--.*'
    pass

# Ignorar espaços em branco
t_ignore = " \t"

# Erro
def t_error(t):
    print("Caractere inválido: '%s'" % t.value[0])