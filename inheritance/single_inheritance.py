from basics.classes_and_objects import User

class Employee(User):
    def __init__(self,name, phone, employee_id):
        super().__init__(name, phone)
        self.employee_id=employee_id

    def show_employee(self):
        return f"{self.name} ({self.phone}) - ID: {self.employee_id}"


if __name__ == "__main__":
    emp = Employee("Yogesh", "1234567890", "E101")
    print(emp.show_employee())