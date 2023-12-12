lista = {}

for i in range(2):
    codigo = int(input("Digite o código do produto: "))
    nome = str(input("Digite o nome do produto: "))
    valor = float(input("Digite o valor do produto (R$): "))
    print(" ")
    lista.update({codigo: [nome, valor]})

for c, i in lista.items():
    if i[1] > 50:
        i[1] *= 0.90
        i[0] += " em promoção"

for c, i in lista.items():
    print(f"Código = {c}")
    print(f"Nome: {i[0]}")
    print(f"Valor: R${i[1]}")
