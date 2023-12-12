minutos = int
valor = float

minutos = int(input("DIgite a quantidade de minutos: "))

if minutos < 100:
    valor = 50.00
elif minutos > 100:
    valor = (minutos - 100) * 2 + 50.00

print(f"Valor a pagar : R$ {valor:.2f}")