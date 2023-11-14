import ply.yacc as sint
from lex_analyzer import tokens

def p_sentencia(p):
  '''sentencia : print
              | print_withoutvalue
              | assignment
              | short_assignment
              | arithmetic_operation
              | while
              | def_function
              | call_function'''
  
              

  
def p_print_withoutvalue(p):
  '''print_withoutvalue : FMT_LIBRARY DOT PRINTLN LPAREN RPAREN
            | FMT_LIBRARY DOT PRINTF LPAREN RPAREN'''

def p_print(p):
  '''print : FMT_LIBRARY DOT PRINTLN LPAREN value RPAREN
           | FMT_LIBRARY DOT PRINTF LPAREN value COMMA RPAREN
           | FMT_LIBRARY DOT PRINTF LPAREN value COMMA identifiers RPAREN'''


def p_identifiers(p):
  '''identifiers : IDENTIFIER
                 | identifiers COMMA identifiers'''
  
def p_assignment(p):
  '''assignment : VAR IDENTIFIER data_type EQUAL value
                | CONST IDENTIFIER data_type EQUAL value
                | VAR IDENTIFIER data_type EQUAL IDENTIFIER
                | CONST IDENTIFIER data_type EQUAL IDENTIFIER'''
  
def p_short_assignment(p):
  '''short_assignment : IDENTIFIER SHORT_VAR_DECL value
                | IDENTIFIER SHORT_VAR_DECL IDENTIFIER'''
  

def p_while(p):
  "while : WHILE un valor singular  TRUE P_DER COLON sentence"

def p_def_function(p):
  '''def_function : DEF IDENTIFIER LPAREN parameters RPAREN COLON sentencia'''

def p_call_funcion(p):
  '''call_function : IDENTIFIER LPAREN values RPAREN'''

def p_parameters(p):
  '''parameters : parameter
                | parameters COMMA parameter'''

def p_parameter(p):
  ''' parameter : IDENTIFIER value'''

def p_values(p):
  '''values : value
            | values COMMA value'''

def p_value(p):
  '''value : STRING
          | INTEGER
          | FLOAT32
          | FLOAT64
          | BOOLEAN'''

def p_arithmetic_operation(p):
    '''
    arithmetic_operation : IDENTIFIER PLUS_EQ value
                        | IDENTIFIER MINUS_EQ value
                        | IDENTIFIER TIMES_EQ value
                        | IDENTIFIER DIVIDE_EQ value
                        | IDENTIFIER MODULO_EQ value
                        | IDENTIFIER BITWISE_AND_EQ value
                        | IDENTIFIER BITWISE_OR_EQ value
                        | IDENTIFIER BITWISE_XOR_EQ value
                        | IDENTIFIER LEFT_SHIFT_EQ value
                        | IDENTIFIER RIGHT_SHIFT_EQ value
    '''

def p_data_type(p):
  '''data_type : INTEGER_DATA_TYPE
               | FLOAT32_DATA_TYPE
               | FLOAT64_DATA_TYPE
               | BOOLEAN_DATA_TYPE
               | STRING_DATA_TYPE'''

def p_input(p):
  '''input : INPUT LPAREN RPAREN'''


def p_error(p):
    print("Error sintáctico en '%s'" % p.value)

parser = sint.yacc()

prueba = """
input()
var x int = 10
const pi float64 = 3.14159
"""

while True:
  try:
    s = input('Ingrese su código: ')
  except EOFError:
    break
  if not s: continue
  result = parser.parse(s)
  print(result)

