# Find the maximum element in an array


arr = [3,5,45,6,7,85]

lar = arr[0]

for i in arr:
    if i>lar:
      lar = i
print(lar)