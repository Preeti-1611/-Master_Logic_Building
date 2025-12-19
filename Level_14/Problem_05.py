

# odd num sum

arr = [3,4,6,2,4,2,9,23]

odd_num = []

for i in arr:
    if i%2!=0:
         odd_num.append(i)

print(odd_num)

sum =0
for i in odd_num:
      sum+=i

print("the  odd number sum",sum)