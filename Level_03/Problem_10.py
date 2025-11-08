# Check if an amount can be evenly divided into 2000, 500, and 100 currency notes
amount = int(input("Enter the amount: "))

if amount % 2000 == 0:
    print("Can be evenly divided into ₹2000 notes.")
elif amount % 500 == 0:
    print("Can be evenly divided into ₹500 notes.")
elif amount % 100 == 0:
    print("Can be evenly divided into ₹100 notes.")
else:
    print("Cannot be evenly divided into 2000, 500, or 100 notes.")

