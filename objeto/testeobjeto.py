class Vendedor:
    def __init__(self, nome, vendas):
        self.nome = nome
        self.vendas = vendas

   # def vendeu(self, vendas):
       # self.vendas = vendas

    def bateu_meta(self, metas):
        self.metas = metas
        if self.vendas > metas:
            print(f"{self.nome} bateu a meta")
        else:
            print(f"{self.nome} não bateu a meta")

nome1 = str(input("Digite o nome: "))
vendedor1 = Vendedor(nome1, 1000)
#vendedor1.vendeu(1000)
vendedor1.bateu_meta(600)
print(vendedor1.metas)
nome2 = str(input("Digite o nome: "))
vendedor2 = Vendedor(nome2, 400)
#vendedor2.vendeu(400)
vendedor2.bateu_meta(600)
