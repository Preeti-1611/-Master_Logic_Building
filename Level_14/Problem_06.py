# perfect square

import math

arr = [1, 2, 4, 6, 9, 10, 16]
count = 0

for num in arr:
    if num >= 0:
        root = int(math.sqrt(num))
        if root * root == num:
            count += 1

print(count)
