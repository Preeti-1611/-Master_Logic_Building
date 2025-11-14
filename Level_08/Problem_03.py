# print the all numbers between a and b divisible by 7
a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

for i in range(a, b+1):
    if i % 7 == 0:
        print(i)
