# write a str in ascii value

st = input("enter a string")

for i in st:
    print(f"{i} ascii value is ", ord(i))

for i in st:
    print(ord(i),end ="")

for i in st:
    sum=0
    sum+=ord(i)
    print(sum)