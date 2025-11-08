# Take a 3-digit number and determine if the middle digit is the largest, smallest, or
# neither

a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))

if b>c and b>a:
    print("the middle is largest")
elif b<a and b<c:
    print("the middle is samllest")
else :
    print("niether")
