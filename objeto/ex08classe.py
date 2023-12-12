class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
    
    def __str__(self):
        return self.nome

    def comer(self, *args):
        for i in args:
            if isinstance(i, Macaco):
                canibal = Canibal(self.nome)
            self.bucho.append(i)
    
    def verBucho(self):
        print(f"O macaco {self.nome} comeu:")
        for i in self.bucho:
            print(i)

    def digerir(self):
        self.bucho = "Vazio"
        return print(f"O macaco {self.nome} fez a digestão do alimento")
    
class Canibal(Macaco):
    def __init__(self, nome):
        super().__init__(nome)
        print(f"O macaco {self.nome} é canibal!!!")
        
Babu = Macaco("Babu")
Tonhao = Macaco("Tonhão")
Tonhao.comer("maçã", "arroz")
Tonhao.verBucho()
Babu.comer("banana", Tonhao)
Babu.verBucho()

