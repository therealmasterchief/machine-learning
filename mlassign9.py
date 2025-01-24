def is_power_of_8(n):
    if n <= 0:
        return False  
    if n & (n - 1) == 0:
       
        position = 0
        while n > 1:
            n >>= 1
            position += 1
        return position % 3 == 0
    return False
x=int(input("type a number and we will check if its a power of 8 "))
print("It is",is_power_of_8(x),"that your number is a power of 8")