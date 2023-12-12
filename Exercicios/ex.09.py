lista = []
quad = 0
soma = 0

for i in range(3):
    n = int(input("Digite os números: "))
    lista.append(n)
    
for i in lista:
    quad = i**0.5
    soma += quad

print(soma)


