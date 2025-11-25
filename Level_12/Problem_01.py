# array phase 3. Input n and take n integers into an array; print them

n = int (input ("entera number elements u want to enter"))

arr = []


for i in range(n):
    m = int(input(f"enter the {i+1} element"))
    arr.append(m)

print(arr)

