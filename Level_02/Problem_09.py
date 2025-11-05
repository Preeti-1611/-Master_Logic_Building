# Take a day number (1–7) and print the corresponding day name
d = int(input("Enter day number (1-7): "))

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

if 1 <= d <= 7:
    print(days[d-1])
else:
    print("Invalid day number. Enter 1-7.")
