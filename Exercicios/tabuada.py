n = int; resultado = int; 

n = int(input("Deseja a tabuada para qual valor? "))

resultado = 0

for i in range(1, 11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")

x = 4
l = 0

while l <= 10:
    print(l * x)
    l += 1
