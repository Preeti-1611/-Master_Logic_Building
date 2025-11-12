# check if number is perfect number

n = int(input("enter a number"))
sum=0
for i in (1,n):
    if n%i==0:
       sum+=i
if sum ==n:
    print(f"{n} is perfect number")
else:
    print(f"{n} is not a perfect number")

# What’s a Perfect Number?

# A Perfect Number is a number that is equal to the sum of its proper divisors
# (excluding the number itself).

# In plain words:

# Take all the numbers that divide it completely (except itself).
# Add them up.
# If the total equals the original number → it’s a perfect number.

# ⚙️ Example 1 — 6

# Let’s test 6.

# Divisors of 6 (except itself) → 1, 2, 3
# Sum = 1 + 2 + 3 = 6

# ✅ 6 = 6 → Perfect number

# ⚙️ Example 2 — 28

# Divisors of 28 (except itself) → 1, 2, 4, 7, 14
# Sum = 1 + 2 + 4 + 7 + 14 = 28

# ✅ 28 = 28 → Perfect number
