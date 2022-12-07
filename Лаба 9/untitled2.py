b = []
c = []
d = []
Z = 601
for i in range(2, 30):
    a=(i**300)%Z
    b.append(a)
print(*b, sep = '\t')

for i in range(2, 30):
    a=(i**200)%Z
    c.append(a)
print(*c, sep = '\t')

for i in range(2, 30):
    a=(i**120)%Z
    d.append(a)
print(*d, sep = '\t')


