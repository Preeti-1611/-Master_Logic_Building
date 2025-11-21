
# Check if two strings are anagrams
# Definition:

# Two strings are anagrams if they contain the same characters with same frequency, but order does not matter.
# Example: "listen" and "silent"



s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")
