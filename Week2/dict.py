"""Dictionary"""
dictionary = {
    "key": "value",
    "key1": "Value replaced"
}
print(dictionary)
print(dictionary["key"])

# If key is repeated the last key formed will replace/overwrite the value of the last key present

dictionary["Mentor"] = ["Teacher"]
print(dictionary)

print(list(dictionary.keys()))
print(list(dictionary.values()))

# Returns a tuple of key: value pairs
print(list(dictionary.items()))

"""Delete"""
del dictionary["Mentor"]
print(dictionary)

dictionary.pop("key")
# In dictionary, we always have to specify the key which we have to pop
print(dictionary)

l = [11, 3, 45, 5, 6, 7, "Shreyash", "Singh"]
l1_num = []
l2_str = []
for i in l:
    if type(i) == int or type(i) == float:
        l1_num.append(i)
    else:
        l2_str.append(i)
print(l1_num, l2_str)

d7 = {}
d7 = d7.fromkeys([1, 3, 4])
print(d7)
