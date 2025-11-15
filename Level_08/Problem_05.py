
# find lcm  of two numbers using loops.


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# LCM can never be smaller than the biggest number
lcm = max(a, b)

while True:
    if lcm % a == 0 and lcm % b == 0:
        print("The LCM is:", lcm)
        break
    lcm += 1


#  LCM = Least Common Multiple

# It means:

#  The smallest number that BOTH numbers can divide completely (no remainder).


