#würfel simulator

import random

#funktionen
def zufalls_zahl():
     dice = random.randint(1,6)          #randint spare ich mir die liste
     return dice                               #dice = würfel auf englisch


while True:

    dice = zufalls_zahl()

    print("Würfel Zahl betragt:",dice)

    weiter = input("Nochmal Würfeln? (y/n):")

    if weiter == "y":
        continue

    else:
        break