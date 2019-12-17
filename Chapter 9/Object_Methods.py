class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print("Hello my Name is " + self.name)


p1 = Person("Johan", 36)
p1.myfun()
