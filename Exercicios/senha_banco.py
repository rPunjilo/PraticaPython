erros = 0
while erros < 3:
    senha = int(input("Digite a senha: "))
    if senha == 123456:
        print("Olá <seu nome>. Seja bem vindo ao nosso banco!")
        break
    else:
        erros += 1
        if erros < 3:
            print(f"Senha incorreta. Voce ainda tem {3 - erros} tentativas")
        else:
            print("Senha incorreta! Sua conta foi bloqueada.")
        


