
def Checkifsame(number1,number2):
    if(number1 ^ number2 !=0):
        print("numbers are not equal")
    else:
        print("Numbers are equal")
n1 =int(input("1st number: "))
n2 =int(input("2nd number:"))
Checkifsame(n1,n2)