# Remove duplicates from a list

arr = [1, 2, 2, 3, 4, 4]
unique = []

for num in arr:
    if num not in unique:
        unique.append(num)

print(unique)


# arr = [1, 2, 2, 3, 4, 4]
# unique = list(set(arr))
# print(unique)
