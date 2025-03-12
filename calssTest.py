class student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"Math":0,"English":0,"Science":0}
    def set_grade(self,subject,grade):
        self.grades[subject] = grade
    def print_grade(self):
        for subject,grade in self.grades.items():
            print(subject,":",grade)



student1 = student("John",1)
#student1.print_grade()
student1.set_grade("Math",90)
#student1.print_grade()
print(student1.name)
fo