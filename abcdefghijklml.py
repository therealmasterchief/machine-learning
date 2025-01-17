def Setornumber(number,n):
    if number &(1<<(n-1)):
        print("\nSet")
    else:
        print("\nNot set")

number= int(input("Enter number:"))
n= int(input("Enter bit number : "))
Setornumber(number,n)
