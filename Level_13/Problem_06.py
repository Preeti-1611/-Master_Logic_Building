
arr=[2,-2,4,6,10,3,0,-3,-9,0]

CO_P = 0
CO_N = 0
CO_Z = 0
for i in arr:
    if i>0:
        CO_P+=1
    elif i<0:
        CO_N+=1
    else :
        CO_Z+=1
        
print("positive ,negative , zero",CO_P,CO_N,CO_Z)