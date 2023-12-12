class Bola:
    def __init__(self,cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def troca_Cor(self, cor_nova):
        if cor_nova == self.cor:
            print("É a mesma cor.")
        else:
            self.cor = cor_nova

    def mostra_Cor(self):
        print(self.cor)


cor = input("Digite a cor: ")
circuferencia = int(input("Digite a circuferencia: "))
material = input("Digite o material: ")
cor_nova = input("Digite a cor nova: ")

Bola1 = Bola(cor,circuferencia, material)
print(f"A cor da bola é {Bola1.cor}")
print(f"A circuferencia da bola é de {Bola1.circuferencia}")
print(f"O material da bola é de {Bola1.material}")
Bola1.troca_Cor(cor_nova)
print(f"A cor nova da bola é {Bola1.cor}")