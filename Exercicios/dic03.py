voos = {}
dado = []
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
    

for c, i in voos.items():
    if i[0].upper() == "NATAL":
        cont += 1
    if i[1].upper() == 'RECIFE':
        dado.append(c)

for i in dado:
    voos.pop(i)
    
for c, i in voos.items():
    print(f"Número do voo: {c}")
    print(f"Origem: {i[0]}")
    print(f"Destino: {i[1]}")
    print(" ")
        
print(f"A quantidade de voos cujo origem é Natal é de {cont}")