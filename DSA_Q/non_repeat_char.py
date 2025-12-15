# find the frist non repeating char in th str

# s = "aabbc"

# for ch in s:
#     if s.count(ch) == 1:
#         print(ch)
#         break


s = "Hello"
freq = {}

for ch in s:
    freq[ch] = freq.get(ch, 0) + 1

for ch in s:
    if freq[ch] == 1:
        print(ch)
        break




# STEP 1: Understand the VARIABLES
# s
# s = "Hello"


# This is our string:

# H  e  l  l  o

# freq
# freq = {}


# An empty dictionary
# It will store:

# character → how many times it appears

# 🟢 STEP 2: FIRST LOOP (Counting characters)
# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1


# 👉 This loop ONLY COUNTS characters
# 👉 Nothing is printed here

# 🔍 What does freq.get(ch, 0) mean?

# If ch exists in dictionary → give its value

# If ch does NOT exist → return 0

# 🧪 DRY RUN (VERY IMPORTANT)
# 🔹 Iteration 1
# ch = 'H'


# Dictionary now:

# freq.get('H', 0) → 0
# freq['H'] = 0 + 1 → 1


# 👉 freq = {'H': 1}

# 🔹 Iteration 2
# ch = 'e'

# freq.get('e', 0) → 0
# freq['e'] = 1


# 👉 freq = {'H': 1, 'e': 1}

# 🔹 Iteration 3
# ch = 'l'

# freq.get('l', 0) → 0
# freq['l'] = 1


# 👉 freq = {'H': 1, 'e': 1, 'l': 1}

# 🔹 Iteration 4
# ch = 'l'

# freq.get('l', 0) → 1
# freq['l'] = 1 + 1 → 2


# 👉 freq = {'H': 1, 'e': 1, 'l': 2}

# 🔹 Iteration 5
# ch = 'o'

# freq.get('o', 0) → 0
# freq['o'] = 1


# 👉 FINAL dictionary:

# {'H': 1, 'e': 1, 'l': 2, 'o': 1}

# 🟢 STEP 3: SECOND LOOP (Finding first non-repeating)
# for ch in s:
#     if freq[ch] == 1:
#         print(ch)
#         break


# 👉 This loop CHECKS order
# 👉 We loop again over "Hello"

# 🔍 DRY RUN SECOND LOOP
# 🔹 Iteration 1
# ch = 'H'


# Check:

# freq['H'] == 1 → TRUE


# 👉 Print:

# H


# 👉 break → STOP LOOP

# 🟢 WHY TWO LOOPS?
# Loop	Purpose
# First loop	Count all characters
# Second loop	Find FIRST character with count = 1
# 🧠 VERY IMPORTANT REAL-LIFE EXAMPLE

# Imagine a class:

# Student	Attendance
# H	1
# e	1
# l	2
# o	1

# Now teacher asks:
# 👉 “Who attended only once and came first?”

# Answer = H