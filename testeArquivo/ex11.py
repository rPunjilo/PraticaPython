numberChar = 0
numberWord = 0
dict = {}
letters = ['a','e','i','o','u','A','E','I','O','U']
with open("ex11.txt", 'r') as a:
    for i in a.readlines():
        v = i.rstrip('\n').replace(" ", "")
        numberChar += len(v)
        numberWord += len(i.split())
    print(f"The number of characters in this file is {numberChar}")
    print(f"The number of words in this file is {numberWord}")
    
with open("ex11.txt", 'r') as b:
    c = b.readlines()
    print(f"The number of lines in this file is {len(c)}")

print("=-" * 30)
with open("ex11.txt", 'r') as c:
    d = c.read().lower()
    for i in d:
        if i in letters:
            dict.update({i: [d.count(i)]})
            
for c,i in dict.items():
    print(f"The vowel {c} has showed {i} times")
