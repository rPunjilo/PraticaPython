import time

def maior(* num):
    print("=-" * 30)
    print("Analisando os dados passados...")
    time.sleep(1)
    print("Os valores foram", end =" ")
    for num in lista:
        print(num, end = " ", flush = True)
        time.sleep(1)
    print(f"| Foram informados {len(lista)} valores ao todo.", flush = True)
    time.sleep(1)
    print(f"O maior valor informado foi {max(lista)}.")
   

lista = []
while True:
    lista.clear()
    while True:
        num = int(input("Digite um número: "))
        lista.append(num)
        r = str(input("Deseja continuar? [S/N] "))
        if r in "Nn":
            break
    maior(num)
    print("=-" * 30)
    resp = str(input("Deseja recomeçar? [S/N] "))
    if resp in "Nn":
        print("Volte logo!")
        break
