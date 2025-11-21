# Print Fibonacci series up to N terms
n = int(input("Enter the number of terms: "))

a = 0
b = 1

print(a, b, end=" ")   # first two terms

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c












# n = int(input("Enter n: "))

# a = 0
# b = 1

# for i in range(n-1):
#     c = a + b
#     a = b
#     b = c

# print("Nth Fibonacci number:", a)
