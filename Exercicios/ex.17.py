salto = []
soma = 0

while True:
    nome = input("Atleta: ")
    if nome == "":
        break
    print(" ")
    a = float(input("Primeiro salto: "))
    salto.append(a)
    b = float(input("Segundo salto: "))
    salto.append(b)
    c = float(input("Terceiro salto: "))
    salto.append(c)
    d = float(input("Quarto salto: "))
    salto.append(d)
    e = float(input("Quinto salto: "))
    salto.append(e)
    print(" ")
    print("Resultado Final: ")
    print(f"Atleta: {nome}")
    print("Saltos: ", end="")
    for i in salto:
        print(f"{i} - ", end ="")
        soma += i
    media = soma / len(salto)
    print(f"\nMédia dos saltos: {media} m")
    print(" ")

