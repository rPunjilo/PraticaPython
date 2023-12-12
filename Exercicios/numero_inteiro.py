
x = (input("Digite um número inteiro: "))

if not x.isdigit():
    print("Isso não é um numero inteiro")
else:
    x = int(x)
    if x % 2 == 0:
        print("Par")
    else:
        print("Impar")