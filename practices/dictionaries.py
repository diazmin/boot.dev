'''
Dictionaries

- Dictionaries are used to store data values in key:value pairs.

- A dictionary is a collection which is ordered* (version 3.7 >), changeable and do not allow duplicates.
 - When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
   Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

Create a dict:
person = {"name": "Alice", "age": 30}

Add/update elements:
person["city"] = "New York"     # Add new key
person["age"] = 31              # Update existing key
* If you try to set the value of a key that already exists, you'll end up just updating the value of that key.

planets = {
    "Pluto": True,
}
planets["Pluto"] = False
print(planets["Pluto"])
# Prints False


Remove elements:
del person["age"]               # Remove by key
person.pop("city")              # Remove and return value
person.clear()                  # Empty the dictionary

Iterate:
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

'''
# Iterate over key-values in a pythonic way (using items())
my_top_artists = {
    1: "Michael Jackson",
    2: "Coldplay",
    3: "Charlie Puth"
}

for key, name in my_top_artists.items():
    print(f"{name} is the number {key} in my list")

# Dictionary Comprehension
# employees_data = {big_dictionary: {} for item in my_list}
my_list = ['a', 'b', 'c', 1, 2, 3, "do", "re", "mi"]
stuff = {my_stuff: {} for my_stuff in my_list}

print(stuff)
