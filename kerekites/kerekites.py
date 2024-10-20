def kerek_le(n):
    return (n // 100) * 100

def kerek_fel(n):
    return (n // 100 + (n % 100 > 0)) * 100

print("Összegeket kerekítünk.")

osszeg = int(input("Adj meg egy összeget: "))
print(f'A százasokra lefelé kerekített értéke: {kerek_le(osszeg)}')
print(f'A százasokra felfelé kerekített értéke: {kerek_fel(osszeg)}')