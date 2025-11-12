#  tahe three numbers and check if they are in geometric progression.
a = int(input('enter the number'))
b = int(input("enter the number"))
c = int(input("enter a number"))

# b/a = c/b
if b * b ==a *c :
    print("this is GP")
else:
    print("this is not GP")