# Parent class
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print("Engine started!")

    def stop_engine(self):
        print("Engine stopped!")


# Child class 1
class Car(Vehicle):
    def __init__(self, brand, color, num_doors):
        super().__init__(brand, color)
        self.num_doors = num_doors

    def drive(self):
        print(f"The {self.color} car is driving with {self.num_doors} doors.")


# Child class 2
class Motorcycle(Vehicle):
    def __init__(self, brand, color, has_sidecar):
        super().__init__(brand, color)
        self.has_sidecar = has_sidecar

    def ride(self):
        if self.has_sidecar:
            print(f"The {self.color} motorcycle with a sidecar is riding.")
        else:
            print(f"The {self.color} motorcycle is riding.")


# Create instances of the child classes
car1 = Car("Toyota", "Red", 4)
motorcycle1 = Motorcycle("Harley-Davidson", "Black", False)

# Accessing attributes and methods of the parent and child classes
print(car1.brand)  # Output: Toyota
print(motorcycle1.color)  # Output: Black

car1.start_engine()  # Output: Engine started!
motorcycle1.stop_engine()  # Output: Engine stopped!

car1.drive()  # Output: The Red car is driving with 4 doors.
motorcycle1.ride()  # Output: The Black motorcycle is riding.
