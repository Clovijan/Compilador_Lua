
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftGTLTGTEQUALSLTEQUALSEQUALSDIFleftCONCATleftPLUSMINUSleftPERCENTUALTIMESDIVIDEleftNOTTAGleftEXPOAND ATRIB BREAK COLON COMMA CONCAT DIF DIVIDE DO DOT DUALCOLON ELSE ELSEIF END EQUALS EXPO FALSE FOR FUNCTION GOTO GT GTEQUALS IF IN LBRACE LCOLCH LOCAL LPAREN LT LTEQUALS MINUS NAME NIL NOT NUMBER OR PERCENTUAL PLUS RBRACE RCOLCH REPEAT RETURN RPAREN SEMICOLON STRING TAG THEN TIMES TRUE UNTIL VAR VARARGS WHILEprogram : blockblock : command\n             | command command_retcommand : SEMICOLON\n               | list_vars ATRIB list_exps\n               | call_function\n               | rotulo\n               | BREAK\n               | GOTO NAME\n               | DO block END\n               | struct_while\n               | struct_repeat\n               | if\n               | struct_for\n               | struct_for_in\n               | def_function\n               | local_varcommand_ret : RETURN\n                   | RETURN list_exps\n                   | RETURN list_exps SEMICOLONrotulo : DUALCOLON NAME DUALCOLONname_function : NAME\n                     | NAME DOT NAME\n                     | NAME COLON NAMElist_vars : var COMMA varvar : NAME \n           | prefix_exp LCOLCH exp RCOLCH\n           | prefix_exp DOT NAME prefix_exp : var\n                   | call_function \n                   | LPAREN exp RPARENlist_names : NAME COMMA list_names\n                  | NAMElist_exps : exp COMMA list_exps\n                 | expexp : NIL\n           | FALSE\n           | TRUE\n           | NUMBER\n           | STRING\n           | VARARGS\n           | def_function\n           | exp_prefix\n           | construct_table\n           | exp op_bin exp\n           | exp op_unary expexp_prefix : VAR \n                  | call_function\n                  | LPAREN exp RPARENcall_function : exp_prefix args\n                     | exp_prefix COLON NAME args args : LPAREN list_exps RPAREN\n             | construct_tabledef_function : function \n                    | local_functionbody_function : LPAREN list_pars RPAREN block ENDlist_pars : list_names COMMA VARARGS\n                 | VARARGSconstruct_table : LBRACE list_fields RBRACE\n                       | LBRACE RBRACElist_fields : field \n                   | field separator_fields list_fields\n                   | field_empty\n                   | field_empty separator_fields list_fieldsfield_empty : LCOLCH exp RCOLCH\n                 | NAMEfield : LCOLCH exp RCOLCH ATRIB exp\n             | NAME ATRIB exp separator_fields : COMMA\n                        | SEMICOLONlocal_var : LOCAL list_names ATRIB list_exps \n                 | LOCAL NAME ATRIB exp op_bin : exp PLUS exp\n               | exp MINUS exp\n               | exp TIMES exp\n               | exp DIVIDE exp\n               | exp EXPO \n               | exp PERCENTUAL exp\n               | exp CONCAT exp\n               | exp LT exp\n               | exp LTEQUALS exp\n               | exp GT exp\n               | exp GTEQUALS exp\n               | exp EQUALS exp\n               | exp DIF exp\n               | exp AND exp\n               | exp OR expop_unary : MINUS\n                | NOT\n                | TAGfunction : FUNCTION body_functionif : IF exp THEN block END\n          | IF exp THEN else\n          | IF exp THEN block else_ifselse_ifs : else_if else_ifs \n                | else_if else_if : ELSEIF exp THEN block \n               | elseelse : ELSE block ENDstruct_while : WHILE exp DO block ENDstruct_for : FOR NAME ATRIB exp COMMA exp DO block END\n                  | FOR NAME ATRIB exp COMMA exp COMMA exp DO block ENDstruct_for_in : FOR list_names IN list_exps DO block ENDstruct_repeat : REPEAT block UNTIL explocal_function : LOCAL FUNCTION name_function body_function'
    
_lr_action_items = {'SEMICOLON':([0,11,23,26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,70,71,80,81,82,84,87,95,113,114,115,138,139,140,144,150,154,156,160,161,184,195,196,197,199,204,],[4,4,4,-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,110,-35,-60,118,118,-66,4,4,-51,-52,-59,-45,-46,-49,4,-105,4,-34,-65,-68,4,-56,-67,4,4,4,]),'BREAK':([0,11,23,87,95,144,154,184,197,199,204,],[8,8,8,8,8,8,8,8,8,8,8,]),'GOTO':([0,11,23,87,95,144,154,184,197,199,204,],[9,9,9,9,9,9,9,9,9,9,9,]),'DO':([0,11,23,26,27,30,39,42,45,46,47,48,49,50,51,52,53,54,55,68,71,80,87,95,113,114,115,138,139,140,144,147,150,154,156,184,193,195,197,199,202,204,],[11,11,11,-54,-55,-47,-50,-53,87,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-35,-60,11,11,-51,-52,-59,-45,-46,-49,11,184,-105,11,-34,11,199,-56,11,11,204,11,]),'DUALCOLON':([0,11,23,44,87,95,144,154,184,197,199,204,],[21,21,21,85,21,21,21,21,21,21,21,21,]),'WHILE':([0,11,23,87,95,144,154,184,197,199,204,],[22,22,22,22,22,22,22,22,22,22,22,]),'REPEAT':([0,11,23,87,95,144,154,184,197,199,204,],[23,23,23,23,23,23,23,23,23,23,23,]),'IF':([0,11,23,87,95,144,154,184,197,199,204,],[24,24,24,24,24,24,24,24,24,24,24,]),'FOR':([0,11,23,87,95,144,154,184,197,199,204,],[25,25,25,25,25,25,25,25,25,25,25,]),'LOCAL':([0,11,22,23,24,26,27,30,31,34,35,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,59,65,67,68,71,76,80,83,86,87,88,89,90,91,92,93,94,95,96,98,99,100,103,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,144,145,149,150,154,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,184,189,191,193,195,196,197,198,199,202,204,],[28,28,57,28,57,-54,-55,-47,57,57,57,-50,57,-53,57,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,57,57,57,57,-91,57,57,-60,57,57,28,57,57,-88,-89,-90,57,57,28,57,57,57,57,57,57,57,-51,-52,-59,57,57,57,-88,57,57,-77,57,57,57,57,57,57,57,57,57,57,57,57,-49,57,28,57,57,-105,28,57,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,57,57,28,57,57,57,-56,57,28,57,28,57,28,]),'NAME':([0,9,11,21,23,25,28,38,40,43,64,66,69,87,95,97,116,117,118,119,144,151,152,154,184,197,199,204,],[10,36,10,44,10,60,63,10,77,84,102,104,109,10,10,109,84,-69,-70,84,10,185,186,10,10,10,10,10,]),'VAR':([0,11,22,23,24,26,27,30,31,34,35,38,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,59,65,67,68,71,76,80,83,86,87,88,89,90,91,92,93,94,95,96,98,99,100,103,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,144,145,149,150,154,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,184,189,191,193,195,196,197,198,199,202,204,],[30,30,30,30,30,-54,-55,-47,30,30,30,30,-50,30,-53,30,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,30,30,30,30,-91,30,30,-60,30,30,30,30,30,-88,-89,-90,30,30,30,30,30,30,30,30,30,30,-51,-52,-59,30,30,30,-88,30,30,-77,30,30,30,30,30,30,30,30,30,30,30,30,-49,30,30,30,30,-105,30,30,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,30,30,30,30,30,30,-56,30,30,30,30,30,30,]),'LPAREN':([0,6,11,20,22,23,24,26,27,30,31,32,34,35,38,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,59,65,67,68,71,75,76,77,80,83,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,102,103,105,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,144,145,149,150,154,157,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,184,185,186,189,191,193,195,196,197,198,199,202,204,],[31,-48,31,41,56,31,56,-54,-55,-47,56,69,56,56,76,-50,56,-53,56,-36,-37,-38,-39,-40,-41,-42,41,-44,-48,56,56,56,56,-91,56,-48,56,41,-60,56,56,31,56,56,-88,-89,-90,56,56,31,56,56,56,56,69,-22,56,-49,56,56,-51,-52,-59,56,56,56,-88,56,56,-77,56,56,56,56,56,56,56,56,56,56,56,56,-49,56,31,56,56,-105,31,-49,56,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,56,56,31,-23,-24,56,56,56,-56,56,31,56,31,56,31,]),'FUNCTION':([0,11,22,23,24,26,27,28,30,31,34,35,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,57,59,65,67,68,71,76,80,83,86,87,88,89,90,91,92,93,94,95,96,98,99,100,103,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,144,145,149,150,154,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,184,189,191,193,195,196,197,198,199,202,204,],[32,32,32,32,32,-54,-55,64,-47,32,32,32,-50,32,-53,32,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,32,64,32,32,32,-91,32,32,-60,32,32,32,32,32,-88,-89,-90,32,32,32,32,32,32,32,32,32,32,-51,-52,-59,32,32,32,-88,32,32,-77,32,32,32,32,32,32,32,32,32,32,32,32,-49,32,32,32,32,-105,32,32,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,32,32,32,32,32,32,-56,32,32,32,32,32,32,]),'$end':([1,2,3,4,6,7,8,12,13,14,15,16,17,18,26,27,30,33,34,36,39,42,46,47,48,49,50,51,52,53,54,55,68,70,71,72,73,80,85,110,113,114,115,138,139,140,141,143,148,149,150,156,176,177,178,179,181,190,192,195,200,201,205,207,],[0,-1,-2,-4,-6,-7,-8,-11,-12,-13,-14,-15,-16,-17,-54,-55,-47,-3,-18,-9,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-19,-35,-5,-10,-60,-21,-20,-51,-52,-59,-45,-46,-49,-104,-93,-71,-72,-105,-34,-100,-92,-94,-96,-98,-95,-99,-56,-103,-97,-101,-102,]),'END':([3,4,6,7,8,12,13,14,15,16,17,18,26,27,30,33,34,36,37,39,42,46,47,48,49,50,51,52,53,54,55,68,70,71,72,73,80,85,110,113,114,115,137,138,139,140,141,142,143,148,149,150,156,176,177,178,179,181,182,187,190,192,194,195,200,201,203,205,206,207,],[-2,-4,-6,-7,-8,-11,-12,-13,-14,-15,-16,-17,-54,-55,-47,-3,-18,-9,73,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-19,-35,-5,-10,-60,-21,-20,-51,-52,-59,176,-45,-46,-49,-104,177,-93,-71,-72,-105,-34,-100,-92,-94,-96,-98,192,195,-95,-99,200,-56,-103,-97,205,-101,207,-102,]),'UNTIL':([3,4,6,7,8,12,13,14,15,16,17,18,26,27,30,33,34,36,39,42,46,47,48,49,50,51,52,53,54,55,58,68,70,71,72,73,80,85,110,113,114,115,138,139,140,141,143,148,149,150,156,176,177,178,179,181,190,192,195,200,201,205,207,],[-2,-4,-6,-7,-8,-11,-12,-13,-14,-15,-16,-17,-54,-55,-47,-3,-18,-9,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,94,-91,-19,-35,-5,-10,-60,-21,-20,-51,-52,-59,-45,-46,-49,-104,-93,-71,-72,-105,-34,-100,-92,-94,-96,-98,-95,-99,-56,-103,-97,-101,-102,]),'ELSEIF':([3,4,6,7,8,12,13,14,15,16,17,18,26,27,30,33,34,36,39,42,46,47,48,49,50,51,52,53,54,55,68,70,71,72,73,80,85,110,113,114,115,138,139,140,141,142,143,148,149,150,156,176,177,178,179,181,190,192,195,200,201,205,207,],[-2,-4,-6,-7,-8,-11,-12,-13,-14,-15,-16,-17,-54,-55,-47,-3,-18,-9,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-19,-35,-5,-10,-60,-21,-20,-51,-52,-59,-45,-46,-49,-104,180,-93,-71,-72,-105,-34,-100,-92,-94,180,-98,-95,-99,-56,-103,-97,-101,-102,]),'ELSE':([3,4,6,7,8,12,13,14,15,16,17,18,26,27,30,33,34,36,39,42,46,47,48,49,50,51,52,53,54,55,68,70,71,72,73,80,85,95,110,113,114,115,138,139,140,141,142,143,148,149,150,156,176,177,178,179,181,190,192,195,200,201,205,207,],[-2,-4,-6,-7,-8,-11,-12,-13,-14,-15,-16,-17,-54,-55,-47,-3,-18,-9,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-19,-35,-5,-10,-60,-21,144,-20,-51,-52,-59,-45,-46,-49,-104,144,-93,-71,-72,-105,-34,-100,-92,-94,144,-98,-95,-99,-56,-103,-97,-101,-102,]),'RETURN':([3,4,6,7,8,12,13,14,15,16,17,18,26,27,30,33,34,36,39,42,46,47,48,49,50,51,52,53,54,55,68,70,71,72,73,80,85,110,113,114,115,138,139,140,141,143,148,149,150,156,176,177,178,179,181,190,192,195,200,201,205,207,],[34,-4,-6,-7,-8,-11,-12,-13,-14,-15,-16,-17,-54,-55,-47,-3,-18,-9,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-19,-35,-5,-10,-60,-21,-20,-51,-52,-59,-45,-46,-49,-104,-93,-71,-72,-105,-34,-100,-92,-94,-96,-98,-95,-99,-56,-103,-97,-101,-102,]),'ATRIB':([5,10,60,62,63,74,84,104,109,146,153,160,],[35,-26,96,99,100,-25,121,-28,-33,-32,-27,189,]),'COLON':([6,20,30,39,42,53,55,75,80,102,105,113,114,115,140,157,],[-48,40,-47,-50,-53,40,-48,-48,-60,152,-49,-51,-52,-59,-49,-49,]),'LBRACE':([6,20,22,24,26,27,30,31,34,35,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,59,65,67,68,71,75,76,77,80,83,86,88,89,90,91,92,93,94,96,98,99,100,103,105,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,145,149,150,157,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,189,191,193,195,196,198,202,],[-48,43,43,43,-54,-55,-47,43,43,43,-50,43,-53,43,-36,-37,-38,-39,-40,-41,-42,43,-44,-48,43,43,43,43,-91,43,-48,43,43,-60,43,43,43,43,-88,-89,-90,43,43,43,43,43,43,43,-49,43,43,-51,-52,-59,43,43,43,-88,43,43,-77,43,43,43,43,43,43,43,43,43,43,43,43,-49,43,43,43,-105,-49,43,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,43,43,43,43,43,-56,43,43,43,]),'LCOLCH':([6,10,19,29,39,42,43,74,75,80,104,105,113,114,115,116,117,118,119,153,157,],[-30,-26,-29,65,-50,-53,83,-29,-30,-60,-28,-31,-51,-52,-59,83,-69,-70,83,-27,-31,]),'DOT':([6,10,19,29,39,42,74,75,80,102,104,105,113,114,115,153,157,],[-30,-26,-29,66,-50,-53,-29,-30,-60,151,-28,-31,-51,-52,-59,-27,-31,]),'COMMA':([10,19,26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,60,63,68,71,80,81,82,84,104,107,109,113,114,115,138,139,140,145,146,150,153,160,161,193,195,196,],[-26,38,-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,97,97,-91,111,-60,117,117,-66,-28,155,97,-51,-52,-59,-45,-46,-49,183,-32,-105,-27,-65,-68,198,-56,-67,]),'NIL':([22,24,26,27,30,31,34,35,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,59,65,67,68,71,76,80,83,86,88,89,90,91,92,93,94,96,98,99,100,103,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,145,149,150,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,189,191,193,195,196,198,202,],[46,46,-54,-55,-47,46,46,46,-50,46,-53,46,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,46,46,46,46,-91,46,46,-60,46,46,46,46,-88,-89,-90,46,46,46,46,46,46,46,46,46,-51,-52,-59,46,46,46,-88,46,46,-77,46,46,46,46,46,46,46,46,46,46,46,46,-49,46,46,46,-105,46,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,46,46,46,46,46,-56,46,46,46,]),'FALSE':([22,24,26,27,30,31,34,35,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,59,65,67,68,71,76,80,83,86,88,89,90,91,92,93,94,96,98,99,100,103,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,145,149,150,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,189,191,193,195,196,198,202,],[47,47,-54,-55,-47,47,47,47,-50,47,-53,47,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,47,47,47,47,-91,47,47,-60,47,47,47,47,-88,-89,-90,47,47,47,47,47,47,47,47,47,-51,-52,-59,47,47,47,-88,47,47,-77,47,47,47,47,47,47,47,47,47,47,47,47,-49,47,47,47,-105,47,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,47,47,47,47,47,-56,47,47,47,]),'TRUE':([22,24,26,27,30,31,34,35,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,59,65,67,68,71,76,80,83,86,88,89,90,91,92,93,94,96,98,99,100,103,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,145,149,150,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,189,191,193,195,196,198,202,],[48,48,-54,-55,-47,48,48,48,-50,48,-53,48,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,48,48,48,48,-91,48,48,-60,48,48,48,48,-88,-89,-90,48,48,48,48,48,48,48,48,48,-51,-52,-59,48,48,48,-88,48,48,-77,48,48,48,48,48,48,48,48,48,48,48,48,-49,48,48,48,-105,48,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,48,48,48,48,48,-56,48,48,48,]),'NUMBER':([22,24,26,27,30,31,34,35,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,59,65,67,68,71,76,80,83,86,88,89,90,91,92,93,94,96,98,99,100,103,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,145,149,150,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,189,191,193,195,196,198,202,],[49,49,-54,-55,-47,49,49,49,-50,49,-53,49,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,49,49,49,49,-91,49,49,-60,49,49,49,49,-88,-89,-90,49,49,49,49,49,49,49,49,49,-51,-52,-59,49,49,49,-88,49,49,-77,49,49,49,49,49,49,49,49,49,49,49,49,-49,49,49,49,-105,49,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,49,49,49,49,49,-56,49,49,49,]),'STRING':([22,24,26,27,30,31,34,35,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,59,65,67,68,71,76,80,83,86,88,89,90,91,92,93,94,96,98,99,100,103,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,145,149,150,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,189,191,193,195,196,198,202,],[50,50,-54,-55,-47,50,50,50,-50,50,-53,50,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,50,50,50,50,-91,50,50,-60,50,50,50,50,-88,-89,-90,50,50,50,50,50,50,50,50,50,-51,-52,-59,50,50,50,-88,50,50,-77,50,50,50,50,50,50,50,50,50,50,50,50,-49,50,50,50,-105,50,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,50,50,50,50,50,-56,50,50,50,]),'VARARGS':([22,24,26,27,30,31,34,35,39,41,42,45,46,47,48,49,50,51,52,53,54,55,56,59,65,67,68,69,71,76,80,83,86,88,89,90,91,92,93,94,96,98,99,100,103,111,112,113,114,115,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,138,139,140,141,145,149,150,155,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,189,191,193,195,196,198,202,],[51,51,-54,-55,-47,51,51,51,-50,51,-53,51,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,51,51,51,51,-91,108,51,51,-60,51,51,51,51,-88,-89,-90,51,51,51,51,51,51,51,51,51,-51,-52,-59,51,51,51,-88,51,51,-77,51,51,51,51,51,51,51,51,51,51,51,51,-49,51,51,51,-105,188,51,-73,-74,-75,-76,-78,-79,-80,-81,-82,-83,-84,-85,-86,-87,51,51,51,51,51,-56,51,51,51,]),'MINUS':([26,27,30,39,42,45,46,47,48,49,50,51,52,53,54,55,59,67,68,71,80,86,93,103,112,113,114,115,120,138,139,140,141,145,149,150,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,191,193,195,196,202,],[-54,-55,-47,-50,-53,90,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,90,90,-91,90,-60,123,90,90,90,-51,-52,-59,90,90,90,-49,90,90,90,-105,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,-56,90,90,]),'NOT':([26,27,30,39,42,45,46,47,48,49,50,51,52,53,54,55,59,67,68,71,80,86,93,103,112,113,114,115,120,138,139,140,141,145,149,150,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,191,193,195,196,202,],[-54,-55,-47,-50,-53,91,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,91,91,-91,91,-60,91,91,91,91,-51,-52,-59,91,91,91,-49,91,91,91,-105,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,91,-56,91,91,]),'TAG':([26,27,30,39,42,45,46,47,48,49,50,51,52,53,54,55,59,67,68,71,80,86,93,103,112,113,114,115,120,138,139,140,141,145,149,150,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,191,193,195,196,202,],[-54,-55,-47,-50,-53,92,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,92,92,-91,92,-60,92,92,92,92,-51,-52,-59,92,92,92,-49,92,92,92,-105,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,-56,92,92,]),'THEN':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,59,68,80,113,114,115,138,139,140,150,191,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,95,-91,-60,-51,-52,-59,-45,-46,-49,-105,197,-56,]),'RPAREN':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,67,68,71,78,80,93,106,108,112,113,114,115,138,139,140,150,156,188,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,105,-91,-35,114,-60,140,154,-58,157,-51,-52,-59,-45,-46,-49,-105,-34,-57,-56,]),'PLUS':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,122,-51,-52,-59,-45,-46,-49,-105,-56,]),'TIMES':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,124,-51,-52,-59,-45,-46,-49,-105,-56,]),'DIVIDE':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,125,-51,-52,-59,-45,-46,-49,-105,-56,]),'EXPO':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,126,-51,-52,-59,-45,-46,-49,-105,-56,]),'PERCENTUAL':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,127,-51,-52,-59,-45,-46,-49,-105,-56,]),'CONCAT':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,128,-51,-52,-59,-45,-46,-49,-105,-56,]),'LT':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,129,-51,-52,-59,-45,-46,-49,-105,-56,]),'LTEQUALS':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,130,-51,-52,-59,-45,-46,-49,-105,-56,]),'GT':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,131,-51,-52,-59,-45,-46,-49,-105,-56,]),'GTEQUALS':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,132,-51,-52,-59,-45,-46,-49,-105,-56,]),'EQUALS':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,133,-51,-52,-59,-45,-46,-49,-105,-56,]),'DIF':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,134,-51,-52,-59,-45,-46,-49,-105,-56,]),'AND':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,135,-51,-52,-59,-45,-46,-49,-105,-56,]),'OR':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,86,113,114,115,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,136,-51,-52,-59,-45,-46,-49,-105,-56,]),'RCOLCH':([26,27,30,39,42,46,47,48,49,50,51,52,53,54,55,68,80,103,113,114,115,120,138,139,140,150,195,],[-54,-55,-47,-50,-53,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,-60,153,-51,-52,-59,160,-45,-46,-49,-105,-56,]),'RBRACE':([26,27,30,39,42,43,46,47,48,49,50,51,52,53,54,55,68,79,80,81,82,84,113,114,115,138,139,140,150,158,159,160,161,195,196,],[-54,-55,-47,-50,-53,80,-36,-37,-38,-39,-40,-41,-42,-43,-44,-48,-91,115,-60,-61,-63,-66,-51,-52,-59,-45,-46,-49,-105,-62,-64,-65,-68,-56,-67,]),'IN':([60,61,109,146,],[-33,98,-33,-32,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'block':([0,11,23,87,95,144,154,184,197,199,204,],[2,37,58,137,142,182,187,194,201,203,206,]),'command':([0,11,23,87,95,144,154,184,197,199,204,],[3,3,3,3,3,3,3,3,3,3,3,]),'list_vars':([0,11,23,87,95,144,154,184,197,199,204,],[5,5,5,5,5,5,5,5,5,5,5,]),'call_function':([0,11,22,23,24,31,34,35,38,41,45,56,59,65,67,71,76,83,86,87,88,89,93,94,95,96,98,99,100,103,111,112,120,121,122,123,124,125,127,128,129,130,131,132,133,134,135,136,138,139,141,144,145,149,154,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,184,189,191,193,196,197,198,199,202,204,],[6,6,55,6,55,55,55,55,75,55,55,55,55,55,55,55,55,55,55,6,55,55,55,55,6,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,6,55,55,6,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,6,55,55,55,55,6,55,6,55,6,]),'rotulo':([0,11,23,87,95,144,154,184,197,199,204,],[7,7,7,7,7,7,7,7,7,7,7,]),'struct_while':([0,11,23,87,95,144,154,184,197,199,204,],[12,12,12,12,12,12,12,12,12,12,12,]),'struct_repeat':([0,11,23,87,95,144,154,184,197,199,204,],[13,13,13,13,13,13,13,13,13,13,13,]),'if':([0,11,23,87,95,144,154,184,197,199,204,],[14,14,14,14,14,14,14,14,14,14,14,]),'struct_for':([0,11,23,87,95,144,154,184,197,199,204,],[15,15,15,15,15,15,15,15,15,15,15,]),'struct_for_in':([0,11,23,87,95,144,154,184,197,199,204,],[16,16,16,16,16,16,16,16,16,16,16,]),'def_function':([0,11,22,23,24,31,34,35,41,45,56,59,65,67,71,76,83,86,87,88,89,93,94,95,96,98,99,100,103,111,112,120,121,122,123,124,125,127,128,129,130,131,132,133,134,135,136,138,139,141,144,145,149,154,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,184,189,191,193,196,197,198,199,202,204,],[17,17,52,17,52,52,52,52,52,52,52,52,52,52,52,52,52,52,17,52,52,52,52,17,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,17,52,52,17,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,17,52,52,52,52,17,52,17,52,17,]),'local_var':([0,11,23,87,95,144,154,184,197,199,204,],[18,18,18,18,18,18,18,18,18,18,18,]),'var':([0,11,23,38,87,95,144,154,184,197,199,204,],[19,19,19,74,19,19,19,19,19,19,19,19,]),'exp_prefix':([0,11,22,23,24,31,34,35,38,41,45,56,59,65,67,71,76,83,86,87,88,89,93,94,95,96,98,99,100,103,111,112,120,121,122,123,124,125,127,128,129,130,131,132,133,134,135,136,138,139,141,144,145,149,154,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,184,189,191,193,196,197,198,199,202,204,],[20,20,53,20,53,53,53,53,20,53,53,53,53,53,53,53,53,53,53,20,53,53,53,53,20,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,20,53,53,20,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,20,53,53,53,53,20,53,20,53,20,]),'function':([0,11,22,23,24,31,34,35,41,45,56,59,65,67,71,76,83,86,87,88,89,93,94,95,96,98,99,100,103,111,112,120,121,122,123,124,125,127,128,129,130,131,132,133,134,135,136,138,139,141,144,145,149,154,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,184,189,191,193,196,197,198,199,202,204,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'local_function':([0,11,22,23,24,31,34,35,41,45,56,59,65,67,71,76,83,86,87,88,89,93,94,95,96,98,99,100,103,111,112,120,121,122,123,124,125,127,128,129,130,131,132,133,134,135,136,138,139,141,144,145,149,154,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,184,189,191,193,196,197,198,199,202,204,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'prefix_exp':([0,11,23,38,87,95,144,154,184,197,199,204,],[29,29,29,29,29,29,29,29,29,29,29,29,]),'command_ret':([3,],[33,]),'args':([20,53,77,],[39,39,113,]),'construct_table':([20,22,24,31,34,35,41,45,53,56,59,65,67,71,76,77,83,86,88,89,93,94,96,98,99,100,103,111,112,120,121,122,123,124,125,127,128,129,130,131,132,133,134,135,136,138,139,141,145,149,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,189,191,193,196,198,202,],[42,54,54,54,54,54,54,54,42,54,54,54,54,54,54,42,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'exp':([22,24,31,34,35,41,45,56,59,65,67,71,76,83,86,88,89,93,94,96,98,99,100,103,111,112,120,121,122,123,124,125,127,128,129,130,131,132,133,134,135,136,138,139,141,145,149,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,180,183,189,191,193,196,198,202,],[45,59,67,71,71,71,86,93,86,103,86,86,112,120,86,138,139,86,141,145,71,71,149,86,71,86,86,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,86,191,193,196,86,86,86,202,86,]),'list_names':([25,28,69,97,],[61,62,107,146,]),'body_function':([32,101,],[68,150,]),'list_exps':([34,35,41,98,99,111,],[70,72,78,147,148,156,]),'list_fields':([43,116,119,],[79,158,159,]),'field':([43,116,119,],[81,81,81,]),'field_empty':([43,116,119,],[82,82,82,]),'op_bin':([45,59,67,71,86,93,103,112,120,138,139,141,145,149,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,191,193,196,202,],[88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,88,]),'op_unary':([45,59,67,71,86,93,103,112,120,138,139,141,145,149,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,191,193,196,202,],[89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,89,]),'name_function':([64,],[101,]),'list_pars':([69,],[106,]),'separator_fields':([81,82,],[116,119,]),'else':([95,142,179,],[143,181,181,]),'else_ifs':([142,179,],[178,190,]),'else_if':([142,179,],[179,179,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> block','program',1,'p_program','ExpressionLanguageParser.py',13),
  ('block -> command','block',1,'p_block','ExpressionLanguageParser.py',18),
  ('block -> command command_ret','block',2,'p_block','ExpressionLanguageParser.py',19),
  ('command -> SEMICOLON','command',1,'p_command','ExpressionLanguageParser.py',24),
  ('command -> list_vars ATRIB list_exps','command',3,'p_command','ExpressionLanguageParser.py',25),
  ('command -> call_function','command',1,'p_command','ExpressionLanguageParser.py',26),
  ('command -> rotulo','command',1,'p_command','ExpressionLanguageParser.py',27),
  ('command -> BREAK','command',1,'p_command','ExpressionLanguageParser.py',28),
  ('command -> GOTO NAME','command',2,'p_command','ExpressionLanguageParser.py',29),
  ('command -> DO block END','command',3,'p_command','ExpressionLanguageParser.py',30),
  ('command -> struct_while','command',1,'p_command','ExpressionLanguageParser.py',31),
  ('command -> struct_repeat','command',1,'p_command','ExpressionLanguageParser.py',32),
  ('command -> if','command',1,'p_command','ExpressionLanguageParser.py',33),
  ('command -> struct_for','command',1,'p_command','ExpressionLanguageParser.py',34),
  ('command -> struct_for_in','command',1,'p_command','ExpressionLanguageParser.py',35),
  ('command -> def_function','command',1,'p_command','ExpressionLanguageParser.py',36),
  ('command -> local_var','command',1,'p_command','ExpressionLanguageParser.py',37),
  ('command_ret -> RETURN','command_ret',1,'p_command_ret','ExpressionLanguageParser.py',42),
  ('command_ret -> RETURN list_exps','command_ret',2,'p_command_ret','ExpressionLanguageParser.py',43),
  ('command_ret -> RETURN list_exps SEMICOLON','command_ret',3,'p_command_ret','ExpressionLanguageParser.py',44),
  ('rotulo -> DUALCOLON NAME DUALCOLON','rotulo',3,'p_rotulo','ExpressionLanguageParser.py',49),
  ('name_function -> NAME','name_function',1,'p_name_function','ExpressionLanguageParser.py',54),
  ('name_function -> NAME DOT NAME','name_function',3,'p_name_function','ExpressionLanguageParser.py',55),
  ('name_function -> NAME COLON NAME','name_function',3,'p_name_function','ExpressionLanguageParser.py',56),
  ('list_vars -> var COMMA var','list_vars',3,'p_list_vars','ExpressionLanguageParser.py',61),
  ('var -> NAME','var',1,'p_var','ExpressionLanguageParser.py',66),
  ('var -> prefix_exp LCOLCH exp RCOLCH','var',4,'p_var','ExpressionLanguageParser.py',67),
  ('var -> prefix_exp DOT NAME','var',3,'p_var','ExpressionLanguageParser.py',68),
  ('prefix_exp -> var','prefix_exp',1,'p_prefix_exp','ExpressionLanguageParser.py',72),
  ('prefix_exp -> call_function','prefix_exp',1,'p_prefix_exp','ExpressionLanguageParser.py',73),
  ('prefix_exp -> LPAREN exp RPAREN','prefix_exp',3,'p_prefix_exp','ExpressionLanguageParser.py',74),
  ('list_names -> NAME COMMA list_names','list_names',3,'p_list_names','ExpressionLanguageParser.py',79),
  ('list_names -> NAME','list_names',1,'p_list_names','ExpressionLanguageParser.py',80),
  ('list_exps -> exp COMMA list_exps','list_exps',3,'p_list_exps','ExpressionLanguageParser.py',85),
  ('list_exps -> exp','list_exps',1,'p_list_exps','ExpressionLanguageParser.py',86),
  ('exp -> NIL','exp',1,'p_exp','ExpressionLanguageParser.py',91),
  ('exp -> FALSE','exp',1,'p_exp','ExpressionLanguageParser.py',92),
  ('exp -> TRUE','exp',1,'p_exp','ExpressionLanguageParser.py',93),
  ('exp -> NUMBER','exp',1,'p_exp','ExpressionLanguageParser.py',94),
  ('exp -> STRING','exp',1,'p_exp','ExpressionLanguageParser.py',95),
  ('exp -> VARARGS','exp',1,'p_exp','ExpressionLanguageParser.py',96),
  ('exp -> def_function','exp',1,'p_exp','ExpressionLanguageParser.py',97),
  ('exp -> exp_prefix','exp',1,'p_exp','ExpressionLanguageParser.py',98),
  ('exp -> construct_table','exp',1,'p_exp','ExpressionLanguageParser.py',99),
  ('exp -> exp op_bin exp','exp',3,'p_exp','ExpressionLanguageParser.py',100),
  ('exp -> exp op_unary exp','exp',3,'p_exp','ExpressionLanguageParser.py',101),
  ('exp_prefix -> VAR','exp_prefix',1,'p_exp_prefix','ExpressionLanguageParser.py',106),
  ('exp_prefix -> call_function','exp_prefix',1,'p_exp_prefix','ExpressionLanguageParser.py',107),
  ('exp_prefix -> LPAREN exp RPAREN','exp_prefix',3,'p_exp_prefix','ExpressionLanguageParser.py',108),
  ('call_function -> exp_prefix args','call_function',2,'p_call_function','ExpressionLanguageParser.py',113),
  ('call_function -> exp_prefix COLON NAME args','call_function',4,'p_call_function','ExpressionLanguageParser.py',114),
  ('args -> LPAREN list_exps RPAREN','args',3,'p_args','ExpressionLanguageParser.py',119),
  ('args -> construct_table','args',1,'p_args','ExpressionLanguageParser.py',120),
  ('def_function -> function','def_function',1,'p_def_function','ExpressionLanguageParser.py',125),
  ('def_function -> local_function','def_function',1,'p_def_function','ExpressionLanguageParser.py',126),
  ('body_function -> LPAREN list_pars RPAREN block END','body_function',5,'p_body_function','ExpressionLanguageParser.py',131),
  ('list_pars -> list_names COMMA VARARGS','list_pars',3,'p_list_pars','ExpressionLanguageParser.py',136),
  ('list_pars -> VARARGS','list_pars',1,'p_list_pars','ExpressionLanguageParser.py',137),
  ('construct_table -> LBRACE list_fields RBRACE','construct_table',3,'p_construct_table','ExpressionLanguageParser.py',142),
  ('construct_table -> LBRACE RBRACE','construct_table',2,'p_construct_table','ExpressionLanguageParser.py',143),
  ('list_fields -> field','list_fields',1,'p_list_fields','ExpressionLanguageParser.py',148),
  ('list_fields -> field separator_fields list_fields','list_fields',3,'p_list_fields','ExpressionLanguageParser.py',149),
  ('list_fields -> field_empty','list_fields',1,'p_list_fields','ExpressionLanguageParser.py',150),
  ('list_fields -> field_empty separator_fields list_fields','list_fields',3,'p_list_fields','ExpressionLanguageParser.py',151),
  ('field_empty -> LCOLCH exp RCOLCH','field_empty',3,'p_field_empty','ExpressionLanguageParser.py',156),
  ('field_empty -> NAME','field_empty',1,'p_field_empty','ExpressionLanguageParser.py',157),
  ('field -> LCOLCH exp RCOLCH ATRIB exp','field',5,'p_field','ExpressionLanguageParser.py',162),
  ('field -> NAME ATRIB exp','field',3,'p_field','ExpressionLanguageParser.py',163),
  ('separator_fields -> COMMA','separator_fields',1,'p_separator_fields','ExpressionLanguageParser.py',168),
  ('separator_fields -> SEMICOLON','separator_fields',1,'p_separator_fields','ExpressionLanguageParser.py',169),
  ('local_var -> LOCAL list_names ATRIB list_exps','local_var',4,'p_local_var','ExpressionLanguageParser.py',174),
  ('local_var -> LOCAL NAME ATRIB exp','local_var',4,'p_local_var','ExpressionLanguageParser.py',175),
  ('op_bin -> exp PLUS exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',180),
  ('op_bin -> exp MINUS exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',181),
  ('op_bin -> exp TIMES exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',182),
  ('op_bin -> exp DIVIDE exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',183),
  ('op_bin -> exp EXPO','op_bin',2,'p_op_bin','ExpressionLanguageParser.py',184),
  ('op_bin -> exp PERCENTUAL exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',185),
  ('op_bin -> exp CONCAT exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',186),
  ('op_bin -> exp LT exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',187),
  ('op_bin -> exp LTEQUALS exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',188),
  ('op_bin -> exp GT exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',189),
  ('op_bin -> exp GTEQUALS exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',190),
  ('op_bin -> exp EQUALS exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',191),
  ('op_bin -> exp DIF exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',192),
  ('op_bin -> exp AND exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',193),
  ('op_bin -> exp OR exp','op_bin',3,'p_op_bin','ExpressionLanguageParser.py',194),
  ('op_unary -> MINUS','op_unary',1,'p_op_unary','ExpressionLanguageParser.py',199),
  ('op_unary -> NOT','op_unary',1,'p_op_unary','ExpressionLanguageParser.py',200),
  ('op_unary -> TAG','op_unary',1,'p_op_unary','ExpressionLanguageParser.py',201),
  ('function -> FUNCTION body_function','function',2,'p_function','ExpressionLanguageParser.py',206),
  ('if -> IF exp THEN block END','if',5,'p_if','ExpressionLanguageParser.py',211),
  ('if -> IF exp THEN else','if',4,'p_if','ExpressionLanguageParser.py',212),
  ('if -> IF exp THEN block else_ifs','if',5,'p_if','ExpressionLanguageParser.py',213),
  ('else_ifs -> else_if else_ifs','else_ifs',2,'p_else_ifs','ExpressionLanguageParser.py',217),
  ('else_ifs -> else_if','else_ifs',1,'p_else_ifs','ExpressionLanguageParser.py',218),
  ('else_if -> ELSEIF exp THEN block','else_if',4,'p_else_if','ExpressionLanguageParser.py',222),
  ('else_if -> else','else_if',1,'p_else_if','ExpressionLanguageParser.py',223),
  ('else -> ELSE block END','else',3,'p_else','ExpressionLanguageParser.py',227),
  ('struct_while -> WHILE exp DO block END','struct_while',5,'p_struct_while','ExpressionLanguageParser.py',232),
  ('struct_for -> FOR NAME ATRIB exp COMMA exp DO block END','struct_for',9,'p_struct_for','ExpressionLanguageParser.py',237),
  ('struct_for -> FOR NAME ATRIB exp COMMA exp COMMA exp DO block END','struct_for',11,'p_struct_for','ExpressionLanguageParser.py',238),
  ('struct_for_in -> FOR list_names IN list_exps DO block END','struct_for_in',7,'p_struct_for_in','ExpressionLanguageParser.py',243),
  ('struct_repeat -> REPEAT block UNTIL exp','struct_repeat',4,'p_struct_repeat','ExpressionLanguageParser.py',248),
  ('local_function -> LOCAL FUNCTION name_function body_function','local_function',4,'p_local_function','ExpressionLanguageParser.py',253),
]
