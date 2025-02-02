def longest_consecutive_ones(n):
    max_count = 0
    current_count = 0

    while n > 0:
        if n & 1: 
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0 

        n >>= 1  

    return max_count

num =int(input("enter a number"))
print(longest_consecutive_ones(num))