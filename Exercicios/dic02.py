aluno = {}


while True:
    nome = str(input("Digite o nome do aluno: "))
    alt = float(input("Digite a altura do aluno: "))
    peso = int(input("Digite o peso do aluno: "))
    imc = peso / (alt**2)
    aluno.update({nome : imc})
    r = str(input("Deseja continuar? [S/N] "))
    if r in 'Nn':
        break

for c,i in aluno.items():
    print(f"O IMC do aluno {c} é {i}")


