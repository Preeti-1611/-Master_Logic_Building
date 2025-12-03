#factorial numer

n = int(input("enter a number"))

fact = 1

for i in range(1,n+1):
    fact*=i
print(f"the factorial of the {n}  is = ",fact)


n = int(input("Enter a number: "))
fact = 1
i = 1

while i <= n:
    fact = fact * i
    i += 1

print("Factorial =", fact)


def factorial(n):
    if n == 0 or n == 1:   # base condition
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial =", factorial(num))

