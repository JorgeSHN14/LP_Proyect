import ply.lex as lex

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'def': 'DEF',
}

# Secuencia de tokens
tokens = (
    'STRING',
    'IDENTIFIER',
    'BOOLEAN',
    'INTEGER',
    'PLUS',
    'FLOAT32',
    'FLOAT64',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LKEY',
    'RKEY',
    'EQUAL',
    'COMMA',
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
t_COMMA = r','
t_RBRACKET = '\['
t_LBRACKET = '\]'
t_RKEY = '\['
t_LKEY = '\]'


# Expresión regular para bool

def t_BOOLEAN(t):
  r'(true|false)'
  return t

# Expresión regular para identificadores

def t_STRING(t):
  r'(\"[^\"]*\"|\`[^\`]*\`)'
  print(t)
  return t


# Expresión regular para identificadores

def t_IDENTIFIER(t):
  r'[a-zA-Z_]+[a-zA-Z0-9_]*'
  t.type = reserved.get(t.value, 'IDENTIFIER')
  return t


# Expresión regular para números flotantes
def t_FLOAT32(t):
    r'\d+\.\d+f32'
    t.value = float(t.value[:-3])  # Elimina el sufijo "f32" y convierte a float
    return t

def t_FLOAT64(t):
    r'\d+\.\d+f64'
    t.value = float(t.value[:-3])  # Elimina el sufijo "f64" y convierte a float
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