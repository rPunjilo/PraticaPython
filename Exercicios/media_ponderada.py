n = int; x = float; media = float; soma = float

n = int(input("Quantos casos voce irá digitar? "))

media = 0
soma = 0

print("Digite os números: ")
for i in range (0, n):
    x = float(input())
    soma = soma + x

media = soma / n
print(f"MEDIA = {media:.2f}")
