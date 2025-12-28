# count the number of digit  in a number recursively
def number(n):
    if n == 0:
        return 0
    return 1 + number(n // 10)

print(number(123))



# number(0)  → 0
# number(1)  → 1 + 0 = 1
# number(12) → 1 + 1 = 2
# number(123)→ 1 + 2 = 3
