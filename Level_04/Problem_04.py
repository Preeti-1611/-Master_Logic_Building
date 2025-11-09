# Take 24-hour time (hours and minutes) and print whether it is AM or PM.
h = int(input("Enter the hour (0–23): "))
m = int(input("Enter the minutes (0–59): "))

if 0 <= h < 12:
    print(f"{h}:{m:02d} AM")
elif 12 <= h < 24:
    if h > 12:
        h -= 12  # Convert 24-hour to 12-hour format
    print(f"{h}:{m:02d} PM")
else:
    print("Invalid hour entered")



# e-by-line explanation

# h = int(input("Enter the hour (0–23): "))

# input("...") shows a prompt and reads what the user types as a string.

# int(...) converts that string to an integer.

# The result is stored in variable h (hour).

# Example: if user types 15, then h == 15.

# m = int(input("Enter the minutes (0–59): "))

# Same idea for minutes: prompt, read string, convert to integer, store in m.

# Example: if user types 7, then m == 7.

# if 0 <= h < 12:

# This condition checks whether h is in the range 0 through 11 (inclusive 0, exclusive 12).

# In 24-hour time, hours 0–11 are AM (midnight through 11 AM).

# If this is true, the code inside this if runs.

# print(f"{h}:{m:02d} AM")

# This prints the time in 12-hour style with AM.

# f"..." is an f-string (formatted string literal).

# {h} inserts the hour value.

# {m:02d} inserts the minutes as a two-digit integer, padding with a leading zero if needed (7 → 07).

# Example: h=9, m=5 → prints 9:05 AM.

# elif 12 <= h < 24:

# This elif runs if the if above was false and h is in 12–23.

# In 24-hour time, 12–23 are PM (noon through 11 PM).

# if h > 12:

# Inside the PM branch we check whether the hour is greater than 12.

# For hours 13–23, we need to convert to 12-hour format by subtracting 12.

# Example: 15 (3 PM) → 15 > 12 true.

# h -= 12 # Convert 24-hour to 12-hour format

# This is shorthand for h = h - 12.

# It converts 13→1, 14→2, ..., 23→11.

# Note: this modifies the h variable itself.

# print(f"{h}:{m:02d} PM")

# Print the converted hour and minutes followed by PM.

# Example flows:

# If original h=12, m=0 → inner if h>12 false, prints 12:00 PM (noon).

# If original h=15, m=5 → h becomes 3, prints 3:05 PM.

# else:

# This runs if neither if nor elif conditions held — i.e., h was not in 0..23.

# print("Invalid hour entered")

# Shows an error message when the entered hour is outside the valid range (e.g., -1 or 24).