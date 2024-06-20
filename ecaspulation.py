class Person:
    __name = "Bravin"

    def get_name(self):
        return self.__name


p = Person()
print(p.get_name())  # this will print John
