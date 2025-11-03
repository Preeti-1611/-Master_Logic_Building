# Take three numbers and print the largest.
# a = 10
# b=30
# c= 50


a = float(input("enter a number"))
b = float(input("enter a second number"))
c = float(input("enter a thrid number"))
if a>b or a>c:
    print("a is largest")
elif b>c:
    print("b is largest")
else:
    print("C is largest")