# reverse a number using recyrsively

def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

print(reverse_num(1234))   # Output: 4321
