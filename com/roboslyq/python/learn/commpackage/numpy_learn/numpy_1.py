from numpy import *
import sympy as sp

"""

"""
print(eye(4))

x = sp.Symbol('x')
y = sp.Symbol('y')
print(sp.solve([x - 4 * y, x + y - 75], [x, y]))
