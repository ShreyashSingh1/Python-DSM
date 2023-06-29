"""Giving data one by one, generating data rather storing it at one place"""
range(0, 10)

def test_fib(n):
    """
    In Python, the yield keyword is used in the context of generator functions.
    A generator function is a special type of function that can be paused and resumed,
    allowing it to produce a sequence of values over time instead of returning a single value like a regular function.
    When a generator function encounters a yield statement, it temporarily suspends its execution and returns
    the yielded value. The generator's state is saved so that it can be resumed from
    where it left off the next time it's called.
    """
    a, b = 0, 1
    """
    Output banaye aur dete jaye
    it optimize the entire memory utilization
    """
    for i in range(n):
        """Yield generates an object  which is iterable"""
        yield a
        '''After yield if function called again it will continue from here'''
        a, b = b, a + b

for _ in test_fib(10):
    print(_)

"""
Iterator is something/object where we can go from next element to next element and element can be accessed
iterable (access their values one by one) is something that can be converted iterator
str -> is iterable
int -> is not 
so str can be converted to iterator
and int can't
"""

def test2():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

fib = test2()
"""Yield generates an object  which is iterable"""
"""Generator is iterator"""
print(type(fib))

for i in range(10):
    """The next() Function is used to retrieve the next item from an iterator"""
    print(next(fib))

"""
An iterator in Python is like a tool that helps you go through a
collection of things, one thing at a time.
It's like a conveyor belt that brings you each item,
and you can take a look at it or do something with it before moving on to the next item.
It makes it easy to work with a bunch of things without worrying about
how they are stored or organized.
"""

s = "Shrey"
# String object is not an Iterator
# i.e u can't go automatically to next, next....
# So object were u can go next, next that is iterator

'''This how for loop works'''
# iter converts iterable object to iterator
s1 = iter(s)
print(type(s1))
# str_iterator -> object
"""The next() Function is used to retrieve the next item from an iterator"""
print(next(s1))
print(next(s1))
print(next(s1))
#String iterable

def count_test(n):
    count = 1
    while count <= n:
        yield count
        count += 1

"""Yield generates an object which is iterable"""
c = count_test(5)

print(type(c))

# Here c is iterable
for i in c:
    print(i)

# Generator is already iterator the work of next() is done by for loop itself
for i in count_test(5):
    print(i)
