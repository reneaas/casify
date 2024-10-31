# `casify`
`casify` is a Python package that implements a simplified CAS (Computer Algebra System) for symbolic computation, wrapping around `sympy` for facilitate its computations. The implementation provides both Norwegian and English names for all of its functions. 

## Basic examples

### Example 1: solving equations

```python
from casify import *

solution = solve("x**2 - x - 6 = 0")
print(solution)

```

### Eksempel 1: løse likninger

```python
from casify import *

løsning = løs("x**2 - x - 6 = 0")
print(løsning)

```


### Example 2: function evalution

```python
from casify import *

f = function("x**2 - x - 6")

print(f(2)) # Computes f(2)
```

### Eksempel 2: funksjonsverdier

```python
from casify import *

f = funksjon("x**2 - x - 6")

print(f(2)) # Regner ut f(2)
```


### Example 3: Differentiation

```python
from casify import *

f = function("x**2 - x - 6")

derivative = f.deriative() # Gives the general expression for the derivative
print(derivative)

print(f.derivative(2)) # computes f'(2)
```

### Eksempel 3: Derivasjon

```python
from casify import *

f = funksjon("x**2 - x - 6")

derivert = f.derivert() # Gir det generelle uttrykket for den deriverte

print(derivert)

print(f.derivert(2)) # regner ut f'(2)
```
