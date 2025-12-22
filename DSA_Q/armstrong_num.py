n = int(input('enter a number'))
count = 0

for i in str(n):
    count+=1
print(count)

ans = 0

for i in str(n):
    ans +=int(i)**count
print(ans)


if ans == n:
    print("This is armstrong numner")
else:
    print("not an armstrong number")






# why we use temp here
num = int(input("Enter a number: "))
temp = num
n = len(str(num))
sum = 0

while temp > 0:  #bcz when num>0 means after iteration it will become 0
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
