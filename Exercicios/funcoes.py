def lin():
    print("=-" * 30)


def espaco():
    print(" ")


lin()
print("Bagual")
lin()
espaco()


def mensagem(msg):
    lin()
    print(msg)
    lin()
    espaco()


mensagem("Fala bafo")
mensagem("Bafora e passa")

def soma(a,b):
    s = a+b
    print(f"A soma de {a} com {b} é {s}")
    lin()
    espaco()

soma(1,7)

def contador(* num):
    for i in num:
        print(f"{i}", end = " ")
    print("FIM!")
    print(len(num))
    espaco()


contador(1,2,3,5)



def dobra(lst):
    #d = [i * 2 for i in lst]
    for i in lst:
        print(i * 2, end = " ")



lista = [1, 3, 4, 8]
dobra(lista)

    
