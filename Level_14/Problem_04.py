# Find the sum of even elements only.

arr = [3,4,6,2,4,2,9,23]

even_num = []

for i in arr:
    if i%2==0:
         even_num.append(i)

print(even_num)

sum =0
for i in even_num:
      sum+=i

print("the even number sum",sum)