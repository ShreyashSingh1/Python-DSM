v = 1 + 5j
print(v.imag)

""" Slicing """
a = "PwSkills"
# Upper bound minus one karta hai
print(a[0:3])
print(a[0:8:2])
print(a[0:8:1])
print(a[::2])

"""In this case it takes reverse indexing and no start/end index is given and direction is negative(jump)"""
print(a[::-1])

print(a[8:0:1])

"""In this case it takes positive indexing and no start/end index is given and direction is positive(jump)"""
print(a[::1])

"""It will return an empty string"""
print(a[2:7:-1])

"""It will throw error in case of indexing """
# print(a[90])

"""It won't throw error  in case of slicing"""
print(a[:-9000:-1])

# String manipulation
print(len(a))
print(a.find("s"))
print(a.count("s"))
print(a.upper())
print(a.lower())
print(a.title())
print(a.capitalize())

b = "we"
print(b*4)
