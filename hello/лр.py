import math
def create_mass():
    a=float(input('Введіть початок діапазону '))
    b=float(input('Введіть кінець діапазону '))
    h=float(input('Введіть крок діапазону '))
    k=0
    t=a
    m=[]
    xx=[]
    while(t<=b):
        if t<=0:
            m.append(math.sin(t)*math.sin(t/2))
        else:
            m.append(math.sin(t**3)-math.sin(t))
            k+=1
            xx.append(t)
            t+=h
    return m,xx,k
def print_mass(xx,m,k):
    for i in range(0,k):
        print(xx[i], ' ',m[i])
        


def found_min(m,k):
    imin=0
    for i in range(0,k):
        if m[i]<m[imin]:
            imin=i
        print('Мінімальний елемент= ',m[imin],'Його номер= ',imin+1)
        return imin


def found_max(m,k):
    imax=0
    for i in range(0,k):
        if m[i]>m[imax]:
            imax=i
    print('Максимальний елемент',m[imax],'Його номер',imax+1 )
    return imax 


def sum(m,a,b):
    if b<a:
        k=a
        a=b
        b=k
    summa=0
    for i in range(a+1,b):
        summa+=m[i]
    print('Сумма між максимальним і мінімальним елементом', summa)
        


#main program
y=[]
x=[]
y,x,n=create_mass()
print_mass(x,y,n)
imn=found_min(y,n)
imx=found_max(y,n)
sum(y,imn,imx) 



        
        