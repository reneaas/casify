import sympy


def solve(*equations):
    eqs = []
    for eq in equations:
        if "==" in eq:
            lhs, rhs = eq.split("==")
            lhs = sympy.sympify(lhs)
            rhs = sympy.sympify(rhs)
            eqs.append(sympy.Eq(lhs, rhs))
        elif "=" in eq:
            lhs, rhs = eq.split("=")
            lhs = sympy.sympify(lhs)
            rhs = sympy.sympify(rhs)
            eqs.append(sympy.Eq(lhs, rhs))
        else:
            eqs.append(sympy.sympify(eq))

    solutions = sympy.solve(eqs)
    solutions = [sol for sol in solutions if solutions.get(sol).is_real]
    if solutions == []:
        return "No solution"
    else:
        return solutions


def løs(*likninger):
    løsning = solve(*likninger)
    if løsning == []:
        return "Ingen løsning"
    else:
        return løsning


def Løs(*likninger):
    return løs(*likninger)


def Solve(*equations):
    return solve(*equations)


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


def deriver(expr, var="x"):
    return derivative(expr, var)


def integral(expr, var="x"):
    expr = sympy.sympify(expr)
    return sympy.integrate(expr, sympy.symbols(var))
