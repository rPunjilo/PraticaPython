pais = {}

while True:
    p = str(input("Digite o pais: "))
    uf = str(input("Digite o nome do estado: "))
    sigla = str(input("Digite a sigla do estado: "))
    estado = []
    estado.append(uf)
    estado.append(sigla)
    pais.update({p: estado})
    r = str(input("Deseja continuar? "))
    if r in "Nn":
        break
    
print(pais)