"""
Egy függvényt tesztelünk, amely két szám közül adja vissza a nagyobb háromszorosát.
Írj egy függvényt "nagyobb_tripla néven, amely két számot kap paraméterül és visszaadja a nagyobb szám tripláját.
"""

# Egy lehetséges megoldás:

# Tájékoztatjuk a felhasználót a program működéséről
print("Egy függvényt tesztelünk, amely két szám közül adja vissza a nagyobb háromszorosát.")

# Definiáljuk a függvényt
def nagyobb_tripla(x, y):
    print(f'A két szám közül a nagyobb: ', max(x, y))
    return max(x, y) * 3

# Ez itt a tesztelés:
# Bekérjük a két számot és egyből valós számítpussá (float) is alakítjuk a változókat
num1 = float(input("Adj meg egy számot: "))
num2 = float(input("Adj meg még egy számot: "))

# Teszteljük a függvényt
print(f'A két szám közül a nagyobb triplája: ', nagyobb_tripla(num1, num2))