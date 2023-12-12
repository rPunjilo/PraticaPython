def ex4(a):
    if a > 0:
        return ("POSITIVO")
    elif a < 0:
        return ("NEGATIVO")
    else:
        return ("ZERO")


a = int(input("Digite um valor: "))
print(ex4(a))
