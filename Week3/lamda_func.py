"""Lamda Function"""
n = 3
p = 2
def test(n, p):
    return n**p

print(test(n, p))

# One-liner function/ anonymous function
a = lambda n, p: n**p
print(a(3, 2))

add = lambda x, y: x+y
print(add(2, 3))

c_to_f = lambda c: (9/5) * c + 32
print(c_to_f(45))

max = lambda x, y: x if x > y else y
print(max(3, 5))

len_s = lambda b: len(b)
print(len_s("Shreyash"))
