# Take income and age, and check if eligible for tax (age > 18 and income > 5 L)
age = int(input("entera age"))
income =float(input("what is your income"))

if age>18 and income>50000:
    print("you have to pay TAX")
else:
    print("not eligible for  TAX")
