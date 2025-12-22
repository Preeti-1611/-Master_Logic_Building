arr = [10, 25, 30, 45, 60]
key = 45

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")




arr = [10, 25, 30, 45, 60]
key = 45

for i in arr:
    if i == key:
        print("Element found")
        break
else:
    print("Not found")
