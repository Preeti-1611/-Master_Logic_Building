# Find the minimum element in an array.
# 

arr = [4,5,7,3,2,0]

min = arr[0]

for i in arr:
    if i<min:
       min = i

print(min)