# Create a new array containing only even elements


arr  = [3,4,2,8,7,4,15,8,9]

new_arr = []

for i in arr:
    if i%2==0:
        new_arr.append(i)
    
print(new_arr)