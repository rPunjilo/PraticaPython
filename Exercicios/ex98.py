import time
def linha():
    print()
    print("=-" * 35)



def contador(i,f,p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    linha()
    print(f"Contagem de {i} até {f} de {p} em {p}")
    if i < f:   
        cont = i
        while cont <= f:
            print(cont, end = " ", flush = True)
            time.sleep(1)
            cont += p
        print("FIM!", end = "")
        linha()
    else:
        cont = i
        while cont >= f:
            print(cont, end = " ", flush = True)
            time.sleep(1)
            cont -= p
        print("FIM!", end = "")
        linha()


contador(0,10,1)
contador(10,0,2)
print("Agora é a sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Final: "))
p = int(input("Passo: "))
contador(i,f,p)