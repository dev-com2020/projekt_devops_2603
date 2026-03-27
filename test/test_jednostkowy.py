from kalkulator import dodaj, podziel
import pytest

def test_dodaj():
    assert dodaj(2, 3) == 5

def test_dodaj_ujemne():
    assert dodaj(-1, -2) == -3

def test_podziel():
    assert podziel(10, 2) == 5.0

def test_podziel_przez_zero():
    with pytest.raises(ValueError):
        podziel(10, 0)


def test_odejmij():
    assert odejmij(10, 3) == 7
    assert odejmij(-2, 5) == -7


def test_pomnoz():
    assert pomnoz(4, 5) == 20
    assert pomnoz(-3, -2) == 6


def test_potega():
    assert potega(2, 5) == 32
    assert potega(9, 0.5) == 3.0


def test_pierwiastek():
    assert pierwiastek(16) == 4.0
    assert pierwiastek(2) == 2 ** 0.5


def test_pierwiastek_ujemny():
    with pytest.raises(ValueError):
        pierwiastek(-1)


@pytest.mark.parametrize("a,b,expected", [
    (5, 2, 2.5),
    (-6, 3, -2.0),
    (0, 10, 0.0),
])
def test_podziel_parametryzacja(a, b, expected):
    assert podziel(a, b) == expected