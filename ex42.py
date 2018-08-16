## Animal is-a object
class Animal(object):
    
    type = "Animal"
    def __init__(self):
        self.type = "Animal"

    def printSomething(self):
        print("父类的方法可以由子类直接调用")

## Dog is-a Animal
class Dog(Animal):
    
    def __init__(self, name):
        ## Dog has-a init
        self.name = name

    def printType(self):
        my_type = super().type
        print(my_type)

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a init
        self.name = name
        # 调用父类的 init 方法
        super().__init__()

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a init
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

##
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is a Person
mary = Person("Mary")

## mary has-a pet, pet is-a Cat
mary.pet = satan

## frank is-a Employee is-a Person
frank = Employee("Frank", 120000)

## frank has-a pet, pet is-a Dog
frank.pet = rover

## flipper is-a Fish
filipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()

satan.printSomething()
rover.printType()