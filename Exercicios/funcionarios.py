funcionarios = {}
while True:
    mat = int(input("Matrícula: "))
    nome = input("Nome: ")
    sal = float(input("Salário: R$ "))
    func = []
    func.append(nome)
    func.append(sal)
    funcionarios.update({mat: func})
    resp = input("Deseja continuar [S|N]? ")
    if resp == "N" or resp == "n":
        break

print(funcionarios)