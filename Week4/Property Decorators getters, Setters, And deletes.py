"""
Property decorators are a feature in Python that allow you to define special
behavior for accessing, setting, and deleting attributes of a class.
They are useful for implementing computed properties, data validation,
and encapsulation.
- -> Private
__ -> Protected
"""
class PwSkills:

    def __init__(self, course_price, course_name):
        self.__course_price = course_price
        self.course_name = course_name

    @property
    def course_price_access(self):
        """@property: This decorator is used to define a getter method for a property.
        When applied to a method within a class, it allows you to access the method
        like an attribute without invoking it explicitly. It provides a way to
        define computed properties."""
        return self.__course_price

    @course_price_access.setter
    def course_price_set(self, price):
        """@<property_name>.setter: This decorator is used to define a setter method for
         a property. It allows you to customize the behavior when assigning a value
         to the property."""
        if price <= 3500:
            pass
        else:
            self.__course_price = price

    @course_price_access.deleter
    def course_price_delete(self):
        """@<property_name>.deleter: This decorator is used to define a deleter method for
         a property. It allows you to customize the behavior
         when deleting the property."""
        del self.__course_price



pw = PwSkills("3500", "DSM")

# Getter
print(pw.course_name)
print(pw.course_price_access)

# Setter
pw.course_price_set = 4500
print(pw.course_price_access)

# Deleter
del pw.course_price_delete

"""
Property decorators provide a way to control attribute access and enable you 
to define computed properties with custom getter, setter, and deleter methods. 
They help in implementing cleaner and more maintainable code by encapsulating 
attribute logic within the class.
"""
