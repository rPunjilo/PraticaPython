lista = []
total = 0
qtd = 0
maior = 0

print("Projeção de Gastos com Abono")
print("="*30)
print(" ")

while True:
    try:
        n = float(input("Digite o salário: "))
        if n == 0:
            break
        lista.append((n))
    except ValueError:
        print("Você não digitou um valor válido!")

print(" ")
print("Salário    - Abono")

for i in lista:
    if i < 500:
        abono = 100.00
    else:
        abono = i * 0.10
        qtd += 1 
    print(f"R$ {i:<7.2f} - R$ {abono:>6.2f}")
    total += abono
    if abono > maior:
        maior = abono

print(" ")
print(f"Foram processados {len(lista)} colaboradores")
print(f"Total gasto com abonos: R$ {total:.2f}")
print(f"Valor mínimo pago a {qtd} colaboradores")
print(f"Maior valor de abono pago: R$ {maior:.2f}")
