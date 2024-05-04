# basic

list_1 = [1,2,3,4,5,6,7,8,9]

# index based
dict_compr = {x:y for x, y in enumerate(list_1)}
print(dict_compr)

# statement based
dict_compr_1 = {x:x**2 for x in list_1}
print(dict_compr_1)

# dollar to rupees
dollar_price = {"milk": 1.02, "coffee": 2.5, 'cake' : 2.5}
rupee_price = {item:value*82.5 for item, value in dollar_price.items()}
print(f"dollar prices {dollar_price}")
print(f"rupee prices {rupee_price}")

# if-else Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict = {key:('old' if value > 55 else 'young') for key, value in original_dict.items()}
print(f"original dict {original_dict}")
print(f"new dict {new_dict}")