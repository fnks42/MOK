def get_indices(lst, el):
    return [i for i in range(len(lst)) if lst[i] == el]
a=  1
b = 8
p = 43
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
print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Это массив x')
print(*m, sep = '\t')
print(*x, sep = '\t')

print()
for i in range(p):
    z = (i**2)%p
    q.append(z)
print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t Это массив y')   
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
print(get_indices(q, 4))
print('Общие элементы', sorted(y))