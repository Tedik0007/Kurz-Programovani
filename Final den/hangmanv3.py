tajne_slovo = "programovani"
uhodnuta = []
zivoty = 6
vyhrano = False

while not vyhrano and zivoty > 0:
    zobrazene_slovo = ""
    vse_odhaleno = True

    for p in tajne_slovo:
        if p in uhodnuta:
            zobrazene_slovo += p
        else:
            zobrazene_slovo += "_"
            vse_odhaleno = False

    print(f"\nSlovo: {zobrazene_slovo}")

    if vse_odhaleno:
        vyhrano = True
        break

    print(f"Zbývající životy: {zivoty}")
    pismeno = input("Hádej písmeno: ").lower()

    if pismeno in uhodnuta:
        print("Toto písmeno jsi už zkoušel!")
    else:
        uhodnuta.append(pismeno)

        if pismeno in tajne_slovo:
            print("Zásah!")
        else:
            zivoty -= 1
            print("Vedle! Ztrácíš život.")

if vyhrano:
    print(f"Gratuluji, vyhrál jsi! Tajné slovo bylo: {tajne_slovo}")
else:
    print(
        f"Prohrál jsi! Došly ti všechny životy. "
        f"Hledané slovo bylo: {tajne_slovo}"
    )