#find the missing number in the range from 1 to n


arr =[1,3,4,5,2,8,7]
n=8

sum_n = n*(n+1)//2
sum_arr=0
for i in arr:
    sum_arr+=i
print(sum_arr)


missing=sum_n-sum_arr

print("The missing value is ",missing)