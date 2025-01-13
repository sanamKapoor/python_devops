# 1. Creating lists
list_of_cloud_providers = ["AWS", "Azure", "GCP"]

# 2. Adding elements
list_of_cloud_providers.append("DigitalOcean")  # Adds at the end
list_of_cloud_providers.insert(0, "Alibaba")    # Adds at specific index
list_of_cloud_providers.extend(["IBM", "Oracle"])  # Adds multiple items

# 3. Removing elements
list_of_cloud_providers.remove("AWS")     # Removes specific element
removed_item = list_of_cloud_providers.pop()     # Removes and returns last element
removed_item = list_of_cloud_providers.pop(1)    # Removes element at index
del list_of_cloud_providers[0]            # Removes element at index
# list_of_cloud_providers.clear()           # Removes all elements

# 4. Accessing elements
first_provider = list_of_cloud_providers[0]      # Access by index
last_provider = list_of_cloud_providers[-1]      # Access last element
subset = list_of_cloud_providers[1:3]            # Slicing

# 5. List operations
length = len(list_of_cloud_providers)            # Get length
index = list_of_cloud_providers.index("GCP")   # Find index of element
count = list_of_cloud_providers.count("AWS")     # Count occurrences
list_of_cloud_providers.sort()                   # Sort list in place
list_of_cloud_providers.reverse()                # Reverse list in place

# 6. List comprehension
squared_numbers = [x**2 for x in range(5)]       # [0, 1, 4, 9, 16]
print(squared_numbers)

# 7. Checking elements
if "GCP" in list_of_cloud_providers:             # Check if element exists
    print("GCP is in the list")

# 8. Copying lists
shallow_copy = list_of_cloud_providers.copy()    # Create shallow copy
import copy
deep_copy = copy.deepcopy(list_of_cloud_providers)  # Create deep copy

# 9. List concatenation
new_list = list_of_cloud_providers + ["NewProvider"]
print(new_list)

# Original loop
for provider in list_of_cloud_providers:
    print(provider)

# 10. Enumerate for index and value
for index, provider in enumerate(list_of_cloud_providers):
    print(f"Index {index}: {provider}")

