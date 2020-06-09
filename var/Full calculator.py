tokens = ('ASSIGN','NAME','NUMBER','PLUS', 'MINUS', 'MUL', 'DIV', 'LPAR', 'RPAR','POWER')
t_PLUS     = r'\+'
t_MINUS    = r'\-'
t_MUL    = r'\*'
t_DIV    = r'/'
t_LPAR    = r'\('
t_RPAR    = r'\)'
t_POWER = r'\^'
t_ASSIGN = r'\='
def t_NUMBER(t):
  r'[0-9]+'
  t.value = int(t.value)
  return t
def t_NAME(t):
  r'[a-zA-Z_][a-zA-Z0-9_]*'
  return t
t_ignore = " \t"
def t_error(t):
  print("Illegal character '%s'" % t.value[0])
  t.lexer.skip(1)
import ply.lex as lex
lex.lex()
vars = {}

def p_S_U(p):
      'S : U' # S → U
      p[0] = p[1]

def p_ASSIGN_S(p):
      'U : NAME ASSIGN E'  # U → NAME = E
      vars[p[1]] = p[3]
      print('U → NAME = E : ',p[1]," = ",p[3])
      
def p_F_NAME(p):
      'A : NAME' # A → NAME
      p[0] = vars[p[1]]
      print("A → NAME : ",p[1] ," = ", p[0])
def p_S(p):
  'S : E' # S → E
  p[0] = p[1]
  print('S → E ', p[1])
def p_E_plus_T(p):
  'E : E PLUS T' # E → E + T
  p[0] = p[1] + p[3]
  print('E → E + T :', 'E: ',p[0], ' \t E1: ', p[1], '\t T: ', p[3])
def p_E_MINUS_T(p):
  'E : E MINUS T' # E → E - T
  p[0] = p[1] - p[3]
  print('E → E - T :', 'E: ',p[0], ' \t E1: ', p[1], '\t T: ', p[3])

def p_E_T(p):
  'E : T' # E → T
  p[0]=p[1]
  print('E → T :', p[1])
def p_T_MUL_F(p):
  'T : T MUL F' # T → T * F
  p[0] = p[1] * p[3]
  print('T → T * F :', 'T: ',p[0], ' \t T1: ', p[1], '\t F: ', p[3])

def p_T_DIV_F(p):
  'T : T DIV F' # T → T / F
  if p[3] != 0:  p[0] = p[1] / p[3]
  else: print('Error: Divide by zero '); p[0]=p[1]
  print('T → T / F :', 'T: ',p[0], ' \t T1: ', p[1], '\t F: ', p[3])

def p_T_F(p):
  'T : F' # T → F
  p[0]=p[1]
  print('T → F :', p[1])

def p_F_MINUS_a(p):
    'A : MINUS NUMBER' # A → - a
    p[0]= p[2] * -1
    print('A → - a :', p[2])

def p_F_power_E(p):
    'F : F POWER A ' # F → F ^ A
    p[0] = p[1] ** p[3]
    print('F → F ^ A : ',p[0])

def p_F_A(p):
    'F : A ' # F → A
    p[0] = p[1]
    print('F → A : ',p[0])

def p_F_a(p):
  'A : NUMBER' # A → a
  p[0]=p[1]
  print('A → a :', p[1])
def p_F_lpar_E_rpar(p):
  'A : LPAR E RPAR' # A → ( E )
  p[0]=p[2]
  print('F → (E) :', p[0])

def p_error(p):
  print("Syntax error at '%s'" % p)
import ply.yacc as yacc; yacc.yacc()
while True:
  try:
    s = input('calc > ')
    if s.strip()=='':break
    yacc.parse(s)
  except: print('unexpected error')
