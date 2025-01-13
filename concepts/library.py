# 1. Standard Library Modules
print("\n1. Standard Library Modules:")

# DateTime Module
print("\nDateTime Operations:")
from datetime import datetime, timedelta

# Get current date and time
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Formatted date: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Date arithmetic
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow}")

# Math Module
print("\nMath Operations:")
import math

print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"GCD of 36 and 48: {math.gcd(36, 48)}")

# Random Module
print("\nRandom Operations:")
import random

print(f"Random number (0-1): {random.random()}")
print(f"Random int (1-10): {random.randint(1, 10)}")
print(f"Random choice from list: {random.choice(['apple', 'banana', 'cherry'])}")
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

# Collections Module
print("\nCollections Operations:")
from collections import Counter, defaultdict, OrderedDict

# Counter
text = "hello world"
counter = Counter(text)
print(f"Character count: {counter}")

# defaultdict
d = defaultdict(list)
d['a'].append(1)  # No KeyError if key doesn't exist
print(f"defaultdict: {dict(d)}")

# OrderedDict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(f"OrderedDict: {dict(od)}")

# 2. File and Path Operations
print("\n2. File and Path Operations:")
import os
import pathlib
from pathlib import Path

# OS Path operations
print(f"Current directory: {os.getcwd()}")
print(f"Directory separator: {os.sep}")
print(f"Path exists: {os.path.exists('library.py')}")

# Pathlib operations
current_file = Path('library.py')
print(f"File suffix: {current_file.suffix}")
print(f"File stem: {current_file.stem}")

# 3. Data Processing
print("\n3. Data Processing:")
import json
import csv
import pickle

# JSON operations
data = {'name': 'John', 'age': 30}
json_str = json.dumps(data)
print(f"JSON string: {json_str}")
parsed_data = json.loads(json_str)
print(f"Parsed JSON: {parsed_data}")

# CSV operations
with open('sample.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['John', 30])

# Pickle operations
with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)

# 4. System and OS Operations
print("\n4. System and OS Operations:")
import sys
import platform
import subprocess

print(f"Python version: {sys.version}")
print(f"Platform: {platform.system()}")
print(f"Machine: {platform.machine()}")

# 5. Regular Expressions
print("\n5. Regular Expressions:")
import re

text = "Email: john@example.com, Phone: 123-456-7890"
email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'
phone_pattern = r'\d{3}-\d{3}-\d{4}'

emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
print(f"Found email: {emails}")
print(f"Found phone: {phones}")

# 6. URL and Web
print("\n6. URL and Web Operations:")
from urllib import request, parse
import base64

# URL encoding
params = {'name': 'John Doe', 'age': '30'}
encoded_params = parse.urlencode(params)
print(f"Encoded URL parameters: {encoded_params}")

# Base64 encoding/decoding
text = "Hello, World!"
encoded = base64.b64encode(text.encode())
decoded = base64.b64decode(encoded).decode()
print(f"Base64 encoded: {encoded}")
print(f"Base64 decoded: {decoded}")

# 7. Itertools and Functools
print("\n7. Itertools and Functools:")
from itertools import combinations, cycle, count
from functools import reduce, partial

# Combinations
items = ['a', 'b', 'c']
combs = list(combinations(items, 2))
print(f"Combinations: {combs}")

# Reduce
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"Reduced product: {product}")

# 8. Time and Performance
print("\n8. Time and Performance:")
import time
from timeit import timeit

# Time measurement
start = time.time()
time.sleep(1)
end = time.time()
print(f"Elapsed time: {end - start} seconds")

# 9. Logging
print("\n9. Logging:")
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("This is an info message")
logger.warning("This is a warning message")

# 10. Environment and Configuration
print("\n10. Environment and Configuration:")
import configparser
import os

# Environment variables
os.environ['MY_VAR'] = 'my_value'
print(f"Environment variable: {os.getenv('MY_VAR')}")

# Config parser
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                    'Compression': 'yes'}
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Cleanup
def cleanup():
    """Remove created files"""
    try:
        os.remove('sample.csv')
        os.remove('data.pickle')
        os.remove('config.ini')
    except FileNotFoundError:
        pass

cleanup()
