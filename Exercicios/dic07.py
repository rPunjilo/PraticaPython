filme = {}

while True:
    try:
        titulo = str(input("Digite o título do filme: "))
        nome1 = str(input("Digite o nome do ator: "))
        nome2 = str(input("Digite o nome de outro ator: "))
        r = str(input("Deseja continuar [S/N]? "))
        filme.update({titulo: [nome1, nome2]})
        if r in "Nn":
            break
    except ValueError:
        print("Você não digitou um valor válido!")

for i, c in filme.items():
    buscar = str(input("Digite o nome do filme: "))
    if buscar in filme:
        print(f"O filme {buscar} tem no elenco os atores {c[0]} e {c[1]}")
    else:
        print("Este filme não está cadastrado.")
    r = str(input("Deseja continuar? "))
    if r in "Nn":
        break
