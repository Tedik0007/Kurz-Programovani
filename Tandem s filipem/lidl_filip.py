nakupni_seznam = []

polozka = input("Zadejte polozku z nakupniho seznamu [nebo konec]: ")

while polozka != "konec":
    nakupni_seznam.append(polozka)
    polozka = input("Zadej polozku z nakupniho seznamu [nebo konec]: ")

print("Váš nakupní seznam:", nakupni_seznam)

kontrola = input("Zadejte polozku, kterou chcete zkontrolovat, zda je v seznamu: ")

if kontrola in nakupni_seznam:
    print("Položka je v seznamu.")
else:
    print("Položka není v seznamu.")