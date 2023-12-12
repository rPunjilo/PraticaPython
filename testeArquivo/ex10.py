count = 0
text = str(input("Digite o texto: "))
word = str(input("Digite a palavra que deseja procurar: "))

with open("ex10.txt", 'w') as a:
    a.write(text)

with open("ex10.txt", 'r') as b:
    for i in b.readlines():
        x = i.count(word)

print(x)