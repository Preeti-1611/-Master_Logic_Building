def count_digit(n):
    num = n

    count =0

    while num>0:
        count+=1
        num//=10

    return count


print(count_digit(3533))



