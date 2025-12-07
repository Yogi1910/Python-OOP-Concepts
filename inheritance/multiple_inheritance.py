from basics.classes_and_objects import User


class ContactInfo:
    def __init__(self,email,address):
        self.email = email
        self.address = address


    def show_contact(self):
        return f"Email : {self.email}, Address : {self.address}"



class Employee(User, ContactInfo):
    def __init__(self, name, phone, email, address, employee_id):
        User.__init__(self, name , phone)
        ContactInfo.__init__(self, email, address)
        self.employee_id = employee_id


    def show_employee(self):
        return f"{self.name} ({self.phone}) - ID: {self.employee_id}\n{self.show_contact()}"




if __name__ == "__main__":
    emp = Employee("Yogesh", "1234567890", "yogesh@example.com", "123 Main St", "E101") 
    print(emp.show_employee()) 
    print(f"\nMRO: {[cls.__name__ for cls in Employee.__mro__]}")