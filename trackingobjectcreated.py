class Student:
    count = 0  # class variable

    def __init__(self, name):
        self.name = name
        Student.count += 1
        print(f"{self.name} created. Total objects: {Student.count}")

    def __del__(self):
        Student.count -= 1
        print(f"{self.name} deleted. Total objects: {Student.count}")

s1 = Student("Milan")
s2 = Student("Ram")
s3 = Student("Sita")
del s2
del s1