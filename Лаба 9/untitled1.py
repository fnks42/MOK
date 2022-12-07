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


a = 6
print(gensimple(a)[-2])

