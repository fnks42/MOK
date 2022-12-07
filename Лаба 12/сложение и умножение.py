def sumX():
    x1 = 7
    y1 = 10
    x2 = 40
    y2 = 8
    Z = 43
    b = (y2-y1)**2
    b1 = (x2-x1)**2
    z = ((b*b1**(Z-2) )-x2-x1)%Z
    return z

def sumY():
    x1 = 7
    y1 = 10
    x2 = 40
    y2 = 8
    Z = 43
    x3 = 27
    b = y2-y1
    b1 = x2 -x1
    b3 = b*b1**(Z-2)
    b4 = b3*(x1-x3)-y1
    b4 = b4%Z
    return b4

def proizvX():
    x1 = 81
    y1 = 113
    a = -6
    Z = 233
    b1= (3*x1**2+a)**2
    b2=(2*y1)**2
    X3 = b1*b2**(Z-2) - 2*x1
    X4 = X3%Z
    return X4
    
def proizvY():
    x1 = 81
    y1 = 113
    a = -6
    Z = 233
    x3 = 63
    b1=3*x1**2+a
    b2=2*y1
    b3 = b1*b2**(Z-2)
    b4 = b3*(x1-x3)-y1
    b4 = b4%Z
    return b4
print('Сумма')
print('x= ',sumX())
print('y= ',sumY())
print()
print('Произведение')
print(proizvX())
print(proizvY())


