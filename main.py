#würfel simulator

import random

#""" erlaubt Text mit mehreren Zeilen
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
|   o |
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
            bild_dice1 = dice1_bild
        case 2:
            bild_dice1 = dice2_bild
        case 3:
            bild_dice1 = dice3_bild
        case 4 :
            bild_dice1 = dice4_bild
        case 5:
            bild_dice1 = dice5_bild
        case 6:
            bild_dice1 = dice6_bild

    match dice2:
        case 1 :
            bild_dice2 = dice1_bild
        case 2:
            bild_dice2 = dice2_bild
        case 3:
            bild_dice2 = dice3_bild
        case 4 :
            bild_dice2 = dice4_bild
        case 5:
            bild_dice2 = dice5_bild
        case 6:
            bild_dice2 = dice6_bild

    zeilen1 = bild_dice1.splitlines()       #splitlines teilt das Würfelbild in einzele zeilen
    zeilen2 = bild_dice2.splitlines()

    for i in range(6):                      #5 da es die  6 Würfel zeilen runterlaufen soll
        print(zeilen1[i]," ",zeilen2[i])    #i wählt die zeile des würfelbildes

    weiter = input("Nochmal Würfeln? (y/n):")

    if weiter == "y":
        continue

    else:
        break


