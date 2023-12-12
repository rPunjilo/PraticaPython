
soma_enf = 0
qtd_enf = 0
qtd_medico = 0

while True:
    codigo = int(input("Digite o código do cargo: "))
    if codigo <= 0:
        break
    else:
        salario = float(input("Digite o valor do salário: "))
        if codigo == 1:
            cargo = "Enfermeiro"
            soma_enf += salario
            qtd_enf += 1
        elif codigo == 2:
            cargo = "Nutricionista"
        elif codigo == 3:
            cargo = "Medico"

media = 0
media = soma_enf / qtd_enf
print(f"Média salarial dos enfermeiros: {media:.2f}")