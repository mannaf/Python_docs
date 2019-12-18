# Create a Parent Class
# Create a class named Person, with firstname and lastname properties, and a printname method
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("Abde", "Mannaf")
x.printname()


# Create a Child Class
# Create a class named Student, which will inherit the properties and methods from the Person class
class Student(Person):
    pass


y = Student("Ali", "Akbor")
y.printname()
