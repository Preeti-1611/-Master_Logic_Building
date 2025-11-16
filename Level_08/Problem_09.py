a = int(input("Enter first term (a): "))
r = int(input("Enter common ratio (r): "))
n = int(input("Enter number of terms (n): "))

print("The GP is:")

for i in range(n):            # loop from 0 to n-1
    term = a * (r ** i)       # Tn = a * r^(n-1)
    print(term)
