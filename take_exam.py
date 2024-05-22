from school import Classroom
import random


class Take_Exam:
    def __init__(self,school) -> None:
        for key,class_name in school.classrooms.items():
            for subject in class_name.subjects:
                for student in class_name.students:
                    self.get_result(subject,student)

            for student in class_name.students:
                self.get_final_result(student)
                
        
    def get_result(self,subject,student):
        mark=random.randint(70,95)
        student.marks[subject]=mark
        student.grades[subject]= self.get_grade(mark)
        student.points[subject]= self.get_point(mark)



    def get_grade(self,mark):
        if mark>=80:
            return "A+"
        elif mark>=70:
            return "A"
        elif mark>=60:
            return "A_"
        elif mark>=50:
            return "B"
        elif mark>=40:
            return "C"
        elif mark>=33:
            return "D"
        else:
            return "F"
        
    def get_point(self,mark):
        if mark>=80:
            return 5.00
        elif mark>=70:
            return 4.00
        elif mark>=60:
            return 3.50
        elif mark>=50:
            return 3.00
        elif mark>=40:
            return 2.00
        elif mark>=33:
            return 1.00
        else:
            return 0.00
        
    def get_final_result(self,student):
        subject=0
        total_point=0
        flag=True
        for key,point in student.points.items():
            if point==0.00:
                flag=False
            total_point+=point
            subject+=1
        
        final_point= total_point/subject
        if flag:
            final_grade= self.get_converted_grade(final_point)
            student.final_grade=final_grade
            student.final_point=final_point
        else:
            student.final_grade="F"
            student.final_point=0.00

    
    def get_converted_grade(self,mark):
        if mark>=5.00:
            return "A+"
        elif mark>=4.00:
            return "A"
        elif mark>=3.50:
            return "A-"
        elif mark>=3.00:
            return "B"
        elif mark>=2.00:
            return "C"
        elif mark>=1.00:
            return "D"
        else:
            return "F"