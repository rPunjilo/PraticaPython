def area(l,c):
    a = l * c
    return (f"A área de um terreno {l}x{c} é de {a}m²")


print(" Controle de Terrenos")
print("=-" * 20)
l = float(input("Largura (m): "))
c = float(input("Comprimento (m): "))
print(area(l,c))

