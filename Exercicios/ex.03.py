lista = []
soma = 0

for i in range(4):
    num = float(input("Digite as notas: "))
    lista.append(num)
    soma += num

media = soma / len(lista)
print(f"Média: {media}")