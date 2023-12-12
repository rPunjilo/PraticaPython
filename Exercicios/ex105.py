dici = {}
lista = []

def notas(n):
    dici["Total"] = len(lista)
    dici["Maior"] = max(lista)
    dici["Menor"] = min(lista)
    soma = 0
    for i in lista:
        soma += i
    media = soma / len(lista)    
    dici["Média"] = media
    sit = True
    if sit == True:
        if media >= 8:
            dici["Situação"] = "BOA"
        elif media >= 5:
            dici["Situação"] = "RAZOAVEL"
        else:
            dici["Situação"] = "RUIM"
    return dici
    
    

while True:
    n = float(input("Digite as notas: "))
    lista.append(n)
    r = str(input("Deseja continuar? [S/N] "))
    if r in "Nn":
        break
print(notas(n))