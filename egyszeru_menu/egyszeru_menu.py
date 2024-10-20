print("A program bekér egy szöveget és a választásod alapján kiír ezt-azt a szövegről. Üres szövegre leáll.")

def a_betu():
    darab = 0
    for a in szoveg.lower():
        if a == 'a':
            darab += 1
    print(f'{darab} db "a" betű van a szövegben.')

def szoveg_hossz():
    print(f'{szoveg.__len__()} karakter hosszú a szöveg.')

def szoveg_upper():
    print(szoveg.upper())

szoveg = input("Adj meg egy tetszőleges szöveget: ")
if szoveg == "":
    print("Viszlát!")
    exit()
else:
    print ('Válassz:\na) Kiírjuk hány "a" betű van a szövegben\nb) Kiírjuk a szöveg hosszát\nc) Kiírjuk a szöveg nagybetűs változatát')

valasz = input("Válasz: [a, b, c]: ")
if valasz == 'a':
    a_betu()
if valasz == 'b':
    szoveg_hossz()
if valasz == 'c':
    szoveg_upper()