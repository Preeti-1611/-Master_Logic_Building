# all zero at the end of the array

arr=[2,3,5,1,0,4,6,0,55,0,33]

res =[]

for i in arr:
    if i != 0:
        res.append(i)

zero = arr.count(0)

for _ in range(zero):
      res.append(0)

print(res)