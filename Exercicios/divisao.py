n = int; num = int; den = int; divisao = float

n = int(input("Quantos casos voce irá digitar? "))

for i in range (0, n):
    num = int(input("Entre com o numerador: "))
    den = int(input("Entre com o denominador: "))
    if num < 0:
        print("DIVISÃO IMPOSSÍVEL")
    else:
        divisao = num / den
        print(f"DIVISÃO = {divisao:.2f}")

