
def Checkifsame(number1,number2):
    if(number1 ^ number2 !=0):
        print("numbers are equal")
    else:
        print("Numbers are not equal")
n1 =int(input("1st number: "))
n2 =int(input("2nd number:"))
Checkifsame(n1,n2)