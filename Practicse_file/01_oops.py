class Car:
    def __init__(self, brand, model): # Constructor method
        self.__brand = brand    # Instance variable
        self.model = model

    def get_brand(self):  # Getter method
        return self.__brand + " (private)" # Accessing private variable with a getter like encapsulation

    def full_name(self):  # Instance method
        return f" Brand is {self.brand} and model is {self.model}" # Returns full name of the car
   
    def fuel_type(self): # Instance method with parameter
        return self.get_brand() + "runs on Patrol" # Returns fuel type of the car
    

class ElectricCar(Car): # Inheritance
    
    def __init__(self, brand, model, battery_capacity): # Constructor method
        self.battery_capacity = battery_capacity    # Instance variable
        super().__init__(brand, model) # Call parent constructor
    
    def full_name(self):  # Overriding method
        return f"{self.brand} {self.model} with {self.battery_capacity} battery" # Returns full name of the car
    
    def fuel_type(self):
        return self.get_brand()+ "runs on Electricity" 
    
my_tesla = ElectricCar("Tesla", "Model S", "100 kWh")  
my_car = Car("Toyota", "Corolla")
# print(my_car.brand, my_car.model)  # Output: Toyota

#print(my_car.full_name())
# print(my_tesla.full_name())  # Output: Tesla Model S
# print(my_tesla.get_brand())  # Accessing private variable using getter method

print(my_car.fuel_type())  # Output: Toyota runs on Patrol