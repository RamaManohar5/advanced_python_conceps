"""
A lambda function is a small (one line) anonymous function that is defined without a name. 
A lambda function can take any number of arguments, but can only have one expression. 
While normal functions are defined using the def keyword, 
in Python anonymous functions are defined using the lambda keyword.

lambda arguments: expression
"""
f = lambda x : x**2
print(f(25))

f1 = lambda x,y : x*y
print(f1(90, 56))

# Lamdba inside another function
def myfunc(n):
    return lambda x: x*n

doubler = myfunc(2)
print(doubler(125))

# Custom sorting using a lambda function as key parameter
points2D =  [(1, 9), (4, 1), (5, -3), (10, 2)]
sorted_by_y = sorted(points2D, key=lambda x: x[1])
print(sorted_by_y)

mylist = [- 1, -4, -2, -3, 1, 2, 3, 4]
sorted_by_abs = sorted(mylist, key=lambda x:abs(x))
print(sorted_by_abs)

# Use lambda for map function
# map(func, seq), transforms each element with the function.\

mylist_1  = [1, 2, 3, 4, 5, 6]

lamba_map = list(map(lambda x : x**2, mylist_1))
print(lamba_map)

# Use lambda for filter function
# filter(func, seq), returns all elements for which func evaluates to True.
lambda_filter = list(filter(lambda x : (x%2==0), mylist_1))
print(lambda_filter)

# reduce
# reduce(func, seq), repeatedly applies the func to the elements and returns a single value.
# func takes 2 arguments.
from functools import reduce
lambda_reduce_product_list = reduce(lambda x, y : x*y, mylist_1)
print(lambda_reduce_product_list )
lambda_reduce_sum_list = reduce(lambda x, y : x+y, mylist_1)
print(lambda_reduce_sum_list)