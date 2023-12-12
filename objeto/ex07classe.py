class Bichinho:
    def __init__(self,nome, saude, fome, idade):
        self.nome = nome
        self.saude = saude
        self.fome = fome
        self.idade = idade

    def retorno(self):
        print("")
        print(f"O nome do Tamagushi é {self.nome}")
        print(f"O Tamagushi está {self.saude}")
        print(f"O Tamagushi está {self.fome}")
        print(f"O Tamagushi está com {self.idade} anos")
        if self.saude == "doente" and self.fome == "com fome":
            return print("O Tamagushi está morrendo")
        if self.saude == "doente" and self.fome == "sem fome":
            return print("O Tamagushi está bravo")
        if self.saude == "saudável" and self.fome == "com fome":
            return print("O Tamagushi está bravo")
        if self.saude == "saudável" and self.fome == "sem fome":
            return print("O Tamagushi está feliz")

    def mudar_nome(self):
        novo_nome = str(input("Digite o novo nome: "))
        while novo_nome == self.nome:
            print("O nome do Tamaguchi é igual a este")
        self.nome = novo_nome

    def mudar_fome(self):
        opcao = str(input("O Tamagushi está com fome? ").lower())
        if opcao == "sim" or opcao == "s":
            novo_fome = "com fome"
        if opcao == "nao" or opcao == "n":
            novo_fome = "sem fome"
        while novo_fome == self.fome:
            print("A situação do Tamaguchi é a mesma")
        self.fome = novo_fome

    def mudar_saude(self):
        opcao = str(input("O Tamagushi está saudável? ").lower())
        if opcao == "sim" or opcao == "s":
            novo_saude = "saudável"
        if opcao == "nao" or opcao == "n":
            novo_saude = "doente"
        while novo_saude == self.saude:
            print("A situação do Tamaguchi é a mesma")
        self.saude = novo_saude

    def mudar_idade(self):
        novo_idade = int(input("Digite a nova idade: "))
        while novo_idade == self.idade:
            print("A idade do Tamaguchi é a mesma")
        self.nome = novo_idade
        



nome = str(input("Qual o nome do Tamaguchi? "))
idade = int(input("Qual é a idade do Tamaguchi? "))
opcao1 = input("O Tamagushi está saudável? ").lower()
if opcao1 == "sim" or opcao1 == "s":
    saude = "saudável"
if opcao1 == "nao" or opcao1 == "n":
    saude = "doente"
opcao = str(input("O Tamagushi está com fome? ").lower())
if opcao == "sim" or opcao == "s":
    fome = "com fome"
if opcao == "nao" or opcao == "n":
    fome = "sem fome"
tama = Bichinho(nome, saude, fome, idade)
tama.retorno()
print("")


check = True  
while check == True:   
    resp = str(input("Deseja continuar? ").lower()) 
    if resp == "sim" or resp == "s":
        print("")
        print("N == Nome; I == Idade; S == Saúde; F == Fome")
        opcao3 = str(input("O que você deseja mudar? ")).upper()
        if opcao3 == 'N':
            tama.mudar_nome()
        if opcao3 == 'I':
            tama.mudar_idade()
        if opcao3 == "S":
            tama.mudar_saude()
        if opcao3 == 'F':
            tama.mudar_fome()
        tama.retorno()
    else:    
        check = False
        break
    





