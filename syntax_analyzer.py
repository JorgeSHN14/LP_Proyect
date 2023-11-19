import ply.yacc as sint
from lex_analyzer import tokens

def p_loop_program(p):
  ''' loop_program : program
                  | BREAK
                  | loop_program program
                  | loop_program BREAK
  '''

def p_program(p):
  '''program : sentencia
             | loop
             | program sentencia
             | program loop
  '''

def p_loop(p):
  '''loop : for
  '''

def p_sentencia(p):
  '''sentencia : print
               | print_withoutvalue
               | def_function
               | call_function
               | input
               | assignment
               | short_assignment
               | arithmetic_operation
               | direct_arithmetic_operation'''
               

##########            PAULA PERALTA            ############
def p_for(p):
  '''for : FOR LKEY loop_program RKEY
         | FOR comparation_operation LKEY loop_program RKEY'''

##########            JORGE HERRERA            ############

  
def p_print(p):
  '''print : FMT_LIBRARY DOT PRINTLN LPAREN data RPAREN
           | FMT_LIBRARY DOT PRINTF LPAREN value RPAREN
           | FMT_LIBRARY DOT PRINTF LPAREN value COMMA RPAREN
           | FMT_LIBRARY DOT PRINTF LPAREN value COMMA data RPAREN'''
  
def p_data(p):
  '''data : value
         | IDENTIFIER
         | data COMMA value
         | data COMMA IDENTIFIER'''
  
def p_print_withoutvalue(p):
  '''print_withoutvalue : FMT_LIBRARY DOT PRINTLN LPAREN RPAREN
            | FMT_LIBRARY DOT PRINTF LPAREN RPAREN'''

def p_assignment(p):
  '''assignment : VAR IDENTIFIER data_type EQUAL usable_value
                | CONST IDENTIFIER data_type EQUAL usable_value'''
  
def p_short_assignment(p):
  '''short_assignment : IDENTIFIER SHORT_VAR_DECL usable_value'''

def p_usable_value(p): 
  ''' usable_value : value
                 | call_function
                 | IDENTIFIER
                 | arithmetic_operation
                 | comparation_operation
  '''

##########            PAULA PERALTA            ############
def p_direct_arithmetic_operation(p):
    '''
    direct_arithmetic_operation : IDENTIFIER PLUS_EQ value
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
  
def p_arithmetic_operation(p):
    '''
    arithmetic_operation : usable_value PLUS usable_value
                        | usable_value MINUS usable_value
                        | usable_value DIVIDE usable_value
                        | usable_value TIMES usable_value
                        | usable_value ENTERE_DIVIDE usable_value
                        | usable_value MODULE usable_value
    '''

##########            JORGE HERRERA            ############

def p_comparation_operation(p):
  '''
    comparation_operation : usable_value EQUALEQUAL usable_value
                        | usable_value NOT_EQUAL usable_value
                        | usable_value LESS_EQUAL usable_value
                        | usable_value GREATER_EQUAL usable_value
                        | usable_value LESS usable_value
                        | usable_value GREATER usable_value
                        | usable_value LOGICAL_AND usable_value
                        | usable_value LOGICAL_OR usable_value
    '''


def p_identifiers(p):
  '''identifiers : IDENTIFIER
                 | identifiers COMMA identifiers'''

##########            JUAN DEMERA            ############

def p_def_function(p):
  '''def_function : FUNC IDENTIFIER LPAREN parameters RPAREN LKEY program RKEY'''

def p_call_funcion(p):
  '''call_function : IDENTIFIER LPAREN values RPAREN'''

def p_parameters(p):
  '''parameters : parameter
                | parameters COMMA parameter'''

def p_parameter(p):
  ''' parameter : IDENTIFIER data_type'''

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
codeJuan = """var x int = 10
func sumar(a int, b int) {
a := a + b
fmt.Println(a)
}
resultado := sumar(5, 3)
fmt.Println("Resultado de la suma:", resultado)
for {
fmt.Println("Este es un bucle infinito")
break}
const pi float64 = 3.14159f32
fmt.Println("Valor de pi:", pi)"""

code = codePaula + codeJorge + codeJuan
result = parser.parse(code)
print(result)
