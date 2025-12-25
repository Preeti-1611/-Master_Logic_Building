# print number from n - 1 


def number(n):
    if n == 0:
        return
    print(n)
    number(n-1)

number(4)











# AFTER recursion (1 → n)
# call call call STOP
# print print print

# BEFORE recursion (n → 1)
# print print print STOP

# ⭐ Super Easy Memory Trick

# 🧠 Print before call → n to 1
# 🧠 Print after call → 1 to n