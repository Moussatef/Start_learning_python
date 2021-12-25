class User:
    def __init__(self, name, age, national, country):
        self.name = name
        self.age = age
        self.national = national
        self.country = country


user = User("Moussatef Othman", 23, "Morcco", "Morocco")

print("Your name is : " + user.name.capitalize())
print("Your age is : " + str(user.age))
print("Your national is : " + user.national.upper())
print("Your country is : " + user.country.upper())
