class ControleRemoto:
    def __init__(self, cor, altura, comprimento, largura):
        self.cor = cor
        self.altura = altura
        self.comprimento = comprimento
        self.largura = largura

    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentou o canal")
        elif botao == "-":
            print("Diminuiu o canal")

Controle1 = ControleRemoto("Preto","15 cm", "5 cm", "3 cm")
Controle1.passar_canal("+")
print(Controle1.cor)

        