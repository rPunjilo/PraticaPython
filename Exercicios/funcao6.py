
def conversor(x):
    s = x - 12
    return (f"São {s:.2f} p.m")

def horas(x, periodo):
    if periodo == "A":
        return (f"São {x:.2f} a.m")
    elif periodo == "P":
        return conversor(x)
    
while True:
    x = float(input("Digite as horas: "))
    if x < 12:
        periodo = "A"
    else:
        periodo = "P"
    print(horas(x, periodo))
    r = str(input("Deseja continuar? [S/N] "))
    if r in "Nn":
        break
