l = [1, 345, 45, "Shreyash", True, 5+5j, 345.1]
print(l[0:3])
print(l[::-1])
s = "PwSkills"
print(list(s) + l)

print(l[3][0:2])

l1 = [3, 4, 5]
print(l + l1)

print(l1 * 3)

print(len(l))

l.append(5)
print(l)

l.extend("SH")
print(l)

"""It iterates the object and and add to list,
it just separates the object by its index and will add to list.
used for iterable objects only"""

l.extend([3, "Shreyash", 5])
"""[1, 345, 45, 'Shreyash', True, (5+5j), 345.1, 5, 's', 'h', 3, 4, 5]"""
"""[1, 345, 45, 'Shreyash', True, (5+5j), 345.1, 5, 'S', 'H', 3, 'Shreyash', 5]"""
print(l)

l1.insert(1, [3, 4, 5])
print(l1)

l1.insert(-1, 34)
print(l1)

'''Remove data with reference to index'''
l1.pop(2)
print(l1)
l1.pop()
print(l1)

"""Removes value"""
l1.remove(3)
print(l1)

l1[0].remove(3)
print(l1)

l1.reverse()
print(l1)

l3 = [2, 7, 4, 32, 1, 13, 5, 6]
l3.sort()
print(l3)

l4 = ["shreyash", "Singh", "AI&DS"]
l4.sort(reverse=True)
print(l4)

print(l4.index("AI&DS"))

print(l4.count("AI&DS"))

"""Tuples"""
t = (12, "fje", [2, 3, 3, 11])
#  Tuples me do hi function use hota hai that is count and index
print(t[0])
print(t[::-1])

"""SET"""
# Removes all the duplicate data
s1 = {}
print(type(s1))
# It only takes immutable objects it won't take list, but it will take tuple
s2 = {1, 3, 4, 5, 67, 4}
print(type(s2))

s4 = {2, 3, 4, 56, 76, 78, 9, 34, 4, 2, 2, 5, 54, 6, 65, 75, 7, 3, 4, 2}
print(s4)

"""Set never arrange/Sort the data"""
l6 = [2, 3, 4, 56, 76, 78, 9, 34, 4, 2, 2, 5, 54, 6, 65, 75, 7, 3, 4, 2]
l6 = set(l6)
print(list(l6))

'''set object is not subscriptable print(l6[0])'''
s4.add(433)
s4.remove(4)
print(s4)
