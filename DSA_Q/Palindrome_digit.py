# # check if number is palindrome

# n = int(input("Enter the number: "))
# original = n
# reverse_num = 0

# while n > 0:
#     last_digit = n % 10
#     reverse_num = reverse_num * 10 + last_digit
#     n = n // 10

# if reverse_num == original:
#     print("Yes, Palindrome")
# else:
#     print("Not Palindrome")


a=[5,4,3,22,22,2,3,85]
print(set(a)) 



names = ["Preeti", "anu", "ZARA"]
names.sort(key=str.lower)
print(names)



names = ["preeti", "anu", "zara"]
print(sorted(names))



arr = [5, 1, 3]
arr.sort(reverse=True)
print(arr)   # [5, 3, 1]



arr = [5, 2, 8, 1]
sorted_arr = sorted(arr)



print(sorted_arr)     # [1, 2, 5, 8]
print(arr)            # [5, 2, 8, 1]  → original unchanged
