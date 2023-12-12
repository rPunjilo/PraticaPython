class Retangulo:
    def __init__(self, Comp_Larg, Base_Altu):
        self.Comp_Larg = Comp_Larg
        self.Base_Altu = Base_Altu
    
    def mudar(self, opcao, novo):
        if opcao == "Comp_Larg":
            self.Comp_Larg = novo
        elif opcao == "Base_Altu":
            self.Base_Altu = novo
        else:
            print("Opção errada")

    def retornar(self):
        return print(f"O valor do comprimento e largura é {self.Comp_Larg} e da base e altura é de {self.Base_Altu}")
    
    def area(self):
        valor = self.Comp_Larg * self.Base_Altu
        return print(f"O valor da área é {valor}")
    
    def perimetro(self):
        valor = 2 * (self.Base_Altu + self.Comp_Larg)
        return print(f"O valor do perimetro é de {valor}")
    

Comp_Larg = int(input("Digite o valor do comprimento/largura: "))
Base_Larg = int(input("Digite o valor da base/altura: "))
retangulo = Retangulo(Comp_Larg,Base_Larg)
retangulo.retornar()
retangulo.area()
retangulo.perimetro()
trocar = input("Você deseja trocar o valor de alguma medida? Sim ou não: ").lower()
if trocar == "sim":
    opcao = input("Qual medida? ")
    valor = int(input("Qual o valor? "))
    retangulo.mudar(opcao, valor)

retangulo.retornar()



    
        

