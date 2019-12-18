class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_tricks(self, trick):
        self.tricks.append(trick)


d = Dog('fido')
e = Dog('buddy')
d.add_tricks("roll over")
e.add_tricks("play Dead")

print(d.tricks)
print(e.tricks)
