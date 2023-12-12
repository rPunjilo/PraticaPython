x = int; y = int

print("Digite dois números: ")
x = int(input())
y = int(input())

while x != y:
    if x > y:
        print("Decrescente")
    else:
        print("Crescente")
    print("Digite outros dois numeros: ")
    x = int(input())
    y = int(input())