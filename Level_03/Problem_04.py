# Check whether a given integer is single-digit, double-digit, or multi-digit
num = input('enter a number i will find it how much digit it has')
count = 0
for i in num:
    count+=1
print(count)

if count==1:
    print("it is single digit")
elif count ==2:
    print("it is double digit")
else :
    print("multi digit")