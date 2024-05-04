basket = [1, 2, 3, 4]
basket1 = [5, 6, 7, 8, 9]
# list operations
"""
Accessing Elements:
Example: my_list[0] accesses the first element of the list my_list.
Appending:
Example: my_list.append(5) adds the number 5 to the end of my_list.
Inserting:
Example: my_list.insert(2, "apple") inserts the string "apple" at index 2 in my_list.
Removing:
Example: my_list.remove("apple") removes the string "apple" from my_list.
Slicing:
Example: subset = my_list[1:4] creates a new list containing elements at indices 1, 2, and 3 from my_list.
Concatenating:
Example: combined_list = list1 + list2 combines list1 and list2 into combined_list.
Sorting:
Example: my_list.sort() sorts my_list in ascending order.
"""

basket.extend(basket1)
print(basket)

print(basket.index(5))
print(5 in basket)
print(basket.count(5))

basket = ['a', 'c', 'b', 'a', 'i', 'e', 'd', 'f', 'g']
#basket.sort()
print(basket)
# sorted() produces a new array
print(sorted(basket))
basket.sort()
basket.reverse()
print(basket)

# list slicing
print(basket[::-1])

#range
list1 = list(range(1, 100))
list2 = list(range(0, 100, 2))
print(list1)
print(list2)

# join operation
str1 = " ! "
str2 = str1.join(["hi", "mime", "py"])
print(str2)

# list unpacking
list2 = [1, 2, 3]
a, b, c = [1, 2, 3]
print(a, b, c)

a, b, c, *d = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a, b, c)
print(d)