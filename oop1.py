
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def details(self):
        print(self.name, "is studying")
accountant = Person("Joe",34,"Male")
print(accountant.name)
print(accountant.age)
print(accountant.gender)

consultant = Person("Martha",65,"Female")
print(consultant.name)
print(consultant.age)
print(consultant.gender)

doctor = Person("James",43,"Male")
print(doctor.name)
print(doctor.age)
print(doctor.gender)


