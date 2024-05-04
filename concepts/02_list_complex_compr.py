# list comprehensions - filtering
list_compr = [x for x in range(10) if x % 2 == 0]
print(list_compr)

list_compr1 = [(x, x**3) for x in range(10)]
print(list_compr1)

# flat-list from nested list
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
flat_list = [num for sublist in nested_list for num in sublist]
print(flat_list)

# list - zip comprehension
list1 = [1, 2, 3]
list2 = ["A", "B", "C"]
list_zip = [x for x in zip(list1, list2)]
print(list_zip)

# list compreshensions with conditionals
# ex - squares for even, cubes for odd
list3 = list(range(1, 10))
print(list3)
conditionals_list = [num**2 if num%2==0 else num**3 for num in list3]
print(conditionals_list)

# list comprehensions - matrix transpose
# rows to matrix vice versa
list_matrix=[[1,2,3],
             [4,5,6],
             [7,8,9]]

list_matrix_transpose = [[row[i] for row in list_matrix] for i in range(len(list_matrix))]
print(list_matrix)
print(list_matrix_transpose)
