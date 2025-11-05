# ch = input("enter a ch")

# if 'A'<= ch <='Z':
#     print("upper case")
# elif 'a'<= ch<='b':
#     print("lowercase")
# elif '0'<=ch<='9':
#     print("digit")
# else:
#     print("this is a speacial number ")


ch = input("enter a character")
if 65<=ord(ch)<=90:
    print("it is uppercase")
elif 97<=ord(ch)<=122:
    print("it is a lowercase ")
elif 48<=ord(ch)<=57:
    print("it is a digit")
else :
    print("it is a special variable")


ch = input("Enter any character: ")

if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")



