# print The 1 to n using recursion



def num(n):
    if n==0:
        return 
    num(n-1)
    print(n)

num(3)


#  Base Case → stops the recursion
# Recursive Call → function calls itself


# def function_name(parameters):
#     if condition:        # Base case (stop)
#         return
#     else:
#         function_name(parameters)   # Recursive call
#  Easy Memory Formula
#  Function → Stop condition → Call itself

