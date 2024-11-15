
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CCURLB DIRECTIVES DIVIDE ELSE EQUALS EXP IDENTIFIER IF LIBRARIES LPAREN MINUS NS NUMBER OCURLB OP_BOOL PLUS PRINT RPAREN SEMIC SQR TIMES TYPE VAL_BOOLprogram  : code\n                | code : code statement \n            | statementstatement    : declaration\n                    | assignment\n                    | prt\n                    | directives\n                    | ifstdirectives  : NS DIRECTIVES LIBRARIESdeclaration  : TYPE IDENTIFIER SEMIC\n                    | TYPE IDENTIFIER EQUALS expression SEMICassignment   : IDENTIFIER EQUALS expression SEMICprt  : PRINT LPAREN expression RPAREN SEMICifst : IF LPAREN valbool RPAREN OCURLB program CCURLB\n            | IF LPAREN valbool RPAREN OCURLB program CCURLB ELSE OCURLB program CCURLBexpression   : expression PLUS termexpression   : expression MINUS termterm : term TIMES factorterm : term DIVIDE factorfactor : EXP LPAREN factor value RPARENfactor : SQR LPAREN factor RPARENvalue   : NUMBER valbool     : VAL_BOOL\n                    | LPAREN valbool RPAREN\n                    | expression OP_BOOL expressionexpression   : termterm : factorfactor   : value\n                | IDENTIFIER\n                | LPAREN expression RPAREN\n                | MINUS factor'
    
_lr_action_items = {'$end':([0,1,2,3,4,5,6,7,8,14,20,33,39,53,61,69,73,],[-2,0,-1,-4,-5,-6,-7,-8,-9,-3,-11,-10,-13,-12,-14,-15,-16,]),'TYPE':([0,2,3,4,5,6,7,8,14,20,33,39,53,61,63,69,71,73,],[9,9,-4,-5,-6,-7,-8,-9,-3,-11,-10,-13,-12,-14,9,-15,9,-16,]),'IDENTIFIER':([0,2,3,4,5,6,7,8,9,14,16,17,19,20,21,25,28,33,34,39,40,41,42,43,45,47,52,53,61,63,69,71,73,],[10,10,-4,-5,-6,-7,-8,-9,15,-3,22,22,22,-11,22,22,22,-10,22,-13,22,22,22,22,22,22,22,-12,-14,10,-15,10,-16,]),'PRINT':([0,2,3,4,5,6,7,8,14,20,33,39,53,61,63,69,71,73,],[11,11,-4,-5,-6,-7,-8,-9,-3,-11,-10,-13,-12,-14,11,-15,11,-16,]),'NS':([0,2,3,4,5,6,7,8,14,20,33,39,53,61,63,69,71,73,],[12,12,-4,-5,-6,-7,-8,-9,-3,-11,-10,-13,-12,-14,12,-15,12,-16,]),'IF':([0,2,3,4,5,6,7,8,14,20,33,39,53,61,63,69,71,73,],[13,13,-4,-5,-6,-7,-8,-9,-3,-11,-10,-13,-12,-14,13,-15,13,-16,]),'CCURLB':([2,3,4,5,6,7,8,14,20,33,39,53,61,63,67,69,71,72,73,],[-1,-4,-5,-6,-7,-8,-9,-3,-11,-10,-13,-12,-14,-2,69,-15,-2,73,-16,]),'EQUALS':([10,15,],[16,21,]),'LPAREN':([11,13,16,17,19,21,25,27,28,30,34,40,41,42,43,45,47,52,],[17,19,28,28,34,28,28,45,28,47,34,28,28,28,28,28,28,28,]),'DIRECTIVES':([12,],[18,]),'SEMIC':([15,22,23,24,26,29,31,38,44,48,54,55,56,57,59,66,68,],[20,-30,39,-27,-28,-29,-23,53,-32,61,-17,-18,-19,-20,-31,-22,-21,]),'EXP':([16,17,19,21,25,28,34,40,41,42,43,45,47,52,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'SQR':([16,17,19,21,25,28,34,40,41,42,43,45,47,52,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'MINUS':([16,17,19,21,22,23,24,25,26,28,29,31,32,34,37,38,40,41,42,43,44,45,46,47,50,52,54,55,56,57,59,64,66,68,],[25,25,25,25,-30,41,-27,25,-28,25,-29,-23,41,25,41,41,25,25,25,25,-32,25,41,25,41,25,-17,-18,-19,-20,-31,41,-22,-21,]),'NUMBER':([16,17,19,21,22,25,28,29,31,34,40,41,42,43,44,45,47,52,58,59,66,68,],[31,31,31,31,-30,31,31,-29,-23,31,31,31,31,31,-32,31,31,31,31,-31,-22,-21,]),'LIBRARIES':([18,],[33,]),'VAL_BOOL':([19,34,],[36,36,]),'TIMES':([22,24,26,29,31,44,54,55,56,57,59,66,68,],[-30,42,-28,-29,-23,-32,42,42,-19,-20,-31,-22,-21,]),'DIVIDE':([22,24,26,29,31,44,54,55,56,57,59,66,68,],[-30,43,-28,-29,-23,-32,43,43,-19,-20,-31,-22,-21,]),'PLUS':([22,23,24,26,29,31,32,37,38,44,46,50,54,55,56,57,59,64,66,68,],[-30,40,-27,-28,-29,-23,40,40,40,-32,40,40,-17,-18,-19,-20,-31,40,-22,-21,]),'RPAREN':([22,24,26,29,31,32,35,36,44,46,49,50,54,55,56,57,59,60,62,64,65,66,68,],[-30,-27,-28,-29,-23,48,51,-24,-32,59,62,59,-17,-18,-19,-20,-31,66,-25,-26,68,-22,-21,]),'OP_BOOL':([22,24,26,29,31,37,44,50,54,55,56,57,59,66,68,],[-30,-27,-28,-29,-23,52,-32,52,-17,-18,-19,-20,-31,-22,-21,]),'OCURLB':([51,70,],[63,71,]),'ELSE':([69,],[70,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,63,71,],[1,67,72,]),'code':([0,63,71,],[2,2,2,]),'statement':([0,2,63,71,],[3,14,3,3,]),'declaration':([0,2,63,71,],[4,4,4,4,]),'assignment':([0,2,63,71,],[5,5,5,5,]),'prt':([0,2,63,71,],[6,6,6,6,]),'directives':([0,2,63,71,],[7,7,7,7,]),'ifst':([0,2,63,71,],[8,8,8,8,]),'expression':([16,17,19,21,28,34,52,],[23,32,37,38,46,50,64,]),'term':([16,17,19,21,28,34,40,41,52,],[24,24,24,24,24,24,54,55,24,]),'factor':([16,17,19,21,25,28,34,40,41,42,43,45,47,52,],[26,26,26,26,44,26,26,26,26,56,57,58,60,26,]),'value':([16,17,19,21,25,28,34,40,41,42,43,45,47,52,58,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,65,]),'valbool':([19,34,],[35,49,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> code','program',1,'p_program','Syntax.py',27),
  ('program -> <empty>','program',0,'p_program','Syntax.py',28),
  ('code -> code statement','code',2,'p_code','Syntax.py',32),
  ('code -> statement','code',1,'p_code','Syntax.py',33),
  ('statement -> declaration','statement',1,'p_statement','Syntax.py',40),
  ('statement -> assignment','statement',1,'p_statement','Syntax.py',41),
  ('statement -> prt','statement',1,'p_statement','Syntax.py',42),
  ('statement -> directives','statement',1,'p_statement','Syntax.py',43),
  ('statement -> ifst','statement',1,'p_statement','Syntax.py',44),
  ('directives -> NS DIRECTIVES LIBRARIES','directives',3,'p_directives','Syntax.py',48),
  ('declaration -> TYPE IDENTIFIER SEMIC','declaration',3,'p_declaration','Syntax.py',53),
  ('declaration -> TYPE IDENTIFIER EQUALS expression SEMIC','declaration',5,'p_declaration','Syntax.py',54),
  ('assignment -> IDENTIFIER EQUALS expression SEMIC','assignment',4,'p_assignment','Syntax.py',87),
  ('prt -> PRINT LPAREN expression RPAREN SEMIC','prt',5,'p_print','Syntax.py',110),
  ('ifst -> IF LPAREN valbool RPAREN OCURLB program CCURLB','ifst',7,'p_if','Syntax.py',116),
  ('ifst -> IF LPAREN valbool RPAREN OCURLB program CCURLB ELSE OCURLB program CCURLB','ifst',11,'p_if','Syntax.py',117),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','Syntax.py',123),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','Syntax.py',132),
  ('term -> term TIMES factor','term',3,'p_term_times','Syntax.py',142),
  ('term -> term DIVIDE factor','term',3,'p_term_div','Syntax.py',152),
  ('factor -> EXP LPAREN factor value RPAREN','factor',5,'p_factor_exp','Syntax.py',161),
  ('factor -> SQR LPAREN factor RPAREN','factor',4,'p_factor_sqr','Syntax.py',172),
  ('value -> NUMBER','value',1,'p_values_num','Syntax.py',183),
  ('valbool -> VAL_BOOL','valbool',1,'p_value_bool','Syntax.py',188),
  ('valbool -> LPAREN valbool RPAREN','valbool',3,'p_value_bool','Syntax.py',189),
  ('valbool -> expression OP_BOOL expression','valbool',3,'p_value_bool','Syntax.py',190),
  ('expression -> term','expression',1,'p_expression_term','Syntax.py',209),
  ('term -> factor','term',1,'p_term_factor','Syntax.py',214),
  ('factor -> value','factor',1,'p_factor_value','Syntax.py',219),
  ('factor -> IDENTIFIER','factor',1,'p_factor_value','Syntax.py',220),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_value','Syntax.py',221),
  ('factor -> MINUS factor','factor',2,'p_factor_value','Syntax.py',222),
]
