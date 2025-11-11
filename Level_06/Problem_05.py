# Print the table of a given number (n × 1 to n × 10).
n = int(input("enter the number you want to which you want the table"))
for i in range(1,11):
    print(f"{n}*{i} =",n*i)


# n = "5"
# i = 3
# print(n * i)
# Output 👉 555 (string repeated 3 times)
# But you wanted 15 (number multiplication).

# You said:
# n = input("enter the number you want to which you want the table")
# for i in range(1,11):
#     print(f"{n}*{i} =",n*i)
# ChatGPT said:
# Nice try, Preeti 😊
# But there’s a small mistake in your code — the input() function takes input as a string, so when you try to do n * i, it multiplies the string instead of the number.

# Let’s fix it 👇

# n = int(input("Enter the number you want the table for: "))  # convert to integer
# for i in range(1, 11):
#     print(f"{n} * {i} = {n * i}")
# ✅ Explanation:

# int(input(...)) converts the user input from string → integer.

# range(1, 11) means it will run from 1 to 10.

# f"{n} * {i} = {n * i}" prints the formatted multiplication like 2 * 1 = 2.

# 🧮 Example Output:

# Enter the number you want the table for: 5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# ...
# 5 * 10 = 50
# Would you like me to show how to print it in a neat column format (like a proper table)?

# You said:
# what ia mistaked
# ChatGPT said:
# Good question, Preeti 👍

# Let’s look at your original code carefully 👇

# n = input("enter the number you want to which you want the table")
# for i in range(1,11):
#     print(f"{n}*{i} =",n*i)