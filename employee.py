class Employee:
    def __init__(self, name,employee_id):
        self.name = name
        self.employee_id = employee_id

    def display1(self):
        print(f"Name: {self.name}, Salary: {self.employee_id}")

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id,salary):
        super().__init__(name, employee_id)
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id,hourly_rate,time_sheet):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.time_sheet = time_sheet
    def display(self):
        salary = self.hourly_rate * self.time_sheet
        print(f"Name: {self.name}, Salary: {salary}")


employee1 = FullTimeEmployee("John",1,50000)
employee2 = PartTimeEmployee("Jane",2,50,160)
employee1.display1()
employee2.display()