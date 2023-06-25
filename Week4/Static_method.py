class PwSkills:

    def student_details(self, name, email):
        """
        -> Self is a way for an object (or instance) of a
        class to refer to itself. When you create an object from a class,
        self is used inside the class methods to access and modify the object's attributes.
        Think of self as a placeholder or a reference to the object itself.
        It allows the object to keep track of its own data and perform
        actions on itself.
        """
        print(name, email)

pw = PwSkills()
pw.student_details("name", "@gmail.com")

class PwSkills1:

    def student_details(self, name, email):
        print(name, email)

    @staticmethod
    def mentor_class(list_mentor):
        """
        -> Aisa function jisko hum bina object create kiye
            access kar paye
        -> No need to bind it as we do for class method
        -> It is used to create utilities
           - Database connectivity
           - File Communication
           - Database storage
        -> These type of functions is used again an again
        -> These function is not generated for every instance of this class
        """
        print(list_mentor)

    def mentor(self, mentor_list):
        print(mentor_list)

# This function will be created, as we create an object form this class


PwSkills1.mentor_class(["Shreyash", "Ansh"])

student1 = PwSkills1()
student2 = PwSkills1()
student3 = PwSkills1()
"""
If we are using same data for n objects then declare the method as static
"""

class PwSkills2:

    def student_details(self, name, email):
        print(name, email)

    @staticmethod
    def mentor_id(mail_id):
        print(mail_id)


    @staticmethod
    def mentor_class(list_mentor):
        print(list_mentor)
        PwSkills2.mentor_id(["@h2", "@flf"])

    @classmethod
    def class_name(cls):
        cls.mentor_class(["Shreyash", 'Ansh1'])

    def mentor(self, mentor_list):
        print(mentor_list)
        self.mentor_class(["as", "kr"])

"""Using Static method inside a class method """
PwSkills2.class_name()
PwSkills2.mentor_class(["S", "a"])

pw = PwSkills2()
pw.mentor(["Shreyash"])

"""
Difference between static and class method
Static methods and class methods are both types of methods that belong to a class rather than to an instance of the
class. However, they have some key differences in terms of behavior and usage:

Accessing class attributes: Static methods cannot access or modify any instance-specific data or attributes of the 
                            class. They can only work with the data passed as parameters or other static members of 
                            the class. On the other hand, class methods have access to both the class-level attributes 
                            and the instance attributes through the cls parameter, which represents the class itself.

Bound to the class: Static methods are bound to the class itself and do not have access to the instance or the ability
                    to modify instance-specific data. They are primarily used for utility functions or operations that
                    are independent of any specific instance. Class methods, however, are bound to the class and have 
                    access to both the class-level data and the instance data. They are often used to create alternate 
                    constructors or perform operations that involve the class itself.

Method invocation: Static methods are called directly on the class itself, without the need to create an instance. 
                   They are invoked using the class name, such as ClassName.static_method(). Class methods, on the
                   other hand, are typically called on the class itself and can also be called on instances. 
                   They are invoked using the class name or an instance, such as ClassName.class_method() or 
                   instance.class_method().
"""
