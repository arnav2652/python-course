# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# 1. Using get() to access a value
age = student.get("age")  # Returns 21
print("Age:", age)

# Using get() with a default value
hobby = student.get("hobby", "Not specified")  # Returns "Not specified"   
print("Hobby:", hobby)

# 2. Getting all keys
keys = student.keys()
print("Keys:", keys)  # Output: dict_keys(['name', 'age', 'major'])

# 3. Getting all values
values = student.values()
print("Values:", values)  # Output: dict_values(['Alice', 21, 'Computer Science'])

# 4. Getting all key-value pairs
items = student.items()
print("Items:", items)  # Output: dict_items([('name', 'Alice'), ('age', 21), ('major', 'Computer Science')])

# Iterating over key-value pairs
print("Key-Value Pairs:")
for key, value in items:
    print(f"{key}: {value}")

# 5. Updating the dictionary
new_info = {
    "age": 22,  # This will update the existing age
    "GPA": 3.8  # This will add a new key-value pair
}
student.update(new_info)
print("Updated Student Dictionary:", student)

# 6. Removing a key-value pair
removed_value = student.pop("GPA")  # Removes "GPA" and returns its value
print("Removed GPA:", removed_value)
print("Student Dictionary after pop:", student)

# 7. Clearing the dictionary
student.clear()
print("Student Dictionary after clear:", student)  # Output: {}



# Explanation of Each Method in the Code

# get(): Retrieves the value for a specified key. If the key is not found, it returns a default value if provided.
# keys(): Returns a view object containing all the keys in the dictionary.
# values(): Returns a view object containing all the values in the dictionary.
# items(): Returns a view object containing all key-value pairs as tuples.
# update(): Updates the dictionary with key-value pairs from another dictionary or iterable. If a key already exists, its value is updated.
# pop(): Removes a specified key and returns its value. If the key does not exist, it raises a KeyError.
# clear(): Removes all items from the dictionary, leaving it empty.


# This code snippet provides a comprehensive overview of how to use various dictionary methods in Python!