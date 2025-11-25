# Count how many elements are positive, negative, or zero.
# 

arr = [3,-5,7,2,0,5,7-3,-67,4,9,33,-33,0,2]

p_c =0
n_c =0
z_c = 0

for i in arr:
    if i>0:
        p_c+=1
    elif i<0:
        n_c+=1
    elif i==0:
        z_c +=1

print( " The number of Pos , neg,zeros are ",p_c,n_c,z_c)