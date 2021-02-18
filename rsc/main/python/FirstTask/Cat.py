class PatCat:
    prop = dict(breed='persian',
                color='white',
                age=3
                )

    def __init__(self, name):
        print(f'Name: {name}\n{self.prop}')
        self.name = name
        print(name)

    def voice(self):
        print(f'Voice {self.name}: "May!", "May", "May!", "May!"\n')