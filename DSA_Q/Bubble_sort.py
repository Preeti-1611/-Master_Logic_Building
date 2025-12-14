#bubble sort
# n=int(input("entera number"))
# arr=[]

# for i in range(n):
#     n=int(input('enter a number'))
#     arr.append(n)
# print("the array is",arr)

arr = [4,62,6,3,7,9]
for i in range(len(arr)-1):
    for j in range(len(arr)-i-1):       
        if arr[j]>arr[j+1]:
          arr[j],arr[j+1]=arr[j+1],arr[j]

print(arr)


