'''
Tuples
- Tuple items are ordered, unchangeable, and allow duplicate values.
    - we cannot change, add or remove items after the tuple has been created

Create a tuple:
thistuple = ("apple",) # One item tuple

'''
# Create and print a tuple, and accesing elements
colors = ("blue", "pink", "yellow")
print(colors[1])

# Un-packing values
person = ("Tyler", 35, "singer")

name, age, job = person
print(f"{name} is a {job} and is {age} years old. ")

# Nested tuples
albums = (("Thriller", "Michael Jackson", 1982), ("Clancy", "Twenty One Pilots", 2024), ("Embrace", "Roosevelt", 2023))

for name, artist, year in albums:
    print(f"{name} by {artist} was released on {year}")

# Challenges

'''
1. Count how many times "a" appears in ("a", "b", "a", "c", "a").
'''
letters = ("a", "b", "a", "c", "a")
print("letter 'a' was found ", letters.count("a"), "times. ")

'''
2. Slice the middle values from a 5-element tuple.
'''
t = (10, 20, 30, 40, 50)
mid = len(t) // 2
print(t[mid:])   # (20, 30, 40)
