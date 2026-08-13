def sum_N_Numbers (n):
    if n <= 1:
        return n 
    else:
        return sum_N_Numbers(n-1) + n

print("Sum of N Numbers:")
print(sum_N_Numbers(5))