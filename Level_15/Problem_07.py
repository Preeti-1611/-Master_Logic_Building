# Replace all even numbers with 1 and all odd with 0


arr = [3,2,4,9,5,2,4,5,7]

for i in range(len(arr)):
    if arr[i]%2==0:
        arr[i]=1
    else :
        arr[i]=0

print(arr)