"""In Python, a class method is a special method that is bound to
 the class rather than an instance of the class. It is defined using
 the @classmethod decorator and takes the class itself as the first
 parameter, conventionally named cls."""

"""
A class method is a type of method in programming that belongs to the 
class itself rather than an instance of the class. It can be called on
the class directly and operates on class-level variables and attributes.
In simpler terms, a class method is like a special function that can
access and modify class-level data, but it doesn't require creating an
object or instance of the class.
"""

class PwSkills:

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def student_details(self):
        print(self.name, self.email)

pw = PwSkills("Shreyash", "@gmail.com")
print(pw.name)
pw.student_details()

""" With help of class-method we overload the __init__() """
class PwSkills1:

    def __init__(self, name, email):
        """
        In Python, "overloading" refers to the ability to define multiple
        methods or functions with the same name but different parameters
        or argument types. This concept is known as "function overloading.
        " However, Python does not natively support function overloading
        like some other programming languages such as Java or C++.
        """
        self.name = name
        self.email = email

    @classmethod
    def details(cls, name, email):
        # This is a class method
        # It takes the class itself as the first parameter (cls)
        # It can be used to create an instance of the class using alternative constructors
        """
        Here @class method will decorate detail() in such way, instead of calling __init__
        for passing data we can use details(), and data will be available throughout the class
        And will be able to access class method without creating an object
        """
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email)

""" Without object creation here we are able to pass data """
pw1 = PwSkills1.details("shreyash", "email")
pw1.student_details()
print(f"####{pw1.name}####")


class PwSkills2:
    # Class variable
    mobile_number = 912324242

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def change_mb_no_(cls, mb_no):
        PwSkills2.mobile_number = mb_no

    @classmethod
    def details(cls, name, email):
        """cls ek alag se reference/pointer bana liya hai
        jo ki directly class se bind karega"""
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email, PwSkills2.mobile_number)

print(PwSkills2.mobile_number)
PwSkills2.change_mb_no_(999999999)
print(PwSkills2.mobile_number)

pw = PwSkills2.details("Shreyash Singh", "emaiak")
pw.student_details()

pw_obj = PwSkills2("Ansh", "efafa")
pw_obj.student_details()


class PwSkills3:
    # class variable
    mobile_number = 912324242

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def change_mb_no_(cls, mb_no):
        PwSkills2.mobile_number = mb_no

    @classmethod
    def details(cls, name, email):
        """cls ek alag se reference/pointer bana liya hai
        jo ki directly class se bind karega"""
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email, PwSkills2.mobile_number)

"""Attaching external function to ur class"""
def course_detail(cls, course_name):
    print(f"course name is {course_name}")
# This way we attach
PwSkills3.course_detail = classmethod(course_detail)
PwSkills3.course_detail("DSM")

def mentor(cls, list_of_mentor):
    print(list_of_mentor)

PwSkills3.mentor = classmethod(mentor)

PwSkills3.mentor(["sudh sir", "Krish sir"])

"""Deactivating class function"""
del PwSkills3.change_mb_no_

# PwSkills3.change_mb_("ddwdw")

delattr(PwSkills3, "details")

# PwSkills3.details()

delattr(PwSkills3, "student_details")

delattr(PwSkills3, "mobile_number")

# print(PwSkills3.mobile_number)
