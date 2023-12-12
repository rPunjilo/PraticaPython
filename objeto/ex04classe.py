class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, nova_idade):
        self.idade += nova_idade
        if self.idade <= 21:
            self.altura += 0.05
            print(f"A altura da pessoa agora é de {self.altura:.2f}m")
        print(f"A idade da pessoa agora é de {self.idade}")

    def engordar(self, novo_peso):
        self.peso += novo_peso
        return print(f"O peso da pessoa agora é de {self.peso} quilos")

    def emagrecer(self, novo_peso):
        self.peso -= novo_peso
        return print(f"O peso da pessoa agora é de {self.peso} quilos")
    
    def crescer(self, nova_altura):
        self.altura += nova_altura
        return print(f"A altura da pessoa agora é de {self.altura:.2f}")


nome = input("Qual o nome da pessoa? ")
idade = int(input("Qual a idade da pessoa? "))
peso = float(input("Qual o peso da pessoa? "))
altura = float(input("Qual a altura da pessoa? "))
pessoa = Pessoa(nome,idade,peso,altura)
pessoa.envelhecer(1)
pessoa.engordar(3)
pessoa.emagrecer(6)
pessoa.crescer(0.10)
        