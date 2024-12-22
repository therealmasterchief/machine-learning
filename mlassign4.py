def calculate_nxm(n, m):
    print(f"Calculating {n} x {m} with iterations:")
    iterations = 0  
    for i in range(n):
        for j in range(m):
            iterations += 1
    print(f"Total iterations: {iterations}")
    

# Example Usage
n = 5
m = 6
calculate_nxm(n, m)