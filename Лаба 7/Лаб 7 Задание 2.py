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
    q1=int(input("введите q1:"))
    lst=gensimple(q1+1)
    #q1=lst[q1-1]
    n=int(input("введите N"))
    fepr=fe(n)   
    return(n,fepr,q1)

def podbor(n,q1,ltext):
    count=0
    elem=(ltext**q1)%n
    while not( elem == ltext):
        elem=(elem**q1)%n
        count+=1
    return(count)
           
def decode():
    n,fepr,q1=inputt()
    print("q1 = ",q1)
    print("N=",n)
    print("func el ot proizv: ",fepr)
    listtext = list(map(int, input().split(",")))
    print(listtext)
    elem=listtext[2]
    stp=podbor(n,q1,elem)
    print("stp= ",stp)    
    dectext=[]
    for i in listtext:
        l0=i
        for _ in range(stp):
            l0=(l0**q1)%n 
        dectext.append(dist2[l0])
    print(dectext)
    return()

decode()