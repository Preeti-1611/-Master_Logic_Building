x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

if x == 0 and y == 0:
    print("Both are zero (every number divides 0) — ambiguous.")
elif y != 0 and x % y == 0:
    print(f"{x} is a multiple of {y}")
elif x != 0 and y % x == 0:
    print(f"{y} is a multiple of {x}")
else:
    print("Neither is a multiple of the other.")
