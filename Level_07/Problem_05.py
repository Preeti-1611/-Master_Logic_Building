# Check if a number is an Armstrong number

n = input('enter the number')
# print(len(str(n)))
p= len(str(n))
print(p)
sum = 0
for i in str(n):
    sum+=int(i)**p
print(sum)

if int(n)==sum:
    print("Yes it is armstrong number")
else:
    print("NO it is not armstrong")
