lis = []
sum = 0

with open('ex15.txt', 'r') as a:
    for i in a.readlines():
        v= i.rstrip('\n')
        lis.append(v[-5:])
        
for i in lis:
    x = i.replace(" ", "")
    sum += float(x)
    
print(f"The total purchase was {sum} reais.")