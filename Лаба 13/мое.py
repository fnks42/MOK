import re
massiv = [[104,70], [128,350], [134,140], [38,255], [134,140], [329,26], [201,66], [190,314],
[80,10], [38,255], [281,38], [150,18], [329,26], [105,89], [190,314], [346,73], [190,314],
[4,4], [104,70], [190,314], [80,10], [38,255], [163,97], [276,103], [115,365], [150,18],
[80,10], [38,255], [201,66], [190,314], [134,140], [190,314], [346,73], [329,26], [182,255],
[38,255], [104,70], [128,350], [38,255], [276,264], [115,365], [134,140], [346,73], [128,350],
[270,68], [329,26], [150,18], [329,26], [38,255], [281,38], [276,103], [38,255], [115,365],
[190,314], [270,68], [269,233], [115,365], [134,140], [276,264], [80,10], [182,255]]

 

massive_cod = []
massive_decode =[]
fraza = []
P=[262,287]
Z = 367
k = 8
a = -13
x1, x2 = P[0], P[0]
y1, y2 = P[1], P[1]

rezervX = x2
rezervY = y2

for i in range(1, 3):
    B1= (3*x1**2+a)**2
    B2=(2*y1)**2
    X3 = B1*B2**(Z-2) - 2*x1
    X4 = X3%Z
    x33 = X4
    b17=3*x1**2+a
    b27=2*y1
    b33 = b17*b27**(Z-2)
    b44 = b33*(x1-x33)-y1
    b44 = b44%Z
    x1 = X4
    x2 = X4
    y1 = b44
    y2 = b44
    print(i+i,'P(x)= ',X4)
    print(i+i,'P(y)= ',b44)
    print()
    if i == 2:
        for i in range(1):
                x2 = rezervX
                y2 = rezervY
                b = (y2-y1)**2
                b1 = (x2-x1)**2
                z = ((b*b1**(Z-2) )-x2-x1)%Z
                x3 = z
                b11 = y2-y1
                b12 = x2 -x1
                b3 = b11*b12**(Z-2)
                b4 = b3*(x1-x3)-y1
                y3 = b4%Z
                print('5P(x)= ', x3)
                print('5P(y)= ', y3)
                print()
                x1 = x3
                y1 = y3

for i in range(len(massiv)):
    y2= -3
    y1 = massiv[i][1]
    x2 = 116
    x1 = massiv[i][0]
    b = (y2-y1)**2
    b1 = (x2-x1)**2
    z = ((b*b1**(Z-2) )-x2-x1)%Z
    massive_cod.append(z)

print('Результат вычета подсказки из второй точки: ')
print(massive_cod)

def get_decimcal(n: float) -> float:
    return float(re.search(r'\.\d+', str(n)).group(0))

def get_count(number):
    s = str(number)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0

for i in range(len(massive_cod)):
    t = (massive_cod[i])
    massive_decode.append(t)

n = 0
x1 = 0
i = 0
while n < len(massive_cod):
    x1 = (massive_decode[n]-i)/k
    i = i +1
    if (get_decimcal(x1) == 0):
        fraza.append(x1)
        n = n+1
        i = 0

for i in range(len(fraza)):
    fraza[i] = int(fraza[i])
print()
print('Декодирование будет происходить по алгоритму в котором мы извлекаем целое число')
print(fraza)
print()
n = fraza
b1 = []
dist2={0:'_', 1:'а',2:'б',3:'в',4:'г',5:'д',6:'е',7:'ж',8:'з',9:'и',10:'к',11:'л',12:'м',13:'н',14:'о',15:'п',16:'р',17:'с',18:'т',19:'у',20:'ф',21:'х',22:'ц',23:'ч',24:'ш',25:'щ',26:'ы',27:'ь',28:'э',29:'ю',30:'я',31:'_'}
for i in range(len(n)):
    s = ((n[i]))
    g = dist2.get(s, '#')
    b1.append(g)
print('В сообщении надо подставиь каждому значению свой символ из таблицы')
print (*b1, sep = " ")






