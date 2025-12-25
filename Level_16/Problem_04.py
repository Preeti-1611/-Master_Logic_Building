# odd number


def odd_num(s):
    if s == 0 :
        return
    if s%2!=0:
        print(s)
    odd_num(s-1) 


odd_num(3)