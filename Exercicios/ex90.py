lista = {}

nome = str(input("Nome: "))
lista.update({nome: []})

for i, c in lista.items():
    media = float(input(f"Média de {i}: "))
    if media >= 5.0:
        situacao = 'aprovado'
    else:
        situacao = 'reprovado'
    lista.update({nome: [media, situacao]})
    
    
for i, c in lista.items():   
    print(f"Nome é igual a {i}")
    print(f"Média é igual a {c[0]}")
    print(f"Situação é igual a {c[1]}")






