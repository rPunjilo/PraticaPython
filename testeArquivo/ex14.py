import datetime
date = datetime.date.today()
year = date.year


with open('textoex13.txt', 'r') as a:
    with open('ex14.txt', 'w') as b:
        for i in a.readlines():
            v = i.rstrip("\n")
            ano = int(v[-4:])
            x = year - ano
            if x < 18:
                age = "Underage"
            elif x == 18:
                age = "Entering the legal age"
            else:
                age = "an Adult"
            name = str(v[:-11])
            b.write(f"{name} is {age}\n")