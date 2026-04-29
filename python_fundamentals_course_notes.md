## Variables
### F-string
```python
num_bananas = 10
bananas = f"You have {num_bananas} bananas"
print(bananas)
# You have 10 bananas
```
### Dynamic typing
Python is dynamically typed, which means a variable can store any type, and that type can change.
```python
speed = 5
speed = "five"
```
### Multi-Variable Declaration
We can save space when creating many new variables by declaring them on the same line:
```python
sword_name, sword_damage, sword_length = "Excalibur", 10, 200
```

## Functions
Code executes in order from top to bottom, so a variable needs to be created before it can be used. That means that if you define a function, you can't call that function until after it has been defined.
```python
def subtract(a, b):
    result = a - b
    return result
```
#### Order of functions
All functions must be defined before they're used.

You might think this would make structuring Python code hard because the order of the functions needs to be just right. As it turns out, there's a simple trick that makes it super easy.

Most Python developers solve this problem by defining all the functions in their program first, then they call an "entry point" function at the end of the file. That way all of the functions have been read by the Python interpreter before the first one is called.

```python
def main():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

# call entrypoint at the end
main()
```

* When no return value is specified in a function, it will automatically return *None*. 

* In Python you can specify a default value for a function parameter. It's nice for when a function has parameters that are "optional". You as the function definer can specify a specific default value in case the caller doesn't provide one.

#### Multiple return values
A function can return more than one value by separating them with commas.
```python
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # return two values
```
#### Receiving Multiple Values
When calling a function that returns multiple values, you can assign them to multiple variables.
```python
damage, mana = cast_iceblast(5, 100)
print(f"Damage: {damage}, Remaining Mana: {mana}")
# Damage: 10, Remaining Mana: 90
```

### Parameters vs. Arguments
Parameters are the names used for inputs when defining a function. Arguments are the values of the inputs supplied when a function is called.

To reiterate, arguments are the actual values that go into the function, such as 42.0, "the dark knight", or True. Parameters are the names we use in the function definition to refer to those values, which at the time of writing the function, can be whatever we like.

## Testing and Debug
Unit-test-style lessons will test your code's functionality rather than its output.

Trying to write entire programs at once is a recipe for pain and suffering. The goal is to write a few lines, test them, and then write a few more lines, and repeat until you're done.

## Numbers
* Floor division:
```python
7 // 3
# 2 (an integer, rounded down from 2.333)
-7 // 3
# -3 (an integer, rounded down from -2.333)
```
* Exponents
```python
# reads as "three squared" or
# "three raised to the second power"
3 ** 2
# 9
```
* Plus equals
```python
+=, -=, *=, /=
```
* Scientific notation
```python
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071
```
* Underscores for readability
```python
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000
```

## If-Else
```python
if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
elif score > third_highest_score:
    print("You got third place!")
else:
    print("Better luck next time")
```

## Loops
### Range
```python
for i in range(0, 10):
    print(i)
```
The numbers a, b in range(a, b) are inclusive of a and exclusive of b.
So range(0, 10) includes 0 but not 10.

#### Counting items in a list (with index)
```python
for i in range(0, len(sports)):
    print(sports[i])
```

### While
```python
num = 0
while num < 3:
    num += 1
    print(num)

# prints:
# 1
# 2
# 3
# (the loop stops when num >= 3)
```

### Continue statement
```python
# Remember, `range` is inclusive of the start, but exclusive of the end
counter = 0
for number in range(1, 51):
    counter = counter + 1

    if counter == 7:
        counter = 0 # Reset the counter
        continue # Skip this number

    print(number)
```

### Break statement
For if we want to exit the loop entirely.

## Lists
* Indexes
```python
best_languages = ["JavaScript", "Go", "Rust", "Python", "C"]
print(best_languages[1])
# prints "Go", because index 1 was provided
```
* List lenght
```python
fruits = ["apple", "banana", "pear"]
length = len(fruits)
# 3 items in fruits

len("supercalifragilisticexpialidocious")
# 34 characters
```
* List updates
```python
inventory = ["Leather", "Iron Ore", "Healing Potion"]
inventory[0] = "Leather Armor"
# inventory: ['Leather Armor', 'Iron Ore', 'Healing Potion']
```
### Appending in lists
It's common to create an empty list then fill it with values using a loop. We can add values to the end of a list using the .append() method:
```python
cards = []
cards.append("nvidia")
cards.append("amd")
# the cards list is now ['nvidia', 'amd']
```

### Pop values
.pop() is the opposite of .append(). Pop removes the last element from a list and returns it for use. For example:
```python
vegetables = ["broccoli", "cabbage", "kale", "tomato"]
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'
```
Note: While .pop() typically removes the last item of a list, it can also be used to remove an item at a specific index. For example, vegetables.pop(1) would remove "cabbage" from the list. This can be useful when you need to remove items from other positions in your list.

### Iterating over lists
#### Counting items in a list (with index)
```python
for i in range(0, len(sports)):
    print(sports[i])
```

#### No-Index Syntax
The most elegant syntax for iterating Python has it.
```python
trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple
```

### Slicing Lists

Python makes it easy to slice and dice lists to work only with the section you care about. One way to do this is to use the simple slicing operator, which is just a colon `:`.

With this operator, you can specify where to start and end the slice, and how to step through the original list. List slicing returns a *new list* from the existing list.

The syntax is as follows:

```python
my_list[ start : stop : step ]

scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]
```

The above reads as "give me a slice of the `scores` list from index 1, up to but not including 5, skipping every 2nd value". *All of the sections are optional*.

#### Ommitting sections
You can also omit various sections ("start", "stop", or "step"). For example, numbers[:3] means "get all items from the start up to (but not including) index 3". numbers[3:] means "get all items from index 3 to the end".
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3] # Gives [0, 1, 2]
numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]
```

#### Using only the "step" section
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] # Gives [0, 2, 4, 6, 8]}
```

#### Negative indices
Negative indices count from the end of the list. For example, numbers[-1] gives the last item in the list, numbers[-2] gives the second last item, and so on.

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[-3:] # Gives [7, 8, 9]
```

### List operations 
#### Concatenate
```python
total = [1, 2, 3] + [4, 5, 6]
print(total)
# Prints: [1, 2, 3, 4, 5, 6]
```
#### Contains
```python
fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True


fruits = ["apple", "orange", "banana"]
print("banana" not in fruits)
# Prints: False
```

### List deletion
Python has a built-in keyword del that deletes items from objects. In the case of a list, you can delete specific indexes or entire slices.
```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []
```

### Infinity
The built-in float() function can create a numeric floating point value of negative infinity. Instead of initializing a base value like 0 or -100000, we can use float("-inf") to represent negative infinity. Because every value will be greater than negative infinity, we can use it as a starting point to help us achieve our goal of finding the max value.
```python
negative_infinity = float("-inf")
positive_infinity = float("inf")
```

### Split a String into a list of words
The .split() method in Python is called on a string and returns a list by splitting the string based on a given delimiter. If no delimiter is provided, it will split the string on whitespace. Here's a quick example:

```python
message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]
```

### Join a list of Strings into a Single String
The .join() method is called on a delimiter (what goes between all the words in the list), and takes a list of strings as input.
```python
list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Prints: "hello there sam"
```

## Tuples
Tuples are collections of data that are ordered and unchangeable. You can think of a tuple as a List with a fixed size. 

While it's typically considered bad practice to store items of different types in a List, it's not a problem with Tuples. Because they have a fixed size, it's easy to keep track of which indexes store which types of data.

Tuples are often used to store very small groups (like 2 or 3 items) of data. 


## Dictionaries
* Because dictionaries rely on unique keys, you can't have two of the same key in the same dictionary. If you try to use the same key twice, the first value will simply be overwritten.

### --- Even teams
Fantasy Quest PvP teams are uneven when the match begins. We need a function that will correctly split the two teams evenly.