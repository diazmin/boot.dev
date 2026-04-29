'''
Lists
- List items are ordered, changeable, and allow duplicate values.
- If you add new items to a list, the new items will be placed 
AT THE END of the list.
-  Ps. There are some list methods that will change the order.

Create a list:
fruits = ["apple", "banana", "cherry"]

Add elements:
fruits.append("orange")         # Adds to the end
fruits.insert(1, "mango")       # Inserts at index 1
fruits += ["grape"]             # Adds another list

Remove elements:
fruits.remove("banana")         # Removes by value
fruits.pop()                    # Removes last item
fruits.pop(0)                   # Removes item at index 0
del fruits[1]                   # Deletes by index
fruits.clear()                  # Empties the whole list

Edit elements:
fruits[0] = "kiwi"              # Changes first item

Iterate: 
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(i, fruit)
'''

# Practice Problems:
'''
Reverse an Array

Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Hint: Use slicing: arr[::-1].

'''
numbers = [1, 2, 3, 4, 5]

#Slicing
#print(numbers[::-1]) 

# Reverse (modifies the original list)
letters = ['a', 'b', 'c', 'd', 'e']
letters.reverse()
#print(letters)

# Using a for loop
decades = [10, 20, 30, 40, 50]
reversed_list = []

for i in range(len(decades)-1, -1, -1): # Start from last index and go to 0
    reversed_list.append(decades[i])
#print(reversed_list)

'''
Find Maximum/Minimum Element

Input: [1, 5, 2, 8, 3]
Output: Max = 8, Min = 1
Hint: Use max() and min() functions.
'''

input = [1, 5, 2, 8, 3]

# Using built-in functions
#print("minimum value is: ", min(input))
#print("maximum value is: ", max(input))

# Making the manual process
max_number = 0
min_number = float("inf")
for i in input:
    if i > max_number:
        max_number = i
    if i < min_number:
        min_number = i
print("maximum value is: ", max_number)
print("minimum value is: ", min_number)
