# Projekt Python - Dokumentacja katalogu

## Cel projektu
Przykładowy projekt Python z prostym API Flask oraz zestawem testów w `pytest`.

## Struktura katalogów i plików

### Główne pliki
- `app.py` - aplikacja Flask z endpointami:
  - `/health` - dostępność usługi (zwraca `{"status": "ok"}`)
  - `/add/<a>/<b>` - dodawanie dwóch liczb całkowitych
- `main.py` - prosty skrypt z logiem (drukuje `LOGOWANIE!`)
- `requirements.txt` - zależności pythona:
  - `pytest`
  - `selenium`
  - `pytest-benchmark`
  - `flask`
- `Jenkinsfile` - potok CI w Jenkinsie (nie analizowany w dokumentacji funkcjonalnej)
- `jenkins_matrix.txt` - macierz konfiguracji Jenkins (dodatkowy asset)

### Testy jednostkowe
- `test_app.py` - testy endpointów Flask:
  - `test_health` - status 200
  - `test_add` - wynik 2+3=5
- `test/test_jednostkowy.py` - testy funkcji z `test/kalkulator.py`:
  - `test_dodaj` - 2+3=5
  - `test_dodaj_ujemne` - -1-2=-3
  - `test_podziel` - 10/2=5.0
  - `test_podziel_przez_zero` - rzuca `ValueError`
  - `test_podziel_parametryzacja` - dodatkowe przypadki w `pytest.mark.parametrize`
- `test/test_slow_fast.py` - benchmarki i walidacje poprawności:
  - `slow_sum` i `fast_sum` dla 10_000
- `test/test_ui.py` - testy UI Selenium (kiedy środowisko potrafi uruchomić Chrome webdriver):
  - `test_tytul_google`
  - `test_szukaj`

### Library
- `test/kalkulator.py` - proste funkcje arytmetyczne:
  - `dodaj(a, b)`
  - `podziel(a, b)` z obsługą `ValueError` dla `b == 0`

## Jak uruchomić
1. Stwórz wirtualne środowisko:
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
2. Zainstaluj zależności:
   - `pip install -r requirements.txt`
3. Uruchom testy:
   - `pytest -q`
4. Uruchom API:
   - `python app.py`
   - (domyślnie `http://127.0.0.1:5000`)

## Wskazówki
- `test/test_ui.py` wymaga sterownika Chrome (`chromedriver`) i może nie działać we wszystkich kontenerach/CI bez GUI.
- `pytest-benchmark` uruchamia testy wydajności (może wprowadzać dodatkowe dane w wynikach).

## Propozycje rozszerzeń
- dodanie obsługi `POST /add` z JSON
- dodanie walidacji ujemnych liczb jako `int`/`float`
- dodanie wrapperów `black` i `flake8` do CI
- rozbudowanie testów integracyjnych z uruchomieniem serwera w tle `app.test_client()`
