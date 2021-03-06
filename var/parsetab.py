
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN DIV LPAR MINUS MUL NAME NUMBER PLUS POWER RPARS : UU : NAME ASSIGN EA : NAMES : EE : E PLUS TE : E MINUS TE : TT : T MUL FT : T DIV FT : FA : MINUS NUMBERF : F POWER A F : A A : NUMBERA : LPAR E RPAR'
    
_lr_action_items = {'NAME':([0,10,11,12,13,14,15,17,],[4,19,19,19,19,19,19,19,]),'MINUS':([0,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,],[6,12,-3,-7,-10,-13,-14,6,6,6,6,6,6,-11,6,12,-3,-5,-6,12,-8,-9,-12,-15,]),'NUMBER':([0,6,10,11,12,13,14,15,17,],[9,16,9,9,9,9,9,9,9,]),'LPAR':([0,10,11,12,13,14,15,17,],[10,10,10,10,10,10,10,10,]),'$end':([1,2,3,4,5,7,8,9,16,19,20,21,22,23,24,25,26,],[0,-1,-4,-3,-7,-10,-13,-14,-11,-3,-5,-6,-2,-8,-9,-12,-15,]),'PLUS':([3,4,5,7,8,9,16,18,19,20,21,22,23,24,25,26,],[11,-3,-7,-10,-13,-14,-11,11,-3,-5,-6,11,-8,-9,-12,-15,]),'ASSIGN':([4,],[13,]),'POWER':([4,7,8,9,16,19,23,24,25,26,],[-3,17,-13,-14,-11,-3,17,17,-12,-15,]),'MUL':([4,5,7,8,9,16,19,20,21,23,24,25,26,],[-3,14,-10,-13,-14,-11,-3,14,14,-8,-9,-12,-15,]),'DIV':([4,5,7,8,9,16,19,20,21,23,24,25,26,],[-3,15,-10,-13,-14,-11,-3,15,15,-8,-9,-12,-15,]),'RPAR':([5,7,8,9,16,18,19,20,21,23,24,25,26,],[-7,-10,-13,-14,-11,26,-3,-5,-6,-8,-9,-12,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'U':([0,],[2,]),'E':([0,10,13,],[3,18,22,]),'T':([0,10,11,12,13,],[5,5,20,21,5,]),'F':([0,10,11,12,13,14,15,],[7,7,7,7,7,23,24,]),'A':([0,10,11,12,13,14,15,17,],[8,8,8,8,8,8,8,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> U','S',1,'p_S_U','Full calculator.py',26),
  ('U -> NAME ASSIGN E','U',3,'p_ASSIGN_S','Full calculator.py',31),
  ('A -> NAME','A',1,'p_F_NAME','Full calculator.py',36),
  ('S -> E','S',1,'p_S','Full calculator.py',40),
  ('E -> E PLUS T','E',3,'p_E_plus_T','Full calculator.py',44),
  ('E -> E MINUS T','E',3,'p_E_MINUS_T','Full calculator.py',48),
  ('E -> T','E',1,'p_E_T','Full calculator.py',53),
  ('T -> T MUL F','T',3,'p_T_MUL_F','Full calculator.py',57),
  ('T -> T DIV F','T',3,'p_T_DIV_F','Full calculator.py',62),
  ('T -> F','T',1,'p_T_F','Full calculator.py',68),
  ('A -> MINUS NUMBER','A',2,'p_F_MINUS_a','Full calculator.py',73),
  ('F -> F POWER A','F',3,'p_F_power_E','Full calculator.py',78),
  ('F -> A','F',1,'p_F_A','Full calculator.py',83),
  ('A -> NUMBER','A',1,'p_F_a','Full calculator.py',88),
  ('A -> LPAR E RPAR','A',3,'p_F_lpar_E_rpar','Full calculator.py',92),
]
