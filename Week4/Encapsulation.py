"""
Encapsulation means packaging data and the operations on that data
together in a way that keeps them safe and hidden from outside interference.
It's like putting your belongings in a box and only allowing specific
ways to access or modify them.

Hiding the internal structure of our class so that user can't modify it
"""

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b

t = Test(23, 34)
"""
Without encapsulation an user can access the inner variable/instance 
and can change it
"""
t.b = 45787
print(t.b)

class Car:
    def __init__(self, year, make, model, speed):
        self.__year = year
        self.__make = make
        self.__model = model
        self.__speed = speed

    def set_speed(self, speed):
        self.__speed = 0 if speed < 0 else speed

    def get_speed(self):
        return self.__speed

c = Car(2021, "Aston Martin", "s", 0)
"""
To encapsulate just add two __ in front of an attribute/variable/instance
In this case we have hidden all the attributes/instance/variable of class Car 
in this case year has became aa private variable
"""
# c.year, c.__year now I can't access the year attribute in any way

"""To access it we have specific way"""
print(c._Car__model)

"""
Here we have made Two function Public
"""
c.set_speed(-353)
print(c.get_speed())


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amt):
        self.__balance += amt

    def withdraw(self, amt):
        if self.__balance >= amt:
            self.__balance -= amt
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance

Shreyash = BankAccount(1000)
Shreyash.deposit(5000)
Shreyash.withdraw(1000)
print(Shreyash.get_balance())

"""
We are accessing the attributes through functions
and user ko pata bhi nhi hai ki aise attributes exists karte hai
"""
