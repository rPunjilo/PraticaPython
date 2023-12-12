sexo = str; idade = int; qtdh = int; qtdm = int

qtdh = 0
qtdm = 0

while True:
    idade = int(input("Idade: "))
    if idade < 0:
        print("Encerrando o programa") 
        break
    else:
        sexo = input("Sexo: ")
        if sexo == 'F' or sexo == 'f':
            qtdm += 1
        elif sexo == 'M' or sexo == 'm':
            if idade < 18:
                qtdh += 1
    

print(f"Quantidade de mulheres: {qtdm}")
print(f"Quantidade de homens com menos de 18 anos: {qtdm}")
