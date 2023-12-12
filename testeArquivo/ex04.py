a = open("ex04.txt", 'w')
text = str(input("Digite o texto: "))
crt = str(input("Qual caracter você deseja contar? "))
a.write(text)
a.close()

b = open("ex04.txt", 'r')
qtd = 0
c = b.read()
for i in c:
    if i in crt:
        qtd += 1
print(f"Há {qtd} desse caracter")
b.close()