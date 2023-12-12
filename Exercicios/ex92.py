lista = {}

while True:
    nome = str(input("Nome: "))
    ano = int(input("Ano de nascimento: "))
    ctps = int(input("Carteira de trabalho (0 não tem): "))
    idade = 2023 - ano
    lista.update({nome: [idade,ctps]})
    if ctps != 0:
        contratacao = int(input("Ano de contratação: "))
        salario = float(input("Salário: R$"))
        aposentadoria = (contratacao + 35) - ano
        lista.update({nome: [idade, ctps, contratacao, salario, aposentadoria]})
    r = str(input("Deseja continuar? [S/N]: "))
    if r in 'Nn':
        break

print("=-" * 40)
for i, c in lista.items():
    if c[1] != 0:
        print(f"O nome é {i}")
        print(f"A idade é de {c[0]} anos")
        print(f"O número da CTPS é {c[1]}")
        print(f"O ano de contratação foi em {c[2]}")
        print(f"O salário é de R${c[3]}")
        print(f"O trabalhador se formará com {c[4]} anos")
    else:
        print("O trabalhor não possui CTPS")
