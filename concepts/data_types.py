# 1. Numeric Types
print("\n1. Numeric Types:")

# Integer
integer_num = 42
print(f"Integer: {integer_num}, Type: {type(integer_num)}")

# Float
float_num = 3.14
print(f"Float: {float_num}, Type: {type(float_num)}")

# Complex
complex_num = 3 + 4j
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

# Numeric Operations
print("\nNumeric Operations:")
x, y = 10, 3
print(f"Addition: {x + y}")
print(f"Subtraction: {x - y}")
print(f"Multiplication: {x * y}")
print(f"Division: {x / y}")
print(f"Floor Division: {x // y}")
print(f"Modulus: {x % y}")
print(f"Power: {x ** y}")

# 2. String Type
print("\n2. String Type:")
single_quoted = 'Hello'
double_quoted = "World"
multi_line = """This is a
multi-line string"""

# String Operations
text = "Python Programming"
print(f"Original String: {text}")
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Split: {text.split()}")
print(f"Join: {'-'.join(['Python', 'Programming'])}")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Slice: {text[0:6]}")
print(f"Reverse: {text[::-1]}")

# String Formatting
name = "Alice"
age = 25
print(f"Format string: {name} is {age} years old")
print("Format method: {} is {} years old".format(name, age))
print("Old style: %s is %d years old" % (name, age))

# 3. Boolean Type
print("\n3. Boolean Type:")
true_val = True
false_val = False
print(f"AND: {true_val and false_val}")
print(f"OR: {true_val or false_val}")
print(f"NOT: {not true_val}")

# Boolean Operations
x = 5
y = 10
print(f"Equals: {x == y}")
print(f"Not Equals: {x != y}")
print(f"Greater Than: {x > y}")
print(f"Less Than: {x < y}")
print(f"Greater or Equal: {x >= y}")
print(f"Less or Equal: {x <= y}")

# 4. List Type
print("\n4. List Type:")
my_list = [1, "hello", 3.14, True]
print(f"Original List: {my_list}")
print(f"Length: {len(my_list)}")
print(f"First Element: {my_list[0]}")
print(f"Last Element: {my_list[-1]}")
print(f"Slice: {my_list[1:3]}")

# List Operations
my_list.append(42)
print(f"After Append: {my_list}")
my_list.insert(1, "inserted")
print(f"After Insert: {my_list}")
my_list.remove("hello")
print(f"After Remove: {my_list}")
popped_value = my_list.pop()
print(f"Popped Value: {popped_value}")
print(f"After Pop: {my_list}")

# List Comprehension
squares = [x**2 for x in range(5)]
print(f"List Comprehension: {squares}")

# 5. Tuple Type
print("\n5. Tuple Type:")
my_tuple = (1, "hello", 3.14)
print(f"Tuple: {my_tuple}")
print(f"Length: {len(my_tuple)}")
print(f"Index: {my_tuple.index('hello')}")
print(f"Count: {my_tuple.count(1)}")

# Tuple Packing and Unpacking
coordinates = 4, 5
x, y = coordinates
print(f"Unpacked Coordinates: x={x}, y={y}")

# 6. Dictionary Type
print("\n6. Dictionary Type:")
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(f"Dictionary: {my_dict}")
print(f"Keys: {my_dict.keys()}")
print(f"Values: {my_dict.values()}")
print(f"Items: {my_dict.items()}")

# Dictionary Operations
my_dict["email"] = "john@example.com"
print(f"After Adding Key: {my_dict}")
print(f"Get Value: {my_dict.get('name', 'Not Found')}")
popped_item = my_dict.pop("age")
print(f"After Pop: {my_dict}")

# Dictionary Comprehension
square_dict = {x: x**2 for x in range(5)}
print(f"Dictionary Comprehension: {square_dict}")

# 7. Set Type
print("\n7. Set Type:")
my_set = {1, 2, 3, 3, 4, 4, 5}  # Duplicates are removed
print(f"Set: {my_set}")

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric Difference: {set1 ^ set2}")

# Set Methods
my_set.add(6)
print(f"After Add: {my_set}")
my_set.remove(1)
print(f"After Remove: {my_set}")

# 8. None Type
print("\n8. None Type:")
none_value = None
print(f"None Value: {none_value}")
print(f"Is None: {none_value is None}")

# 9. Bytes and Bytearray
print("\n9. Bytes and Bytearray:")
# Bytes (immutable)
bytes_data = bytes([65, 66, 67])
print(f"Bytes: {bytes_data}")
print(f"Decoded Bytes: {bytes_data.decode()}")

# Bytearray (mutable)
bytearray_data = bytearray([65, 66, 67])
bytearray_data[0] = 68
print(f"Modified Bytearray: {bytearray_data}")
print(f"Decoded Bytearray: {bytearray_data.decode()}")

# 10. Type Conversion
print("\n10. Type Conversion:")
# String to Int
str_num = "123"
converted_int = int(str_num)
print(f"String to Int: {converted_int}, Type: {type(converted_int)}")

# Int to String
num = 456
converted_str = str(num)
print(f"Int to String: {converted_str}, Type: {type(converted_str)}")

# Float to Int
float_num = 3.14
converted_float = int(float_num)
print(f"Float to Int: {converted_float}, Type: {type(converted_float)}")

# List to Tuple
list_to_tuple = tuple([1, 2, 3])
print(f"List to Tuple: {list_to_tuple}, Type: {type(list_to_tuple)}")

# Tuple to List
tuple_to_list = list((1, 2, 3))
print(f"Tuple to List: {tuple_to_list}, Type: {type(tuple_to_list)}")

# List to Set
list_to_set = set([1, 2, 2, 3, 3])
print(f"List to Set: {list_to_set}, Type: {type(list_to_set)}")
