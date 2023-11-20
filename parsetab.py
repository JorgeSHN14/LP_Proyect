
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AMPERSAND AND ARROW_FUNCTION_TYPE ARROW_SEND_RECEIVE AS ASSERT BITWISE_AND_EQ BITWISE_OR_EQ BITWISE_XOR BITWISE_XOR_ASSIGN BITWISE_XOR_EQ BOOLEAN BOOLEAN_DATA_TYPE BREAK CLASS COLON COMMA COMMENT COMMENT_MULTI CONST CONTINUE DEL DIVIDE DIVIDE_EQ DOT ELIF ELLIPSIS ELSE ENTERE_DIVIDE EQUAL EQUALEQUAL EXCEPT FALSE FAT_ARROW FINALLY FLOAT32 FLOAT32_DATA_TYPE FLOAT64 FLOAT64_DATA_TYPE FMT_LIBRARY FOR FROM FUNC GLOBAL GREATER GREATER_EQUAL GREATER_THAN HEX_NUMBER IDENTIFIER IF IMPORT IN INPUT INTEGER INTEGER_DATA_TYPE IS LAMBDA LBRACKET LEFT_SHIFT_EQ LESS LESS_EQUAL LESS_THAN LKEY LOGICAL_AND LOGICAL_NOT LOGICAL_OR LPAREN MINUS MINUS_EQ MODULE MODULO_EQ NONE NONLOCAL NOT NOT_EQUAL NULL OR PASS PIPE PLUS PLUS_EQ PRINTF PRINTLN RAISE RBRACKET RETURN RIGHT_SHIFT_EQ RKEY RPAREN RULE_COMPARATION SCIENTIFIC_NOTATION SHORT_VAR_DECL STRING STRING_DATA_TYPE TIMES TIMES_EQ TRUE TRY VAR WITH YIELD loop_program : program\n                  | BREAK\n                  | loop_program program\n                  | loop_program BREAK\n  program : sentencia\n             | loop\n             | program sentencia\n             | program loop\n  loop : for\n  sentencia : print\n               | print_withoutvalue\n               | def_function\n               | call_function\n               | input\n               | assignment\n               | short_assignment\n               | arithmetic_operation\n               | direct_arithmetic_operation\n               | if_statement\n               | function_call for : FOR LKEY loop_program RKEY\n         | FOR comparation_operation LKEY loop_program RKEYfunction_call : IDENTIFIER LPAREN values RPARENif_statement : IF rule_comparation LKEY program RKEY\n                    | IF rule_comparation LKEY program RKEY ELSE LKEY program RKEY\n                    | IF value LKEY program RKEY\n                    | IF value LKEY program RKEY ELSE LKEY program RKEY\n    print : FMT_LIBRARY DOT PRINTLN LPAREN data RPAREN\n           | FMT_LIBRARY DOT PRINTF LPAREN value RPAREN\n           | FMT_LIBRARY DOT PRINTF LPAREN value COMMA RPAREN\n           | FMT_LIBRARY DOT PRINTF LPAREN value COMMA data RPARENdata : value\n         | IDENTIFIER\n         | data COMMA value\n         | data COMMA IDENTIFIERprint_withoutvalue : FMT_LIBRARY DOT PRINTLN LPAREN RPAREN\n            | FMT_LIBRARY DOT PRINTF LPAREN RPARENassignment : VAR IDENTIFIER data_type EQUAL usable_value\n                | CONST IDENTIFIER data_type EQUAL usable_valueshort_assignment : IDENTIFIER SHORT_VAR_DECL usable_value usable_value : value\n                 | call_function\n                 | IDENTIFIER\n                 | arithmetic_operation\n                 | comparation_operation\n  \n  direct_arithmetic_operation : IDENTIFIER PLUS_EQ value\n                      | IDENTIFIER MINUS_EQ value\n                      | IDENTIFIER TIMES_EQ value\n                      | IDENTIFIER DIVIDE_EQ value\n                      | IDENTIFIER MODULO_EQ value\n                      | IDENTIFIER BITWISE_AND_EQ value\n                      | IDENTIFIER BITWISE_OR_EQ value\n                      | IDENTIFIER BITWISE_XOR_EQ value\n                      | IDENTIFIER LEFT_SHIFT_EQ value\n                      | IDENTIFIER RIGHT_SHIFT_EQ value\n  \n  arithmetic_operation : usable_value PLUS usable_value\n                      | usable_value MINUS usable_value\n                      | usable_value DIVIDE usable_value\n                      | usable_value TIMES usable_value\n                      | usable_value ENTERE_DIVIDE usable_value\n                      | usable_value MODULE usable_value\n  \n    comparation_operation : usable_value EQUALEQUAL usable_value\n                        | usable_value NOT_EQUAL usable_value\n                        | usable_value LESS_EQUAL usable_value\n                        | usable_value GREATER_EQUAL usable_value\n                        | usable_value LESS usable_value\n                        | usable_value GREATER usable_value\n                        | usable_value LOGICAL_AND usable_value\n                        | usable_value LOGICAL_OR usable_value\n    identifiers : IDENTIFIER\n                 | identifiers COMMA identifiersrule_comparation : IDENTIFIER EQUALEQUAL value\n                        | IDENTIFIER NOT_EQUAL value\n                        | IDENTIFIER LESS_EQUAL value\n                        | IDENTIFIER GREATER_EQUAL value\n                        | IDENTIFIER LESS value\n                        | IDENTIFIER GREATER value\n                        | IDENTIFIER LOGICAL_AND value\n                        | IDENTIFIER LOGICAL_OR value\n    condition : value comparation_operation value\n              | condition LOGICAL_AND condition\n              | condition LOGICAL_OR condition\n              | LOGICAL_NOT condition\n    def_function : FUNC IDENTIFIER LPAREN parameters RPAREN LKEY program RKEYcall_function : IDENTIFIER LPAREN values RPARENparameters : parameter\n                | parameters COMMA parameter parameter : IDENTIFIER data_typevalues : value\n            | values COMMA valuevalue : STRING\n          | INTEGER\n          | FLOAT32\n          | FLOAT64\n          | BOOLEANdata_type : INTEGER_DATA_TYPE\n               | FLOAT32_DATA_TYPE\n               | FLOAT64_DATA_TYPE\n               | BOOLEAN_DATA_TYPE\n               | STRING_DATA_TYPEinput : INPUT LPAREN RPAREN\n             | INPUT LPAREN value RPAREN\n             | INPUT LPAREN identifiers RPAREN\n    '
    
_lr_action_items = {'BREAK':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,28,29,30,31,32,33,34,35,36,37,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,129,130,137,139,140,154,155,158,162,168,169,170,171,172,173,174,176,184,189,190,193,194,],[3,35,-1,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,-45,-91,-92,-93,-94,-95,-3,-4,-7,-8,3,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,35,3,-23,-102,-103,-21,35,-36,-37,-38,-39,-24,-26,-22,-85,-28,-29,-30,-31,-84,-25,-27,]),'FMT_LIBRARY':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,28,29,30,31,32,33,34,35,36,37,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,129,130,137,139,140,144,145,154,155,158,162,168,169,170,171,172,173,174,176,178,184,186,187,188,189,190,191,192,193,194,],[18,18,18,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,-45,-91,-92,-93,-94,-95,18,-4,-7,-8,18,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,18,18,18,18,-23,-102,-103,18,18,-21,18,-36,-37,-38,-39,-24,-26,-22,-85,-28,-29,18,-30,18,18,18,-31,-84,18,18,-25,-27,]),'FUNC':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,28,29,30,31,32,33,34,35,36,37,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,129,130,137,139,140,144,145,154,155,158,162,168,169,170,171,172,173,174,176,178,184,186,187,188,189,190,191,192,193,194,],[20,20,20,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,-45,-91,-92,-93,-94,-95,20,-4,-7,-8,20,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,20,20,20,20,-23,-102,-103,20,20,-21,20,-36,-37,-38,-39,-24,-26,-22,-85,-28,-29,20,-30,20,20,20,-31,-84,20,20,-25,-27,]),'IDENTIFIER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,41,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,75,76,77,80,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,129,130,132,137,139,140,141,142,143,144,145,154,155,158,162,165,168,169,170,171,172,173,174,175,176,177,178,184,186,187,188,189,190,191,192,193,194,],[21,21,21,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,39,53,68,71,76,-45,-91,-92,-93,-94,-95,21,-4,-7,-8,76,97,76,76,76,76,76,76,76,76,76,76,76,76,76,76,21,-42,-43,-44,134,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,21,21,21,21,160,-23,-102,-103,97,76,76,21,21,-21,21,-36,-37,134,-38,-39,-24,-26,-22,-85,-28,183,-29,160,21,-30,21,21,21,-31,-84,21,21,-25,-27,]),'INPUT':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,28,29,30,31,32,33,34,35,36,37,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,129,130,137,139,140,144,145,154,155,158,162,168,169,170,171,172,173,174,176,178,184,186,187,188,189,190,191,192,193,194,],[22,22,22,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,-45,-91,-92,-93,-94,-95,22,-4,-7,-8,22,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,22,22,22,22,-23,-102,-103,22,22,-21,22,-36,-37,-38,-39,-24,-26,-22,-85,-28,-29,22,-30,22,22,22,-31,-84,22,22,-25,-27,]),'VAR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,28,29,30,31,32,33,34,35,36,37,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,129,130,137,139,140,144,145,154,155,158,162,168,169,170,171,172,173,174,176,178,184,186,187,188,189,190,191,192,193,194,],[23,23,23,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,-45,-91,-92,-93,-94,-95,23,-4,-7,-8,23,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,23,23,23,23,-23,-102,-103,23,23,-21,23,-36,-37,-38,-39,-24,-26,-22,-85,-28,-29,23,-30,23,23,23,-31,-84,23,23,-25,-27,]),'CONST':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,28,29,30,31,32,33,34,35,36,37,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,129,130,137,139,140,144,145,154,155,158,162,168,169,170,171,172,173,174,176,178,184,186,187,188,189,190,191,192,193,194,],[25,25,25,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,-45,-91,-92,-93,-94,-95,25,-4,-7,-8,25,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,25,25,25,25,-23,-102,-103,25,25,-21,25,-36,-37,-38,-39,-24,-26,-22,-85,-28,-29,25,-30,25,25,25,-31,-84,25,25,-25,-27,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,28,29,30,31,32,33,34,35,36,37,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,129,130,137,139,140,144,145,154,155,158,162,168,169,170,171,172,173,174,176,178,184,186,187,188,189,190,191,192,193,194,],[26,26,26,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,-45,-91,-92,-93,-94,-95,26,-4,-7,-8,26,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,26,26,26,26,-23,-102,-103,26,26,-21,26,-36,-37,-38,-39,-24,-26,-22,-85,-28,-29,26,-30,26,26,26,-31,-84,26,26,-25,-27,]),'FOR':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,28,29,30,31,32,33,34,35,36,37,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,129,130,137,139,140,144,145,154,155,158,162,168,169,170,171,172,173,174,176,178,184,186,187,188,189,190,191,192,193,194,],[27,27,27,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,-45,-91,-92,-93,-94,-95,27,-4,-7,-8,27,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,27,27,27,27,-23,-102,-103,27,27,-21,27,-36,-37,-38,-39,-24,-26,-22,-85,-28,-29,27,-30,27,27,27,-31,-84,27,27,-25,-27,]),'STRING':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,26,27,28,29,30,31,32,33,34,35,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,137,138,139,140,142,143,144,145,154,155,158,162,168,169,170,171,172,173,174,175,176,177,178,184,186,187,188,189,190,191,192,193,194,],[29,29,29,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,29,29,-45,-91,-92,-93,-94,-95,29,-4,-7,-8,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-23,29,-102,-103,29,29,29,29,-21,29,-36,-37,-38,-39,-24,-26,-22,-85,-28,29,-29,29,29,-30,29,29,29,-31,-84,29,29,-25,-27,]),'INTEGER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,26,27,28,29,30,31,32,33,34,35,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,137,138,139,140,142,143,144,145,154,155,158,162,168,169,170,171,172,173,174,175,176,177,178,184,186,187,188,189,190,191,192,193,194,],[30,30,30,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,30,30,-45,-91,-92,-93,-94,-95,30,-4,-7,-8,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-23,30,-102,-103,30,30,30,30,-21,30,-36,-37,-38,-39,-24,-26,-22,-85,-28,30,-29,30,30,-30,30,30,30,-31,-84,30,30,-25,-27,]),'FLOAT32':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,26,27,28,29,30,31,32,33,34,35,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,137,138,139,140,142,143,144,145,154,155,158,162,168,169,170,171,172,173,174,175,176,177,178,184,186,187,188,189,190,191,192,193,194,],[31,31,31,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,31,31,-45,-91,-92,-93,-94,-95,31,-4,-7,-8,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-23,31,-102,-103,31,31,31,31,-21,31,-36,-37,-38,-39,-24,-26,-22,-85,-28,31,-29,31,31,-30,31,31,31,-31,-84,31,31,-25,-27,]),'FLOAT64':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,26,27,28,29,30,31,32,33,34,35,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,137,138,139,140,142,143,144,145,154,155,158,162,168,169,170,171,172,173,174,175,176,177,178,184,186,187,188,189,190,191,192,193,194,],[32,32,32,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,32,32,-45,-91,-92,-93,-94,-95,32,-4,-7,-8,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-23,32,-102,-103,32,32,32,32,-21,32,-36,-37,-38,-39,-24,-26,-22,-85,-28,32,-29,32,32,-30,32,32,32,-31,-84,32,32,-25,-27,]),'BOOLEAN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,26,27,28,29,30,31,32,33,34,35,36,37,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,137,138,139,140,142,143,144,145,154,155,158,162,168,169,170,171,172,173,174,175,176,177,178,184,186,187,188,189,190,191,192,193,194,],[33,33,33,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,33,33,-45,-91,-92,-93,-94,-95,33,-4,-7,-8,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-23,33,-102,-103,33,33,33,33,-21,33,-36,-37,-38,-39,-24,-26,-22,-85,-28,33,-29,33,33,-30,33,33,33,-31,-84,33,33,-25,-27,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,28,29,30,31,32,33,34,35,36,37,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,139,140,154,158,162,168,169,170,171,172,173,174,176,184,189,190,193,194,],[0,-1,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,-45,-91,-92,-93,-94,-95,-3,-4,-7,-8,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-23,-102,-103,-21,-36,-37,-38,-39,-24,-26,-22,-85,-28,-29,-30,-31,-84,-25,-27,]),'RKEY':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,28,29,30,31,32,33,34,35,36,37,75,76,77,83,84,85,86,87,88,89,90,91,92,93,94,104,105,106,107,108,109,110,111,112,113,114,115,116,117,129,137,139,140,144,145,154,155,158,162,168,169,170,171,172,173,174,176,184,186,189,190,191,192,193,194,],[-1,-2,-5,-6,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-9,-41,-45,-91,-92,-93,-94,-95,-3,-4,-7,-8,-42,-43,-44,-40,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-101,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,154,-23,-102,-103,170,171,-21,172,-36,-37,-38,-39,-24,-26,-22,-85,-28,-29,-30,190,-31,-84,193,194,-25,-27,]),'PLUS':([9,13,19,21,24,28,29,30,31,32,33,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,54,-45,-91,-92,-93,-94,-95,-45,54,-42,-43,-44,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-85,54,54,-85,]),'MINUS':([9,13,19,21,24,28,29,30,31,32,33,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,55,-45,-91,-92,-93,-94,-95,-45,55,-42,-43,-44,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-85,55,55,-85,]),'DIVIDE':([9,13,19,21,24,28,29,30,31,32,33,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,56,-45,-91,-92,-93,-94,-95,-45,56,-42,-43,-44,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-85,56,56,-85,]),'TIMES':([9,13,19,21,24,28,29,30,31,32,33,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,57,-45,-91,-92,-93,-94,-95,-45,57,-42,-43,-44,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-85,57,57,-85,]),'ENTERE_DIVIDE':([9,13,19,21,24,28,29,30,31,32,33,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,58,-45,-91,-92,-93,-94,-95,-45,58,-42,-43,-44,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-85,58,58,-85,]),'MODULE':([9,13,19,21,24,28,29,30,31,32,33,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,59,-45,-91,-92,-93,-94,-95,-45,59,-42,-43,-44,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-85,59,59,-85,]),'EQUALEQUAL':([9,13,19,21,24,28,29,30,31,32,33,71,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,60,-45,-91,-92,-93,-94,-95,121,-45,60,-42,-43,-44,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-85,60,60,-85,]),'NOT_EQUAL':([9,13,19,21,24,28,29,30,31,32,33,71,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,61,-45,-91,-92,-93,-94,-95,122,-45,61,-42,-43,-44,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,-85,61,61,-85,]),'LESS_EQUAL':([9,13,19,21,24,28,29,30,31,32,33,71,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,62,-45,-91,-92,-93,-94,-95,123,-45,62,-42,-43,-44,62,62,62,62,62,62,62,62,62,62,62,62,62,62,62,-85,62,62,-85,]),'GREATER_EQUAL':([9,13,19,21,24,28,29,30,31,32,33,71,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,63,-45,-91,-92,-93,-94,-95,124,-45,63,-42,-43,-44,63,63,63,63,63,63,63,63,63,63,63,63,63,63,63,-85,63,63,-85,]),'LESS':([9,13,19,21,24,28,29,30,31,32,33,71,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,64,-45,-91,-92,-93,-94,-95,125,-45,64,-42,-43,-44,64,64,64,64,64,64,64,64,64,64,64,64,64,64,64,-85,64,64,-85,]),'GREATER':([9,13,19,21,24,28,29,30,31,32,33,71,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,65,-45,-91,-92,-93,-94,-95,126,-45,65,-42,-43,-44,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,-85,65,65,-85,]),'LOGICAL_AND':([9,13,19,21,24,28,29,30,31,32,33,71,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,66,-45,-91,-92,-93,-94,-95,127,-45,66,-42,-43,-44,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,-85,66,66,-85,]),'LOGICAL_OR':([9,13,19,21,24,28,29,30,31,32,33,71,73,74,75,76,77,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,137,168,169,173,],[-42,-44,-41,-43,67,-45,-91,-92,-93,-94,-95,128,-45,67,-42,-43,-44,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,-85,67,67,-85,]),'DOT':([18,],[38,]),'LKEY':([19,27,28,29,30,31,32,33,69,70,73,75,76,77,104,105,106,107,108,109,110,111,112,113,114,115,116,117,146,147,148,149,150,151,152,153,164,173,180,181,],[-41,72,-45,-91,-92,-93,-94,-95,119,120,130,-42,-43,-44,-56,-57,-58,-59,-60,-61,-62,-63,-64,-65,-66,-67,-68,-69,-72,-73,-74,-75,-76,-77,-78,-79,178,-85,187,188,]),'LPAREN':([21,22,39,76,78,79,],[40,52,80,131,132,133,]),'SHORT_VAR_DECL':([21,],[41,]),'PLUS_EQ':([21,],[42,]),'MINUS_EQ':([21,],[43,]),'TIMES_EQ':([21,],[44,]),'DIVIDE_EQ':([21,],[45,]),'MODULO_EQ':([21,],[46,]),'BITWISE_AND_EQ':([21,],[47,]),'BITWISE_OR_EQ':([21,],[48,]),'BITWISE_XOR_EQ':([21,],[49,]),'LEFT_SHIFT_EQ':([21,],[50,]),'RIGHT_SHIFT_EQ':([21,],[51,]),'RPAREN':([29,30,31,32,33,52,81,82,95,96,97,99,100,101,102,103,132,133,135,136,156,157,159,160,161,163,166,167,177,179,182,183,185,],[-91,-92,-93,-94,-95,94,137,-89,139,140,-70,-96,-97,-98,-99,-100,158,162,164,-86,173,174,-32,-33,176,-88,-90,-71,184,-87,-34,-35,189,]),'COMMA':([29,30,31,32,33,81,82,96,97,99,100,101,102,103,135,136,156,157,159,160,161,163,166,167,179,182,183,185,],[-91,-92,-93,-94,-95,138,-89,141,-70,-96,-97,-98,-99,-100,165,-86,138,175,-32,-33,177,-88,-90,141,-87,-34,-35,175,]),'PRINTLN':([38,],[78,]),'PRINTF':([38,],[79,]),'INTEGER_DATA_TYPE':([53,68,134,],[99,99,99,]),'FLOAT32_DATA_TYPE':([53,68,134,],[100,100,100,]),'FLOAT64_DATA_TYPE':([53,68,134,],[101,101,101,]),'BOOLEAN_DATA_TYPE':([53,68,134,],[102,102,102,]),'STRING_DATA_TYPE':([53,68,134,],[103,103,103,]),'EQUAL':([98,99,100,101,102,103,118,],[142,-96,-97,-98,-99,-100,143,]),'ELSE':([170,171,],[180,181,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'loop_program':([0,72,130,],[1,129,155,]),'program':([0,1,72,119,120,129,130,155,178,187,188,],[2,34,2,144,145,34,2,34,186,191,192,]),'sentencia':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[4,4,36,36,4,4,4,4,4,36,36,4,4,36,4,4,36,36,]),'loop':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[5,5,37,37,5,5,5,5,5,37,37,5,5,37,5,5,37,37,]),'print':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'print_withoutvalue':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'def_function':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'call_function':([0,1,2,27,34,41,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,119,120,129,130,142,143,144,145,155,178,186,187,188,191,192,],[9,9,9,75,9,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,9,9,9,9,9,75,75,9,9,9,9,9,9,9,9,9,]),'input':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'assignment':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'short_assignment':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'arithmetic_operation':([0,1,2,27,34,41,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,119,120,129,130,142,143,144,145,155,178,186,187,188,191,192,],[13,13,13,77,13,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,13,13,13,13,13,77,77,13,13,13,13,13,13,13,13,13,]),'direct_arithmetic_operation':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'if_statement':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'function_call':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'for':([0,1,2,34,72,119,120,129,130,144,145,155,178,186,187,188,191,192,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'value':([0,1,2,26,27,34,40,41,42,43,44,45,46,47,48,49,50,51,52,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,138,142,143,144,145,155,175,177,178,186,187,188,191,192,],[19,19,19,70,19,19,82,19,84,85,86,87,88,89,90,91,92,93,95,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,146,147,148,149,150,151,152,153,19,19,82,159,161,166,19,19,19,19,19,182,159,19,19,19,19,19,19,]),'usable_value':([0,1,2,27,34,41,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,119,120,129,130,142,143,144,145,155,178,186,187,188,191,192,],[24,24,24,74,24,83,104,105,106,107,108,109,110,111,112,113,114,115,116,117,24,24,24,24,24,168,169,24,24,24,24,24,24,24,24,24,]),'comparation_operation':([0,1,2,27,34,41,54,55,56,57,58,59,60,61,62,63,64,65,66,67,72,119,120,129,130,142,143,144,145,155,178,186,187,188,191,192,],[28,28,28,73,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'rule_comparation':([26,],[69,]),'values':([40,131,],[81,156,]),'identifiers':([52,141,],[96,167,]),'data_type':([53,68,134,],[98,118,163,]),'parameters':([80,],[135,]),'parameter':([80,165,],[136,179,]),'data':([132,177,],[157,185,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> loop_program","S'",1,None,None,None),
  ('loop_program -> program','loop_program',1,'p_loop_program','syntax_analyzer.py',5),
  ('loop_program -> BREAK','loop_program',1,'p_loop_program','syntax_analyzer.py',6),
  ('loop_program -> loop_program program','loop_program',2,'p_loop_program','syntax_analyzer.py',7),
  ('loop_program -> loop_program BREAK','loop_program',2,'p_loop_program','syntax_analyzer.py',8),
  ('program -> sentencia','program',1,'p_program','syntax_analyzer.py',12),
  ('program -> loop','program',1,'p_program','syntax_analyzer.py',13),
  ('program -> program sentencia','program',2,'p_program','syntax_analyzer.py',14),
  ('program -> program loop','program',2,'p_program','syntax_analyzer.py',15),
  ('loop -> for','loop',1,'p_loop','syntax_analyzer.py',19),
  ('sentencia -> print','sentencia',1,'p_sentencia','syntax_analyzer.py',23),
  ('sentencia -> print_withoutvalue','sentencia',1,'p_sentencia','syntax_analyzer.py',24),
  ('sentencia -> def_function','sentencia',1,'p_sentencia','syntax_analyzer.py',25),
  ('sentencia -> call_function','sentencia',1,'p_sentencia','syntax_analyzer.py',26),
  ('sentencia -> input','sentencia',1,'p_sentencia','syntax_analyzer.py',27),
  ('sentencia -> assignment','sentencia',1,'p_sentencia','syntax_analyzer.py',28),
  ('sentencia -> short_assignment','sentencia',1,'p_sentencia','syntax_analyzer.py',29),
  ('sentencia -> arithmetic_operation','sentencia',1,'p_sentencia','syntax_analyzer.py',30),
  ('sentencia -> direct_arithmetic_operation','sentencia',1,'p_sentencia','syntax_analyzer.py',31),
  ('sentencia -> if_statement','sentencia',1,'p_sentencia','syntax_analyzer.py',32),
  ('sentencia -> function_call','sentencia',1,'p_sentencia','syntax_analyzer.py',33),
  ('for -> FOR LKEY loop_program RKEY','for',4,'p_for','syntax_analyzer.py',38),
  ('for -> FOR comparation_operation LKEY loop_program RKEY','for',5,'p_for','syntax_analyzer.py',39),
  ('function_call -> IDENTIFIER LPAREN values RPAREN','function_call',4,'p_function_call','syntax_analyzer.py',42),
  ('if_statement -> IF rule_comparation LKEY program RKEY','if_statement',5,'p_if_statement','syntax_analyzer.py',45),
  ('if_statement -> IF rule_comparation LKEY program RKEY ELSE LKEY program RKEY','if_statement',9,'p_if_statement','syntax_analyzer.py',46),
  ('if_statement -> IF value LKEY program RKEY','if_statement',5,'p_if_statement','syntax_analyzer.py',47),
  ('if_statement -> IF value LKEY program RKEY ELSE LKEY program RKEY','if_statement',9,'p_if_statement','syntax_analyzer.py',48),
  ('print -> FMT_LIBRARY DOT PRINTLN LPAREN data RPAREN','print',6,'p_print','syntax_analyzer.py',56),
  ('print -> FMT_LIBRARY DOT PRINTF LPAREN value RPAREN','print',6,'p_print','syntax_analyzer.py',57),
  ('print -> FMT_LIBRARY DOT PRINTF LPAREN value COMMA RPAREN','print',7,'p_print','syntax_analyzer.py',58),
  ('print -> FMT_LIBRARY DOT PRINTF LPAREN value COMMA data RPAREN','print',8,'p_print','syntax_analyzer.py',59),
  ('data -> value','data',1,'p_data','syntax_analyzer.py',62),
  ('data -> IDENTIFIER','data',1,'p_data','syntax_analyzer.py',63),
  ('data -> data COMMA value','data',3,'p_data','syntax_analyzer.py',64),
  ('data -> data COMMA IDENTIFIER','data',3,'p_data','syntax_analyzer.py',65),
  ('print_withoutvalue -> FMT_LIBRARY DOT PRINTLN LPAREN RPAREN','print_withoutvalue',5,'p_print_withoutvalue','syntax_analyzer.py',68),
  ('print_withoutvalue -> FMT_LIBRARY DOT PRINTF LPAREN RPAREN','print_withoutvalue',5,'p_print_withoutvalue','syntax_analyzer.py',69),
  ('assignment -> VAR IDENTIFIER data_type EQUAL usable_value','assignment',5,'p_assignment','syntax_analyzer.py',72),
  ('assignment -> CONST IDENTIFIER data_type EQUAL usable_value','assignment',5,'p_assignment','syntax_analyzer.py',73),
  ('short_assignment -> IDENTIFIER SHORT_VAR_DECL usable_value','short_assignment',3,'p_short_assignment','syntax_analyzer.py',76),
  ('usable_value -> value','usable_value',1,'p_usable_value','syntax_analyzer.py',79),
  ('usable_value -> call_function','usable_value',1,'p_usable_value','syntax_analyzer.py',80),
  ('usable_value -> IDENTIFIER','usable_value',1,'p_usable_value','syntax_analyzer.py',81),
  ('usable_value -> arithmetic_operation','usable_value',1,'p_usable_value','syntax_analyzer.py',82),
  ('usable_value -> comparation_operation','usable_value',1,'p_usable_value','syntax_analyzer.py',83),
  ('direct_arithmetic_operation -> IDENTIFIER PLUS_EQ value','direct_arithmetic_operation',3,'p_direct_arithmetic_operation','syntax_analyzer.py',89),
  ('direct_arithmetic_operation -> IDENTIFIER MINUS_EQ value','direct_arithmetic_operation',3,'p_direct_arithmetic_operation','syntax_analyzer.py',90),
  ('direct_arithmetic_operation -> IDENTIFIER TIMES_EQ value','direct_arithmetic_operation',3,'p_direct_arithmetic_operation','syntax_analyzer.py',91),
  ('direct_arithmetic_operation -> IDENTIFIER DIVIDE_EQ value','direct_arithmetic_operation',3,'p_direct_arithmetic_operation','syntax_analyzer.py',92),
  ('direct_arithmetic_operation -> IDENTIFIER MODULO_EQ value','direct_arithmetic_operation',3,'p_direct_arithmetic_operation','syntax_analyzer.py',93),
  ('direct_arithmetic_operation -> IDENTIFIER BITWISE_AND_EQ value','direct_arithmetic_operation',3,'p_direct_arithmetic_operation','syntax_analyzer.py',94),
  ('direct_arithmetic_operation -> IDENTIFIER BITWISE_OR_EQ value','direct_arithmetic_operation',3,'p_direct_arithmetic_operation','syntax_analyzer.py',95),
  ('direct_arithmetic_operation -> IDENTIFIER BITWISE_XOR_EQ value','direct_arithmetic_operation',3,'p_direct_arithmetic_operation','syntax_analyzer.py',96),
  ('direct_arithmetic_operation -> IDENTIFIER LEFT_SHIFT_EQ value','direct_arithmetic_operation',3,'p_direct_arithmetic_operation','syntax_analyzer.py',97),
  ('direct_arithmetic_operation -> IDENTIFIER RIGHT_SHIFT_EQ value','direct_arithmetic_operation',3,'p_direct_arithmetic_operation','syntax_analyzer.py',98),
  ('arithmetic_operation -> usable_value PLUS usable_value','arithmetic_operation',3,'p_arithmetic_operation','syntax_analyzer.py',103),
  ('arithmetic_operation -> usable_value MINUS usable_value','arithmetic_operation',3,'p_arithmetic_operation','syntax_analyzer.py',104),
  ('arithmetic_operation -> usable_value DIVIDE usable_value','arithmetic_operation',3,'p_arithmetic_operation','syntax_analyzer.py',105),
  ('arithmetic_operation -> usable_value TIMES usable_value','arithmetic_operation',3,'p_arithmetic_operation','syntax_analyzer.py',106),
  ('arithmetic_operation -> usable_value ENTERE_DIVIDE usable_value','arithmetic_operation',3,'p_arithmetic_operation','syntax_analyzer.py',107),
  ('arithmetic_operation -> usable_value MODULE usable_value','arithmetic_operation',3,'p_arithmetic_operation','syntax_analyzer.py',108),
  ('comparation_operation -> usable_value EQUALEQUAL usable_value','comparation_operation',3,'p_comparation_operation','syntax_analyzer.py',115),
  ('comparation_operation -> usable_value NOT_EQUAL usable_value','comparation_operation',3,'p_comparation_operation','syntax_analyzer.py',116),
  ('comparation_operation -> usable_value LESS_EQUAL usable_value','comparation_operation',3,'p_comparation_operation','syntax_analyzer.py',117),
  ('comparation_operation -> usable_value GREATER_EQUAL usable_value','comparation_operation',3,'p_comparation_operation','syntax_analyzer.py',118),
  ('comparation_operation -> usable_value LESS usable_value','comparation_operation',3,'p_comparation_operation','syntax_analyzer.py',119),
  ('comparation_operation -> usable_value GREATER usable_value','comparation_operation',3,'p_comparation_operation','syntax_analyzer.py',120),
  ('comparation_operation -> usable_value LOGICAL_AND usable_value','comparation_operation',3,'p_comparation_operation','syntax_analyzer.py',121),
  ('comparation_operation -> usable_value LOGICAL_OR usable_value','comparation_operation',3,'p_comparation_operation','syntax_analyzer.py',122),
  ('identifiers -> IDENTIFIER','identifiers',1,'p_identifiers','syntax_analyzer.py',127),
  ('identifiers -> identifiers COMMA identifiers','identifiers',3,'p_identifiers','syntax_analyzer.py',128),
  ('rule_comparation -> IDENTIFIER EQUALEQUAL value','rule_comparation',3,'p_rule_comparation','syntax_analyzer.py',132),
  ('rule_comparation -> IDENTIFIER NOT_EQUAL value','rule_comparation',3,'p_rule_comparation','syntax_analyzer.py',133),
  ('rule_comparation -> IDENTIFIER LESS_EQUAL value','rule_comparation',3,'p_rule_comparation','syntax_analyzer.py',134),
  ('rule_comparation -> IDENTIFIER GREATER_EQUAL value','rule_comparation',3,'p_rule_comparation','syntax_analyzer.py',135),
  ('rule_comparation -> IDENTIFIER LESS value','rule_comparation',3,'p_rule_comparation','syntax_analyzer.py',136),
  ('rule_comparation -> IDENTIFIER GREATER value','rule_comparation',3,'p_rule_comparation','syntax_analyzer.py',137),
  ('rule_comparation -> IDENTIFIER LOGICAL_AND value','rule_comparation',3,'p_rule_comparation','syntax_analyzer.py',138),
  ('rule_comparation -> IDENTIFIER LOGICAL_OR value','rule_comparation',3,'p_rule_comparation','syntax_analyzer.py',139),
  ('condition -> value comparation_operation value','condition',3,'p_condition','syntax_analyzer.py',143),
  ('condition -> condition LOGICAL_AND condition','condition',3,'p_condition','syntax_analyzer.py',144),
  ('condition -> condition LOGICAL_OR condition','condition',3,'p_condition','syntax_analyzer.py',145),
  ('condition -> LOGICAL_NOT condition','condition',2,'p_condition','syntax_analyzer.py',146),
  ('def_function -> FUNC IDENTIFIER LPAREN parameters RPAREN LKEY program RKEY','def_function',8,'p_def_function','syntax_analyzer.py',152),
  ('call_function -> IDENTIFIER LPAREN values RPAREN','call_function',4,'p_call_funcion','syntax_analyzer.py',155),
  ('parameters -> parameter','parameters',1,'p_parameters','syntax_analyzer.py',158),
  ('parameters -> parameters COMMA parameter','parameters',3,'p_parameters','syntax_analyzer.py',159),
  ('parameter -> IDENTIFIER data_type','parameter',2,'p_parameter','syntax_analyzer.py',162),
  ('values -> value','values',1,'p_values','syntax_analyzer.py',165),
  ('values -> values COMMA value','values',3,'p_values','syntax_analyzer.py',166),
  ('value -> STRING','value',1,'p_value','syntax_analyzer.py',170),
  ('value -> INTEGER','value',1,'p_value','syntax_analyzer.py',171),
  ('value -> FLOAT32','value',1,'p_value','syntax_analyzer.py',172),
  ('value -> FLOAT64','value',1,'p_value','syntax_analyzer.py',173),
  ('value -> BOOLEAN','value',1,'p_value','syntax_analyzer.py',174),
  ('data_type -> INTEGER_DATA_TYPE','data_type',1,'p_data_type','syntax_analyzer.py',177),
  ('data_type -> FLOAT32_DATA_TYPE','data_type',1,'p_data_type','syntax_analyzer.py',178),
  ('data_type -> FLOAT64_DATA_TYPE','data_type',1,'p_data_type','syntax_analyzer.py',179),
  ('data_type -> BOOLEAN_DATA_TYPE','data_type',1,'p_data_type','syntax_analyzer.py',180),
  ('data_type -> STRING_DATA_TYPE','data_type',1,'p_data_type','syntax_analyzer.py',181),
  ('input -> INPUT LPAREN RPAREN','input',3,'p_input','syntax_analyzer.py',185),
  ('input -> INPUT LPAREN value RPAREN','input',4,'p_input','syntax_analyzer.py',186),
  ('input -> INPUT LPAREN identifiers RPAREN','input',4,'p_input','syntax_analyzer.py',187),
]
