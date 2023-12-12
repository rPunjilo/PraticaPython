escala: str
tempC = float; tempF = float; C = float; F = float

escala = input("Voce vai digitar a temperatura em qual escala (C/F)? ")

if escala == 'F':
    tempF = float(input("Digite a temperatura em Fahrenheit: "))
    C = 5 / 9 * (tempF - 32)
    print(f"Temperatura equivalente em Celsius: {C:.2f}")

elif escala == 'C':
    tempC = float(input("Digite a temperatura em Celsius: "))
    F = (tempC * 9) / 5 + 32
    print(f"Temperatura equivalente em Fahrenheit: {F:.2f}")