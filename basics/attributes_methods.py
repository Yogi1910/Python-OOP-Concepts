class User:
    def __init__(self,name, phone):
        self.name = name
        self.phone = phone

    def display_profile(self):
        return f"User {self.name} with phone {self.phone}"
    

if __name__ == "__main__":
    user = User(name="Yogesh", phone="1234567890")
    print(user.display_profile())