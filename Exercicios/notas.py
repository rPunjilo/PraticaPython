primeira = float; segunda = float; final = float

primeira = float(input("Digite a primeira nota: "))
segunda = float(input("Digite a segunda nota: "))

final = primeira + segunda

print(f"NOTA FINAL = {final}")

if final < 60.0:
    print("REPROVADO")
