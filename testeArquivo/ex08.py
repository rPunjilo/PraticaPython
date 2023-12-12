with open("textoEX07.txt", 'r') as a:
   with open("ex08.txt", 'w') as b:
      x = a.read()
      b.write(f'{x}\n')

with open("ex02.txt", 'r') as c:
   with open("ex08.txt", 'a') as d:
      for i in c.read():
         d.write(i)