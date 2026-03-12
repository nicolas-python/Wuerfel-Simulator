#würfel simulator

import random


dice1_bild =  """
+-----+
|     |
|  o  |
|     |
+-----+
"""

dice2_bild =  """
+-----+
| o   |
|     |
|   o |
+-----+
"""

dice3_bild = """
+-----+
| o   |
|  o  | 
|  o  |
+-----+
"""

dice4_bild = """
+-----+
| o o |
|     |
| o o |
+-----+
"""

dice5_bild = """
+-----+
| o o |
|  o  |
| o o |
+-----+
"""

dice6_bild = """
+-----+
| o o |
| o o |
| o o |
+-----+
"""

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

#Würfel anzeigen
    print("Würfel 1")

    match dice1:
        case 1 :
            print(dice1_bild)
        case 2:
            print(dice2_bild)
        case 3:
            print(dice3_bild)
        case 4 :
            print(dice4_bild)
        case 5:
            print(dice5_bild)
        case 6:
            print(dice6_bild)

    match dice2:
        case 1 :
            print(dice1_bild)
        case 2:
            print(dice2_bild)
        case 3:
            print(dice3_bild)
        case 4 :
            print(dice4_bild)
        case 5:
            print(dice5_bild)
        case 6:
            print(dice6_bild)

    weiter = input("Nochmal Würfeln? (y/n):")

    if weiter == "y":
        continue

    else:
        break


