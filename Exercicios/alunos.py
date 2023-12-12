
idade = int(input("Digite a idade do aluno: "))
maior = idade
menor = idade

while True:
    idade = int(input("Digite a idade do aluno: "))
    if idade < 0:
        break
    else:
        if idade < menor:
            menor = idade
        elif idade > maior:
            maior = idade
        
media = 0
media = (maior + menor) / 2

print(f"Media das idades: {media:.1f}")