# s1 = input("Enter first string: ").replace(" ", "").lower()
# s2 = input("Enter second string: ").replace(" ", "").lower()

# if sorted(s1) == sorted(s2):
#     print("Yes, the strings are anagrams.")
# else:
#     print("No, the strings are not anagrams.")


def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    char_count = {}

    # Count characters in s1
    for ch in s1:
        char_count[ch] = char_count.get(ch, 0) + 1

    # Decrease count using s2
    for ch in s2:
        char_count[ch] = char_count.get(ch, 0) - 1

    # Check if all values are zero
    for value in char_count.values():
        if value != 0:
            return False

    return True


# Driver code
s1 = "geeks"
s2 = "kseeg"

print(are_anagrams(s1, s2))  # True
























































# if s1.sort() == s2.sort():
# s1 and s2 are strings

# Strings do NOT have sort() method

# sort() works only on lists
# sorted() works on strings and returns a list.
# 