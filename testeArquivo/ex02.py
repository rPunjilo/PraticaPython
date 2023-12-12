a = open("ex02.txt", 'w')
text = str(input("Digite o texto: "))
a.write(text)
a.close()

b = open("ex02.txt", 'r')
vogal = 'AaEeIiOoUu'
qtd = 0
c = b.read()
for i in c:
    if i in vogal:
        qtd += 1
print(f"Há {qtd} vogais")
b.close()