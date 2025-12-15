#using euclide method

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(48, 18))  # 6

#another method
num1 = 12
num2 = 18
gcd = 1
for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i

print("GCD:", gcd)
