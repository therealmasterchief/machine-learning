def power2(n):
    if(n==0):
        return 0
    if ((n &(~(n - 1)))==n):
        return 1
    return 0
number=int(input("Enter the number:"))
if(power2(number)):
    print("the number is power of 2")
else:
    print("the number is not a power of 2")