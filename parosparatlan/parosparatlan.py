"""
Egy függvényt tesztelünk, amely egy egész szám alapján kiírja, hogy az páratlan-e.
Írj egy függvényt "paros_paratlan" néven, amely a bejövő paraméter alapján kiírja,
hogy az páros-e vagy páratlan.
Pl. így: Ez a szám ... páros!
"""

# Egy lehetséges megoldás:

# Tájékoztatjuk a felhasználót a program működéséről
print("Egy függvényt tesztelünk, amely egy egész szám alapján kiírja, hogy az páratlan-e.")

# Definiáljuk a függvényt
def paros_paratlan(num):
    print(f'Ennek a számnak a maradéka 2-vel osztva: ', num % 2)
    return num % 2 # bool T v F

# Ez itt a tesztelés:
x = int(input("Adj meg egy egész számot: "))

# Meghívjuk a függvényt a bejövő értékkel
if paros_paratlan(x):
    print(f'Tehát a(z) {x} páratlan szám.')
else:
    print(f'Tehát a(z) {x} páros szám.')