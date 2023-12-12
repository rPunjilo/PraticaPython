jogadores = {}
lista = []
total = 0

jogadores['nome'] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogadores['nome']} jogou? "))
for i in range(partidas):
    x = int(input(f"Quantos gols na partida {i}? "))
    lista.append(x)
    jogadores['gols'] = (lista.copy())

print("=-" * 40)

for i in lista:
    total += i
    jogadores['total'] = total

for i, c in jogadores.items():
    print(f"O campo {i} tem o valor {c}")

print("=-" * 40)
print(f"O jogador {jogadores['nome']} jogou {partidas} partidas")
for j, i in enumerate(lista):
    print(f"    => Na partida {j}, fez {i} gols")
print(f"Foi um total de {total} gols")
