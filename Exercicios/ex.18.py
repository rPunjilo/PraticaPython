lista = []
candidatos = []
maior = 0
percmaior = 0
melhor = 0

print("Enquete: Quem foi o melhor jogador?")
print(" ")

while True:
    num = int(input("Número do jogador (0=fim): "))
    if num == 0:
        break
    lista.append(num)
    if num > 23 or num < 0:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        lista.pop()
    
print(" ")
print("Resultado da votação:")
print(" ")
print(f"Foram computados {len(lista)} votos.")
print(" ")
print("Jogador", end = " " * 3)
print("Votos", end = " " * 5)
print("%")

for i in lista:
    if i not in candidatos:
        candidatos.append(i)

for j in candidatos:
    x = lista.count(j)
    perc = x / len(lista) * 100
    print(f"{j: > 4}{x: > 9}{perc: >10.2f}%")
    if x > maior:
        maior = x
        melhor = j
        percmaior = perc
    
print(" ")
print(f"O melhor jogador foi o número {melhor}, com {maior} votos, correspondendo a {percmaior:.0f} % do total de votos")

