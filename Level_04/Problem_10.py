# 8. Take a weekday number (1–7) and determine if it is a weekday or weekend.


# n = int(input("Enter a weekday number (1–7): "))

# if 1 <= n <= 5:
#     print("It's a weekday 🏢")
# elif n == 6 or n == 7:
#     print("It's a weekend 🎉")
# else:
#     print("Invalid number! Please enter between 1 and 7.")




# Take a weekday number (1–7) and determine if it is a weekday or weekend.
n = int(input("Enter a number (1–7): "))

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Check if the number is valid
# if 1 <= n <= 7:
#     day = days[n - 1]   # because list index starts from 0
#     print("The day is:", day)
    
#     # Check weekday or weekend
#     if day == 'Saturday' or day == 'Sunday':
#         print("It’s a weekend!")
#     else:
#         print("It’s a weekday!")
# else:
#     print("Invalid number! Please enter between 1 and 7.")
