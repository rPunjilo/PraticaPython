media = []
soma = 0
cont = 0

for i in range(5):
    print(f"Digite as notas do {i+1}º aluno: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    soma = (nota1 + nota2 + nota3 + nota4) / 4
    media.append(soma)
    print(" ")

for i in media:
    if i >= 7.0:
        cont += 1

print(f"Há {cont} alunos aprovados")