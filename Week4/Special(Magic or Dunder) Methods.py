"""
Dunder functions, also known as magic methods or special methods,
are special functions in Python that have names starting and ending with double underscores (e.g., __init__, __str__).
These functions allow you to customize how objects behave in certain situations.
Overall, dunder functions give you the power to customize the behavior of your objects in
Python by defining these special methods with their specific names and purposes.
"""

print(dir(int))
print(dir(str))

a = 100
print(a + 5)
print((a.__add__(5)))

class PwSkills:
    """__init__ calls __new__ before it"""
    def __new__(cls):
        print("This is my new")

    def __init__(self):
        print("This is my init")
        self.mobile = 23242

"""In general magic function ko use nhi karte hai"""
pw = PwSkills()
# print(pw.mobile)

class PwSkills1:
    def __init__(self):
        self.mobile = 23242

    def __str__(self):
        return "This is my magic call for str"



pw1 = PwSkills1()
print(pw1)
""" 
>> <__main__.PwSkills1 object at 0x0000021D4F70DE10>
>> This is my magic call for str
"""

