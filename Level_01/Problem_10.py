# Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions.


temp = float(input("Enter temperature in °C: "))

if temp < 20:
    print("Cold")
elif temp >= 20 and temp <= 30:
    print("Warm")
else:
    print("Hot")
