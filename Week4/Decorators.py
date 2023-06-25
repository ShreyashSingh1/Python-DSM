import time
def test():
    print('This is start of my function')
    print("This my function to test")
    print(3+4)
    print('This is end of my function')

# test()

def decorate(func):
    """
    Here in decorator function, inner_dec executes automatically
    as soon as the code reaches the line @decorate i.e., line no.21
    """
    def inner_dec():
        print('This is start of my function')
        func()
        print('This is end of my function')

    return inner_dec

@decorate
def test1():
    print(444+9)

"""As soon we call the test1() function the decorator pass 
the test1 to decorate() and execution of code takes place"""

test1()

"""
In Python, decorators are implemented as functions that take a function as input 
and return a new function with additional functionality. The inner_dec function, 
defined within the decorate decorator, is the new function 
that includes the added behavior.
"""

def timer_test(func):
    def timer_test_inner():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    """
    By returning timer_test_inner, the decorator effectively replaces the original 
    function (test2 in this case) with the decorated version (timer_test_inner). 
    This means that when you later call test2(), it will be the 
    decorated version that gets executed.
    """
    return timer_test_inner
"""
If you don't return timer_test_inner, the decorator won't be able to replace the 
original function with the modified version, and the decorated behavior wouldn't
be applied when you call the function.
"""

@timer_test
def test2():
    print(24+345)

test2()

@timer_test
def test3():
    for i in range(100000):
        pass

test3()
