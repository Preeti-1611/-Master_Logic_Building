# Take a character and check if it’s a vowel or consonant.

ch = str(input("enter a charater"))
if ch in "aeiou" or ch in "AEIOU":
    print("This char is vowel")
else :
    print("It is consonant")



# Take a character as input
ch = input("Enter a character: ")

# Convert it to lowercase to handle both uppercase and lowercase letters
ch = ch.lower()

# Check if it is an alphabet
if ch.isalpha():
    # Check for vowels
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("It's a vowel.")
    else:
        print("It's a consonant.")
else:
    print("Not an alphabet character.")
