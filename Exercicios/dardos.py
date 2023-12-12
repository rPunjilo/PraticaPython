a = float; b = float; c = float

print("Digite as tres distancias: ")
a = float(input())
b = float(input())
c = float(input())

if a > b and a > c:
    print(f"Maior distancia: {a:.2f}")
elif b > a and b > c:
    print(f"Maior distancia: {b:.2f}")
else:
    print(f"Maior distancia: {c:.2f}")