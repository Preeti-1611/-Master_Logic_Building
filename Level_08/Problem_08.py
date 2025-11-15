# Print first n terms of an arithmetic progression (a, d)

a = int(input("Enter first term (a): "))
d = int(input("Enter common difference (d): "))
n = int(input("Enter number of terms (n): "))

print("The AP is:")

for i in range(n):      # loop runs from 0 to n-1
    term = a + i * d    # formula Tn = a + (n-1)d
    print(term)

# Important AP Formula

# If

# First term = a

# Common difference = d

# n-th term = Tn

# Then:

#  Tn = a + (n−1) × d