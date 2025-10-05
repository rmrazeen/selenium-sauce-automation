# This program defines a Calculator class and demonstrates its usage.
class Calculator:
    def __init__(self, value1, value2):
        # Constructor method to initialize the two values.
        self.value1 = value1
        self.value2 = value2

    def add(self):
        return self.value1 + self.value2
    
    def subtract(self):
        return self.value1 - self.value2
    
    def multiply(self):
        return self.value1 * self.value2
    
    def divide(self):
        if self.value2 != 0:
            return self.value1 / self.value2
        else:
            return "Error! Division by zero."

calc_instance = Calculator(10, 5)

# Addition
addition_result = calc_instance.add()
print(f"10 + 5 = {addition_result}")

# Subtraction
subtraction_result = calc_instance.subtract()
print(f"10 - 5 = {subtraction_result}")

# Multiplication
multiplication_result = calc_instance.multiply()
print(f"10 * 5 = {multiplication_result}")

# Division
division_result = calc_instance.divide()
print(f"10 / 5 = {division_result}")

# 3. Create a new instance to test division by zero.
calc_zero_division = Calculator(10, 0)
zero_division_result = calc_zero_division.divide()
print(f"10 / 0 = {zero_division_result}")
