# find the product of number


def product(n):
    if n == 0:
        return 1
    return (n % 10) * product(n // 10)

print(product(123))   # Output: 6
