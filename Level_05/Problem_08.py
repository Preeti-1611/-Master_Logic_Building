# Take an integer (1–9999) and check if the sum of its digits is greater than the product
# of its digits.

n = int(input("enter the number (1-9999) :"))

sum = 0
product = 1

for i in str(n):
    sum+=int(i)

print("sum =",sum)

for i in str(n):
    product*= int(i)


print("product=",product)


if sum>product:
    print("yes")
else:
    print('No')
