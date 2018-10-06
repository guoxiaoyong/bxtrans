from sympy import *

A = symbols('A')
a = symbols('a')
b = symbols('b')
C1 = symbols('C1')
C2 = symbols('C2')
x = symbols('x')
y = symbols('y')

E11 = y*(-A+b-C1) + (1-y)*(-C1)
E12 = (1-y)*(-C2)
E1 = x*E11 + (1-x)*E12
print(expand(E1))
