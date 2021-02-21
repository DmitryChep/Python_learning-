class Person1:
    def __init__(self, name, class_level, age, instrument):
        self.name = name
        self.class_level = class_level
        self.age = age
        self.__instrument = instrument

    def get_person(self):
        print(f'Name: {self.name} level: {self.class_level} age: {self.age} instrument {self.__instrument}')


class Person2(Person1):
    hair = 'Short'
    def heir(self):
        print(f'Heircut: {self.hair}')
