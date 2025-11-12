# Take a 3-digit number and check if the sum of the first and last digit equals the middle
# digit

list =[]

for i in range(1,4):
    n = int(input(f"enter the number {i}:"))
    list.append(n)
print(list)
sum =0
sum = list[0]+list[2]

if sum ==list[1]:
    print("Yes its working")
else:
    print(" No its not working")

