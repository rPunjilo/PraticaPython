
with open("ex04.txt", 'r') as a:
    with open ("ex06.txt", 'w') as b:
        for i in a.readlines():
            b.write(i)

with open("ex06.txt", 'r') as c:
    file = c.read()
    
d = open("ex06.txt", 'w') 
d.write(file.replace("a", "*").replace('e', "*").replace('i','*').replace('o', "*").replace("u", "*"))
d.close()

            
    


