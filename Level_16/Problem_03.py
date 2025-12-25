# Print only even from 1 to n


# def even(n):
#     if n == 0 :
#         return
#     even(n-1)
#     if n%2==0:   
#         print(n)
    

# even(5)




# revese order answer


def even_n(n):
     if n == 0:
        return 
     
     if n%2==0:
        print(n)
     even_n(n-1)

even_n(6)
        