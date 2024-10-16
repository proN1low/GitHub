print("Egy függvényt tesztelünk, amely egy egész szám alapján kiírja, hogy az páratlan-e.")

def paros_paratlan():
    szam = int(input("Adj meg egy egész számot: "))
    if szam % 2 == 0:
        print("Ez a szám páros.")
    else:
        print("Ez a szám páratlan.")
paros_paratlan()