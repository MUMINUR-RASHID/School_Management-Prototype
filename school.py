class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.classrooms = {}
        self.teachers = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self,teacher):
        subject=teacher.subject
        if subject not in self.teachers:
            self.teachers[subject] = []
        self.teachers[subject].append(teacher)

    def student_admission(self, student):
        classroom_name = student.classroom.name
        if classroom_name in self.classrooms:
            self.classrooms[classroom_name].add_student(student)
        else:
            print(f'No classroom named {classroom_name}')

    def __repr__(self) -> str:
        return f"School(name={self.name}, address={self.address}, classrooms={list(self.classrooms.keys())},School_Subjects={list(self.teachers.keys())})"

class Classroom:
    def __init__(self, name):
        self.name = name
        self.subjects = None
        self.students = []
        

    def add_subject(self, subjects):
        self.subjects=subjects

    def add_student(self, student):
        st_id=f"{self.name}-{len(self.students)+1}"
        student.id=st_id
        self.students.append(student)

    def __str__(self) -> str:
        return f'Class: {self.name}, Students: {len(self.students)}'

    def get_top_students(self):
        # Sort students by grade and return the sorted list
        return sorted(self.students, key=lambda student: student.grade, reverse=True)


    #def __repr__(self) -> str:
       # return f"Student(name={self.name}, grade={self.grade}, id={self.id}, classroom={self.classroom.name})"
