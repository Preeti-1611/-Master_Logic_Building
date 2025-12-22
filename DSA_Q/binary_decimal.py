# binary to decimal

b1 = "1111"
de = 0
power = 0

for bit in b1[::-1]:
    de += int(bit) * (2 ** power)
    power += 1

print("The decimal is", de)
