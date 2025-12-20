#  Take n elements and print only those greater than a given value k.


arr = [3,6,2,4,56,33,28,43,49,9]

num = int(input("enter a k element"))

greater_ele = []

for i in arr:
    if i>num:
        greater_ele.append(i)

print("the greater elements are",greater_ele)