# Take a password string and check basic rules (length ≥ 8 and contains at least one
# digit).

# p= input("enter a password")
# check = len(p)

# if check>=8:
#     if i == 48<=ord(i)<=57 :

p = input("Enter a password: ")

# Check length rule
if len(p) >= 8:
    has_digit = False  # a flag to check if there’s any digit

    for i in p:  # loop through each character
        if 48 <= ord(i) <= 57:  # check if character is a digit
            has_digit = True
            break  # stop checking once you find a digit

    if has_digit:
        print("Password is valid ✅")
    else:
        print("Password must contain at least one digit ❌")
else:
    print("Password must be at least 8 characters long ❌")


