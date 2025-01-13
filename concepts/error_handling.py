# 1. Basic Try-Except
print("\n1. Basic Try-Except:")
try:
    x = 1 / 0  # Raises ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")

# 2. Multiple Exception Handling
print("\n2. Multiple Exceptions:")
try:
    # Could raise different exceptions
    number = int("abc")  # ValueError
    result = 10 / 0      # ZeroDivisionError
except ValueError as ve:
    print(f"ValueError occurred: {ve}")
except ZeroDivisionError as zde:
    print(f"ZeroDivisionError occurred: {zde}")
except Exception as e:
    print(f"Some other error occurred: {e}")

# 3. Try-Except-Else-Finally
print("\n3. Try-Except-Else-Finally:")
try:
    number = int("123")
except ValueError:
    print("Invalid number!")
else:
    print(f"Conversion successful! Number is {number}")
finally:
    print("This always executes!")

# 4. Raising Exceptions
print("\n4. Raising Exceptions:")
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems too high!")
    return f"Age is valid: {age}"

try:
    print(validate_age(200))
except ValueError as e:
    print(f"Validation Error: {e}")

# 5. Custom Exceptions
print("\n5. Custom Exceptions:")
class CustomError(Exception):
    """Custom error class"""
    def __init__(self, message, error_code):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

try:
    raise CustomError("Something went wrong!", 500)
except CustomError as ce:
    print(f"Custom Error (code {ce.error_code}): {ce.message}")

# 6. Context Managers (with statement)
print("\n6. Context Managers:")
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type:
            print(f"An error occurred: {exc_val}")
        return True  # Suppress any exceptions

# Using context manager
try:
    with FileManager('test.txt', 'w') as file:
        file.write("Hello, World!")
        raise Exception("Test exception")
except Exception as e:
    print(f"Caught exception: {e}")

# 7. Assert Statements
print("\n7. Assert Statements:")
def calculate_square_root(number):
    assert number >= 0, "Number must be non-negative!"
    return number ** 0.5

try:
    print(calculate_square_root(-5))
except AssertionError as ae:
    print(f"Assertion Error: {ae}")

# 8. Exception Chaining
print("\n8. Exception Chaining:")
try:
    try:
        raise ValueError("Original error")
    except ValueError as e:
        raise RuntimeError("Subsequent error") from e
except RuntimeError as e:
    print(f"Error chain: {e.__cause__}")

# 9. Exception Groups (Python 3.11+)
print("\n9. Exception Handling Patterns:")
def process_data(data):
    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary")
    if "value" not in data:
        raise KeyError("Missing 'value' key")
    if data["value"] < 0:
        raise ValueError("Value must be non-negative")

try:
    process_data({"value": -5})
except (TypeError, KeyError) as e:
    print(f"Data format error: {e}")
except ValueError as e:
    print(f"Data validation error: {e}")

# 10. Clean-up Actions
print("\n10. Clean-up Actions:")
def resource_manager():
    try:
        print("Resource acquired")
        raise Exception("Operation failed")
    finally:
        print("Resource released")

try:
    resource_manager()
except Exception as e:
    print(f"Caught exception: {e}")

# 11. Handling System Exits
print("\n11. Handling System Exits:")
import sys

try:
    sys.exit("Terminating program")
except SystemExit as e:
    print(f"Caught system exit: {e}")

# 12. Debugging with pdb
print("\n12. Debugging Example:")
def debug_function():
    try:
        x = 1
        y = 0
        z = x / y
    except:
        import pdb; pdb.set_trace()  # Breakpoint for debugging
        print("Error occurred")

# Commented out to avoid entering debug mode
# debug_function()

# 13. Logging Exceptions
print("\n13. Logging Exceptions:")
import logging
logging.basicConfig(level=logging.INFO)

try:
    raise ValueError("A demonstration error")
except ValueError as e:
    logging.error(f"An error occurred: {e}", exc_info=True)

# 14. Exception Handling Best Practices
print("\n14. Best Practices Example:")
def divide_numbers(a, b):
    """
    Divides two numbers with proper error handling
    """
    try:
        # Validate inputs
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Inputs must be numbers")
        
        # Check for zero division
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        # Perform division
        result = a / b
        
        # Validate output
        if not isinstance(result, (int, float)):
            raise ValueError("Calculation resulted in invalid value")
        
        return result
    
    except (TypeError, ZeroDivisionError, ValueError) as e:
        logging.error(f"Error in divide_numbers: {e}")
        raise  # Re-raise the exception after logging
    except Exception as e:
        logging.critical(f"Unexpected error: {e}")
        raise RuntimeError("An unexpected error occurred") from e

# Example usage
try:
    result = divide_numbers(10, "2")
except Exception as e:
    print(f"Error handled: {e}")
