from math import *

y= [22850107, 149219993, 73078093, 71830496,
56242949, 82350946, 43928485, 156722642, 118469586, 49914767]
Y1 = []
Y2 = []
X1 = []
X2 = []
X3 = []
X4 = []
p1 = 17471
p2 = 9791
N = p1*p2
g1 = int(((p1+1)/4))
g2 = int(((p2+1)/4))
print(g1)
for i in range(len(y)):
    y1 = (y[i]**g1)%p1
    y2 = (y[i]**g2)%p2
    Y1.append(y1)
    Y2.append(y2)
#Коэффициенты Безу
a1 = 4652
a2 = -8301
for i in range(len(y)):
    x1 = (-p1*a1*Y2[i]+p2*a2*(Y1[i]))%N
   
    X1.append(x1)
print(X1)

for i in range(len(y)):
    x2 = (-p1*a1*Y2[i]-p2*a2*Y1[i])%N
    
    X2.append(x2)
print(X2)

for i in range(len(y)):
    x3 = (p1*a1*Y2[i]-p2*a2*Y1[i])%N
    
    X3.append(x3)
print(X3)

for i in range(len(y)):
    x4 = (p1*a1*Y2[i]+p2*a2*Y1[i])%N
    
    X4.append(x4)
print(X4)