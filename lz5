#z3
from math import gcd

dist1={'а':1,'б':2,'в':3,'г':4,'д':5,'е':6,'ж':7,'з':8,'и':9,'к':10,'л':11,'м':12,'н':13,'о':14,'п':15,'р':16,'с':17,'т':18,'у':19,'ф':20,'х':21,'ц':22,'ч':23,'ш':24,'щ':25,'ы':26,'ь':27,'э':28,'ю':29,'я':30,'_':31}
dist2={0:'_',1:'а',2:'б',3:'в',4:'г',5:'д',6:'е',7:'ж',8:'з',9:'и',10:'к',11:'л',12:'м',13:'н',14:'о',15:'п',16:'р',17:'с',18:'т',19:'у',20:'ф',21:'х',22:'ц',23:'ч',24:'ш',25:'щ',26:'ы',27:'ь',28:'э',29:'ю',30:'я',31:'_'}

def gensimple(n):
    lst=[2]
    i=3
    count=0
    while count<n:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            lst.append(i)
            count+=1
        i+=1
    return(lst[n-1])

def decrypt():
    text=list(input('введите текст  '))
    numtext=[] 
    for i in text:
        numtext.append(dist1[i])
    print(numtext)
    q1=gensimple(int(input('Введите Q1  ')))
    print('Находим Q2=31-Q1')
    q2=(31-q1)%31
    decnumtext=[]
    for i in numtext:
        decnumtext.append(dist2[(i+q2)%31])
    print(*decnumtext)
    return 
decrypt()
#z2
from math import gcd

dist1={'а':1,'б':2,'в':3,'г':4,'д':5,'е':6,'ж':7,'з':8,'и':9,'к':10,'л':11,'м':12,'н':13,'о':14,'п':15,'р':16,'с':17,'т':18,'у':19,'ф':20,'х':21,'ц':22,'ч':23,'ш':24,'щ':25,'ы':26,'ь':27,'э':28,'ю':29,'я':30,'_':31}
dist2={0:'_',1:'а',2:'б',3:'в',4:'г',5:'д',6:'е',7:'ж',8:'з',9:'и',10:'к',11:'л',12:'м',13:'н',14:'о',15:'п',16:'р',17:'с',18:'т',19:'у',20:'ф',21:'х',22:'ц',23:'ч',24:'ш',25:'щ',26:'ы',27:'ь',28:'э',29:'ю',30:'я',31:'_'}

def gensimple(n):
    lst=[2]
    i=3
    count=0
    while count<n:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            lst.append(i)
            count+=1
        i+=1
    return(lst[n-1])

def decrypt():
    text=list(input('введите текст  '))
    numtext=[] 
    for i in text:
        numtext.append(dist1[i])
    print(numtext)
    a=gensimple(int(input('Для генерации a=P(n) введите n:  ')))
    print(f'a={a}')
    print('Находим A:    A*a=1(mod 31)')
    A=(a**29)%31
    print('A = ',A)
    decnumtext=[]
    for i in numtext:
        decnumtext.append(dist2[(i*A)%31])
    print(*decnumtext)
    return 
decrypt()

#z3
from math import gcd

dist1={'а':1,'б':2,'в':3,'г':4,'д':5,'е':6,'ж':7,'з':8,'и':9,'к':10,'л':11,'м':12,'н':13,'о':14,'п':15,'р':16,'с':17,'т':18,'у':19,'ф':20,'х':21,'ц':22,'ч':23,'ш':24,'щ':25,'ы':26,'ь':27,'э':28,'ю':29,'я':30,'_':31}
dist2={0:'_',1:'а',2:'б',3:'в',4:'г',5:'д',6:'е',7:'ж',8:'з',9:'и',10:'к',11:'л',12:'м',13:'н',14:'о',15:'п',16:'р',17:'с',18:'т',19:'у',20:'ф',21:'х',22:'ц',23:'ч',24:'ш',25:'щ',26:'ы',27:'ь',28:'э',29:'ю',30:'я',31:'_'}

def gensimple(n):
    lst=[2]
    i=3
    count=0
    while count<n:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            lst.append(i)
            count+=1
        i+=1
    return(lst[n-1])

def fe(ch):
    count=0
    for i in range(ch):
        if (gcd(ch,i)==1):
            count+=1
    return(count)

def decrypt():
    text=list(input('введите текст  '))
    numtext=[] 
    print('Используем формулу: x=(a^(φ(n)-1))*(y-b)(mod p )')
    for i in text:
        numtext.append(dist1[i])
    print(numtext)
    a,b=gensimple(int(input('p for a: '))),gensimple(int(input('p for b: ')))
    print(f'a={a}, b={b}')
    decnumtext=[]
    for i in numtext:
        decnumtext.append(dist2[((a**29)*(i-b))%31])
    print(*decnumtext)
    return 
decrypt()
