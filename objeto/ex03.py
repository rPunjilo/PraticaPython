import ex03classe

Comp_Larg = int(input("Digite o valor do comprimento/largura: "))
Base_Larg = int(input("Digite o valor da base/altura: "))
retangulo = ex03classe.Retangulo(Comp_Larg,Base_Larg)
retangulo.retornar()
retangulo.area()
retangulo.perimetro()
trocar = input("Você deseja trocar o valor de alguma medida? Sim ou não: ").lower()
if trocar == "sim":
    opcao = input("Qual medida? ")
    valor = int(input("Qual o valor? "))
    retangulo.mudar(opcao, valor)

retangulo.retornar()