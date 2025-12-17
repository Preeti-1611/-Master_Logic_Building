


# Input n and take n integers into an array; print them.


n = int(input("enter an number element"))

arr =[]

for i in range(n+1):
    n1= int(input(f"enter the {i} element :"))
    arr.append(n1)

print(arr)