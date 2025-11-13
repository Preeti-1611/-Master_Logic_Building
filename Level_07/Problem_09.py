# fibonacci series 
n = int(input("Enter how many terms you want: "))

a = 0
b = 1


print("Fibonacci Series:")

for i in range(n):
    print(a)

    c = a + b
    a = b
    b = c
    
print(sum)





# What is the Fibonacci series?

# It’s a sequence of numbers where each number is the sum of the previous two.

# So it starts with:

# 0, 1, 1, 2, 3, 5, 8, 13, ...


# Here’s how it’s formed:

# Start with 0 and 1

# Then add the last two numbers to get the next one
# (0 + 1 = 1)
# (1 + 1 = 2)
# (1 + 2 = 3)
# (2 + 3 = 5) ... and so
