"""Object-Oriented Programming System"""
# Class -> is something which classify real world entity
# Blueprint of real world entity
# Object/Variable/instance -> real world entity

class Test:
    pass

a = Test()

class PwSkills:
    def welcome_msg(self):
        print("welcome")

shreyash = PwSkills()
shreyash.welcome_msg()

class PwSkills1:
    def __init__(self, age, Phone, email):
        """It will make object specific data"""
        self.age = age
        self.Phone = Phone
        self.email = email

    def return_detail(self):
        return self.email, self.Phone, self.age

Ansh = PwSkills1(12, 999, "@gmail")
print(Ansh.return_detail())

Gaurav = PwSkills1(18, 9999, "@13")
print(Gaurav.return_detail())

"""Self behaves as a pointer to a class which points and object to the class it belongs"""
