a = int; b = int; soma1 = int

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B "))

soma = 0
if a > b:
    print("Erro")
else:
    for i in range(a , b + 1):
        soma += i

print(f"Soma = {soma}")
