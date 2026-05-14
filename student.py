class Student:
    def __init__(self,name,roll,marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display_grade(self):
        if self.marks>=90:
            grade = 'A+'
        elif self.marks >= 75:
            grade = 'A'
        elif self.marks >= 60:
            grade = 'B'
        elif self.marks >= 45:
            grade = 'C'
        else:
            grade = 'F'
        print(f"Name: {self.name} | Roll: {self.roll} | Marks: {self.marks} | Grade: {grade}")


s = Student("Milan",101,93)
s.display_grade()