def escreva(texto):
    print("~" * len(texto)) 
    print(texto)
    print("~" * len(texto))

while True:
    texto = str(input("Digite uma string: "))
    escreva(texto)
    r = str(input("Deseja continuar? [S/N] "))
    if r in "Nn":
        break