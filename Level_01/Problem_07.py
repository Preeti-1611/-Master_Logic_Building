# Take a character and check if it’s a vowel or consonant.

ch = str(input("enter a charater"))
if ch in "aeiou" or ch in "AEIOU":
    print("This char is vowel")
else :
    print("It is consonant")