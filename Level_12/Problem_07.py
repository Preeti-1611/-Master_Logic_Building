# Count how many elements are even and odd.


arr = [3,4,6,21,33,6,7,35]

even_c = 0
odd_c =0

for i in arr:
    if i%2==0:
     even_c+=1
    else :
       odd_c+=1

print("The even and odd counts of an arr is ",even_c,odd_c)