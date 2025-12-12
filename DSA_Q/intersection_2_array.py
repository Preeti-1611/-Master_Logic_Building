#intersection of two array

a1 = [2,3,4,5]
a2 = [6,3,5,1]

intersection= []

for i in a1:
    if i in a2:
        intersection.append(i)

print(intersection)




A = [1, 2, 3, 4]
B = [3, 4, 5]

intersection = list(set(A) & set(B))
print(intersection)
