clientes = {}

while True:
    razao = int(input("Digite a razão social do cliente: "))
    valor = float(input("Digite o valor total em compras: "))
    clientes.update({razao: valor})
    r = str(input("Deseja continuar? [S/N] "))
    if r in "Nn":
        break

print(" ")
print("Demonstrativo de vendas: ")
for i in sorted(clientes, key = clientes.get, reverse = True):
    print(f"O cliente {i} gastou um valor de R$ {clientes[i]:.2f}")
