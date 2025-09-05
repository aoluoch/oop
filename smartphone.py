# Base class (Parent)
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Device: {self.brand} {self.model}"


# Child class (Inheritance + Encapsulation)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)   # Inherit brand and model from Device
        self.__storage = storage        # Private attribute (encapsulation)
        self.battery = battery

    def get_storage(self):  # Public getter for encapsulated attribute
        return f"{self.__storage} GB"

    def install_app(self, app_name):
        return f"📱 Installing {app_name} on {self.brand} {self.model}"

    def battery_status(self):
        return f"🔋 Battery: {self.battery}%"


# Create objects
phone1 = Smartphone("Apple", "iPhone 15", 256, 90)
phone2 = Smartphone("Samsung", "Galaxy S24", 512, 75)

# Demonstrate methods
print(phone1.info())
print(phone1.get_storage())
print(phone1.install_app("Instagram"))
print(phone1.battery_status())
