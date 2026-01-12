# using bit
n = int(input("enter a number"))

if n & 1 ==0:
    print("even")
else:
    print("odd")



def even_or_odd(n):
    if n & 1:
        return "Odd"
    else:
        return "Even"
