# list to str and print first char


lst = [3,4,6,2,3]

s = ''.join(map(str,lst))
print(s)

print(s[0])


# using loop

s1 = [3,5,2,6,3]
s2=''

for i in str(s1):
    s2+=i
print(s2)
print(type(s2))
print(type(s1))
