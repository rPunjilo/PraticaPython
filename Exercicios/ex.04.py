lista = []
cont = 0

for i in range(10):
    n = str(input("Digite as letras: "))
    if n not in 'aeiou':
        lista.append(n)
        cont += 1

print(f"Há {len(lista)} consoantes")
print(lista)
