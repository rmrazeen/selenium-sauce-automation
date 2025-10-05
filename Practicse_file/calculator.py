class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Returns the difference between two numbers."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Returns the product of two numbers."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Returns the result of the division of two numbers.
        Raises:
            ValueError: If the divisor (b) is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

# --- Usage Example ---
calc = Calculator()
print(f"{calc.add(10, 5) = }")
print(f"{calc.subtract(10, 5) = }")
print(f"{calc.multiply(10, 5) = }")
print(f"{calc.divide(10, 5) = }")

# Example of handling the division by zero error
try:
    print(f"{calc.divide(10, 0) = }")
except ValueError as e:
    print(e)