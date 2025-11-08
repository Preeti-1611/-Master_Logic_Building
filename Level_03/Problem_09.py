# 10. Check whether a number is a perfect square (without using the square root function).
# num = int(input("enter the square number"))

# if num%2 ==0 :
#     print( "its a perfect square")
# else:
#     print("not a perfect square")


num = int(input("Enter a number: "))
is_square = False

for i in range(1, num + 1):
    if i * i == num:
        is_square = True
        break
    elif i * i > num:
        break

if is_square:
    print(num, "is a perfect square.")
else:
    print(num, "is not a perfect square.")
