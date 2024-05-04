"""
The collections module in Python implements specialized container datatypes providing alternatives to Python’s general purpose
 built-in containers, dict, list, set, and tuple.
The following tools exist:
- namedtuple : factory function for creating tuple subclasses with named fields 
- OrderedDict : dict subclass that remembers the order entries were added 
- Counter : dict subclass for counting hashable objects 
- defaultdict : dict subclass that calls a factory function to supply missing values 
- deque : list-like container with fast appends and pops on either end

In Python 3 some more modules exist (ChainMap, UserDict, UserList, UserString). See https://docs.python.org/3/library/collections.html for further references.
"""

from collections import Counter
str1 = "aaaaaaaaaaaadddddddddddddgggggggeesfsagsgetsafsdfs1346"
print(f"number of occurances of d is {str1.count('d')}")

my_counter = Counter(str1)

print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

# namedtuple
from collections import namedtuple
# create a namedtuple with its class name as string and its fields as string
# fields have to be separated by comma or space in the given string
Point = namedtuple('Point','x, y')
pt = Point(1, -4)
print(pt)
print(pt._fields)
print(type(pt))
print(pt.x, pt.y)

Person = namedtuple('Person','name, age')
friend = Person(name='Tom', age=25)
print(friend.name, friend.age)

# OrderedDicts are just like regular dictionaries but they remember the order that items were inserted.
from collections import OrderedDict
ordinary_dict = {}
ordinary_dict['a'] = 1
ordinary_dict['b'] = 2
ordinary_dict['c'] = 3
ordinary_dict['d'] = 4
ordinary_dict['e'] = 5
# this may be in orbitrary order prior to Python 3.7
print(ordinary_dict)

ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5
print(ordered_dict)
# same functionality as with ordinary dict, but always ordered
for k, v in ordinary_dict.items():
    print(k, v)
"""
    A deque is a double-ended queue. It can be used to add or remove elements from both ends. 
    Deques support thread safe, memory efficient appends and pops from either side of the deque 
        with approximately the same O(1) performance in either direction. 
    The more commonly used stacks and queues are degenerate forms of deques
        where the inputs and outputs are restricted to a single end.
"""
from collections import deque
d = deque()

# append() : add elements to the right end 
d.append('a')
d.append('b')
print(d)

# appendleft() : add elements to the left end 
d.appendleft('c')
print(d)

# pop() : return and remove elements from the right
print(d.pop())
print(d)

# popleft() : return and remove elements from the left
print(d.popleft())
print(d)

# clear() : remove all elements
d.clear()
print(d)

d = deque(['a', 'b', 'c', 'd'])

# extend at right or left side
d.extend(['e', 'f', 'g'])
d.extendleft(['h', 'i', 'j']) # note that 'j' is now at the left most position
print(d)

# count(x) : returns the number of found elements
print(d.count('h'))

# rotate 1 positions to the right
d.rotate(1)
print(d)

# rotate 2 positions to the left
d.rotate(-2)
print(d)    