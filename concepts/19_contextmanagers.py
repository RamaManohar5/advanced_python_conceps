"""
    Context managers are a great tool for resource management.
    They allow you to allocate and release resources precisely when you want to.
    A well-known example is the with open() statemtent:
"""
with open('notes.txt', 'w') as f:
    f.write('some todo...')

f = open('notes.txt', 'w')
try:
    f.write('some todo...')
finally:
    f.close()

# Examples of context managers
# Open and close files
# open and close database connections
# Acquire and release locks:

# handling exceptions
# If an exception occurs, Python passes the type, value, and traceback to the __exit__ method.
# It can handle the exception here.
# If anything other than True is returned by the __exit__ method, then the exception is raised by the with statement.

class ManagedFile:
    def __init__(self, filename):
        print('init', filename)
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exc:', exc_type, exc_value)
        print('exit')

# No exception
with ManagedFile('notes.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
print('continuing...')

print()

# Exception is raised, but the file can still be closed
with ManagedFile('notes2.txt') as f:
    print('doing stuff...')
    f.write('some todo...')
    #f.do_something()
print('continuing...')

# Implementing a context manager as a generator
# Instead of writing a class, we can also write a generator function and decorate it with the contextlib.contextmanager decorator.
# Then we can also call the function using a with statement. 
# For this approach, the function must yield the resource in a try statement, and all the content of the __exit__ method to free up the resource goes now inside the corresponding finally statement.

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todo...')

