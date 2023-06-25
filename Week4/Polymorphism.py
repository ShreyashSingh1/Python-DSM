"""
One Entity with different behaviour in different circumstances
"""

def test(a, b):
    return a + b

print(test(3, 5))
# 8

print(test("Shreyash ", "Singh"))
# Shreyash Singh

"""
Here our base functions behaves differently with different data in case of int it adds
and in case of string it contacts, so our base function is not changing (test())
but its behaviour is changing  when we are giving different data so this is polymorphism
"""

class DataScience:

    def syllabus(self):
        print("Python")

class WebDev:

    def syllabus(self):
        print("HTML/CSS/JAVA")

def class_parcer(class_obj):
    for i in class_obj:
        i.syllabus()

DS = DataScience()
WD = WebDev()

class_obj = [DS, WD]
class_parcer(class_obj)

"""
Here class_parcer Function behaves differently when i pass DS class object
and WD class object and it start functioning according passed class 
So nature of our outcome is different in  different context so this is polymorphism
"""

"""
our behaviour is the biggest example of polymorphism
we behave differently in different circumstances
"""
