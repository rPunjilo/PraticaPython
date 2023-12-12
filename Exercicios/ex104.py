def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            return int(n)
        else:
            print("Erro")




n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar {n}")