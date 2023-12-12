import random
import time


def sorteio(* num):
    print("Sorteando os 5 valores da lista: ", end = " ")
    for num in lista:
        print(num, end = " ", flush = True)
        time.sleep(1)
    print("PRONTO!")
    print(par(num))
    
    
def par(num):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    return(f"Somando os valores de {lista}, temos {soma}")


lista = []
for i in range(5):
    num = random.randrange(0,10)
    lista.append(num)

sorteio(num)

