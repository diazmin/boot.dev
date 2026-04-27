'''
Sets
A set is a collection which is unordered, unchangeable*, and unindexed.
    - Set items are unchangeable, but you can remove items and add new items.
    -  Only ONE of each value can be in a set.
    - No error will be raised if you add an item already in the set

Create a set:
colors = {"red", "green", "blue"}

Add elements:
colors.add("yellow")
colors.update(["pink", "purple"])  # Add multiple

Remove elements:
colors.remove("green")         # Raises error if not found
colors.discard("black")        # No error if not found
colors.pop()                   # Removes arbitrary element
colors.clear()                 # Empties the set

'''

# Exercises
# Create a set from a list (remove duplicates)
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(my_list)
print(unique_numbers)

#  Add a new number to the set
numbers = {1, 2, 3}
numbers.add(4)
print(numbers)

'''
Set operations

# Find common numbers (intersection)
# Find all numbers (union)
# Find numbers in a but not in b (difference)
'''
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

common_numbers = a & b
all_numbers = a.union(b)
different_numbers = a - b
print(f"common_numbers: {common_numbers}")
print(f"all_numbers: {all_numbers}")
print(f"different_numbers: {different_numbers}")

'''
Subset check
Check if 'small' is a subset of 'big'

Is A a subset of B? A <= B
Does B contain everything in A? B >= A
'''
small = {1, 2}
big = {1, 2, 3, 4}

subset_check = small <= big
print(f"subset_check: {subset_check}")

'''
More challenging problems

1. Find values that are in either a or b, but not in both.
'''
a = {1, 2, 3}
b = {2, 3, 4}

different_values = a ^ b
print(f"different_values: {different_values}")





