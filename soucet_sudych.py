maximum = 0
soucet = 0
cisla = [int(x) for x in range(1, int(input("Zadejte nejvyší číslo: ")) + 1)]

for i in cisla:
    if i %2 == 0:
        soucet += i

print(f"Součet sudých čísel od 1 do {cisla[-1]} je: {soucet}")