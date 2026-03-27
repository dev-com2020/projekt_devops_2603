def dodaj(a, b):
    return a + b


def odejmij(a, b):
    return a - b


def pomnoz(a, b):
    return a * b


def potega(a, b):
    return a ** b


def pierwiastek(a):
    if a < 0:
        raise ValueError("Pierwiastek z liczby ujemnej")
    return a ** 0.5


def podziel(a, b):
    if b == 0:
        raise ValueError("Dzielenie przez zero")
    return a / b