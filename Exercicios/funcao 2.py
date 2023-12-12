def imprimeLinha(num):
    for i in range(1, num + 1):
        print(f"{i} ", end = " ")
    print()

def imprimeSequencia(num):
    for num in range(num + 1):
        imprimeLinha(num)
    

imprimeSequencia(3)

