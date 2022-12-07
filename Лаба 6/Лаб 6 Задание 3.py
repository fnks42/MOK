dist1={'а':1,'б':2,'в':3,'г':4,'д':5,'е':6,'ж':7,'з':8,'и':9,'к':10,'л':11,'м':12,'н':13,'о':14,'п':15,'р':16,'с':17,'т':18,'у':19,'ф':20,'х':21,'ц':22,'ч':23,'ш':24,'щ':25,'ы':26,'ь':27,'э':28,'ю':29,'я':30,'_':31}
dist2={1:'а',2:'б',3:'в',4:'г',5:'д',6:'е',7:'ж',8:'з',9:'и',10:'к',11:'л',12:'м',13:'н',14:'о',15:'п',16:'р',17:'с',18:'т',19:'у',20:'ф',21:'х',22:'ц',23:'ч',24:'ш',25:'щ',26:'ы',27:'ь',28:'э',29:'ю',30:'я',31:'_'}
a=[[14,5,13],[1,10,14],[0,13,6]]
b=[[],[],[]]

def matumn(a,b):
    summ=0
    c=[]
    for i in range(len(a)):
        for j in range(len(b[i])):
            for k in range(len(b)):
                summ+=(a[i][k]*b[k][j])
                
            summ=summ%31
            c.append(summ)
            summ=0
    return(c)

def decode(origtext, dist1=dist1, dist2=dist2):
    dectext=[] 
    listtext=[[[],[],[]] for i in range(int(len(origtext)/3))]
    k=0
    for i in range(len(listtext)):
        for j in range(3):
            listtext[i][j].append((dist1[origtext[k]]-bb[j]))
            k+=1   
    print(listtext)
    ck=0
    for i in range(len(listtext)):
        dectext.append(matumn(obr, listtext[i]))
        ck+=1
    print("готовый текст  ", dectext)    
    bukvtext=""
    for i in range(len(dectext)):
        for j in range(3):
            if dectext[i][j]==0:
                bukvtext+="_"
                continue
            bukvtext+=dist2[dectext[i][j]]
    print(bukvtext)    
    return()

print("введите обратную матрицу: ")
obr=[[] for i in range(3)]
bb=[]
for i in range(3):
    for j in range(3):
        obr[i].append(int(input()))
print("введите В  ")
for i in range(3):
    bb.append(int(input()))
print(obr)
origtext=input("Введите текст для декодирования ")
while not(len(origtext)%3==0):
    origtext+="_" 
print(origtext)    
decode(origtext, dist1=dist1, dist2=dist2)




    