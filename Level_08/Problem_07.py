# find the sum of all factors of a number.

a = int(input("entera number"))
sum =0
for i in range(1,a+1):
    if a%i==0:
        print(i)
        sum +=i
print("the sum of aall factor is",sum )