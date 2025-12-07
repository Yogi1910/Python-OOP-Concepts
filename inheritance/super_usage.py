from basics.classes_and_objects import User


class Manager(User):
    def __init__(self, name, phone, department):
        super().__init__(name, phone)
        self.department = department

    def show_info(self):
        return f"Manager: {self.name}, Phone: {self.phone}, Department: {self.department}"


class SeniorManager(Manager):
    def __init__(self, name, phone, department, team_size):
        super().__init__(name, phone, department)
        self.team_size = team_size

    def show_info(self):
        base_info = super().show_info()
        return f"{base_info}, Team Size: {self.team_size}"


if __name__ == "__main__":
    manager = Manager("Alice", "9876543210", "Engineering")
    print(manager.show_info())

    senior = SeniorManager("Bob", "5555555555", "Product", 15)
    print(senior.show_info())
