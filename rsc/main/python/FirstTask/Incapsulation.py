class Person:
    def __init__(self, name):
        self.name = name
        self.__age = 30  # _var модификатор доступа: Protected(Не стого, по соглашению...)
        # self.__age = 30  #__var модификатор доступа: Private

    def proper(self):
        print(f'Name:{self.name} Age:{self.__age}\n')

    # def get_age(self):
    #     return self.__age
    #
    # def set_age(self, value):
    #     self.__age = value
    #     return value

    @property  # Getter
    def age(self):
        return self.__age

    @age.setter  # Setter
    def age(self, value):
        self.__age = value
        return value
