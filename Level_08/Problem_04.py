# print hcf (GCD) of two numbers using loops\
# HCF = Highest Common Factor

#  The biggest number that divides BOTH numbers without leaving any remainder

# HCF (Highest Common Factor) is the largest number that divides two or more numbers exactly without leaving a remainder.

a= int(input("enter first number"))
b = int(input("enter the second number"))
hcf = 1
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        hcf = i

print("the hcf (gcd) is :",hcf)