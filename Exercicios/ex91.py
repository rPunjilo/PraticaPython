import random
from time import sleep
lista = {}

for i in range(1,5):
    x = random.randint(1,6)
    jogador = f"Jogador{i}"
    lista.update({jogador: x})

print("Valores Sorteados:")
for i, c in lista.items():
    print(f"O {i} tirou {c} no dado")
    sleep(1)
print(" ")

x = 1
print("Ranking dos Jogadores: ")
for i in sorted(lista, key = lista.get, reverse = True):
    print(f"{x}º Lugar: {i} com {lista[i]}")
    x += 1