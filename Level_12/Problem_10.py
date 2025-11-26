# Take n elements and print only those greater than a given value

n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

x = int(input("Enter the value to compare: "))

print("Numbers greater than", x, ":")
for num in arr:
    if num > x:
        print(num)
