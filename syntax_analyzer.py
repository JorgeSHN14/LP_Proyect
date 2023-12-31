import ply.yacc as sint
from lex_analyzer import tokens,lexer

def p_loop_program(p):
  ''' loop_program : program
                  | loop_reserved
                  | loop_program program
                  | loop_program loop_reserved
  '''
def p_func_program(p):
  ''' func_program : program
                  | RETURN
                  | RETURN usable_value
                  | func_program program
                  | func_program RETURN
                  | func_program RETURN usable_value
  '''

def p_program(p):
  '''program : sentencia
             | loop
             | program sentencia
             | program loop
  '''

def p_loop_reserved(p):
   ''' loop_reserved : BREAK
                  | CONTINUE
                  | PASS
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
               | short_assignment
               | arithmetic_operation
               | direct_arithmetic_operation
               | if_statement
               | function_call
               | assignment_semantic
               | switch_statement'''
               

##########            JORGE HERRERA            ############
def p_for(p):
  '''for : FOR LKEY loop_program RKEY
         | FOR comparation_operation LKEY loop_program RKEY
         | FOR short_assignment SEMICOLON comparation_operation SEMICOLON IDENTIFIER operator_for LKEY loop_program RKEY'''

def p_operator_for(p):
   '''operator_for : INCREASE
                   | DECREASE'''

def p_function_call(p):
    '''function_call : IDENTIFIER LPAREN values RPAREN'''

##########            PAULA PERALTA           ############

def p_if_statement(p):
    '''if_statement : IF comparation_operation LKEY program RKEY
                    | IF comparation_operation LKEY program RKEY conditions_elseif
                    | IF comparation_operation LKEY program RKEY ELSE LKEY program RKEY
                    | IF comparation_operation LKEY program RKEY conditions_elseif ELSE LKEY program RKEY
    '''


def p_conditions_elseif(p):
   '''conditions_elseif : else_if
                        | conditions_elseif else_if
   '''

def p_else_if(p):
   '''else_if : ELSE IF comparation_operation LKEY program RKEY
   '''
def p_switch_statement(p):
    '''
    switch_statement : SWITCH expression LKEY case_clauses RKEY
                     | SWITCH expression LKEY case_clauses DEFAULT COLON statements RKEY
    '''

def p_case_clauses(p):
    '''
    case_clauses : case_clause case_clauses
                 |
    '''

def p_case_clause(p):
    '''
    case_clause : CASE value COLON statements
    '''

def p_statements(p):
    '''
    statements : statement statements
              |
    '''

def p_statement(p):
    '''statement : print
                 | print_withoutvalue
                 | def_function
                 | call_function
                 | input
                 | short_assignment
                 | arithmetic_operation
                 | direct_arithmetic_operation
                 | if_statement
                 | function_call
                 | switch_statement
                 | assignment_semantic
                 | statement
    '''

def p_expression(p):
    '''
    expression : value
               | expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression ENTERE_DIVIDE expression
               | expression MODULE expression
               | expression EQUALEQUAL expression
               | expression NOT_EQUAL expression
               | expression LESS_EQUAL expression
               | expression GREATER_EQUAL expression
               | expression LESS expression
               | expression GREATER expression
               | expression LOGICAL_AND expression
               | expression LOGICAL_OR expression
    '''


##########            JORGE HERRERA            ############

#################             REGLAS SEMANTICAS PARA PRONT FORMAT DEFINIDAS POR PAULA PERALTA
def p_print(p):
    '''print : FMT_LIBRARY DOT PRINTLN LPAREN data RPAREN
             | FMT_LIBRARY DOT PRINTF LPAREN STRING RPAREN
             | FMT_LIBRARY DOT PRINTF LPAREN STRING COMMA RPAREN
             | FMT_LIBRARY DOT PRINTF LPAREN STRING COMMA data RPAREN
    '''

  
def p_data(p):
  '''data : value
         | IDENTIFIER
         | data COMMA value
         | data COMMA IDENTIFIER'''
  
def p_print_withoutvalue(p):
  '''print_withoutvalue : FMT_LIBRARY DOT PRINTLN LPAREN RPAREN
            | FMT_LIBRARY DOT PRINTF LPAREN RPAREN'''


##########            JUAN DEMERA            ############

##########     REGAL SEMANTICA PARA LA DECLARACION DE VARIABLES
def p_assignment_semantic(p):
  '''assignment_semantic : VAR IDENTIFIER INTEGER_DATA_TYPE EQUAL INTEGER
                | CONST IDENTIFIER INTEGER_DATA_TYPE EQUAL INTEGER
                | VAR IDENTIFIER FLOAT_DATA_TYPE EQUAL FLOAT
                | CONST IDENTIFIER FLOAT_DATA_TYPE EQUAL FLOAT
                | VAR IDENTIFIER STRING_DATA_TYPE EQUAL STRING
                | CONST IDENTIFIER STRING_DATA_TYPE EQUAL STRING
                | VAR IDENTIFIER BOOLEAN_DATA_TYPE EQUAL BOOLEAN
                | CONST IDENTIFIER BOOLEAN_DATA_TYPE EQUAL BOOLEAN'''

  
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
  
##########            PAULA PERALTA            ############
def p_rule_comparation(p):
    '''rule_comparation : IDENTIFIER EQUALEQUAL value
                        | IDENTIFIER NOT_EQUAL value
                        | IDENTIFIER LESS_EQUAL value
                        | IDENTIFIER GREATER_EQUAL value
                        | IDENTIFIER LESS value
                        | IDENTIFIER GREATER value
                        | IDENTIFIER LOGICAL_AND value
                        | IDENTIFIER LOGICAL_OR value'''

def p_condition(p):
    '''
    condition : value comparation_operation value
              | condition LOGICAL_AND condition
              | condition LOGICAL_OR condition
              | LOGICAL_NOT condition
    '''


##########            JUAN DEMERA            ############

def p_def_function(p):
  '''def_function : FUNC IDENTIFIER LPAREN parameters RPAREN LKEY func_program RKEY
                  | FUNC IDENTIFIER LPAREN parameters RPAREN data_type LKEY func_program RKEY
                 '''


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
          | FLOAT
          | BOOLEAN
          | IDENTIFIER'''

def p_data_type(p):
  '''data_type : INTEGER_DATA_TYPE
               | FLOAT_DATA_TYPE
               | BOOLEAN_DATA_TYPE
               | STRING_DATA_TYPE'''

##########            PAULA PERALTA            ############
def p_input(p):
    '''input : INPUT LPAREN RPAREN
             | INPUT LPAREN value RPAREN
             | INPUT LPAREN identifiers RPAREN
    '''


def p_error(p):
    errors.append("Error sintáctico en '%s'" % p)

# parser = sint.yacc()

codePaula = '''
input()
var id int = 4
input(y, z)
input(3)
var x float = 3.14
const pi float = 3.14159
input(a, b)
c := a + b
fmt.Println("Resultado:", c)
if x > 0 {
    fmt.Println("x es positivo")
    a := 3
} else if x > 0 {
    fmt.Println("x es cero o negativo")
} else {
    fmt.Println("x es cero o negativo")
}
for i := 0; i < 5; i++ {
    fmt.Println(i)
}
func suma(a int, b int) int {
    return a + b
}
resultado := suma(2, 3)
fmt.Println("Suma:", resultado)

'''

codeJorge = '''var id int = 4
a := 3
fmt.Printf("Number: \%\d", id)
fmt.Println("Este es un print simple")
'''

codeJuan = """
var x int = 10
func sumar(a int, b int) {
  a := a + b
  fmt.Println(a)
}
switch x {
    case 1:
        fmt.Println("Uno")
    case 2:
        fmt.Println("Dos o Tres")
    case 4:
        fmt.Println("Cuatro")
    default:
        if x > 10 {
            fmt.Println("Mayor que 10")
        } else {
            fmt.Println("Otro")
        }
}
switch x {
    case 1:
        fmt.Println("Uno")
    case 2:
        fmt.Println("Dos")
    default:
        fmt.Println("Otro")
}

resultado := sumar(5, 3)
fmt.Println("Resultado de la suma:", resultado)
for {
fmt.Println("Este es un bucle infinito")
break}
const pi float = 3.14159
fmt.Println("Valor de pi:", pi)"""

code = codePaula + codeJorge + codeJuan
# result = parser.parse(code)
# print(result)

def get_parser():
    return sint.yacc()

errors = []
def analizeSyntax(code):
  parser = get_parser()
  parser.parse(code)
  returnErrors = errors.copy()
  errors.clear()
  list(lexer)
  return returnErrors

print(analizeSyntax(code))