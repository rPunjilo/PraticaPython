n = int; x = int; 

n = int(input("Quantos numeros voce vai digitar? "))

for i in range (0, n):
    x = int(input("Digite um numero: "))
    if x == 0:
        print("NULO")
    elif x > 0 and x % 2 == 0:
        print("PAR POSITIVO")
    elif x < 0 and x % 2 == 0:
        print("PAR NEGATIVO")
    elif x > 0 and x % 2 != 0:
        print("IMPAR POSITIVO")
    else:
        print("IMPAR NEGATIVO")