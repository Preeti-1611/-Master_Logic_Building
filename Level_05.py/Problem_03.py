# Take day and month and check if it forms a valid calendar date (ignoring leap years)
day = int(input("Enter day: "))
month = int(input("Enter month: "))

# Days in each month (ignoring leap years)
days_in_month = {
    1: 31,  # January
    2: 28,  # February
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Check if month is valid first
if month < 1 or month > 12:
    print("Invalid month! Month must be between 1 and 12.")
# Check if day is valid for the given month
elif day < 1 or day > days_in_month[month]:
    print("Invalid day for the given month.")
else:
    print("Valid calendar date!")
