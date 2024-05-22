from school import School,Classroom
from person import Student,Teacher
from take_exam import Take_Exam

def main():
    school=School("MMR ACADEMY", 'MYMENSINGH')

    #Classroom Add
    eight=Classroom("Eight")
    school.add_classroom(eight)
    
    nine=Classroom("Nine")
    school.add_classroom(nine)
    
    ten=Classroom("Ten")
    school.add_classroom(ten)

    

    #Teacher Add
    teacher1=Teacher("Muminur Rashid","ICT")
    teacher2=Teacher("Omor Faruk","ICT")
    teacher3=Teacher("Topon","PHYSICS")
    teacher4=Teacher("Munim","PHYSICS")
    teacher5=Teacher("Haradhon","CHEMISTRY")
    teacher6=Teacher("Mubasher","CHEMISTRY")
    school.add_teacher(teacher1)
    school.add_teacher(teacher2)
    school.add_teacher(teacher3)
    school.add_teacher(teacher4)
    school.add_teacher(teacher5)
    school.add_teacher(teacher6)
    

    #Student Add
    student1=Student("Abir Khan",eight)
    school.student_admission(student1)
    student2=Student("Munib Khan",eight)
    school.student_admission(student2)
    student3=Student("Sakib Khan",nine)
    school.student_admission(student3)
    student4=Student("Rakib Khan",nine)
    school.student_admission(student4)
    student5=Student("Tuhin Khan",ten)
    school.student_admission(student5)
    student6=Student("Mahin Khan",ten)
    school.student_admission(student6)

    #Subject Add
    eight.add_subject(["PHYSICS","CHEMISTRY"])
    nine.add_subject(["ICT","PHYSICS"])
    ten.add_subject(["ICT","PHYSICS","CHEMISTRY"])

    print(school)


    Take_Exam(school)
    
    

    for key,class_name in school.classrooms.items():
        print(key,":",class_name.subjects)
        for student in class_name.students:
            print(f"Name: {student.name}, Id: {student.id}, Final_Grade:{student.final_grade}, Final_Point: {student.final_point:.2f}")
    

if __name__=="__main__":
    main()