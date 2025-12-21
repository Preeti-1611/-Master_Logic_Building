# Swap the first and last elements of the array


arr= [3,5,2,4,9,3,8]

n = len(arr)
    
arr[0],arr[n-1]= arr[n-1],arr[0]

print(arr)