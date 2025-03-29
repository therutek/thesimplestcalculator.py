print("Witaj w kalkulatorze!")

liczba1 = float(input("Podaj pierwszą liczbę: "))                 # Float konwertuje tekst na liczbę zmiennoprzecinkową, np. 3, 14.2, 1.24 itd.
liczba2 = float(input("Podaj drugą liczbę: "))
operacja = input("Wybierz operację (+, -, *, /): ")

if operacja == "+":
    wynik = liczba1 + liczba2
elif operacja == "-":
    wynik = liczba1 - liczba2
elif operacja == "*":
    wynik = liczba1 * liczba2
elif operacja == "/":
    if liczba2 != 0:
        wynik = liczba1 / liczba2
    else:
        wynik = "Błąd! Nie można dzielić przez zero."
else:
    wynik = "Nieznana operacja!"

print("Wynik:", wynik)

kolejna = input("Czy chcesz wykonać kolejne obliczenia? (tak/nie): ")
while kolejna == "tak":           # Pętla "while" pozwala na wielokrotne wykonywanie tego samego kodu
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    operacja = input("Wybierz operację (+, -, *, /): ")

    if operacja == "+":
        wynik = liczba1 + liczba2
    elif operacja == "-":
        wynik = liczba1 - liczba2
    elif operacja == "*":
        wynik = liczba1 * liczba2
    elif operacja == "/":
        if liczba2 != 0:
            wynik = liczba1 / liczba2
        else:
            wynik = "Błąd! Nie można dzielić przez zero."
    else:
        wynik = "Nieznana operacja!"

    print("Wynik:", wynik)
    kolejna = input("Czy chcesz wykonać kolejne obliczenia? (tak/nie): ")