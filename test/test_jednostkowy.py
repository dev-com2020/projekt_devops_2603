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