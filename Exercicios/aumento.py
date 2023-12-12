salario = float; nvsalario = float; aumento = float
aumentopc = int

salario = float(input("Digite o salário da pessoa: "))

if salario <= 1000:
    aumentopc = 20
elif salario <= 3000:
    aumentopc = 15
elif salario <= 8000:
    aumentopc = 10
else:
    aumento = 5

nvsalario = (salario * aumentopc) / 100 + salario
aumento = (salario * aumentopc) / 100

print(f"Novo Salário: {nvsalario:.2f}")
print(f"Aumento: {aumento:.2f}")
print(f"Porcentagem: {aumentopc} %")