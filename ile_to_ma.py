import string
# wpisanie tekstu
tekst_uzytkownika = input("Wpisz jakiś tekst: ")

# liczba liter i znaków
liczba_liter_znakow = sum(1 for znak in tekst_uzytkownika
                                if znak.isalpha()
                                   or znak in string.punctuation)

# liczba spacji
liczba_spacji = tekst_uzytkownika.count(' ')

# liczba wyrazów
liczba_wyrazow = len(tekst_uzytkownika.split())

# jakie lotery ile razy
czestotliwosc_liter = {}
for znak in tekst_uzytkownika.lower():
    if znak.isalpha():
        if znak in czestotliwosc_liter:
            czestotliwosc_liter[znak] += 1
        else:
            czestotliwosc_liter[znak] = 1

# wyswietlanie
print(f"Liczba liter oraz znaków interpunkcyjnych: {liczba_liter_znakow}")
print(f"Liczba spacji: {liczba_spacji}")
print(f"Liczba wyrazów: {liczba_wyrazow}")
print("Częstotliwość użycia liter:")
for litera, czestosc in sorted(czestotliwosc_liter.items()):
    print(f"{litera}: {czestosc}")
