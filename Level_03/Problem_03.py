# 3. Take a 4-digit number and check if the first and last digits are equal

list = []


for i in range(0,4):
    num = int(input("enter a number"))
    list.append(num)


print("the 4 digit is ",list)

if list[0] == list[3]:
    print("the first and last digit are equal")
else:
    print("not equal")

