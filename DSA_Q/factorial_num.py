#factorial numer

n = int(input("enter a number"))

fact = 1

for i in range(1,n+1):
    fact*=i
print(f"the factorial of the {n}  is = ",fact)