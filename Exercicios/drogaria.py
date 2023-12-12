
nome = input("Digite o nome do medicamento: ")
preco = float(input("Digite o valor do medicamento: "))
mais_barato = nome
menor_preco = preco

for i in range(3):
    nome = input("Digite o nome do medicamento: ")
    preco = float(input("Digite o valor do medicamento: "))
    if preco < menor_preco:
        menor_preco = preco
        mais_barato = nome

print(f"Menor preco = {menor_preco:.2f}") 
