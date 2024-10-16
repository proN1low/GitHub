print("Egy függvényt tesztelünk, amely két szám közül adja vissza a kisebb dupláját.")

def kisebb_dupla():
    elso = int(input("Adj meg egy számot: "))
    masodik = int(input("Adj meg még egy számot: "))
    if elso < masodik:
        kisebb_dupla = elso*2
    if masodik < elso:
        kisebb_dupla = masodik*2
    if elso == masodik:
        print("A két szám megegyezik.")
    print(f'A két szám közül a kisebb duplája: {kisebb_dupla}')
kisebb_dupla()