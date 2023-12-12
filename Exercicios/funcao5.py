def somaImposto(taxa, custo):
    valor = ((custo * taxa) / 100) + custo
    return f"O valor final do produto será de {valor:.2f} reais"


taxa = int(input("Qual é a taxa de imposto? "))
custo = float(input("Qual é o preço do produto antes do imposto? "))
print(somaImposto(taxa, custo))