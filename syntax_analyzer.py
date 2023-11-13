import ply.yacc as sint
from lex_analyzer import tokens

def p_print(p):
  '''print : FMT_LIBRARY DOT PRINTLN LPAREN value RPAREN
          | FMT_LIBRARY DOT PRINTF LPAREN value RPAREN'''

def p_sentencia(p):
  '''sentencia : impresion
              | asignacion
              | mientras'''
  
def p_asignacion(p):
  '''asignacion : VAR IDENTIFIER data_type EQUAL value
                | CONST IDENTIFIER data_type EQUAL value'''
  
def p_impresion(p):
  "impresion : IMPRESION P_IZQ  valor P_DER"

def p_impresion_sinvalor(p):
  "impresion : IMPRESION P_IZQ P_DER"

def p_mientras(p):
  "mientras : MIENTRAS P_IZQ VERDADERO P_DER DOSP sentencia"

def p_valores(p):
  '''valores : valor
            | valores COMA valor'''

def p_data_type(p):
  '''data_type : STRING
   | INTEGER_DATA_TYPE
   | FLOAT32_DATA_TYPE
   | FLOAT64_DATA_TYPE
   | BOOLEAN_DATA_TYPE
   | STRING_DATA_TYPE'''

def p_value(p):
  '''value : STRING
         | INTEGER
         | FLOAT32
         | FLOAT64
         | BOOLEAN'''



def p_error(p):
    print("Error sintáctico en '%s'" % p.value)

parser = sint.yacc()
while True:
  try:
    s = input('Ingrese su código: ')
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)