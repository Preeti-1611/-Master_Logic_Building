# Replace every negative number with 0.


arr = [4, 3, -2, 9, -5]

for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0

print(arr)








# If you must use replace(), then remember one rule:

# 🔴 replace() works only on strings, NOT directly on lists

# So we’ll convert the list to a string, use replace(), then convert it back.

# ✅ Using replace() to replace negative numbers with 0
# 🔹 Given
# arr = [4, 3, -2, 9, -5]

# ✅ Method: List → String → Replace → List
# arr = [4, 3, -2, 9, -5]

# # convert list to string
# s = str(arr)

# # replace negative numbers
# s = s.replace("-2", "0").replace("-5", "0")

# # convert back to list
# arr = eval(s)

# print(arr)