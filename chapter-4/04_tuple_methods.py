# Tuple of items purchased
purchased_items = ("Apple", "Banana", "Apple", "Orange", "Banana")

# Count how many times "Apple" was bought
apple_count = purchased_items.count("Apple")
print("Apple was purchased", apple_count, "times.")

# Find the position of "Banana"
banana_index = purchased_items.index("Banana")
print("Banana was first purchased at position:", banana_index)


#SUMMARY

# count()   #tells you how many times something appears in the tuple.

# index()   #tells you the position of the first occurrence of something in the tuple.



#HERE ARE SOME MORE  TUPLE METHOD IN PYTHON

# 1. Tuple of fruits
fruits = ("Apple", "Banana", "Apple", "Orange", "Apple", "Banana")

# 2. Using count() to count how many times "Apple" appears
apple_count = fruits.count("Apple")
print("Apple appears", apple_count, "times.")

# 3. Using index() to find the position of "Banana"
banana_index = fruits.index("Banana")
print("Banana is at position:", banana_index)

# 4. Using len() to find the length of the tuple
tuple_length = len(fruits)
print("The tuple contains", tuple_length, "items.")

# 5. Using min() and max() (only works for tuples with numbers)
numbers = (10, 20, 30, 40, 50)
min_number = min(numbers)
max_number = max(numbers)
print("Minimum number:", min_number)
print("Maximum number:", max_number)

# 6. Using sum() to find the sum of the numbers in the tuple
total_sum = sum(numbers)
print("The total sum of numbers is:", total_sum)

# 7. Slicing the tuple to get a subtuple (from index 1 to 3)
subtuple = fruits[1:4]
print("The sliced tuple is:", subtuple)

# 8. Concatenating two tuples
more_fruits = ("Grapes", "Mango")
combined_fruits = fruits + more_fruits
print("Combined fruits:", combined_fruits)

# 9. Repeating the tuple 3 times
repeated_fruits = fruits * 3
print("Repeated fruits:", repeated_fruits)

# 10. Nested tuple (a tuple within a tuple)
nested_tuple = (1, 2, (3, 4), 5)
print("Nested tuple:", nested_tuple)

# Accessing elements from the nested tuple
print("Accessing the nested tuple:", nested_tuple[2])  # Output: (3, 4)


# Explanation of the Code:


# Counting with count(): We check how many times "Apple" appears in the fruits tuple.

# Finding the Index with index(): We find the position of the first "Banana".

# Finding Length with len(): We find how many items are in the fruits tuple.

# Min and Max with min() and max(): For the numbers tuple, we find the minimum and maximum values.

# Summing Values with sum(): We calculate the sum of all the numbers in the numbers tuple.

# Slicing: We create a subtuple from the fruits tuple using slicing.

# Concatenation: We combine fruits with another tuple more_fruits.

# Repetition: We repeat the fruits tuple 3 times using the * operator.

# Nested Tuple: We create a tuple that contains another tuple inside it and access it.