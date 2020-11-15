c = open('file.txt')

print(c.read())
 

c = open('file.txt','a')
c.write(' tomasss ')

c = open('file.txt')
print(c.read())


