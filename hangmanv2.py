import random

slova = [
    "pes", "kocka", "auto", "dvere", "okno", "stul", "zidle", "postel", "zena", "muz",
    "dite", "matka", "otec", "bratr", "sestra", "babicka", "dedecek", "rodina", "pritel", "nepritel",
    "delat", "spat", "jist", "pit", "cist", "psat", "chodit", "behat", "skakat", "videt",
    "slyset", "mluvit", "myslet", "znat", "umet", "chtit", "muset", "moct", "mit", "byt",
    "dobry", "spatny", "velky", "maly", "novy", "stary", "rychly", "pomaly", "krasny", "osklivy",
    "chytry", "hloupy", "silny", "slaby", "zdravy", "nemocny", "bohaty", "chudy", "cisty", "spinavy",
    "cerveny", "modry", "zeleny", "zluty", "cerny", "bily", "ruzovy", "fialovy", "oranzovy", "hnedy",
    "sedy", "zlaty", "stribrny", "jasny", "tmavy", "svetly", "barevny", "leskly", "matny", "hladky",
    "strom", "les", "voda", "ohen", "zeme", "slunce", "mesic", "hvezda", "nebe", "mrak",
    "vitr", "dest", "snih", "led", "zima", "jaro", "leto", "podzim", "pocasi", "teplota",
    "mesto", "vesnice", "ulice", "dum", "skola", "prace", "obchod", "nemocnice", "letiste", "nadrazi",
    "zastavka", "namesti", "most", "reka", "hora", "kopec", "udoli", "pole", "louka", "zahrada",
    "chleb", "maso", "mleko", "syr", "jablko", "hruska", "brambor", "ryze", "polevka", "pivo",
    "vino", "caj", "kava", "cukr", "sul", "pepr", "koreni", "ovoce", "zelenina", "jidlo",
    "ptak", "ryba", "had", "medved", "vlk", "liska", "zajic", "slon", "zirafa", "tygr",
    "lev", "opice", "prase", "kava", "kun", "ovce", "koza", "slepice", "kachna", "husa",
    "den", "noc", "rano", "vecer", "rok", "tyden", "hodina", "minuta", "sekunda", "pondeli",
    "utery", "streda", "ctvrtek", "patek", "sobota", "nedele", "leden", "unor", "brezen", "duben",
    "hlava", "krk", "ruka", "noha", "oko", "ucho", "nos", "usta", "zub", "jazyk",
    "vlasy", "kuze", "srdce", "krev", "kost", "sval", "bricho", "zada", "prst", "nehet"
]

slovo = ""
uhodnuto = []
neni_tam = []

def vyber_slova():
    global slovo
    slovo = slova.pop(random.randrange(len(slova)))
    for a in range(len(slovo)):
            uhodnuto.append("_")

def zadej_tip(tip):
    global uhodnuto, neni_tam
    
    
    print("".join(uhodnuto))

    print("Slovo má {} písmen.".format(len(slovo))) 

    
    print("---------------------")
    # tip = input("Zadej písmeno: ")

    if tip in slovo:

        for i in range(len(slovo)):
                if slovo[i] == tip:
                    uhodnuto[i] = tip

        print("Správně! Písmeno '{}' je ve slově.".format(tip))
        
    else:
        print("Špatně! Písmeno '{}' není ve slově.".format(tip))
        neni_tam.append(tip)

    print("Zatím máš toto: {}".format("".join(uhodnuto)))
    print("A víš že tam není toto: {}".format(", ".join(neni_tam)))

    if "".join(uhodnuto) == slovo:
        print("---------------------")
        print("Gratulujeme! Uhodl jsi slovo '{}'.".format(slovo))
        return "Uhodnuto"
            