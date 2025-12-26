# Print Fibonacci series up to n terms recursively

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)


for i in range(0,6):
     print(fib(i))
    