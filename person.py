import random

class Persons:
    def __init__(self,name):
        self.name=name


class Teacher(Persons):
    def __init__(self, name,subject):
        super().__init__(name)
        self.subject=subject

        

    def teach(self):
        pass


    def take_exam(self,subject,students):
        for student in students:
            marks=random.randint(70,100)
            #todo: set marks for the subject for each student


class Student(Persons):
    def __init__(self, name,classroom):
        super().__init__(name)
        self.__id=None
        self.classroom=classroom
        self.marks={}
        self.grades={}
        self.points={}
        self.final_grade=None
        self.final_point=None

    @property
    def id(self):
        return self.__id
    
    @id.setter

    def id(self,value):
        self.__id=value