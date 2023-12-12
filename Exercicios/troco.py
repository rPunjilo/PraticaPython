preco = float; dinheiro = float; troco = float
quantidade = int

preco = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
dinheiro = float(input("Dinheiro recebido: "))

troco = dinheiro - (preco * quantidade)

print(f"TROCO = {troco:.2f}")