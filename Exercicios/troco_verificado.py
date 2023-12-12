preco = float; dinheiro = float; troco = float; sobra = float
quantidade = int

preco = float(input("Preço unítario do produto: "))
quantidade = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

troco = dinheiro - (preco * quantidade)

if troco < 0:
    sobra = (preco * quantidade) - dinheiro
    print(f"Dinheiro Insuficiente! Faltam {sobra:.2f}")
else:
    print(f"Troco = {troco:.2f}")