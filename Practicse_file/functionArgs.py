class calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
calc = calculator()
print(calc.add(10, 5))        # Output: 15  
print(calc.subtract(10, 5))   # Output: 5
print(calc.multiply(10, 5))   # Output: 50

def greet(*names):
    """Prints a greeting to each person in the tuple of names."""
    for name in names:
        print(f"Hello, {name}!")

greet("Alice", "Bob", "Charlie")
# Output:
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!

def calculate_sum(*args):
    """Calculates the sum of an arbitrary number of arguments."""
    total = 0
    for num in args:
        total += num
    return total

print(f"Sum of 1, 2, 3: {calculate_sum(1, 2, 3)}") # Output: Sum of 1, 2, 3: 6
print(f"Sum of 10, 20, 30, 40: {calculate_sum(10, 20, 30, 40)}") # Output: Sum of 10, 20, 30, 40: 100

def describe_person(name, **kwargs):
    """Describes a person using keyword arguments."""
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

describe_person("Alice", age=30, city="New York", occupation="Engineer")
# Output:
# Name: Alice
# Age: 30
# City: New York
# Occupation: Engineer

describe_person("Bob", age=25, hobby="Reading")
# Output:
# Name: Bob
# Age: 25
# Hobby: Reading

def apply_operations(a, b, *args, **kwargs):
    """
    Applies various operations to a and b, and demonstrates *args and **kwargs usage.
    *args will be treated as additional numbers to add to the sum of a and b.
    **kwargs can contain 'operation' to specify an additional operation.
    """
    print(f"\nApplying operations with a={a}, b={b}")
    
    # Using *args
    sum_val = a + b
    for num in args:
        sum_val += num
    print(f"Sum including *args: {sum_val}")