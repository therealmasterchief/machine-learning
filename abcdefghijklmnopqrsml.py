def swap(x,y):
    x= x^y
    y= x^y
    x= x^y
    print("after swapping x= ", x,"y= ",y)
def swap2(x,y):
    x=(x&y)+(x|y)
    y= x+(~y)+1
    x= x+(~y)+1
    print("after swapping, x= ",x,"y= ", y)
swap(1,2)
swap2(1,2)