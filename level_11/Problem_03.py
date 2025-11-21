# s = input("Enter a string: ")
# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


s = input("Enter a string: ")
rev = ""

for i in s:
    rev = i + rev

print("Reversed:", rev)

if s == rev:
    print("Palindrome")
else:
     print("Not Palindrome")
