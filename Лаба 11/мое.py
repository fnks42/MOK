p1 = 2663
p2 = 1331
w = 2
k1 = 19
t = 17
x = 106
r1 = ((w**t)%p1)%p2
print('r1= ',r1)
r2 = (t*x+k1*r1)%p2
print('r2= ',r2)

k2 = (w**k1)%p1
print('k2= ', k2)


y = (pow(x, 1209))%p2
print('y= ',y)
u1 = ((p2-r1)*y)%p2
print('u1= ',u1)
u2 = (r2*y)%p2
print('u2= ',u2)
z = (((w**u2)*(k2**u1))%p1)%p2
print('z= ',z)
if z == r1:
    print("Совпадает")
else:
    print('Считай заново')