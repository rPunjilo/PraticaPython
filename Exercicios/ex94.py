dicionario = {}
lista = []
mulheres = []

while True:
    nome = str(input("Digite o nome da pessoa: "))
    while True:
        sexo = str(input("Qual o sexo da pessoa? [M/F] ")).upper()[0]
        if sexo in 'MF':
            break
        print("Erro! Digite o sexo da pessoa")
    idade = int(input("Digite a idade da pessoa: "))
    dicionario.update({nome: [sexo, idade]})
    r = str(input("Deseja continuar? [S/N] "))
    if r in "Nn":
        break
lista.append(dicionario.copy())    

soma = 0
for c, i in dicionario.items():
    soma += i[1]
    if i[0] == 'F':
        mulheres.append(c[:])

print("=-" * 30)
print(f"-O grupo tem {len(dicionario)} pessoas")
print(f"-A média de idade é de {soma/len(dicionario)} anos")
print(f"-As mulheres cadastradas foram: ", end = '') 
for i in mulheres:
    print(f'{i} ', end = '')
print(" ")
print("-Lista de pessoas que estão acima da média: ")
for c,i in dicionario.items():
    if i[1] > soma/len(dicionario):
        print(f"Nome = {c}; Sexo = {i[0]}; Idade = {i[1]}")



