class Employee:
    def __init__(self):
        self.emp_id = input("Enter Employee ID: ")
        self.emp_name = input("Enter Employee Name: ")

class Salary(Employee):
    def __init__(self):
        super().__init__()
        self.basic_salary = int(input("Enter Basic Salary: "))
        self.bonus = int(input("Enter Bonus: "))

    def total_salary(self):
        total = self.basic_salary + self.bonus
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Basic Salary:", self.basic_salary)
        print("Bonus:", self.bonus)
        print("Total Salary:", total)

obj = Salary()
obj.total_salary()

class Vehicle:
    def __init__(self):
        self.brand = input("Enter Brand: ")
        self.model = input("Enter Model: ")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.fuel_type = input("Enter Fuel Type: ")
        self.seating_capacity = int(input("Enter Seating Capacity: "))

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)
        print("Seating Capacity:", self.seating_capacity)

obj = Car()
obj.display()


