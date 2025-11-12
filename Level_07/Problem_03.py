# # Check if a number is a palindrome
# name = input("enter somthong i willcheck it is palinderome or not")

# if name==name[::-1]:  #if name[::]==name[::-1]:  
#     print("yes it is")
# else:
#     print("NO")


n = int(input("Enter a number: "))
temp = n  # save the original number
rev = 0

while n > 0:
    digit = n % 10        # take last digit
    rev = rev * 10 + digit # build reverse number
    n = n // 10           # remove last digit

if temp == rev:
    print("Yes! It's a palindrome.")
else:
    print("No, it's not a palindrome.")
