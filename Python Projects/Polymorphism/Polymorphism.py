# Parent class: Animal
class Animal:
    def make_sound(self):
        print("The animal makes a sound.")

# Child class 1: Cat
class Cat(Animal):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def make_sound(self):
        print("{} the {} cat says Meow!".format(self.name, self.color))

    def sleep(self):
        print("{} the {} cat is sleeping.".format(self.name, self.color))

# Child class 2: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def make_sound(self):
        print("{} the {} dog says 'Woof!'".format(self.name, self.breed))

    def fetch(self):
        print("{} the {} dog is fetching a ball.".format(self.name, self.breed)) 

# Create instances of the child classes
cat = Cat("Whiskers", "gray")
dog = Dog("Buddy", "Golden Retriever")

# Call the overridden method for each instance
cat.make_sound()  # Output: Whiskers the gray cat says 'Meow!'
dog.make_sound()  # Output: Buddy the Golden Retriever dog says 'Woof!'

# Call the additional methods specific to each child class
cat.sleep()  # Output: Whiskers the gray cat is sleeping.
dog.fetch()  # Output: Buddy the Golden Retriever dog is fetching a ball.

# Call the parent class method using polymorphism
cat.make_sound()  # Output: Whiskers the gray cat says 'Meow!' (overridden method)
dog.make_sound()  # Output: Buddy the Golden Retriever dog says 'Woof!' (overridden method)
