def get_indices(lst, el):
    return [i for i in range(len(lst)) if lst[i] == el]
a= 8
b = 1
p = 17
delta = -16*(4*a**3+27*b**2)
print('Дискриминант= ', delta)
z = 0
x = []
q = []
y = []
m = []
for i in range(p):
    z = (i**3+a*i+b)%p
    x.append(z)
    m.append(i)
print(*m, sep = '\t')
print(*x, sep = '\t')

print()
for i in range(p):
    z = (i**2)%p
    q.append(z)
    
print(*m, sep = '\t')
print(*q, sep = '\t')
print()
for i in x:
    if i in y:
        continue
    for j in q:
        if i == j:
            y.append(i)
            break
al = []
print(sorted(y))
for i in range(len(y)):
        al.append(get_indices(q, y[i]))
print(al)
    