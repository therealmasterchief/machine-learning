def printPrimes():
    for num in range(1,99): 
        is_prime = True
        for i in range(2, int(num**0.5) + 1): 
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")

print("Prime numbers with 2 digits")
printPrimes()