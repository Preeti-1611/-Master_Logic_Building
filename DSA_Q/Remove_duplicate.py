# remove diplicate elemnts in the array


arr= [2,3,4,4,2,5,7,3,3]

n_arr = []

for i in arr:
    if i in n_arr:
        i+=1
    else:
        n_arr.append(i)

print(n_arr)