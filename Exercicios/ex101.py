import datetime

date = datetime.date.today()
year = date.year

def voto(year,ano):
    x = (year - ano)
    if x <= 15:
        return (f"Com {x} anos: NÃO VOTA")
    elif x >= 10 and x <= 65:
        return (f"Com {x} anos: VOTO OBRIGATÓRIO")
    else:
        return (f"Com {x} anos: VOTO OPCIONAL")

print("=-" * 30)
ano = int(input("Em que ano você nasceu? "))
print(voto(year,ano))