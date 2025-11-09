# 2. Take a number and print “Fizz” if divisible by 3, “Buzz” if divisible by 5, and
# “FizzBuzz” if divisible by both.

num = int(input("enter a number"))
if num%5==0 and num%3==0:
        print("FizzBuzz")
elif num%5==0:
        print("Buzz")
elif num%3==0:
         print("Fizz")