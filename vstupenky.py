while True:
    try:
        vek = int(input("Zadejte svůj věk: "))
        break  # platný vstup, cyklus skončí
    except ValueError:
        print("Neplatný vstup. Zadejte prosím celé číslo.")

if vek < 12:
    print("Dětské vstupné: 80 Kč")
elif 12 <= vek <= 64:
    print("Základní vstupné: 160 Kč")
else:
    print("Seniorské vstupné: 100 Kč")