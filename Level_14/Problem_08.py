# Find the count of prime numbers in the array

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
count = 0

for num in arr:
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

print(count)
