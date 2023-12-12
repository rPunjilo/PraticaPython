A = []
B = []
C = []

for i in range(3):
    n = int(input("Digite os números da primeira lista: "))
    A.append(n)
    C.append(A[:])
    A.clear()

print(" ")

for i in range(3):
    x = int(input("Digite os valores da segunda lista: "))
    B.append(x)
    C.append(B[:])
    B.clear()

for i in C:
    print(i, end = "")
