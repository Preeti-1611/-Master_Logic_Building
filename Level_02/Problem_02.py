# if the sides from a valid triangle,determine wheather itis equilateral ,isosceles,or scalene
a = input(" enter a degree of a ")
b=input("enter a degree of b")
c = input("enter a degree of c ") 
if a==b==c:
    print("equilateral Triangle")

elif a==b or b==c or a==c:
    print("isosceles Triangle")

else:
    print("it is scalene triangle")
    