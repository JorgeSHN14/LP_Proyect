import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'def': 'DEF',
}

# Secuencia de tokens
tokens = (
    'IDENTIFIER',
    'INTEGER',
    'PLUS',
    'FLOAT',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUAL',
    'GREATER_THAN',
    'LESS_THAN',
    'COLON',
    'MODULE',
    'ENTERE_DIVIDE',
) + tuple(reserved.values())

# Expresiones Regulares simples para símbolos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_MODULE = r'%'
t_ENTERE_DIVIDE = r'//'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUAL = r'\='
t_GREATER_THAN = r'>'
t_LESS_THAN = r'<'
t_COLON = r':'


# Expresión regular para números flotantes
def t_IDENTIFIER(t):
  r'[a-zA-Z_]+[a-zA-Z0-9_]*'
  t.type = reserved.get(t.value, 'IDENTIFIER')
  return t


# Expresión regular para números flotantes
def t_FLOAT(t):
  r'\d+\.\d+'
  return t


# Expresión regular para números enteros, incluye cast
def t_INTEGER(t):
  r'\d+'
  t.value = int(t.value)
  return t


# Expresión regular para reconocer saltos de línea
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


# Ignorar espacios, tabulaciones
t_ignore = ' \t'


# Manejo de errores
def t_error(t):
  print(
      f"{t.type.upper()}: No se reconoce el caracter {t.value[0]} en la línea {t.lineno}"
  )
  t.lexer.skip(1)


# Construye el lexer
lexer = lex.lex()

# Código para analizar
code = input('Ingrese su código:')

while code != 'end':
  # Enviando el código
  lexer.input(code)
  # Tokenizar
  for token in lexer:
    print(token)
  code = input('Ingrese su código:')