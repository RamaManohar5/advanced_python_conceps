"""
A Python program terminates as soon as it encounters an error. 
In Python, an error can be a syntax error or an exception.
"""

'''
num = -4
if num < 0:
    raise Exception("num can't be negatiuve")
'''

# You can also use the assert statement, which will throw an AssertionError if your assertion is not True. 
# This way, you can actively test some conditions that have to be fulfilled instead of waiting for your program to unexpectedly crash midway. 
# Assertion is also used in unit testing.

'''
x = -5
assert( x >=0 ), 'x is not positive number'

'''

# Handling Exceptions
# You can use a try and except block to catch and handle exceptions.
# If you can catch an exceptions your program won't terminate, and can continue.

# This will catch all possible exceptions
try:
    a = 5 / 0
except:
    print('some error occured.')

# You can also catch the type of exception
try:
    a = 5 / 0
except Exception as e:
    print(e)

# It is good practice to specify the type of Exception you want to catch.
# Therefore, you have to know the possible errors 
try:
    a = 5 / 0
except ZeroDivisionError:
    print('Only a ZeroDivisionError is handled here')

# You can run multiple statements in a try block, and catch different possible exceptions
try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)

# else clause
# You can use an else statement that is run if no exception occured.
try:
    a = 5 / 1
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
else:
    print('Everything is ok')

# finally clause¶
# You can use a finally statement that always runs, no matter if there was an exception or not. 
# This is for example used to make some cleanup operations.

try:
    a = 5 / 1 # Note: No ZeroDivisionError here
    b = a + '10'
except ZeroDivisionError as e:
    print('A ZeroDivisionError occured:', e)
except TypeError as e:
    print('A TypeError occured:', e)
else:
    print('Everything is ok')
finally:
    print('Cleaning up some stuff...')