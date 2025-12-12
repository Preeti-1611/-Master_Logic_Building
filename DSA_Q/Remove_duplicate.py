# remove diplicate elemnts in the array


arr = [2, 3, 2, 5, 3, 2]

unique = list(set(arr))
print(unique)



arr = [2, 3, 2, 5, 3, 2]

result = []
for num in arr:
    if num not in result:   # check if already added
        result.append(num)

print(result)
