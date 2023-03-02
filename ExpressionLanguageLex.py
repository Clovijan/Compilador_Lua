# -------------------------
# ExpressionLanguageLex.py
#----------------------
import ply.lex as lex
reservadas = {
   'while' : 'WHILE',
   'true' : 'TRUE',
   'false' : 'FALSE',
   'return' : 'RETURN'
}
tokens = ['COMMA', 'SOMA', 'ID', 'NUMBER', 'VEZES', 'POT', 'LPAREN',
          'RPAREN', 'IGUAL', 'LCHAV', 'RCHAV', 'PV'] + list(reservadas.values())

t_IGUAL= r'='
t_SOMA = r'\+'
t_VEZES = r'\*'
t_POT = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_LCHAV = r'{'
t_RCHAV = r'}'
t_PV = r';'