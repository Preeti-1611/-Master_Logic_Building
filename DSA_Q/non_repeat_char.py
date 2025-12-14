# find the frist non repeating char in th str

s1="Hello"
s2=[]
for i in s1:
    if i not in s2:
         s2.append(i)

print(s2[0])