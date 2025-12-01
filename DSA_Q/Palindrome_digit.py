# check if number is palindrome

n = int(input("Enter the number: "))
original = n
reverse_num = 0

while n > 0:
    last_digit = n % 10
    reverse_num = reverse_num * 10 + last_digit
    n = n // 10

if reverse_num == original:
    print("Yes, Palindrome")
else:
    print("Not Palindrome")
