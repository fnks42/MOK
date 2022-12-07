from math import gcd
dist2={1:'а',2:'б',3:'в',4:'г',5:'д',6:'е',7:'ж',8:'з',9:'и',10:'к',11:'л',12:'м',13:'н',14:'о',15:'п',16:'р',17:'с',18:'т',19:'у',20:'ф',21:'х',22:'ц',23:'ч',24:'ш',25:'щ',26:'ы',27:'ь',28:'э',29:'ю',30:'я',31:'_',0:'_'}
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
    return(lst)

def fe(ch):
    count=0
    for i in range(ch):
        if (gcd(ch,i)==1):
            count+=1
    return(count)

def inputt():
    lst=[]
    p1,p2,p3=int(input("введите р1:")),int(input("введите р2:")),int(input("введите р3:"))
    if p1>=p2:
        lst=gensimple(p1+1)
    else:
        lst=gensimple(p2+1)
    p1,p2,q1=lst[p1-1],lst[p2-1],lst[p3-1]
    n=p1*p2
    fepr=(p1-1)*(p2-1)   
    return(p1,p2,n,fepr,q1)

def decode():
    p1,p2,n,fepr,q1=inputt()
    print("p1 = ",p1,"p2=  ",p2)
    print("N=",n)
    print("func el ot proizv: ",fepr)
    q2=(q1**(fe(fe(n))-1))%(fe(n))
    print("q2= ",q2)
     
    rowtext=input('vvedite text').split(', ')
    dectext = []
    n=p1*p2
    for i in rowtext:
        dectext.append(dist2[((int(i)**q2)%n)])
    print(dectext)
    return()

decode()