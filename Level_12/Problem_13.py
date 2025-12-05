arr = [2, 3, 2, 5, 2, 6]
x = int(input("Enter element to count: "))

count = 0
for num in arr:
    if num == x:
        count += 1

print("Element appears", count, "times.")
