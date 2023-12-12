class Tv:
    def __init__(self, canal, volume):
        if canal >= 1 and canal <= 100:
            self.canal = canal
        else:
            raise Exception("valor do canal inválido")
        if volume >= 1 and volume <= 100:
            self.volume = volume
        else:
            raise Exception("valor do volume inválido")
        
    
    def mudar_canal(self, novo_canal):
        if novo_canal >= 1 and novo_canal <= 100:
            self.canal = novo_canal
            return print(f"O canal agora é {self.canal}")
        else:
            return print("Valor inválido")
        
    def passar_canal(self, passar):
        if passar == "+":
            if self.canal == 100:
                print("Valor máximo do canal alcançado")
            else:
                self.canal += 1
        if passar == "-":
            if self.canal == 0:
                print("Valor mínimo do canal alcançado")
            else:
                self.canal -= 1
        return print(f"O canal agora é {self.canal}")
    
    def mudar_volume(self, opcao, passar):
        if opcao == "+":
            if self.volume == 100:
                print("Valor máximo do volume alcançado")
            else:
                self.volume += passar
        if opcao == "-":
            if self.volume == 0:
                print("Valor mínimo do volume alcançado")
            else:
                self.volume -= passar
        return print(f"O volume agora é {self.volume}")
    

canal = int(input("Em que canal a TV se encontra? "))
volume = int(input("Em qual volume a TV se encontra? "))
tv = Tv(canal,volume)
print(tv.canal)
tv.mudar_canal(54)
passar = input("Você deseja aumentar ou diminuir o canal? ")
tv.passar_canal(passar)
tv.mudar_volume("+", 12)