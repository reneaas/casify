import sympy
import re
import sys


def _get_func(expr):
    """ """
    match = re.match(r"(\w+)\((-?\w+|-?\d+)\)", expr.strip())
    if match:
        func_name, arg = match.groups()
        return func_name, arg
    else:
        return False, False


def _handle_expression(expr):
    func_name, arg = _get_func(expr)
    if func_name:
        main_module = sys.modules["__main__"]
        main_globals = main_module.__dict__
        func = main_globals.get(func_name)

        return func(arg)
    else:
        return sympy.sympify(expr)


def solve(*equations, pprint=True):
    """Solves an equation or a set of equations or inequalities.

    Args:
        *equations (str): a variable number of strings representing equations or inequalities.
        pprint (bool): Gives a mathematical-like output. Defaults to `True`.

    Returns:
        str or list: A string representation of the solutions if pprint is True, otherwise a list of dictionaries containing the solutions. Return "No solution" if no real solutions are found.

    Examples:
        >>> from casify import *
        >>> solve("x**2 - x - 6 = 0")
        'x = -2    ∨    x = 3'
        >>> solve("x + y - z = 1", "x + y + 2*z = 3", "-x + y + z = -1")
        'x = 5/3 ∧ y = 0 ∧ z = 2/3'
        >>> f = function("a * x**2 + b*x + c")
        >>> solve("f(1) = 2", "f(-1) = 3", "f(3) = 4")
        'a = 3/8 ∧ b = -1/2 ∧ c = 17/8'
    """
    eqs = []
    # Parse the equations
    for eq in equations:
        if ">" in eq or "<" in eq or ">=" in eq or "<=" in eq:
            return _solve_inequality(eq)
        elif "==" in eq:
            lhs, rhs = eq.split("==")
            lhs = _handle_expression(lhs)
            rhs = _handle_expression(rhs)

            eqs.append(sympy.Eq(lhs, rhs))

        elif "=" in eq:
            lhs, rhs = eq.split("=")
            lhs = _handle_expression(lhs)
            rhs = _handle_expression(rhs)

            eqs.append(sympy.Eq(lhs, rhs))

    solutions = sympy.solve(eqs)

    # Remove complex solutions from the solution set.
    real_solutions = []
    if isinstance(solutions, dict):
        real_solutions = {
            key: solutions.get(key) for key in solutions if solutions.get(key).is_real
        }
        real_solutions = [real_solutions]
    else:
        for sol in solutions:
            if not False in [sol.get(key).is_real for key in sol]:
                real_solutions.append(sol)

    if real_solutions == [] or real_solutions == {}:
        return "No solution"

    elif pprint:
        pprint_solution = ""
        for i, sol in enumerate(real_solutions):
            pprint_solution += (
                str(sol)
                .replace(":", " =")
                .replace("{", "")
                .replace("}", "")
                .replace(",", " ∧")
            )
            if i < len(real_solutions) - 1:
                pprint_solution += "    ∨    "

        return pprint_solution
    else:
        return real_solutions


def løs(*likninger, pprint=True):
    """Løser én eller flere likninger, eller én eller flere ulikheter.

    Args:
        *likninger (str): Et variabel antall likninger eller ulikheter separert med komma som representerer likningene eller ulikhetene.
        pprint (bool): Hvis `True` gir en matematisk tekststreng-representasjon av løsningen. Standardverdi: `True`.

    Returns:
        str eller list: En tekststreng-representasjon (str) av løsningen(e) hvis `pprint` er `True`. Hvis ikke en liste med dictionaries som inneholder løsningene. Returnerer "Ingen løsning" hvis ingen reelle løsninger finnes.

    Eksempler:
        >>> from casify import *
        >>> løs("x**2 - x - 6 = 0")
        'x = -2    ∨    x = 3'
        >>> løs("x + y - z = 1", "x + y + 2*z = 3", "-x + y + z = -1")
        'x = 5/3 ∧ y = 0 ∧ z = 2/3'
        >>> f = funksjon("a * x**2 + b*x + c")
        >>> løs("f(1) = 2", "f(-1) = 3", "f(3) = 4")
        'a = 3/8 ∧ b = -1/2 ∧ c = 17/8'
    """
    løsning = solve(*likninger, pprint=pprint)
    if løsning == "No solution":
        return "Ingen løsning"
    else:
        return løsning


def Løs(*likninger, pprint=True):
    """Alternativ skrivemåte for `løs`."""
    return løs(*likninger, pprint=pprint)


def Solve(*equations, pprint=True):
    """Alternative way to write `solve`."""
    return solve(*equations, pprint=pprint)


def _solve_inequality(expr):
    solution = sympy.solve(expr)
    solution = str(solution)
    solution = solution.replace("|", " ∨ ").replace("&", " ∧ ")
    return solution
