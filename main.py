#würfel simulator

import random

#funktionen
def zufalls_zahl():
     dice = random.randint(1,6)          #randint spare ich mir die liste
     return dice                               #dice = würfel auf englisch


while True:

    dice1 = zufalls_zahl()
    dice2 = zufalls_zahl()

    print("Würfel 1 hat:",dice1, "gewürfelt")
    print("Würfel 2 hat:",dice2, "gewürfelt")

    gesamt=dice1 + dice2
    print("Gesamt würde:",gesamt,"gewürfelt")

    weiter = input("Nochmal Würfeln? (y/n):")

    if weiter == "y":
        continue

    else:
        break