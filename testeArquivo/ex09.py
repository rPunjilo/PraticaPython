
lista = []
biggest = 0
pos = 0

with open('textoEX09.txt', 'r') as a:
    for i in a.readlines():
        x = i.rstrip("\n")
        z = x.splitlines()
        lista.append(z)

for i in lista:
    line = int(i[0][-8:])
    if line > biggest:
        biggest = line
        pos = i

print(pos)
print(lista)







