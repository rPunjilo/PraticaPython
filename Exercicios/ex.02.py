lista = []

for i in range(10):
    num = float(input("Digite os números: "))
    lista.append(num)

lista.sort(reverse = True)
print(lista)