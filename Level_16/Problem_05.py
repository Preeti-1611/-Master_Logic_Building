# sum of n natural number


def sum_num(n):
    if n == 0:          # base case
        return 0
    return n + sum_num(n-1)

print(sum_num(4))


# Never use extra variables like sum
# Always return the result