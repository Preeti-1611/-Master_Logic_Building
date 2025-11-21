# Find the largest element in an array

arr = [3, 5, 1, 9, 2]

largest = arr[0]    # assume first element is largest

for num in arr:
    if num > largest:
        largest = num

print("Largest element is:", largest)



# arr = [3, 5, 1, 9, 2]
# print("Largest element is:", max(arr))


arr = [3, 5, 1, 9, 2]
arr.sort()
print("Largest element is:", arr[-1])
