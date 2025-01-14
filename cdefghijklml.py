def no_of_bits(number):
    count=0
    while(number):
        count=count +1
        number>>=1
    print(count)
number = int(input("Enter number"))
no_of_bits(number)