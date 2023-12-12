n = int(input("Quantos medicamentos serão cadstrados? "))

for i in range(n):
    nome = input("Digite o nome do medicamento: ")
    preco = int(input("Digite o valor do medicamento: "))
    mais_barato = nome
    menor_preco = preco
    
for i in range(n):  
    if preco < menor_preco:
        menor_preco = preco
        mais_barato = preco

print(f"Menor preco = {menor_preco:.2f}")