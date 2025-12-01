s1 = input("Enter first string: ").replace(" ", "").lower()
s2 = input("Enter second string: ").replace(" ", "").lower()

if sorted(s1) == sorted(s2):
    print("Yes, the strings are anagrams.")
else:
    print("No, the strings are not anagrams.")