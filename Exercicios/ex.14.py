resposta = []


a = str(input("Telefonou para a vítima? "))
if a in 'Ss':
    resposta.append(a)
b = str(input("Esteve no local do crime? "))
if b in 'Ss':
    resposta.append(b)
c = str(input("Mora perto da vitíma? "))
if c in 'Ss':
    resposta.append(c)
d = str(input("Devia para a vítima? "))
if d in 'Ss':
    resposta.append(d)
e = str(input("Já trabalhou para a vítima? "))
if e in 'Ss':
    resposta.append(e)

if len(resposta) < 2:
    print("Inocente")
elif len(resposta) == 2:
    print("Suspeito")
elif len(resposta) <= 4:
    print("Cúmplice") 
else:
    print("Assassino")  



