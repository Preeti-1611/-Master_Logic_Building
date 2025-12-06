#swapping using 3rd num


a = 5
b = 10

temp = a   # store a in temp
a = b      # put b into a
b = temp   # put temp (old a) into b

print(a, b)



a = 5
b = 10

a, b = b, a
print(a, b)





a = 5
b = 10

a = a + b   # a = 15
b = a - b   # b = 5
a = a - b   # a = 10

print(a, b)
