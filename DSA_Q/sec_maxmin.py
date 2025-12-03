#sec min

arr = [34,2,3,4]
arr = list(set(arr))
arr.sort()

print("Second min =", arr[1])

#secmax
arr = list(set(arr))   # remove duplicates
arr.sort()             # sort array

print("Second max =", arr[-2])
