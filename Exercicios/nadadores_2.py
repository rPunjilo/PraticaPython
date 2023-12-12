media = 0
soma = 0
cont = 0
qtd = 0

n = int(input("Quantos nadadores foram cronometrados? "))

nome = input("Nome do nadador 1: ")
tempo = int(input("Tempo do nadador 1: "))
melhor = nome
menor = tempo
pior = nome
maior = tempo
soma += tempo
cont += 1
if tempo >= 12 and tempo <= 15:
    qtd += 1

for i in range(1,n):
    nome = input(f"Nome do nadador {i+1}: ")
    tempo = int(input(f"Tempo do nadador {i+1}: "))
    if tempo < menor:
        menor = tempo
        melhor = nome
    elif tempo > maior:
        maior = tempo
        pior = nome
    soma += tempo
    cont += 1
    if tempo >= 12 and tempo <= 15:
        qtd += 1

media = soma / cont

print(f"Nadador com o melhor tempo: {melhor}")
print(f"Nadador com o pior tempo: {pior}")
print(f"Media = {media:.1f}")
print(f"Quantidade de atletas com o tempo entre 12s e 15s: {qtd}")