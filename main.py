#würfel simulator

import random

#funktionen
def zufalls_zahl():
    dice = ["1","2","3","4","5","6"]                     #Würfel auf english

    dice = random.choice(dice)
    return dice

dice = zufalls_zahl()

print("Würfel Zahl betragt:",dice)
