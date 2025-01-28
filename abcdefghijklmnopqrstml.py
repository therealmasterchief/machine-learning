def nodiv(a,b):
    sign=(-1 if((a<0)^(b<0))else 1)
    a=abs(a)
    b=abs(b)

    quotientnum= 0
    tempnum= 0
    for i in range(31, -1,-1):
        if (tempnum +(b<<i)<=a):
            tempnum += b <<i
            quotientnum |=1<<i
    if sign== -1:
        quotientnum= -quotientnum
    return quotientnum

a=int(input("Enter a for a/b\n"))
b=int(input("Enter b for a/b\n"))
print("result of",a,"/",b,"is",nodiv(a,b))