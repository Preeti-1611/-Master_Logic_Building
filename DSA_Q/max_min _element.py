#find the maximum element in an array

arr = []

n = int(input('enter the numer of ele u want in array'))

for i in range(n):
    a = int(input(f"enter the {i} element -"))
    arr.append(a)
print(arr)

max =arr[0]
for i in arr:
    if i>max:
      max =i
print("the maximum element =",max)


#min
min = arr[0]
for i in arr:
    if i < min:
        min = i
