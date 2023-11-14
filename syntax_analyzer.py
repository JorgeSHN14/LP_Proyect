import ply.yacc as sint
from lex_analyzer import tokens


def p_program(p):
  ''' program : sentencia
              | sentencia newline program
  '''

def p_sentencia(p):
  '''sentencia : print
               | print_withoutvalue
               | for
               | def_function
               | call_function
               | input
               | assignment
               | short_assignment'''

##########            PAULA PERALTA            ############
def p_for(p):
  '''for : FOR rule_comparation LKEY program RKEY'''

##########            JORGE HERRERA            ############

  
def p_print(p):
  '''print : FMT_LIBRARY DOT PRINTLN LPAREN value RPAREN
           | FMT_LIBRARY DOT PRINTF LPAREN value COMMA RPAREN
           | FMT_LIBRARY DOT PRINTF LPAREN value COMMA identifiers RPAREN'''
  
def p_print_withoutvalue(p):
  '''print_withoutvalue : FMT_LIBRARY DOT PRINTLN LPAREN RPAREN
            | FMT_LIBRARY DOT PRINTF LPAREN RPAREN'''

def p_assignment(p):
  '''assignment : VAR IDENTIFIER data_type EQUAL value
                | CONST IDENTIFIER data_type EQUAL value
                | VAR IDENTIFIER data_type EQUAL IDENTIFIER
                | CONST IDENTIFIER data_type EQUAL IDENTIFIER'''
  
def p_short_assignment(p):
  '''short_assignment : IDENTIFIER SHORT_VAR_DECL value
                | IDENTIFIER SHORT_VAR_DECL IDENTIFIER'''

##########            PAULA PERALTA            ############
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

##########            JORGE HERRERA            ############
def p_rule_comparation(p):
  '''rule_comparation : IDENTIFIER EQUALEQUAL value
                      | IDENTIFIER NOT_EQUAL value
                      | IDENTIFIER LESS_EQUAL value
                      | IDENTIFIER GREATER_EQUAL value
                      | IDENTIFIER LESS value
                      | IDENTIFIER GREATER value
                      | IDENTIFIER LOGICAL_AND value
                      | IDENTIFIER LOGICAL_OR value'''
  
def p_comparation_operation(p):
  '''
    comparation_operation : value EQUALEQUAL value
                        | value NOT_EQUAL value
                        | value LESS_EQUAL value
                        | value GREATER_EQUAL value
                        | value LESS value
                        | value GREATER value
                        | value LOGICAL_AND value
                        | value LOGICAL_OR value
    '''



def p_identifiers(p):
  '''identifiers : IDENTIFIER
                 | identifiers COMMA identifiers'''

##########            JUAN DEMERA            ############

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

##########            JORGE HERRERA            ############
def p_value(p):
  '''value : STRING
          | INTEGER
          | FLOAT32
          | FLOAT64
          | BOOLEAN'''

def p_data_type(p):
  '''data_type : INTEGER_DATA_TYPE
               | FLOAT32_DATA_TYPE
               | FLOAT64_DATA_TYPE
               | BOOLEAN_DATA_TYPE
               | STRING_DATA_TYPE'''

##########            PAULA PERALTA            ############
def p_input(p):
    '''input : INPUT LPAREN RPAREN
             | INPUT LPAREN value RPAREN
             | INPUT LPAREN identifiers RPAREN
    '''

def p_newline(p):
    '''
    newline : \n
    '''

def p_error(p):
    print("Error sintáctico en '%s'" % p)

parser = sint.yacc()

codePaula = '''input()
var id int = 4
input(y, z)
input(3)
'''
codeJorge = '''var id int = 4
a := 3
fmt.Printf("Number: \%\d", id)
fmt.Println("Este es un print simple")'''
codeJuan = """
var x int = 10
sumar := func(a, b int) int {
    return a + b }
resultado := sumar(5, 3)
fmt.Println("Resultado de la suma:", resultado)
   
for {
   fmt.Println("Este es un bucle infinito")
   break 
 }
fmt.Printf("El resultado es: %d\n", 42)
const pi float64 = 3.14159
fmt.Println("Valor de pi:", pi)

"""

code = codePaula + codeJorge + codeJuan
for c in code.split("\n"):
  result = parser.parse(c)
  print(result)
