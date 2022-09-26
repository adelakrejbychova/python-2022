baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

kod_baliku = input("Jaký je kód tvého balíku? ")
if kod_baliku in baliky:
    if baliky[kod_baliku] == True:
        print("Balík byl předán kurýrovi.")
    else:
        print("Balík zatím nebyl předán kurýrovi.")
else:
    print("Tento kód neexistuje.")