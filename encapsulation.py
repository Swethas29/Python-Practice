class Student:
    def __init__(self):
        self.__name = input("Enter Student Name: ")
        self.__marks = int(input("Enter Student Marks: "))

    def update_marks(self):
        self.__marks = int(input("Enter Updated Marks: "))

    def display_details(self):
        print("Student Name:", self.__name)
        print("Student Marks:", self.__marks)
obj = Student()
obj.display_details()
obj.update_marks()

print("\nUpdated Student Details:")
obj.display_details()

obj.__marks = 100
print("\nAfter Direct Modification:")
obj.display_details()
