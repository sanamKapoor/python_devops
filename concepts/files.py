# 1. Basic File Operations
print("\n1. Basic File Operations:")

# Writing to a file
with open('basic_file.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")

# Reading from a file
with open('basic_file.txt', 'r') as file:
    content = file.read()
    print("File contents:", content)

# 2. File Modes
print("\n2. File Modes:")
"""
'r'  - Read (default)
'w'  - Write (truncates)
'a'  - Append
'x'  - Exclusive creation
'b'  - Binary mode
't'  - Text mode (default)
'+'  - Read and write
"""

# Read mode with error handling
try:
    with open('nonexistent.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# Write mode (creates new file or truncates existing)
with open('modes_example.txt', 'w') as file:
    file.write("This will overwrite any existing content\n")

# Append mode
with open('modes_example.txt', 'a') as file:
    file.write("This will be added to the end\n")

# 3. Reading Methods
print("\n3. Reading Methods:")
with open('modes_example.txt', 'r') as file:
    # Read entire file
    print("Read entire file:")
    file.seek(0)  # Reset file pointer to beginning
    print(file.read())

    # Read line by line
    print("\nRead line by line:")
    file.seek(0)
    for line in file:
        print(line.strip())

    # Read specific number of characters
    print("\nRead 10 characters:")
    file.seek(0)
    print(file.read(10))

    # Read all lines into list
    print("\nRead lines into list:")
    file.seek(0)
    lines = file.readlines()
    print(lines)

# 4. Writing Methods
print("\n4. Writing Methods:")
with open('writing_example.txt', 'w') as file:
    # Write single string
    file.write("Line 1\n")
    
    # Write multiple lines
    lines = ['Line 2\n', 'Line 3\n', 'Line 4\n']
    file.writelines(lines)

# 5. Binary Files
print("\n5. Binary Files:")
# Writing binary data
with open('binary_file.bin', 'wb') as file:
    file.write(bytes([65, 66, 67, 68]))  # Writing ASCII values

# Reading binary data
with open('binary_file.bin', 'rb') as file:
    binary_data = file.read()
    print("Binary data:", binary_data)

# 6. File Positions
print("\n6. File Positions:")
with open('position_example.txt', 'w+') as file:
    file.write("Hello, World!")
    
    # Get current position
    position = file.tell()
    print(f"Current position: {position}")
    
    # Move to start
    file.seek(0)
    
    # Read content
    content = file.read()
    print(f"Content: {content}")

# 7. File Properties and Operations
print("\n7. File Properties and Operations:")
import os

filename = 'file_props.txt'
with open(filename, 'w') as file:
    file.write("Testing file properties")

# Check file properties
print(f"File exists: {os.path.exists(filename)}")
print(f"File size: {os.path.getsize(filename)} bytes")
print(f"Is file: {os.path.isfile(filename)}")
print(f"Is directory: {os.path.isdir(filename)}")

# 8. Directory Operations
print("\n8. Directory Operations:")
# Create directory
os.makedirs('test_dir', exist_ok=True)

# List directory contents
print("Directory contents:", os.listdir('.'))

# 9. File Management
print("\n9. File Management:")
import shutil

# Copy file
shutil.copy('file_props.txt', 'test_dir/file_props_copy.txt')

# Move file
os.rename('file_props.txt', 'test_dir/file_props_moved.txt')

# Delete file
try:
    os.remove('binary_file.bin')
    print("File deleted successfully")
except FileNotFoundError:
    print("File not found")

# 10. Advanced File Operations
print("\n10. Advanced File Operations:")
import tempfile
import csv
import json

# Temporary files
with tempfile.TemporaryFile() as temp:
    temp.write(b"Temporary data")
    temp.seek(0)
    print("Temp file content:", temp.read())

# CSV files
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['John', 30])
    writer.writerow(['Alice', 25])

# JSON files
data = {'name': 'John', 'age': 30}
with open('data.json', 'w') as file:
    json.dump(data, file)

# 11. Context Manager for Custom File Operations
print("\n11. Custom Context Manager:")
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

# Using custom context manager
with FileManager('custom_managed.txt', 'w') as file:
    file.write("Using custom context manager")

# 12. Error Handling in File Operations
print("\n12. Error Handling:")
def safe_file_operation(filename, operation):
    try:
        with open(filename, 'r') as file:
            if operation == 'read':
                return file.read()
    except FileNotFoundError:
        print(f"File {filename} not found")
    except PermissionError:
        print(f"Permission denied for {filename}")
    except IOError as e:
        print(f"IO Error: {e}")
    finally:
        print("File operation attempted")

# Clean up created files and directories
def cleanup():
    """Clean up all created files and directories"""
    try:
        shutil.rmtree('test_dir')
        os.remove('basic_file.txt')
        os.remove('modes_example.txt')
        os.remove('writing_example.txt')
        os.remove('data.csv')
        os.remove('data.json')
        os.remove('custom_managed.txt')
    except FileNotFoundError:
        pass

# Run cleanup
cleanup()
