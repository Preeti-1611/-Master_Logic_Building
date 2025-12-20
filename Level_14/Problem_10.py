# Find the last occurrence of a given number.


arr = [3,4,6,1,2,9,3,5]
num = int(input("enter a number"))

position = -1   # means "not found"

for i in range(len(arr)):
    if arr[i] == num:
        position = i

if position != -1:
    print("the last occurrence index is", position)
else:
    print("number not found")
