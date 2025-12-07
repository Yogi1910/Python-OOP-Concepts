from basics.classes_and_objects import User

class Admin(User):
    def get_role(self):
        return "Adminitrator"



if __name__ == "__main__":
    user = Admin(name="Yogesh", phone="1234567890")
    print(user.get_role())