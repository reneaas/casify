from casify import *

f = function("x**2 - x - 6")


print(f.derivative())  # Gives the general expression for the derivative

print(f.derivative(2))  # computes f'(2)
