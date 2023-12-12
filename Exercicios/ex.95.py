jogadores = {}
time = []
lista = []
nomes = []
total = 0

while True:
    jogadores.clear()
    lista.clear()
    jogadores['nome'] = str(input("Nome do jogador: "))
    nomes.append(jogadores['nome'])
    partidas = int(input(f"Quantas partidas {jogadores['nome']} jogou? "))
    for i in range(partidas):
        x = int(input(f"Quantos gols na partida {i+1}? "))
        lista.append(x)
        jogadores['gols'] = (lista.copy())
    print('-' * 35)
    jogadores['total'] = sum(lista)
    time.append(jogadores.copy())
    r = str(input("Deseja continuar? [S/N] "))
    if r in "Nn":
        break

print("=-" * 35)
print("Cod", end= " ")
print("Nome", end = " " * 7)
print("Gols", end = " " * 3)
print("Total", end = " ")
print("")
for c, i in enumerate(time):
    print(f"{c:>3}", end = " ")
    for k in i.values():
        print(f"{str(k):<9}", end = " ")
    print()
print(" ")
while True:
    busca = int(input("Mostrar dados de qual jogador? "))
    if busca == 999:
        break
    else:
        print(" ")
        print(f"LEVANTAMENTO DO JOGADOR {time[busca]['nome']}")
        for c, i in enumerate(time[busca]['gols']):
            print(f"      Na partida {c+1}, fez {i} gols.")




