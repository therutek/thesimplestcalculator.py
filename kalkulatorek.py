print("Witaj w kalkulatorku!")

while True:
    wyrazenie = input("Podaj działanie (np. 3+2-1*4/2): ")

    try:
        wynik = eval(wyrazenie, {"__builtins__": None}, {})  # Ograniczamy eval, by był bezpieczny
        print("Wynik:", wynik)
    except Exception:
        print("Błąd w działaniu! Wpisz poprawne wyrażenie matematyczne.")
        if wyrazenie != "*/0":
            print("Nie można dzielić przez zero.")

    kolejna = input("Czy chcesz wykonać kolejne obliczenia? (tak/nie): ")
    if kolejna.lower() != "tak" and kolejna.lower() != "t":
        break
print("Dziękuję za skorzystanie z kalkulatorka!")
# Kalkulator w Pythonie
