class Quadrado():
    def __init__(self, tamanho):
        self.tamanho = tamanho


    def troca_Valor(self, novo):
        if novo == self.tamanho:
            print("Foi digitado o mesmo valor")
        else:
            self.tamanho = novo

    def retornar(self):
        return print(f"O tamanho dos lados é de {self.tamanho}")
    
    def area(self):
       valor = self.tamanho * self.tamanho
       return print(f"O valor da área é {valor}")
    

tamanho = int(input("Digite o tamanho: "))
quadrado = Quadrado(tamanho)
quadrado.retornar()
valor = int(input("Digite o novo tamanho: "))
quadrado.troca_Valor(valor)
quadrado.area()
