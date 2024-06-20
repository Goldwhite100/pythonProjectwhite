
# A class is a blueprint of an object.
# Object is an instance of a class
class Person:
       #Property/Attribute/Variable/Characteristic
        name = "Patrick"
        age = 18
        height = 2.1

        # Method/Function/Behaviour
        def walk(self):
            print("Person is walking")

accountant = Person() # Creatingb an object
accountant.walk()

teacher = Person()
teacher.walk()