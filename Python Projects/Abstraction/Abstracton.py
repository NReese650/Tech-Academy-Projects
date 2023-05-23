from abc import ABC, abstractmethod

# Parent class with an abstract method
class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def regular_method(self):
        return "This is a regular method"

# Child class that inherits from the parent class
class ChildClass(AbstractClass):
    def abstract_method(self):
        return "Implementation of abstract method in the child class"

# Create an object and utilize both parent and child methods
obj = ChildClass()
print(obj.abstract_method())  # Output: Implementation of abstract method in the child class
print(obj.regular_method())   # Output: This is a regular method
