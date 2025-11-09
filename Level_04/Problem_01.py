# Take a character and check if it is a letter, a digit, or

ch = input("enter a charecter")

if 65<=ord(ch)<=95 or 97<=ord(ch)<=122:

    print("this is a letter")
elif 48<=ord(ch)<=57:
     print("this is a digit")
else:
     print("neither")



# ch = input("Enter a character: ")

# if ch.isalpha():
#     print("It is a letter.")
# elif ch.isdigit():
#     print("It is a digit.")
# else:
#     print("It is neither a letter nor a digit.")
# isalpha() → checks for letters (A-Z or a-z)

# isdigit() → checks for numbers (0–9)