# Calculate power of a number (xⁿ) using recursion
def power(x, n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    return x * power(x, n - 1)

# Input
x = int(input("Enter base number: "))
n = int(input("Enter power: "))

# Output
print("Result:", power(x, n))
