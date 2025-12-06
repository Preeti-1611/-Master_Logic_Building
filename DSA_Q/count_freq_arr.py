#count the fequency of element in an array

arr = [2, 3, 2, 5, 3, 2]

frequency = {}       # empty dictionary to store counts

for num in arr:
    if num in frequency:
        frequency[num] += 1   # increase the count
    else:
        frequency[num] = 1    # add number with count 1

print(frequency)
