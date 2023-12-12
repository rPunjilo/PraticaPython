pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': '22'}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(" ")
for i in pessoas.keys():
    print(i)

print(" ")
for i in pessoas.values():
    print(i)

print(" ")
for i in pessoas.items():
    print(i)

print(" ")
for c,i in pessoas.items():
    print(f"{c} = {i}")