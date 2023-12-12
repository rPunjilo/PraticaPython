import datetime
date = datetime.date.today()
year = date.year


with open('textoex13.txt', 'r') as a:
    for i in a.readlines():
        v = i.rstrip("\n")
        ano = int(v[-4:])
        x = year - ano
        name = str(v[:-11])
        print(f"{name} is {x} years old")

