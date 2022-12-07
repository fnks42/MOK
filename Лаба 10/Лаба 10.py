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
def phi(n: int) -> int:
    result = n
    i = 2
    while i**2 < n:
        while n % i == 0:
            n /= i
            result -= result / i
        i += 1
    if n > 1:
        result -= result / n
    return int(result)

r1 = 185
r2 = 242
x = 164
p1 = int(input('Введите p1 '))
p2 = int(input('Введите p2 '))
k2 = int(input('Введите k2 '))
w = int(input('Введите w '))


u1 = (pow(r2,phi(p2)-1)*x)%p2
print('u1= ',u1)
u2 = (pow(r2,phi(p2)-1)*r1)%p2
print('u2= ', u2)
V = ((((w**u1)*(k2**u2))%p1)%p2)
print('V=r1= ', V)
if V == r1:
    print("Подпись найдена ")
else:
    print('Не найдена')