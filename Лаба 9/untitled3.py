b = []
c = []
d = []
Z = 1331
for i in range(2, 30):
    a=(i**605)%Z
    b.append(a)
print(*b, sep = '\t')

for i in range(2, 30):
    a=(i**242)%Z
    c.append(a)
print(*c, sep = '\t')

for i in range(2, 30):
    a=(i**110)%Z
    d.append(a)
print(*d, sep = '\t')