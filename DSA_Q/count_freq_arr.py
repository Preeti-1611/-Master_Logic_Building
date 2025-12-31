#count the fequency of element in an array

# arr = [2, 3, 2, 5, 3, 2]

# frequency = {}       # empty dictionary to store counts

# for num in arr:
#     if num in frequency:
#         frequency[num] += 1   # increase the count
#     else:
#         frequency[num] = 1    # add number with count 1

# print(frequency)

# using hashmap

num = [3,4,2,3,3,8,6,4]

hash_map = {}
n = len(num)
for i in range(0,n):
    hash_map[num[i]] = hash_map.get(num[i],0)+1

print(hash_map)







# arr = [2, 5, 2, 7, 2, 5]

# x = 2
# count = 0

# for i in arr:
#     if i == x:
#         count += 1

# print(count)   # Output: 3

