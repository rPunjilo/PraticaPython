a = open("ex03.txt", 'w')
text = str(input("Digite o texto: "))
a.write(text)
a.close()

b = open("ex03.txt", 'r')
vogal = 'AaEeIiOoUu'
consoante = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz'
qtdV = 0
qtdC = 0
c = b.read()
for i in c:
    if i in vogal:
        qtdV += 1
    elif i in consoante:
        qtdC += 1

print(f"Há {qtdV} vogais")
print(f"Há {qtdC} consoantes")
b.close()