arr = [0, 1, 2, 0, 4, 0]

count = 0
for num in arr:
    if num == 0:
        count += 1

print("Number of zeros:", count)
