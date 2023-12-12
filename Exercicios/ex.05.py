lista = []
par = []
impar = []

for i in range(10):
    num = int(input("Digite os números: "))
    lista.append(num)
    if i % 2 == 0:
        par.append(num)
    elif i % 2 != 0:
        impar.append(num)

print(lista)
print(par)
print(impar)