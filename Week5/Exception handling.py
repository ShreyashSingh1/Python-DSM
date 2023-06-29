"""Handling errors and exceptions"""
# FileNotFound
try:
    # Something that might cause an exception
    file = open("a_file.txt")
    a_dict = {"key": "Value"}
    # print(a_dict["Sefasf"])

except FileNotFoundError:
    # Do this if there was an exception
    file = open("a_file.txt", "w")
    file.write("Something")

except KeyError as error_mess:
    print(f"That key {error_mess} does not exists.")

else:
    # Do this there were no exceptions
    content = file.read()
    print(content)

finally:
    # Do this no matter what
    file.close()
    print("file was close")


"""Custom exception handling"""
class ValidateHeight(Exception):

    def __init__(self, msg):
        self.msg = msg

def validate_height(h):
    if h > 3:
        raise ValidateHeight("human height should not be greater than 3 meter")

try:
    height = float(input("Height: "))
    weight = float(input("Weight: "))
    validate_height(height)

except ValidateHeight as e:
    print(e)

else:
    bmi = weight / height ** 2
    print(bmi)


class ValidateAge(Exception):
    def __init__(self, msg):
        self.msg = msg

def validate_age(age):
    if age < 0:
        raise ValidateAge("Age entered is negative")
    elif age > 200:
        raise ValidateAge("Entered age is very high")
    else:
        print("Age is valid")

try:
    age = int(input("Enter your age"))
    validate_age(age)

except ValidateAge as e:
    print(e)

