while True:
    nome = str(input("Digite o nome do usuário: "))
    telefone = int(input("Digite o telefone do usuário: "))
    if telefone == 0:
        break
    with open("ex12.txt", 'a') as a:
        a.write(f"{nome} ")
        a.write(f"{telefone}\n")