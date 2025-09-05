# Parent class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Child classes with polymorphism
class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road"


class Plane(Vehicle):
    def move(self):
        return "✈️ Flying in the sky"


class Boat(Vehicle):
    def move(self):
        return "⛵ Sailing on the water"


# Demonstrate polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
