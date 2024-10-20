import math

def kerulet():
    return 2 * sugar * math.pi

def terulet ():
    return sugar**2 * math.pi

print("Egy kör sugarát kérjük be és kiírjuk a kerületét cm-ben és a területét cm²-ben.")

sugar = float(input("Add meg egy kör sugarát cm-ben: "))
print(f'A kör kerülete: {round(kerulet(), 2)} cm')
print(f'A kör területe: {round(terulet(), 2)} cm²')
