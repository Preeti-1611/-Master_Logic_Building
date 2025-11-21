# Count vowels in a string


s = input("Enter a string: ")
s = s.lower()   # convert to lowercase

count = 0

for i in s:
    if i in "aeiou":
        count += 1

print("Number of vowels:", count)
