# Check if a number is a multiple of 7 or ends with 7.

num =int(input('enter a number'))

last_digit = num%10 # to find the last digit of the fiven number
# last_digit = num[-1] # 
# print(int(last_digit))

if num % 7==0 or last_digit == 7:
    print("yes it owrks on on of the above condition")

else:
    print("it will not work on the above condition try again")