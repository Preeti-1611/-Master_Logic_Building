# Take a single digit (0–9) and print its word form (“Zero” to “Nine”)
# Take a single digit (0–9) and print its word form (“Zero” to “Nine”)

n = int(input("Enter a single digit (0–9): "))

words = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']

if 0 <= n <= 9:
    print("The word form is:", words[n])
else:
    print("Invalid input! Please enter a single digit between 0 and 9.")
