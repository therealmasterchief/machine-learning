def reverseBits(n):
    res = 0
    for i in range(4): 
        bit = (n >> i) & 1  
        res = res | (bit << (3 - i)) 
    return res

no1 = int(input("Pick a number you would like to reverse: "))
if no1<=15:
    print("Your reversed number is:", reverseBits(no1))
else:
    print("please enter a number between 1 and 15")