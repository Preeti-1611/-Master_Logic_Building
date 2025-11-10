hour = int(input("Enter the hour (0–23): "))
minute = int(input("Enter the minutes (0–59): "))

# Convert hour to 12-hour format
hour = hour % 12

# Calculate angles
minute_angle = minute * 6
hour_angle = (hour * 30) + (minute * 0.5)

# Find difference13
angle = abs(hour_angle - minute_angle)

# Find smaller angle
smaller_angle = min(angle, 360 - angle)

print(f"The smaller angle between the hands is {smaller_angle:.2f}°")
