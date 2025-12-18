# Count how many elements are even and odd.

arr=[3,4,2,4,5,6,7,2,2,5]

count_even = 0
count_odd = 0

for i in arr:
    if i%2==0:
        count_even +=1
    elif i%2!=0:
        count_odd+=1
    
print(f"The even number {count_even} \n The odd number {count_odd}")