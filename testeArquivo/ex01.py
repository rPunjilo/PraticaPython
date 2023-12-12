a = open("ex01.txt", 'w')
n = int(input("Quantos nomes serão digitados? "))
for i in range(0,n):
    x = str(input("Digite os nomes: "))
    a.write(f"{x}\n")   
a.close()

b = open("ex01.txt", 'r')
qtd = 0
for i in b.readlines():
    i = i.rstrip("\n")
    qtd += len(i)
print(f"Há {qtd} caracteres nesse arquivo ")
b.close()

d = open("ex01.txt", 'r')
e = d.readlines()
print(f"Há {len(e)} linhas nesse arquivo")
d.close()