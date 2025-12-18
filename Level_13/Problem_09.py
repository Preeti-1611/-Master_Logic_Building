# Find the index of the minimum element.
arr = [3,5,7,2,4,0,-2]
min = arr[0]

for i in arr:
    if i<min:
         min = i
print("the index element of min number is ",arr.index(min))