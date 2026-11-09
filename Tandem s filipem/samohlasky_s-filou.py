slovo = input("Zadej slovo [nebo konec]: ")
pocet_samohlasek = 0

while slovo != "konec":
    for a in slovo:
        if a in ["a", "e", "i", "o", "u"]:
            pocet_samohlasek += 1
            print(f"Slovo {slovo} obsahuje samohlasku {a}")
    print(f"Pocet samohlasek v slove {slovo} je {pocet_samohlasek}")
    pocet_samohlasek = 0
    slovo = input("Zadej slovo [nebo konec]: ")