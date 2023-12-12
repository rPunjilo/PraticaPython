brasil = []
estado = {}

while True:
    estado['uf']= str(input("Digite o nome do estado: "))
    estado['sigla']= str(input("Digite a sigla do estado: "))
    brasil.append(estado.copy())
    r = str(input("Deseja continuar? "))
    if r in "Nn":
        break
    
for i in brasil:
    print(f"{i}")