
# Find the first occurrence of a given number.

arr = [3,4,62,2,2,6,0,2,5,0,2]
num = int(input("enter a number to get the first occurrence"))

found = False

for i in range(len(arr)):
    if arr[i] == num:
        print("the first occurrence of the num index is", i)
        found = True
        break

if not found:
    print("number not found")



# if num in arr:
#     print(arr.index(num))
# else:
#     print("number not found")

