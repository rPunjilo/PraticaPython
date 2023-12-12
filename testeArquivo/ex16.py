biggest = 0
pos = 0
lis = []
with open('ex16.txt', 'r') as a:
    for i in a.readlines():
        v = i.replace('\n', "")
        lis.append(v)
        
for i in lis:
    x = int(i[-1:])
    if x > biggest:
        biggest = x
        pos = i
    name = pos.split()

print(f"The student with the highest grade is {name[1]}, with a grade of {biggest}")