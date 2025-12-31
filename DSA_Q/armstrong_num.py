def armstrong_num(n):
    num = n                 # store original number
    nod = len(str(num))     # number of digits
    total = 0

    while num > 0:
        last = num % 10              # get last digit
        total = total + (last ** nod)
        num = num // 10              # remove last digit

    return total == n                # compare with original number

print(armstrong_num(153))







# n = int(input('enter a number'))
# count = 0

# for i in str(n):
#     count+=1
# print(count)

# ans = 0

# for i in str(n):
#     ans +=int(i)**count
# print(ans)


# if ans == n:
#     print("This is armstrong numner")
# else:
#     print("not an armstrong number")






# # why we use temp here
# num = int(input("Enter a number: "))
# temp = num
# n = len(str(num))
# sum = 0

# while temp > 0:  #bcz when num>0 means after iteration it will become 0
#     digit = temp % 10
#     sum += digit ** n
#     temp //= 10

# if sum == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")
