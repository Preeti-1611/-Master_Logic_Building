# take three numbers and check if they are in arithmetic progression 
a = int(input('entera number'))
b= int(input('entera number'))
c =int(input('enter a number'))

d = b-a
e=c-b

if d == e :
    print("this is AP")
else :
    print("This is not AP")