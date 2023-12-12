def ficha(nome, gols):
    if nome == "":
        nome = ("<desconhecido>")
    if gols == "":
        gols = 0 
    else:
        gols = int(gols)
    return (f"O jogador {nome} fez {gols} gol(s) no campeonato.")



print("=-"*30)
nome = str(input("Nome do jogador: "))
gols = input("Número de gols: ")
print(ficha(nome,gols))