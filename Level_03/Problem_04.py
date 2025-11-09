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


# num = input("Enter a number: ")
# count = len(num)

# print("Number of digits:", count)

# if count == 1:
#     print("It is a single-digit number")
# elif count == 2:
#     print("It is a double-digit number")
# else:
#     print("It is a multi-digit number")


# num = int(input("Enter a number: "))

# if -9 <= num <= 9:
#     print("Single-digit number")
# elif -99 <= num <= 99:
#     print("Double-digit number")
# else:
#     print("Multi-digit number")
