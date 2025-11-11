# 
# Print the sum of all even numbers up to n.
 
n = int(input("enter the number"))
sum =0
for i in range(2,n+1,2):
         sum+=i
print(sum)