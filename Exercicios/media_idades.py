x = int; soma = int; cont = 0
media = float

print("Digite as idades: ")
x = int(input())

soma = 0
cont = 0

if x < 0:
    print("Impossível calcular!")
else:
    while x >= 0:
        soma = soma + x
        cont = cont + 1
        x = int(input())

    media = soma / cont
    print(f"Media = {media:.2f}")