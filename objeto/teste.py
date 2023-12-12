idade = int(input("Digite a idade: "))
if idade >= 19:
    categoria = "Categoria "
    percurso = input("Digite o percurso: ")
    if percurso == "longo":
        categoria = categoria + "Percurso longo "
    else:
        categoria = categoria + "Percurso curto "
    sexo = input("Digite o genêro do participante: ")
    if sexo == "masculino":
        categoria = categoria + "Masculino"
    else:
        categoria = categoria + "Feminino"

print(categoria)
