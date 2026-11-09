otazky = ["Jaké je hlavní město Francie?", "Která planeta je nejblíže Slunci?", "Kolik bitů má jeden bajt?"]
odpovedi = ["pariz", "merkur", "8"]

body = 0

for i in otazky:
    pokusy = 2
    uhodnuto = False

    while pokusy > 0 and not uhodnuto:
        print(i)
        odpoved = input("Vaše odpověď: ").lower()

        if odpoved == odpovedi[otazky.index(i)]:

            if pokusy == 2:
                body += 2
                print("Výborně! Správná odpověď (+2 body).")
                uhodnuto = True
            elif pokusy == 1:
                body += 1
                print("Správně na druhý pokus (+1 bod).")
                uhodnuto = True

        else:
            pokusy -= 1
            if pokusy == 1:
                print("Špatně, máš ještě jeden pokus!")
            else:
                print("Bohužel, správná odpověď byla: ", odpovedi[otazky.index(i)])

print("Kvíz skončil! Tvoje celkové skóre: ", body, " z 6 bodů.")
print("Vynikající výsledek!" if body == 6 or body == 5 else "Dobrá práce, zkus to příště ještě lépe!")