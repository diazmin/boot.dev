## Variables
### F-string
```
num_bananas = 10
bananas = f"You have {num_bananas} bananas"
print(bananas)
// You have 10 bananas
```
### Dynamic typing
Python is dynamically typed, which means a variable can store any type, and that type can change.
```
speed = 5
speed = "five"
```
### Multi-Variable Declaration
We can save space when creating many new variables by declaring them on the same line:
```
sword_name, sword_damage, sword_length = "Excalibur", 10, 200
```

## Functions
Code executes in order from top to bottom, so a variable needs to be created before it can be used. That means that if you define a function, you can't call that function until after it has been defined.
```
def subtract(a, b):
    result = a - b
    return result
```
* When no return value is specified in a function, it will automatically return *None*. 

* In Python you can specify a default value for a function parameter. It's nice for when a function has parameters that are "optional". You as the function definer can specify a specific default value in case the caller doesn't provide one.

#### Multiple return values
A function can return more than one value by separating them with commas.
```
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # return two values
```
#### Receiving Multiple Values
When calling a function that returns multiple values, you can assign them to multiple variables.
```
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
```
7 // 3
# 2 (an integer, rounded down from 2.333)
-7 // 3
# -3 (an integer, rounded down from -2.333)
```
* Exponents
```
# reads as "three squared" or
# "three raised to the second power"
3 ** 2
# 9
```
* Plus equals
```
+=, -=, *=, /=
```
* Scientific notation
```
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071
```
* Underscores for readability
```
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000
```

## If-Else
```
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
```
for i in range(0, 10):
    print(i)
```
The numbers a, b in range(a, b) are inclusive of a and exclusive of b.
So range(0, 10) includes 0 but not 10.

### While
```
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
```
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