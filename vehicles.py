# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclass 1
class Car(Vehicle):
    def move(self):
        return "Driving on the road 🚗"

# Subclass 2
class Plane(Vehicle):
    def move(self):
        return "Flying in the sky ✈️"

# Subclass 3
class Boat(Vehicle):
    def move(self):
        return "Sailing on the water 🚢"

# Subclass 4
class Bike(Vehicle):
    def move(self):
        return "Pedaling on the path 🚴"

# Function that uses polymorphism
def vehicle_action(vehicle: Vehicle):
    print(vehicle.move())

# Test the polymorphism
vehicles = [Car(), Plane(), Boat(), Bike()]

for v in vehicles:
    vehicle_action(v)
