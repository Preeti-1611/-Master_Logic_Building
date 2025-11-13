# fibonacci series sum of n terms
n = int(input("Enter how many terms you want: "))

a = 0
b = 1
sum = 0

print("Fibonacci Series:")

for i in range(n):
    print(a)
    sum+=a
    c = a + b
    a = b
    b = c
    
print(sum)