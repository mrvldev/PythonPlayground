try:
    a = int(input("Zahl 1:"))
    b = int(input("Zahl 2:"))
    ergebnisadd = a + b
    ergebnissub = a - b
    ergebnisdiv = a / b
    ergebnismult = a * b
    print("Mit diesen Zahlen kommt man bei den 4 Grundrechnungsarten auf folgende Ergebnisse")
    print("Ergebnis Addition: ", ergebnisadd)
    print("Ergebnis Subtraktion: ", ergebnissub)
    print("Ergebnis Multiplikation: ", ergebnismult)
    print("Ergebnis Division: ", ergebnisdiv)
except ZeroDivisionError:
    print("Nicht durch 0 teilen!!!")
except ValueError:
    print("Nur integre Zahlen eingeben.")