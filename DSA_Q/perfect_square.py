# if a given number is perfect sqaure

import math

n = 36
root = int(math.sqrt(n))

if root * root == n:
    print("Perfect Square")
else:
    print("Not a Perfect Square")
