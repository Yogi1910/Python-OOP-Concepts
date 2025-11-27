class User:
    def __init__(self,name, phone):
        self.name = name
        self.phone = phone

if __name__ == "__main__":
    user = User(name="Yogesh", phone="1234567890")

    print(user.name)
    print(user.phone)