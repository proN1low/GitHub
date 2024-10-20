def dec_bin(n):
    if n == 0:
        return 0
    binaris = ""
    while n > 0:
        binaris = str(n % 2) + binaris
        n = n // 2
    return binaris

print("Egy pozitív egész számot alakítunk bináris számmá.")

szam = int(input("Adj meg egy pozitív egész számot: "))
print(f'A {szam} binárisan: {dec_bin(szam)}')