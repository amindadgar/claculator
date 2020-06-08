
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DIV LPAR MINUS MUL NAME NUMBER PLUS POWER RPARU : NAME ASSIGN SS : EE : E PLUS TE : E MINUS TE : TT : T MUL FT : T DIV FT : FF : MINUS NUMBERF : NUMBER POWER F F : NUMBERF : LPAR E RPAR'
    
_lr_action_items = {'NAME':([0,],[2,]),'$end':([1,4,5,6,8,9,15,18,19,20,21,22,23,],[0,-1,-2,-5,-8,-11,-9,-3,-4,-6,-7,-10,-12,]),'ASSIGN':([2,],[3,]),'MINUS':([3,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,],[7,12,-5,-8,-11,7,7,7,7,7,-9,7,12,-3,-4,-6,-7,-10,-12,]),'NUMBER':([3,7,10,11,12,13,14,16,],[9,15,9,9,9,9,9,9,]),'LPAR':([3,10,11,12,13,14,16,],[10,10,10,10,10,10,10,]),'PLUS':([5,6,8,9,15,17,18,19,20,21,22,23,],[11,-5,-8,-11,-9,11,-3,-4,-6,-7,-10,-12,]),'RPAR':([6,8,9,15,17,18,19,20,21,22,23,],[-5,-8,-11,-9,23,-3,-4,-6,-7,-10,-12,]),'MUL':([6,8,9,15,18,19,20,21,22,23,],[13,-8,-11,-9,13,13,-6,-7,-10,-12,]),'DIV':([6,8,9,15,18,19,20,21,22,23,],[14,-8,-11,-9,14,14,-6,-7,-10,-12,]),'POWER':([9,],[16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'U':([0,],[1,]),'S':([3,],[4,]),'E':([3,10,],[5,17,]),'T':([3,10,11,12,],[6,6,18,19,]),'F':([3,10,11,12,13,14,16,],[8,8,8,8,20,21,22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> U","S'",1,None,None,None),
  ('U -> NAME ASSIGN S','U',3,'p_ASSIGN_S','Full calculator.py',22),
  ('S -> E','S',1,'p_S','Full calculator.py',31),
  ('E -> E PLUS T','E',3,'p_E_plus_T','Full calculator.py',35),
  ('E -> E MINUS T','E',3,'p_E_MINUS_T','Full calculator.py',39),
  ('E -> T','E',1,'p_E_T','Full calculator.py',44),
  ('T -> T MUL F','T',3,'p_T_MUL_F','Full calculator.py',48),
  ('T -> T DIV F','T',3,'p_T_DIV_F','Full calculator.py',53),
  ('T -> F','T',1,'p_T_F','Full calculator.py',59),
  ('F -> MINUS NUMBER','F',2,'p_F_MINUS_a','Full calculator.py',64),
  ('F -> NUMBER POWER F','F',3,'p_F_power_E','Full calculator.py',69),
  ('F -> NUMBER','F',1,'p_F_a','Full calculator.py',74),
  ('F -> LPAR E RPAR','F',3,'p_F_lpar_E_rpar','Full calculator.py',78),
]
