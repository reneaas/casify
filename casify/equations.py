import sympy


def solve(*equations):
    eqs = []

    # Parse the equations
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
            eqs.append(sympy.sympify(eq))  # assume it is an inequality

    solutions = sympy.solve(eqs)

    # Remove complex solutions from the solution set.
    real_solutions = []
    if isinstance(solutions, dict):
        real_solutions = {
            key: solutions.get(key) for key in solutions if solutions.get(key).is_real
        }
    else:
        for sol in solutions:
            print(sol)
            for key in sol:
                if sol.get(key).is_real:
                    real_solutions.append(sol)

    if real_solutions == [] or real_solutions == {}:
        return "No solution"
    else:
        return real_solutions


def løs(*likninger):
    løsning = solve(*likninger)
    if løsning == "No solution":
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


if __name__ == "__main__":
    solution = solve("x + y + z = 2", "x + y - z = 0", "x + 2*y + 3*z = 5")
    print(solution)
