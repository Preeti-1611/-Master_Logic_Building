# Check if a number is a palindrome


n = int(input('enter the number'))
original = n
pro = 0
while n>0:
    last = n%10 
    pro=pro*10+last
    n = n //10
 

if pro == original:
        print("yes this is Plaindrome")
else:
        print("No this is  not a Palindrome")
    
print(pro)