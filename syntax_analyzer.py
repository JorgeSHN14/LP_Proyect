import ply.yacc as sint
from lex_analyzer import tokens

def p_print(p):
  '''print : FMT_LIBRARY DOT PRINTLN LPAREN value RPAREN
          | FMT_LIBRARY DOT PRINTF LPAREN value RPAREN'''

def p_sentence(p):
  '''sentencia : print
              | assignment
              | while
              | def_function
              | call_function'''
  
def p_assignment(p):
  '''assignment : VAR IDENTIFIER data_type EQUAL value
                | CONST IDENTIFIER data_type EQUAL value'''
  

def p_while(p):
  "while : WHILE P_IZQ TRUE P_DER COLON sentence"

def p_def_function(p):
  '''def_function : DEF IDENTIFIER LPAREN parameters RPAREN COLON sentence'''

def p_call_funcion(p):
  '''call_function : IDENTIFIER LPAREN valores RPAREN'''

def p_parameters(p):
  '''parameters : parameter
                | parameters COMMA parameter'''

def p_parameter(p):
  ''' parameter : IDENTIFIER data_type'''
def p_valores(p):
  '''values : value
            | values COMA value'''

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

####Paula Peralta###
def p_input(p):
  '''input : INPUT LPAREN RPAREN'''
  user_input = input("Ingrese un valor:")
  print(f"Valor ingresado: {user_input}")


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