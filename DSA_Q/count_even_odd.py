#count the number of even and odd number in a list

arr = [23,44,2,1,4,5,6,97,4]

even_c=0
odd_c=0

for i in arr:
    if i%2==0:
        even_c+=1
    else :
        odd_c+=1

print("the even number is",even_c)
print("the odd number is ",odd_c)
