import sympy
import re
import sys


from .equation import solve


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
