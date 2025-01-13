# 1. Basic Functions
print("\n1. Basic Functions:")
def greet(name):
    """Simple function with one parameter"""
    return f"Hello, {name}!"

print(greet("Alice"))

# 2. Function with Multiple Parameters
def calculate_total(price, tax_rate=0.1):
    """Function with default parameter"""
    return price + (price * tax_rate)

print(calculate_total(100))  # Using default tax_rate
print(calculate_total(100, 0.2))  # Specifying tax_rate

# 3. Variable Number of Arguments
def sum_all(*args):
    """Function accepting variable number of positional arguments"""
    return sum(args)

print(sum_all(1, 2, 3, 4))

# 4. Keyword Arguments
def print_info(**kwargs):
    """Function accepting variable number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=30, city="New York")

# 5. Lambda Functions (Anonymous Functions)
square = lambda x: x**2
print(square(5))

# Using lambda with map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)

# 6. Nested Functions
def outer_function(x):
    """Function containing another function"""
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(3))  # Returns 8

# 7. Closure
def counter():
    """Function demonstrating closure"""
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter_func = counter()
print(counter_func())  # 1
print(counter_func())  # 2

# 8. Decorators
def timer_decorator(func):
    """Decorator function to measure execution time"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end-start:.2f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "Done!"

print(slow_function())

# 9. Generator Functions
def fibonacci(n):
    """Generator function for Fibonacci sequence"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci(5):
    print(num)

# 10. Recursive Functions
def factorial(n):
    """Recursive function to calculate factorial"""
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# 11. Function with Type Hints (Python 3.5+)
def multiply(x: float, y: float) -> float:
    """Function with type hints"""
    return x * y

print(multiply(2.5, 3.0))

# 12. Partial Functions
from functools import partial

def power(base, exponent):
    return base ** exponent

# Create a new function with base fixed to 2
power_of_two = partial(power, 2)
print(power_of_two(3))  # 2^3 = 8

# 13. Async Functions (Python 3.5+)
import asyncio

async def async_hello():
    """Asynchronous function"""
    await asyncio.sleep(1)
    return "Hello, Async!"

# Run async function
async def main():
    result = await async_hello()
    print(result)

asyncio.run(main())

# 14. Class Methods and Static Methods
class Calculator:
    @staticmethod
    def add_numbers(x, y):
        """Static method example"""
        return x + y
    
    @classmethod
    def multiply_by_two(cls, x):
        """Class method example"""
        return x * 2

print(Calculator.add_numbers(5, 3))
print(Calculator.multiply_by_two(5))

# 15. Property Decorators
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        """Getter method"""
        return self._radius
    
    @radius.setter
    def radius(self, value):
        """Setter method"""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        """Computed property"""
        import math
        return math.pi * self._radius ** 2

circle = Circle(5)
print(circle.area)
circle.radius = 10
print(circle.area)

# 16. Context Manager Functions
from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    """Custom context manager"""
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Usage example (commented out to avoid file operations)
# with file_manager('test.txt', 'w') as f:
#     f.write('Hello, World!')

# 17. Higher-Order Functions
def apply_operation(func, x):
    """Function that takes another function as argument"""
    return func(x)

def double(x):
    return x * 2

print(apply_operation(double, 5))

# 18. Function Annotations
def greet_person(name: str, age: int = 18) -> str:
    """Function with annotations"""
    return f"Hello {name}, you are {age} years old"

print(greet_person("Alice", 25))
print(greet_person.__annotations__)  # View annotations
