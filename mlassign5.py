def get_rightmost_set_bit(num):
    if num == 0:
        return 0  
    return num & -num

number = int(input("Enter a number"))
result = get_rightmost_set_bit(number)
print(f"The value of the rightmost set bit in {number} (binary {bin(number)}) is {result}.")
