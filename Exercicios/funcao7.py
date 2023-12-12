def valorPagamento(valor, dias):
    if dias == 0:
        vf = valor
    else:
        taxa = (valor * 0.1) / 100
        vf = valor + ((valor * 3) / 100) + (taxa * dias)
    relatorio.append(vf)
    return (f"O valor da prestação é de {vf:.2f} reais")

relatorio = []

while True:
    valor = float(input("Qual o valor da prestação? "))
    dias = int(input("Quantos dias está atrasado o pagamento? "))
    print(valorPagamento(valor,dias)) 
    r = str(input("Deseja continuar? [S/N] "))
    print(" ")
    if r in "Nn":
        break

print("                           RELATÓRIO FINAL:")
print("=-" * 35)
soma = 0
for i in relatorio:
    soma += i
print(f'A quantidade de prestações pagas no dia foi {len(relatorio)}')
print(f'O valor total de prestações pagas no dia foi de {soma:.2f} reais')