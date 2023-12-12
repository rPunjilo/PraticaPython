lista = []
sistema = []
sist = ["Windows Server", "Unix", "Linux", "Netware", "Mac Os", "Outro"]
maior = 0
melhor = 0
percmaior = 0

print("Qual o melhor Sistema Operacional para uso em servidores?")
print(" ")
print("As possíveis respostas são:")
print(" ")
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4 -Netware")
print("5- Mac OS")
print("6- Outro")
print(" ")

while True:
    try:
        n = int(input("Digite um número: "))
        if n == 0:
            break
        if n < 0 or n > 7:
            print("Digite um valor de 1 a 6 ou 0 para sair!")
        else:
            lista.append((n))
    except ValueError:
        print("Você não digitou um valor válido!")

for i in lista:
    if i == 1:
        sistema.append("Windows Server")
    elif i == 2:
        sistema.append("Unix")
    elif i == 3:
        sistema.append("Linux")
    elif i == 4:
        sistema.append("Netware")
    elif i == 5:
        sistema.append("Mac Os")
    elif i == 6:
        sistema.append("Outro")

print(" ")
print("Sistema Operacional", end = " " * 5)
print("Votos", end = " " * 5)
print("%")
print("-" * 40)
for i in sist:
    x = sistema.count(i)
    perc = x / len(lista) * 100
    print(f"{i:<15}{x:>12}{perc: >8.0f}%")
    if x > maior:
        maior = x
        melhor = i
        percmaior = perc

print(" ")
print(f"O Sistema Operacional mais votado foi o {melhor}, com {maior} votos, correspondendo a {percmaior:.0f} % dos votos.")