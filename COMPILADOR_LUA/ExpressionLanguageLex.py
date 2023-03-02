import ply.lex as lex

# Lista de tokens
tokens = (
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
    'IF',
    'THEN',
    'ELSEIF',
    'ELSE',
    'END',
    'WHILE',
    'DO',
    'REPEAT',
    'UNTIL',
    'FOR',
    'IN',
    'FUNCTION',
    'LOCAL',
    'RETURN',
    'BREAK',
)

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

# Palavras-chave
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'elseif': 'ELSEIF',
    'else': 'ELSE',
    'end': 'END',
    'while': 'WHILE',
    'do': 'DO',
    'repeat': 'REPEAT',
    'until': 'UNTIL',
    'for': 'FOR',
    'in': 'IN',
    'function': 'FUNCTION',
    'local': 'LOCAL',
    'return': 'RETURN',
    'break': 'BREAK',
}

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