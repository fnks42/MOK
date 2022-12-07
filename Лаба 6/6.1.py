dist1={'а':1,'б':2,'в':3,'г':4,'д':5,'е':6,'ж':7,'з':8,'и':9,'к':10,'л':11,'м':12,'н':13,'о':14,'п':15,'р':16,'с':17,'т':18,'у':19,'ф':20,'х':21,'ц':22,'ч':23,'ш':24,'щ':25,'ы':26,'ь':27,'э':28,'ю':29,'я':30,'_':31}
dist2={1:'а',2:'б',3:'в',4:'г',5:'д',6:'е',7:'ж',8:'з',9:'и',10:'к',11:'л',12:'м',13:'н',14:'о',15:'п',16:'р',17:'с',18:'т',19:'у',20:'ф',21:'х',22:'ц',23:'ч',24:'ш',25:'щ',26:'ы',27:'ь',28:'э',29:'ю',30:'я',31:'_'}
key=[]
def decode(dist1=dist1, dist2=dist2):
    dectext=""
    text=input("введите текст для декодирования  ")
    for i in range(0,len(text)):
        if((dist1[text[i]]-key[i%5])%31==0):
            dectext+="_"
            continue
        else:
            dectext+=(dist2[(dist1[text[i]]-key[i%5])%31])    
    print('Поочередно прибавляем к тексту ключ')
    return dectext
def incode(dist1=dist1, dist2=dist2):
    inctext=""
    text=input("введите текст для кодирования ")
    for i in range(0,len(text)):
        if((dist1[text[i]]+key[i%5])%31==0):
            inctext+="_"
            continue
        else:
            inctext+=(dist2[(dist1[text[i]]+key[i%5])%31])  
    return inctext
s=input("Введите криптоключ  ")
for i in range(0,len(s)):
    key.append(dist1[s[i]])
print(key)
a=input("выберите операцию: [0]кодирование   [1]декодирование")
if a=="0":
    print(incode())
elif a=="1":
    print(decode())  
    