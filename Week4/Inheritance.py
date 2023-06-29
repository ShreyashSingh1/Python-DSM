class Test:
    def test_meth(self):
        return "This is my first class"

class ChildTest(Test):
    pass

child_object = ChildTest()
print(child_object.test_meth())

"""Multi-level inheritance"""
class Class1:
    def test_class1(self):
        return "This is meth from class one"

class Class2(Class1):
    def test_class2(self):
        return "This is meth from class two"

class Class3(Class2):
    pass

c3 = Class3()
print(c3.test_class1())

"""Multiple inheritance"""

class multiple_inheritance(Class1, Class2):
    pass

mi = multiple_inheritance()
mi.test_class1()
mi.test_class2()


