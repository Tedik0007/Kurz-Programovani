zustatek = 1000
historie = []
bezi = True

def vklad_hotovosti():
    global zustatek
    castka = int(input("Zadejte částku pro vložení: "))
    if castka <0:
        print("Částka musí být kladná!")
        return
    zustatek += castka
    historie.append(f"Vklad: +{castka} Kč")
    print("Vklad úspěšný.")

def vyber_hotovosti():
    global zustatek
    castka = int(input("Zadejte částku pro výběr: "))
    if castka < 0:
        print("Částka musí být kladná!")
        return
    if castka > zustatek:
        print("Nedostatek finančních prostředků! ")
        return
    zustatek -= castka
    historie.append(f"Výběr: -{castka} Kč")
    print("Výběr úspěšný.")

def vypis_historie():
    if not historie:
        print("Zatím neproběhly žádné transakce.")
    else:
        for transakce in historie:
            print("-"+transakce)

while bezi:
    print("""--- BANKOMAT ---
            1 - Zobrazit zůstatek
            2 - Vložit hotovost
            3 - Vybrat hotovost
            4 - Historie transakcí
            5 - Ukončit""")

    volba = input("Zvolte akci (1-5): ")

    match volba:
        case "1": print(f"Zůstatek: {zustatek} Kč")
        case "2": vklad_hotovosti()
        case "3": vyber_hotovosti()
        case "4": vypis_historie()
        case "5": print("Děkujeme za použití bankomatu. Nashledanou!"); bezi = False