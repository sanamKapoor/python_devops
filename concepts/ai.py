# In Python, we use '#' for single-line comments
"""
This is a multi-line comment or docstring
Similar to /** ... */ in JavaScript
"""

# Variables and Data Types
# Unlike JavaScript's 'let' and 'const', Python variables are just declared directly
name = "John"  # str (similar to JavaScript string)
age = 30       # int (similar to JavaScript number)
height = 1.75  # float (similar to JavaScript number)
is_active = True  # bool (similar to JavaScript boolean)

# Lists (similar to JavaScript arrays)
fruits = ["apple", "banana", "orange"]
fruits.append("grape")  # Like JavaScript's push()
first_fruit = fruits[0]  # Zero-based indexing, like JavaScript

# Dictionaries (similar to JavaScript objects)
user = {
    "name": "John",
    "age": 30,
    "skills": ["Python", "JavaScript"]
}

# Functions (similar to JavaScript functions)
def greet(name, greeting="Hello"):  # Default parameters work like JavaScript
    """
    This is a function docstring - documents what the function does
    Args:
        name: The name of the person to greet
        greeting: Optional greeting prefix
    """
    return f"{greeting}, {name}!"  # f-strings are like JavaScript template literals

# Classes (similar to JavaScript classes)
class Person:
    def __init__(self, name, age):  # Constructor (like JavaScript constructor)
        self.name = name  # 'self' is like 'this' in JavaScript
        self.age = age
    
    def introduce(self):  # Method
        return f"I am {self.name} and I'm {self.age} years old"

# Error Handling (similar to JavaScript try/catch)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error occurred: {e}")

# List comprehension (Python-specific, very powerful)
# Similar to JavaScript's map/filter but more concise
numbers = [1, 2, 3, 4, 5]
squared = [num * num for num in numbers]  # Creates: [1, 4, 9, 16, 25]

# Working with files
def read_file(filename):
    with open(filename, 'r') as file:  # 'with' ensures file is properly closed
        return file.read()

# Main execution block
if __name__ == "__main__":
    # This block only runs if the file is executed directly
    # Similar to checking if it's the main module
    
    # Create a person instance
    john = Person("John", 30)
    print(john.introduce())
    
    # Demonstrate function usage
    print(greet("Python Developer"))
    
    # Show list operations
    print(fruits)
    
    # Dictionary access
    print(user["name"])  # Like JavaScript object access
    print(user.get("email", "Not found"))  # Safe access with default value
