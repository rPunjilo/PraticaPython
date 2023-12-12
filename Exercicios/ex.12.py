temp = []
lista = []
soma = 0
cont = 0

for i in range(3):
    ida = int(input("Digite a idade: "))
    temp.append(ida)
    alt = float(input("Digite a altura: "))
    soma += alt 
    temp.append(alt)
    lista.append(temp[:])
    temp.clear()

for i in lista:
    media = soma / len(lista)
    if i[0] > 13 and i[1] < media:
        cont += 1

print(cont)
print(media)



