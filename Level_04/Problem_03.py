# Take three numbers and print the median value (neither maximum nor minimum).
a = float(input("entera number a"))
b = float(input("entera number b"))
c = float(input("entera number c"))

d = (a+b+c)/3

print("the meadian value is",d)


# this  is above is mean

# | Term               | Meaning                                                      | Formula           | Example                             |
# | ------------------ | ------------------------------------------------------------ | ----------------- | ----------------------------------- |
# | **Mean (Average)** | The sum of all numbers divided by how many numbers there are | `(a + b + c) / 3` | (10 + 20 + 30)/3 = 20               |
# | **Median**         | The *middle* value when numbers are arranged in order        | Middle number     | Numbers: [10, 20, 30] → median = 20 |

# median

a = float(input("Enter number a: "))
b = float(input("Enter number b: "))
c = float(input("Enter number c: "))

numbers = [a, b, c]
numbers.sort()

median = numbers[1]
print("The median value is:", median)
