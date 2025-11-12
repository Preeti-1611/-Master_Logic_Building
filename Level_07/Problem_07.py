# Print all prime numbers between 1 and 100.

# First, understand the problem

# A prime number is a number greater than 1 that has only two factors:

# 1

# Itself

# Examples: 2, 3, 5, 7, 11, 13, ...

# Non-primes (composite numbers) have more factors.

# ⚙️ Step-by-step logic

# Loop through numbers from 2 to 100
# (1 is not prime)

# For each number, check if it has any divisor between 2 and itself-1.

# If no divisor divides it completely → it’s prime.

# Print it.


for num in range(2, 101):  # start from 2 because 1 is not prime
    is_prime = True         # assume the number is prime

    for i in range(2, num):  # check for factors
        if num % i == 0:
            is_prime = False
            break            # no need to check further

    if is_prime:
        print(num)
    