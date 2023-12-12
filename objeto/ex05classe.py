class Conta_Corrente:
    def __init__(self, numero, nome, saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        if novo_nome == self.nome:
            raise Exception("É o mesmo nome meu nobre")
        else:
            self.nome = novo_nome
            return print(f"O nome foi trocado para {self.nome}")

    def deposito(self, valor):
        self.saldo += valor
        print(f"Realizando o depósito de {valor}")
        return print(f"O saldo agora é de {self.saldo}")
    
    def saque(self, sacar):
        if self.saldo == 0:
            print("O saldo da conta está zerado")
        elif self.saldo - sacar:
            print("O saldo da conta é menor do que o valor a ser sacado")
        else:
            self.saldo -= sacar
            return print(f"O saldo agora é de {self.saldo}")
        

numero = int(input("Digite o número da conta: "))
nome = input("Digite o nome do titular: ")
saldo = float(input("Digite o saldo do titular: "))
conta1 = Conta_Corrente(numero, nome, saldo)

conta1.alterar_nome("Raimundo")
conta1.deposito(1000)
conta1.saque(1500)