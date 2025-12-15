#Factors
# a factors is a number that divids another number completely remainder=0


# n=18

# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end = " ")

#common factor : factor that are common b/w two numbers

num1 = int(input("enter n1: "))
num2 = int(input("enter n2: "))

small = min(num1, num2)

for i in range(1, small + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)

# Yes, you can use num2 + 1
#  But only when num2 is the smaller number

# If you are not sure which number is smaller, you MUST use min(num1, num2).

#  WHY we use min(num1, num2)
# Important rule:

# A common factor can never be greater than the smaller number.

# | Option                       | Correct?  | Recommended? |
# | ---------------------------- | --------- | ------------ |
# | `range(1, num2+1)`           | Sometimes | ❌ No         |
# | `range(1, min(num1,num2)+1)` | Always    | ✅ Yes        |

