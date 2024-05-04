# basic, parentheses are optional
tuple_1 = (0,1,2,"hello", True)
tuple_2 = 0,1,2,"hello", True
print(tuple_1)
print(tuple_2)
"""
Accessing Elements:
Example: my_tuple[0] accesses the first element of the tuple my_tuple.
Concatenating:
Example: combined_tuple = tuple1 + tuple2 combines tuple1 and tuple2 into combined_tuple.
Counting:
Example: count = my_tuple.count(5) counts the number of occurrences of the value 5 in my_tuple.
Indexing:
Example: index = my_tuple.index("apple") returns the index of the first occurrence of "apple" in my_tuple.

"""
# memory and execution times of lists and tuple for same data
import sys
import timeit

my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(f"mem of list :  {sys.getsizeof(my_list)} bytes \nmem of tuple:  {sys.getsizeof(my_tuple)} bytes")

# compare the execution time of a list vs. tuple creation statement
print(f"execution time of list creation statement : {timeit.timeit(stmt='[0,1,2,3,4,5,6]', number=10000000)}")
print(f"execution time of tuple creation statement : {timeit.timeit(stmt='(0,1,2,3,4,5,6)', number=10000000)}")
