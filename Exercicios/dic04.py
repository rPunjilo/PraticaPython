voos = {}
cont = 0

while True:
    try:
        num = int(input("Digite o número do voo: "))
        origem = str(input("Digite a origem do voo: "))
        destino = str(input("Digite o destino do voo: "))
        voos.update({num: [origem, destino]})
        r = str(input("Deseja continuar [S/N]? "))
        if r in "Nn":
            break
    except ValueError:
        print("Você não digitou um valor válido!")

for i in voos.values():
    if i[0].upper() == "NATAL":
        cont += 1
    if i[1].upper() == "RECIFE":
        voos.pop(num)

print(voos)
print(f"A quantidade de voos cujo origem é Natal é de {cont}")