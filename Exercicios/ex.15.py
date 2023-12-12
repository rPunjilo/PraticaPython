lista = []
soma = 0
acima = 0
abaixo = 0

while True:
    n = int(input("Digite os números: "))
    if n == -1:
        #H
        print("Programa encerrado")
        break
    lista.append(n)
    soma += n
print("-=" * 40)
#A
print(f"Foram digitados {len(lista)} números")
#B
print(lista)
#C
lista.reverse()
print(lista)
#D
print(f"A soma dos valores é {soma}")
#E
media = soma / len(lista)
print(f"A média dos valores é {media}")
#F
for i in lista:
    if i > media:
        acima += 1
print(f"A quantidade de valores acima da média é {acima}")
#G
for i in lista:
    if i < 7:
        abaixo += 1
print(f"A quantidade de valores abaixo de 7 é {abaixo}")
