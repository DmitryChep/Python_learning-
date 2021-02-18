class PatDog:
    prop = dict(breed='Laika',
                color='black',
                age=6
                )

    def __init__(self, name):
        print(f'Name: {name}\n{self.prop}')
        self.name = name
        print(name)

    def voice(self):
        print(f'Voice {self.name}: "Gaf!", "Gaf!", "Gaf!", "Gaf!"\n')
