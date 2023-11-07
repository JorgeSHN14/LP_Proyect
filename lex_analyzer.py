import ply.lex as lex

#####Paula Peralta#####
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'def': 'DEF',
    'while':'WHILE',
    'for':'FOR',
    'in':'IN',
    'return':'RETURN', 
    'and':'AND', 
    'or':'OR', 
    'not':'NOT', 
    'true':'TRUE', 
    'false':'FALSE', 
    'null':'NULL', 
    'print':'PRINT',  
    'class':'CLASS',
    'finally':'FINALLY',
    'is':'IS',
    'none':'NONE',
    'continue':'CONTINUE',
    'lambda':'LAMBDA',
    'try':'TRY',
    'from':'FROM',
    'nonlocal':'NONLOCAL',
    'del':'DEL',
    'global':'GLOBAL',
    'with':'WITH',
    'as':'AS',
    'elif':'ELIF',
    'yield':'YIELD',
    'assert':'ASSERT',
    'import':'IMPORT',
    'pass':'PASS',
    'break':'BREAK',
    'except':'EXCEPT',
    'raise':'RAISE',
    'var': 'VAR',
    'const': 'CONST',
    'int' : 'INTEGER_DATA_TYPE',
    'float32' : 'FLOAT32_DATA_TYPE',
    'float64' : 'FLOAT64_DATA_TYPE',
    'string' : 'STRING_DATA_TYPE',
    'bool' : 'BOOLEAN_DATA_TYPE'

}

#####Jorge Herrera#####
# Secuencia de tokens
tokens = (
    'STRING',
    'IDENTIFIER',
    'BOOLEAN',
    'INTEGER',
    'FLOAT32',
    'FLOAT64',
    'SCIENTIFIC_NOTATION',
    'COMMENT',
    'COMMENT_MULTI',
    'HEX_NUMBER',
    'ARROW_SEND_RECEIVE',
    'ELLIPSIS',
    'SHORT_VAR_DECL',
    'FAT_ARROW',
    'ARROW_FUNCTION_TYPE',
    'LOGICAL_NOT',
    'AMPERSAND',
    'PIPE',
    'BITWISE_XOR',
    'BITWISE_XOR_ASSIGN',
    'PLUS_EQ',
    'MINUS_EQ',
    'TIMES_EQ',
    'DIVIDE_EQ',
    'MODULO_EQ',
    'BITWISE_AND_EQ',
    'BITWISE_OR_EQ',
    'BITWISE_XOR_EQ',
    'LEFT_SHIFT_EQ',
    'RIGHT_SHIFT_EQ',
    'EQUALEQUAL',
    'NOT_EQUAL',
    'LESS',
    'GREATER',
    'LESS_EQUAL',
    'GREATER_EQUAL',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'PLUS',
    'MINUS',
    'TIMES',
    'MODULE',
    'ENTERE_DIVIDE',
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
    'DOT',
) + tuple(reserved.values())


#####              Juan Demera              #####

# Expresiones Regulares simples para símbolos
###Juan Demera##
t_ARROW_SEND_RECEIVE = r'<-'
t_ELLIPSIS = r'\.\.\.'
t_SHORT_VAR_DECL = r':='
t_FAT_ARROW = r'=>'
t_ARROW_FUNCTION_TYPE = r'->'
t_BITWISE_XOR_ASSIGN = r'\^='
t_PLUS_EQ = r'\+='
t_MINUS_EQ = r'-='
t_TIMES_EQ = r'\*='
t_DIVIDE_EQ = r'/='
t_MODULO_EQ = r'%='
t_BITWISE_AND_EQ = r'&='
t_BITWISE_OR_EQ = r'\|='
t_BITWISE_XOR_EQ = r'\^='
t_LEFT_SHIFT_EQ = r'<<='
t_RIGHT_SHIFT_EQ = r'>>='
t_EQUALEQUAL = r'=='
t_NOT_EQUAL = r'!='
t_LESS = r'<'
t_GREATER = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_LOGICAL_NOT = r'!'
t_AMPERSAND = '\&'
t_PIPE = '\|'
t_BITWISE_XOR = r'\^'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_MODULE = r'\%'
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
t_DOT = '\.'


#####              Paula Peralta              #####

#Expresión regular para números en notación científica
def t_SCIENTIFIC_NOTATION(t):
   r'\d+(\.\d+)?[eE][+-]?\d+'
   t.value = float(t.value)
   return t

#Expresión regular para números en Hexadecimal
def t_HEX_NUMBER(t):
    r'0x[0-9a-fA-F]+'
    t.value = int(t.value, 16)  # Convierte el número hexadecimal a decimal
    return t

# #Expresión regular para comentarios de una sola linea con #
def t_COMMENT(t):
    r'\\.*'
    pass  # Los comentarios serán ignorados y no generan tokens

# #Expresión regular para comentarios multilinea
def t_COMMENT_MULTI(t):
    r'\/\*[\s\S]*?\*\/'
    pass  # Los comentarios multilínea serán ignorados y no generan tokens


#####              Jorge Herrera              #####

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


# # Construye el lexer
# lexer = lex.lex()

# # Código para analizar
# code = input('Ingrese su código:')

# while code != 'end':
#   # Enviando el código
#   lexer.input(code)
#   # Tokenizar
#   for token in lexer:
#     print(token)
#   code = input('Ingrese su código:')

# Enviando el código


lexer = lex.lex()

codePaula = '''
numero_cientifico = 1.2345e10
hexadecimal = 0x1F

'''
codeJorge = '''
var myString string = "05ee4SS"
var myInt int = 5562
const myBool bool = true
const myFloat32 float32 = 5.65f32
const myFloat64 float64 = 5.65f64
'''
codeJuan = '''

'''

code = codePaula+codeJorge+codeJuan

lexer.input(code)
# Tokenizar
# print(list(lexer))
for token in list(lexer):
  print(token)
