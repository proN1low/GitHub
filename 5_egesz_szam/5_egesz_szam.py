from audioop import avgpp

def closest(lista, avg):
    return lista[min(range(len(lista)), key = lambda i: abs(lista[i]-avg))]

print("Beolvasunk 5 egész számot és e listáról írunk ki információkat.")

lista = []
i = 0
while i < 5:
    szam = int(input("Adj meg egy egész számot: "))
    lista.append(szam)
    i += 1

# print(f'Az eredeti sorrend: {lista[0:5]}')
print(f'Az eredeti sorrend: {lista[0]}-{lista[1]}-{lista[2]}-{lista[3]}-{lista[4]}')
# print(f'A fordított sorrend: {lista[::-1]}')
print(f'A fordított sorrend: {lista[4]}-{lista[3]}-{lista[2]}-{lista[1]}-{lista[0]}')
print(f'A legkisebb elem: {min(lista)}, amelynek az indexe: {lista.index(min(lista))}')
print(f'A legnagyobb elem: {max(lista)}, amelynek az indexe: {lista.index(max(lista))}')
avg = sum(lista) / len(lista)
# print(f'Átlag: {avg}')
print(f'Az átlaghoz legközelebbi elem: {closest(lista, avg)}, melynek indexe: {lista.index(closest(lista, avg))}')