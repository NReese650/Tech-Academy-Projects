class EncapsulationExample:
    def __init__(self):
        self.public_attribute = "Public Attribute"
        self._protected_attribute = "Protected Attribute"
        self.__private_attribute = "Private Attribute"

    def public_method(self):
        """
        Public method can be accessed from outside the class.
        """
        print("Public Method")

    def _protected_method(self):
        """
        Protected method can be accessed within the class and its subclasses.
        """
        print("Protected Method")

    def __private_method(self):
        """
        Private method can only be accessed within the class itself.
        """
        print("Private Method")

    def get_private_attribute(self):
        """
        Getter method for the private attribute.
        """
        return self.__private_attribute

    def set_private_attribute(self, value):
        """
        Setter method for the private attribute.
        """
        self.__private_attribute = value

    def use_attributes_and_methods(self):
        """
        Method to demonstrate the use of attributes and methods.
        """
        # Accessing public attribute
        print(self.public_attribute)

        # Accessing protected attribute
        print(self._protected_attribute)

        # Accessing private attribute
        print(self.__private_attribute)

        # Calling public method
        self.public_method()

        # Calling protected method
        self._protected_method()

        # Calling private method
        self.__private_method()


# Create an object of the EncapsulationExample class
obj = EncapsulationExample()

# Accessing public attribute
print(obj.public_attribute)

# Accessing protected attribute
print(obj._protected_attribute)

# Accessing private attribute 
print(obj._EncapsulationExample__private_attribute)

# Using the setter method to modify the private attribute
obj.set_private_attribute("New Private Attribute")

# Accessing the modified private attribute
print(obj.get_private_attribute())

# Calling public method
obj.public_method()

# Calling protected method
obj._protected_method()

# Calling private method (Name mangling is applied)
obj._EncapsulationExample__private_method()

# Using the method to demonstrate the use of attributes and methods
obj.use_attributes_and_methods()
