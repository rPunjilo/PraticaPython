n = int; qtd = int; tipo = str
total = int; coelho = int; sapo = int; rato = int
pr = float; pc = float; ps = float

n = int(input("Quantos casos de teste serão digitados? "))

coelho = 0
rato = 0
sapo = 0
total = 0

for i in range (0, n):
    qtd = int(input("Quantidade de cobaias: "))
    tipo = input("Tipo de cobaia: ")
    if tipo == 'C':
        coelho = coelho + qtd
    elif tipo == 'R':
        rato = rato + qtd
    elif tipo == 'S':
        sapo = sapo + qtd

print("RELATÓRIO FINAL:")
total = coelho + rato + sapo
print(f"Total: {total}")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")

pc = coelho / total * 100
pr = rato / total * 100
ps = sapo / total * 100

print(f"Porcentual de coelhos: {pc:.2f} %")
print(f"Porcentual de ratos: {pr:.2f} %")
print(f"Porcentual de sapos: {ps:.2f} %")
