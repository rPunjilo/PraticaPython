
with open("textoEX07.txt", 'r') as a:
   with open("ex07.txt", 'w') as b:
      for i in a.read():
         b.write(i)


with open("ex07.txt", 'r') as c:
    file = c.read()
    
d = open("ex07.txt", 'w')
d.write(file.replace(file,file.upper()))
d.close()