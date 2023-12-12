primeira = float; segunda = float; media = float

primeira = float(input("Digite a primeira nota: "))

while primeira < 0 or primeira > 10:
    primeira = float(input("Valor invalido! Tente novamente: "))

segunda = float(input("Digite a segunda nota: "))

while segunda < 0 or segunda > 10:
    segunda =  float(input("Valor invalido! Tente novamente: "))

media = (primeira + segunda) / 2
print(f"MEDIA = {media:.2f}")