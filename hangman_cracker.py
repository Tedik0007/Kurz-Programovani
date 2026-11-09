import hangmanv2 as hangman
import random
import time

abeceda = list("abcdefghijklmnopqrstuvwxyz")

hangman.vyber_slova()

while True:
    for a in range(len(abeceda)):
        vysledek = hangman.zadej_tip(abeceda.pop(random.randrange(len(abeceda))))
        time.sleep(0.2)

        if vysledek == "Uhodnuto":
            quit()
        