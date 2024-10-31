import sympy


def function(f):
    f_expr = sympy.sympify(f)
    var = list(f_expr.free_symbols)[0]

    def func(x):
        return f_expr.subs(var, x)

    # Derivative function
    def derivative(x=None, order=1):
        if x is not None:
            return sympy.diff(f_expr, var, order).subs(var, x)
        else:
            return sympy.diff(f_expr, var, order)

    func.derivative = derivative  # Attach the derivative function
    func.derivert = derivative

    return func


def funksjon(f):
    return function(f)


def Funksjon(f):
    return funksjon(f)


def Function(f):
    return function(f)


def derivative(expr, var="x"):
    expr = sympy.sympify(expr)
    return sympy.diff(expr, sympy.symbols(var))


def derivert(expr, var="x"):
    return derivative(expr, var)


def integral(expr, var="x"):
    expr = sympy.sympify(expr)
    return sympy.integrate(expr, sympy.symbols(var))
