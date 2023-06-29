import abc

"""
Abstract class is used to create Skeleton/blueprint/outline of class.
so then u say take this as blueprint and write ur own definition/code according to this abstract/blueprint
don't forget to inherit the abstract class in ur class then only we will able toto the skeleton/blueprint
"""

class PwSkills:

    @abc.abstractmethod
    def student_details(self):
        pass

    @abc.abstractmethod
    def student_assignement(self):
        pass

    @abc.abstractmethod
    def student_marks(self):
        pass


class StudentDetail(PwSkills):
    def student_details(self):
        return "this is method for taking students detail"

    def student_assignement(self):
        return "This is meth for assignment for a particular student"


class DataScienceMasters(PwSkills):

    def student_details(self):
        return "this is method for taking students detail of datascience_masters"

    def student_assignement(self):
        return "This is meth for assignment for a particular student in DSM"

dsm = DataScienceMasters()
print(dsm.student_assignement())

sd = StudentDetail()
print(sd.student_assignement())
