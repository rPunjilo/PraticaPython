codigo = int; qtd = int
valor = float; preco = float

codigo = int(input("Código do produto comprado: "))
qtd = int(input("Quantidade comprada: "))

if codigo == 1:
    preco = 5.00
elif codigo == 2:
    preco = 3.50
elif codigo == 3:
    preco = 4.80
elif codigo == 4:
    preco = 8.90
elif codigo == 5:
    preco = 7.32

valor = preco * qtd
print(f"Valor a pagar: {valor:.2f}")




