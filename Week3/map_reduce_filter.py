"""MAP"""
l = [2, 3, 4, 5, 6]
def test(l):
    li = []
    for i in l:
        li.append(i**2)
    return(li)

"""map(func, *iterable)
Map function maps element of iterable to function given and 
gives output accordingly"""

sq = lambda a: a**2
print(list(map(sq, l)))

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

print(list(map(lambda x, y: x+y, l1, l2)))

def add(x, y):
    return x + y

# It will pass these iterables to function accordingly
print(list(map(add, l1, l2)))

s = "shreyash"

upper_f = lambda a: a.upper()
print(list(map(upper_f, s)))


"""Reduce"""
from functools import reduce
l2 = [1, 2, 3, 3, 4, 5]

"""
it will collapse all item will return a single item
reduces no. of element one by one
you can only pass two parameters in reduce it won't allow 3 parameters
"""

print(reduce(lambda x, y: x + y, l2))
print(reduce(lambda x, y: x + y, [1]))
# Mapping aur storing aur comparison ka kaam reduces func kud dek lega
print(reduce(lambda x, y: x if x > y else y, l2))


"""Filter"""
print(list(filter(lambda x: x if x % 2 == 0 else None, l2)))
print(list(filter(lambda x: x if x % 2 != 0 else None, l2)))

print(list(filter(lambda x: x % 2 != 0, l2)))

print(list(filter(lambda x: x if x < 0 else None, [-1, 3, 5, 5])))
print(list(filter(lambda x: x < 0, [-1, 3, 5, 5])))

st = ["Shreyash", "hi"]
print(list(filter(lambda x: len(x) < 6, st)))
