a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a_even = (a % 2 == 0)
b_even = (b % 2 == 0)

if a_even and b_even:
    print("Both are even")
elif (not a_even) and (not b_even):
    print("Both are odd")
else:
    print("One is even and one is odd")
