class Car:
    def __init__(self, brand, model):  # Constructor method
        self.__brand = brand    # Private attribute
        self.model = model

    def get_brand(self):  # Getter method
        return self.__brand + " (private)"  # Accessing private variable

    def full_name(self):  # Instance method
        return f"Brand is {self.get_brand()} and model is {self.model}"

    def fuel_type(self):  # Instance method
        return self.get_brand() + " runs on Petrol"


class ElectricCar(Car):  # Inheritance
    def __init__(self, brand, model, battery_capacity):
        self.battery_capacity = battery_capacity
        super().__init__(brand, model)  # Call parent constructor

    def full_name(self):  # Overriding method
        return f"{self.get_brand()} {self.model} with {self.battery_capacity} battery"

    def fuel_type(self):  # Overriding method
        return self.get_brand() + " runs on Electricity"


# Objects
my_tesla = ElectricCar("Tesla", "Model S", "100 kWh")
my_car = Car("Toyota", "Corolla")

print(my_car.fuel_type())    # Toyota (private) runs on Petrol
print(my_tesla.full_name())  # Tesla (private) Model S with 100 kWh battery
