***************
uminus Grammer
***************

S → E

S → U

U → NAME = E

E → E + T

E → E - T

E → T

T → T * F

T → T / F

T → F 

F → A ^ F

A → NAME

A → - a

A → ( E )