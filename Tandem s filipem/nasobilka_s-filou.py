cislo = float(input("zadej cislo [0=konec]"))

while cislo != 0:
    for a in range(1, 11):
        print(f"{cislo} * {a} = {cislo * a}")

    cislo = int(input("zadej cislo [0=konec]"))
    