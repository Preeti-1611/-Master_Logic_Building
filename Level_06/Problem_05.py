# Print the table of a given number (n × 1 to n × 10).
n = int(input("enter the number you want to which you want the table"))
for i in range(1,11):
    print(f"{n}*{i} =",n*i)