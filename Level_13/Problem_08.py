# Find the index of the maximum element.

arr = [3,5,7,2,4]
max = arr[0]

for i in arr:
    if i>max:
         max = i
print("the index element of max number is ",arr.index(max))