# 1. Creating Dictionaries
print("1. Creating Dictionaries:")
# Empty dictionary
empty_dict = {}
# Dictionary with items
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Using dict() constructor
dict_constructor = dict(name="Alice", age=25)
print(dict_constructor)
# Creating from lists of tuples
items = [("a", 1), ("b", 2)]
dict_from_tuples = dict(items)
print(dict_from_tuples)

# 2. Accessing Values
print("\n2. Accessing Values:")
print(person["name"])  # Using key
print(person.get("age"))  # Using get() method
print(person.get("country", "Not Found"))  # Get with default value

# 3. Modifying Dictionaries
print("\n3. Modifying Dictionaries:")
# Adding/Updating single items
person["email"] = "john@example.com"  # Add new key-value
person["age"] = 31  # Update existing value
print(person)

# Update multiple items at once
person.update({
    "phone": "123-456-7890",
    "occupation": "Engineer"
})

# 4. Removing Items
print("\n4. Removing Items:")
# Remove and return value
removed_age = person.pop("age")
print(f"Removed age: {removed_age}")

# Remove and return last inserted item (Python 3.7+)
last_item = person.popitem()
print(f"Removed last item: {last_item}")
print(person)

# Delete specific key
del person["email"]

# Clear all items
person_copy = person.copy()
person_copy.clear()

# 5. Dictionary Methods
print("\n5. Dictionary Methods:")
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}

# Get all keys
print("Keys:", car.keys())

# Get all values
print("Values:", car.values())

# Get all key-value pairs
print("Items:", car.items())

# Check if key exists
print("Has 'brand'?", "brand" in car)

# Get length
print("Dictionary length:", len(car))

# 6. Dictionary Comprehension
print("\n6. Dictionary Comprehension:")
# Create dictionary of squares
squares = {x: x**2 for x in range(5)}
print("Squares:", squares)

# Filtering with comprehension
even_squares = {x: x**2 for x in range(5) if x % 2 == 0}
print("Even squares:", even_squares)

# 7. Nested Dictionaries
print("\n7. Nested Dictionaries:")
company = {
    "department1": {
        "name": "Engineering",
        "employees": ["John", "Alice"],
        "location": "Floor 2"
    },
    "department2": {
        "name": "Marketing",
        "employees": ["Bob", "Carol"],
        "location": "Floor 1"
    }
}

# Accessing nested values
print(company["department1"]["employees"][0])

# 8. Dictionary Merging (Python 3.5+)
print("\n8. Dictionary Merging:")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
# Merge using | operator (Python 3.9+)
merged = dict1 | dict2
print("Merged:", merged)

# 9. Advanced Operations
print("\n9. Advanced Operations:")
student_scores = {
    "John": 85,
    "Alice": 92,
    "Bob": 78
}

# Find max value
highest_score = max(student_scores.values())
print("Highest score:", highest_score)

# Find key with max value
top_student = max(student_scores, key=student_scores.get)
print("Top student:", top_student)

# Sort dictionary by values
sorted_scores = dict(sorted(student_scores.items(), key=lambda x: x[1], reverse=True))
print("Sorted scores:", sorted_scores)

# 10. Dictionary Type Conversion
print("\n10. Dictionary Type Conversion:")
# Convert to list of keys
keys_list = list(student_scores.keys())
print("Keys list:", keys_list)

# Convert to list of values
values_list = list(student_scores.values())
print("Values list:", values_list)

# Convert to list of tuples
items_list = list(student_scores.items())
print("Items list:", items_list)

# 11. Dictionary fromkeys() method
print("\n11. Dictionary fromkeys():")
# Create dictionary with default values
keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "Unknown")
print("Default dictionary:", default_dict)

# 12. Safe Dictionary Access
print("\n12. Safe Dictionary Access:")
# Using setdefault (returns value if key exists, else sets and returns default)
contacts = {}
contacts.setdefault("John", []).append("123-456-7890")
print("Contacts:", contacts)

# 13. Dictionary Views
print("\n13. Dictionary Views:")
scores = {"Math": 90, "Science": 85}
# Views are dynamic (they reflect dictionary changes)
score_values = scores.values()
scores["History"] = 88
print("Updated values view:", score_values)
