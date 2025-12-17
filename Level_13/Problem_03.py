# Find the average of array elements.


arr=[4,5,3,6,2,8,1,3.7]

count=0
sum=0
for i in arr:
    sum+=i
    count+=1

avg = sum/count
print("the average of an array is ",avg)