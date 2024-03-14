cyfry_niu = [8,2,5,3]

#pytanie o liczbe
wprowadzona_liczba = int(input("Wprowadź liczbę: "))

#zmienne pomocnicze
suma_spełniona = False
iloczyn_spełniony = False
pary_sumy = []
pary_iloczynu = []

# Sprawdzenie par liczb z listy
for i in range(len(cyfry_niu)):
    for j in range(i + 1, len(cyfry_niu)):
        # czy suma jakiś dwóch cyfr równa się wprowadzonej liczbie
        if cyfry_niu[i] + cyfry_niu[j] == wprowadzona_liczba:
            suma_spełniona = True
            pary_sumy.append((cyfry_niu[i], cyfry_niu[j]))
        # czy iloczyn jakiś dwóch cyfr równa się wprowadzonej liczbie
        if cyfry_niu[i] * cyfry_niu[j] == wprowadzona_liczba:
            iloczyn_spełniony = True
            pary_iloczynu.append((cyfry_niu[i], cyfry_niu[j]))

# Info o wynikach
if suma_spełniona:
    print(f"Suma liczb {pary_sumy} daje wprowadzoną wartość.")
if iloczyn_spełniony:
    print(f"Iloczyn liczb {pary_iloczynu} daje wprowadzoną wartość.")
if not suma_spełniona and not iloczyn_spełniony:
    print("Żaden z warunków nie został spełniony.")
