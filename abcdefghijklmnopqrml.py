def computerpower(x,y):
    res=1
    while(y>0):
        if(y%2==0):
            x=x*x
            y>>=1
        else:
            res = res * x
            y=y-1
    return res
x=int(input("Enter x for x^y"))
y=int(input("Enter y for x^y"))
print("total:",(computerpower(x,y)))