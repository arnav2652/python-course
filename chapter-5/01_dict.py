# Creating a dictionary
student = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}

# Accessing a value
print(student["name"])  # Output: Alice

# Adding a new key-value pair
student["GPA"] = 3.8

# Updating an existing value
student["age"] = 22

# Removing a key-value pair
del student["major"]

# Iterating over the dictionary
for key, value in student.items():
    print(key, value)


  
# Summary of Dictionary Syntax

# Creation: Use {} with key-value pairs.
# Access: Use my_dict["key"].
# Add/Update: Use my_dict["key"] = value.
# Remove: Use del my_dict["key"].
# Iterate: Use for key in my_dict, for value in my_dict.values(), or for key, value in my_dict.items().
# This covers the basic syntax and usage of dictionaries in Python!