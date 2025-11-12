# Find the sum of digits of a num

num = int(input('entera number'))
sum=0
for i in str(num):
    sum+=int(i)

print(sum)

# Find the sum of digits of a num

num = int(input('entera number'))
sum=0
for i in str(num):
    sum+=i

print(sum)


# Find the sum of digits of a num

num = int(input('entera number'))
sum=0
for i in str(num):
    sum+=i

print(sum)



# | Topic          | Mistake                | Reason                                   | Fixed Version      |
# | -------------- | ---------------------- | ---------------------------------------- | ------------------ |
# | Count digits   | `'n'` in quotes        | Looped over a string instead of variable | `for i in str(n):` |
# | Count digits   | `count += i`           | Tried to add string instead of number    | `count += 1`       |
# | Sum of digits  | `sum += i`             | Added string, not integer                | `sum += int(i)`    |
# | Sum of digits  | Used `sum` as variable | Overwrites Python built-in               | Use `digit_sum`    |
# | Floor division | None                   | You did it right ✅                       | —                  |
# | Palindrome     | None                   | You understood the problem ✅             | —                  |

# | Mistake                      | Why it’s wrong                        | Correct way          |
# | ---------------------------- | ------------------------------------- | -------------------- |
# | Used `'i'` as a string       | Strings can’t be added to numbers     | `int(i)`             |
# | Variable name `sum`          | Overwrites Python’s built-in function | use `digit_sum`      |
# | Input prompt not spaced well | (just readability)                    | `'Enter a number: '` |
