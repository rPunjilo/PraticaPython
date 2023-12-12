print("Login FATEC Americana")
print("")
print("")
print("")

ra_meu = '004321123'
senha_meu = '1234567'



ra_dec = input("Digite o seu RA: ")
senha_dec = input("Digite a sua senha: ")

if ra_dec == ra_meu and senha_dec == senha_meu:
    print("O RA e a senha digitados conferem com o definido")
else:
    print("O RA ou a senha digitados não conferem com o definido")

