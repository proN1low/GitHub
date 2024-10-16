szaz = int(input("Százas (db): ")) * 100
osszeg = szaz

ketszaz = int(input("Kétszázas (db): ")) * 200
osszeg += ketszaz

otszaz = int(input("Ötszázas (db): ")) * 500
osszeg += otszaz

print(f'Összeg: {osszeg} Ft')