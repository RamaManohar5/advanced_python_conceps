"""
A dictionary is a collection which is unordered, changeable and indexed. A dictionary consists of a collection of key-value pairs.
"""

# basic
my_dict = {"name":"Max", "age":28, "city":"New York"}
print(my_dict)

# or use the dict constructor, note: no quotes necessary for keys
my_dict_2 = dict(name="Lisa", age=27, city="Boston")
print(my_dict_2)

# loop over keys
for item in my_dict:
    print(f"key : {item}, value : {my_dict[item]}")

for key, value in my_dict.items():
    print(f"key : {key}, value : {value}")

# copy dictionaries
# this is just copies reference to the dict
# soft copy - changes made in one dict will reflect in another vice versa
my_dict3 = my_dict_2
# hard copy - changes made in one dict, will not reflect
my_dict_copy = my_dict.copy()

# merge dictionaries
my_dict4 = {'email' : "lisa@gmail.com"}
my_dict.update(my_dict4)
print(my_dict)

# nested dictionaries
my_dict_A = {"name": "Max", "age": 28}
my_dict_B = {"name": "Alex", "age": 25}
my_dict_records = {'recordA' : my_dict_A,
                   'recordB' : my_dict_B }
# another way
my_dict_records_another = dict(recordA = my_dict_A,
                               recordB = my_dict_B)

print(my_dict_records_another)
