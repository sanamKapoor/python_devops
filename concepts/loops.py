# 1. Basic for loop with range
print("Basic for loop:")
for i in range(3):
    print(i)  # Prints 0, 1, 2

# 2. For loop with range start, stop, step
print("\nFor loop with step:")
for i in range(2, 10, 2):
    print(i)  # Prints 2, 4, 6, 8

# 3. While loop
print("\nWhile loop:")
count = 0
while count < 3:
    print(count)
    count += 1

# 4. List iteration
print("\nList iteration:")
fruits = ["apple", "banana", "cherry"]
# Simple iteration
for fruit in fruits:
    print(fruit)

# With index using enumerate
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# 5. Dictionary iteration
print("\nDictionary iteration:")
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
# Iterate keys
for key in person.keys():
    print(key)

# Iterate values
for value in person.values():
    print(value)

# Iterate items (key-value pairs)
for key, value in person.items():
    print(f"{key}: {value}")

# 6. Nested loops
print("\nNested loops:")
for i in range(2):
    for j in range(2):
        print(f"i={i}, j={j}")

# 7. Loop with break
print("\nLoop with break:")
for i in range(5):
    if i == 3:
        break
    print(i)

# 8. Loop with continue
print("\nLoop with continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)

# 9. While loop with else
print("\nWhile loop with else:")
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("Loop completed!")

# 10. For loop with else
print("\nFor loop with else:")
for i in range(3):
    print(i)
else:
    print("Loop completed!")

# 11. List comprehension
print("\nList comprehension:")
squares = [x**2 for x in range(4)]
print(squares)

# 12. Set iteration
print("\nSet iteration:")
unique_numbers = {1, 2, 3, 3}  # Note: duplicates are removed
for num in unique_numbers:
    print(num)

# 13. Tuple iteration
print("\nTuple iteration:")
coordinates = (1, 2, 3)
for coord in coordinates:
    print(coord)

# 14. String iteration (character by character)
print("\nString iteration:")
for char in "Python":
    print(char)

# 15. Infinite loop with break
print("\nControlled infinite loop:")
counter = 0
while True:
    print(counter)
    counter += 1
    if counter >= 3:
        break

# 16. Zip iteration (multiple lists)
print("\nZip iteration:")
names = ["John", "Jane"]
ages = [25, 24]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# 17. Generator expression iteration
print("\nGenerator expression:")
sum_squares = sum(x**2 for x in range(4))
print(f"Sum of squares: {sum_squares}")

# 18. Custom object iteration
print("\nCustom object iteration:")
class Counter:
    def __init__(self, limit):
        self.limit = limit
        
    def __iter__(self):
        self.current = 0
        return self
        
    def __next__(self):
        if self.current < self.limit:
            self.current += 1
            return self.current - 1
        raise StopIteration

for num in Counter(3):
    print(num)
