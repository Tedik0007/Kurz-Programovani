tajne_slovo = "polyna"
uhdonuto = []
stav = []

for a in range(len(tajne_slovo)):
    stav.append("_")
while True:
    tip = input("Zadej pismeno: ")
    if tip in tajne_slovo:
        uhdonuto.append(tip)
        stav[tajne_slovo.index(tip)] = tip
        print(stav)
    else:
        print ("Spatne!")

    if stav == list(tajne_slovo):
        print("Vyhral jsi!")
        break