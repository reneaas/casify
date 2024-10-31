from casify import *

f = funksjon("x**2 - x - 6")

derivert = f.derivert()  # Gir det generelle uttrykket for den deriverte

print(derivert)

print(f.derivert(2))  # regner ut f'(2)
