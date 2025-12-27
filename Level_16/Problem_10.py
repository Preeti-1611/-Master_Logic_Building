# Find sum of digits of a number recursively.

def  sum_digit(n):
    if n==0:
        return 
    return n%10+sum_digit(n//10)

print(sum_digit(53))

