s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Yes, the strings are anagrams.")
else:
    print("No, the strings are not anagrams.")


# if s1.sort() == s2.sort():
# s1 and s2 are strings

# Strings do NOT have sort() method

# sort() works only on lists
# sorted() works on strings and returns a list.
# 