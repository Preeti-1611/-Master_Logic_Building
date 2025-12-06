n = int(input('enter a number'))
count = 0

for i in str(n):
    count+=1
print(count)

ans = 0

for i in str(n):
    ans +=int(i)**count
print(ans)
