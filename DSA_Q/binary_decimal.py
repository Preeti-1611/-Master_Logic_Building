# binary to decimal

b1="1000"
b2=b1[::-1]
de = 0
j=0
for i in b2:
     de+=int(i)*2**j
     j+=1

print("the decimal is",de)