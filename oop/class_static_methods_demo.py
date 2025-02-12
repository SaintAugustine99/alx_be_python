#Definition of Calculator class, including a static and class method to perform calculations.  

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b

    # Class method to multiply two numbers
    @classmethod
    def multiply(cls, a, b):
        # Print the class attribute
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
