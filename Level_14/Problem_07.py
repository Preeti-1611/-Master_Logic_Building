# Count how many numbers are divisible by 3 and 5 both

arr = [ 4,8,9,3,46,7,38,45,15]

count = 0

new_arr = []

for i in arr:
     if i%3==0 and i%5==0:
          count+=1
          new_arr.append(i)


print("these are elements are divisible by both",count)
print("the element are",new_arr)