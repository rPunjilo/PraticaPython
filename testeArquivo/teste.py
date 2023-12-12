from testeArquivo.funcoes import *
a = open("carro.txt", 'w')
a.write("Civic\n")
a.write("Corolla\n")
a.write("Amarok\n")
a.close()

b = open("carro.txt", 'a')
b.write("Supra")
b.close()

with open("carro.txt", 'r') as c:
    print(c.read())
c.close()

d = "fruta.txt"
print(arquivoExiste(d))

e = 'carro.txt'
print(arquivoExiste(e))

