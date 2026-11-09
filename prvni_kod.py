
import time

jmena = [
    "Jakub", "Jan", "Tomáš", "Lukáš", "Matěj", "Vojtěch", "Ondřej", "Filip", "Jiří", "Martin",
    "Petr", "Václav", "Michal", "Josef", "Pavel", "Richard", "Karel", "Milan", "David", "Zdeněk",
    "Antonín", "František", "Štěpán", "Adam", "Dominik", "Daniel", "Marek", "Šimon", "Kryštof", "Radek",
    "Miroslav", "Jaroslav", "Vladimír", "Vlastimil", "Aleš", "Kamil", "Vít", "Jindřich", "Luboš", "Radim",
    "Eduard", "Patrik", "Roman", "Stanislav", "Ivan", "Igor", "Bohumil", "Rostislav", "Radomír", "Vratislav",
    "Luděk", "Miloš", "Bohuslav", "Dalibor", "Dušan", "Emil", "Erik", "Evžen", "Gabriel", "Havel",
    "Hubert", "Hugo", "Hynek", "Ignác", "Ilja", "Jáchym", "Jeroným", "Jiljí", "Julius", "Justýn",
    "Kazimír", "Klement", "Kristián", "Kvído", "Ladislav", "Libor", "Lumír", "Marcel", "Marián", "Maxmilián",
    "Mikuláš", "Mojmír", "Oldřich", "Oliver", "Oskar", "Ota", "Otakar", "Přemysl", "Radovan", "René",
    "Robert", "Robin", "Rudolf", "Samuel", "Sebastián", "Slavomír", "Soběslav", "Svatopluk", "Svatoslav", "Tadeáš",
    "Eliška", "Tereza", "Anna", "Adéla", "Natálie", "Kristýna", "Nela", "Viktorie", "Amálie", "Ema",
    "Julie", "Sofie", "Kateřina", "Barbora", "Veronika", "Lucie", "Marie", "Eva", "Hana", "Jana",
    "Lenka", "Michaela", "Martina", "Alena", "Petra", "Klára", "Zuzana", "Markéta", "Jitka", "Ludmila",
    "Jarmila", "Věra", "Dagmar", "Dana", "Irena", "Ivana", "Monika", "Nikola", "Simona", "Radka",
    "Romana", "Kamila", "Milada", "Vlasta", "Růžena", "Helena", "Blanka", "Zdenka", "Olga", "Andrea",
    "Agáta", "Alžběta", "Anastázie", "Anežka", "Anita", "Antonie", "Apolena", "Beáta", "Běla", "Bohdana",
    "Bohumila", "Božena", "Brigita", "Cecílie", "Dita", "Dobromila", "Dominika", "Dorota", "Doubravka", "Drahomíra",
    "Filip", "Elena", "Evelína", "Františka", "Gabriela", "Gizela", "Hedvika", "Ida", "Ilona", "Ingrida",
    "Iveta", "Izabela", "Johana", "Jolana", "Judita", "Justýna", "Karin", "Karolína", "Květa", "Lada",
    "Laura", "Leona", "Linda", "Livia", "Magdaléna", "Mahulena", "Marcela", "Mariana", "Marika", "Marta"
]
jmeno = jmena.pop()

while jmeno.lower() != 'filip':
    print('Nespravne jmeno. Zadej znovu')
    jmeno = jmeno = jmena.pop()
    time.sleep(10)

print('Vitej Filipe')