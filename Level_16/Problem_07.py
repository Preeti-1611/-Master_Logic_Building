# fiboncci series

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

# print first 6 fibonacci numbers
for i in range(6):
    print(fib(i), end=" ")
