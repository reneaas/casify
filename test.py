from casify import *

f = funksjon("a*x**2 + b*x + c")

løsning = løs("f(2) = 1", "f(-1) = 1", "f(0) = -2")
print(løsning)
