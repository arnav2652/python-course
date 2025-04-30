# Create a set
my_set = {1, 2, 3}
print("Initial set:", my_set)

# 1. add(element)
my_set.add(4)  # Adds 4 to the set
print("After add(4):", my_set)

# 2. remove(element)
my_set.remove(2)  # Removes 2 from the set
print("After remove(2):", my_set)

# 3. discard(element)
my_set.discard(3)  # Removes 3 from the set; does nothing if 3 is not present
print("After discard(3):", my_set)

# 4. pop()
popped_element = my_set.pop()  # Removes and returns an arbitrary element
print("Popped element:", popped_element)
print("After pop():", my_set)

# 5. clear()
my_set.clear()  # Removes all elements from the set
print("After clear():", my_set)

# Reinitialize the set for further operations
my_set = {1, 2, 3}
print("\nReinitialized set:", my_set)

# 6. union(other_set)
set2 = {3, 4, 5}
union_set = my_set.union(set2)  # Combines elements from both sets
print("Union of my_set and set2:", union_set)

# 7. intersection(other_set)
intersection_set = my_set.intersection(set2)  # Common elements in both sets
print("Intersection of my_set and set2:", intersection_set)

# 8. difference(other_set)
difference_set = my_set.difference(set2)  # Elements in my_set not in set2
print("Difference of my_set and set2:", difference_set)

# 9. symmetric_difference(other_set)
sym_diff_set = my_set.symmetric_difference(set2)  # Elements in either set but not both
print("Symmetric difference of my_set and set2:", sym_diff_set)

# 10. issubset(other_set)
is_subset = {1, 2}.issubset(my_set)  # Check if {1, 2} is a subset of my_set
print("{1, 2} is a subset of my_set:", is_subset)

# 11. issuperset(other_set)
is_superset = my_set.issuperset({1})  # Check if my_set is a superset of {1}
print("my_set is a superset of {1}:", is_superset)

# 12. copy()
set_copy = my_set.copy()  # Creates a shallow copy of my_set
print("Copy of my_set:", set_copy)


# Explanation of Each Method: 


# add(element): Adds a specified element to the set. If the element already exists, it does nothing.
# remove(element): Removes a specified element from the set. Raises a KeyError if the element is not found.
# discard(element): Similar to remove(), but does not raise an error if the element is not found.
# pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
# clear(): Removes all elements from the set, resulting in an empty set.
# union(other_set): Returns a new set containing all unique elements from both sets.
# intersection(other_set): Returns a new set containing only the elements that are present in both sets.
# difference(other_set): Returns a new set containing elements that are in the first set but not in the second.
# symmetric_difference(other_set): Returns a new set containing elements that are in either set but not in both.
# issubset(other_set): Checks if the current set is a subset of another set.
# issuperset(other_set): Checks if the current set is a superset of another set.
# copy(): Creates a shallow copy of the set, allowing you to work with a duplicate without affecting the original set.
# This code provides a comprehensive overview of how to use the various set methods in Python, along with their expected behavior.