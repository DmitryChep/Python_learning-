import Incapsulation, Dog, Cat

# dog = Dog.PatDog('"Sharik"')
# dog.voice()
# dog = Cat.PatCat('"Murka"')
# dog.voice()

person = Incapsulation.Person('Oksana')
# print(person._Person__age)  # Получает Private поле.
person.proper()
person.age = 10
print(person.age)
