#-------------------------
#ABOUT ENUMERATE
#-------------------------

#Python let's us iterate directly over the values of a list - (does not require an indexing variable to set beforehand)
#In some other languages you iterate over the length of an array by an index, then use the index to get the value at that location

#Enumerate is a built in function
#We can get both the index and value of an element while iterating

#-------------------------
#ENUMERATE A LIST
#-------------------------

#Create a list to enumerate
fruit = ["apple", "pear", "orange", "cherry", "grape", "watermelon", "banana", "grapefruit"]
print("Enumerated List Below:")

#Use two arguments in the for loop (index, value)
for index, value in enumerate(fruit):
    if (index < len(fruit) - 1):
        print(index, value, end=", ")
    else:
        print(index, value)
print()
print("-" *20)

#-------------------------
#ENUMERATE A TUPLE
#-------------------------

#Convert the list into a tuple - sort ascending (to differentiate when we print)
more_fruit = tuple(fruit)
more_fruit = sorted(more_fruit)
print("Enumerated Tuple Below:")

#Enumerate the same as a list
for index, value in enumerate(more_fruit):
    if (index < len(more_fruit) - 1):
        print(index, value, end=", ")
    else:
        print(index, value)
print()
print("-" *20)

#-------------------------
#ENUMERATE A LIST OF TUPLES
#-------------------------

#Say you have a list of tuples with value pairs
people = [("John", "Boy", 34), ("James", "Boy", 36), ("Jamie", "Girl", 4)]

#One way to enumerate is like this ...
for index, value in enumerate(people):
    name = value[0]
    sex = value[1]
    age = value[2]
    print(str((index + 1)) + ":", "%s is a %s, and is %d years old." % (name, sex, age))
print()

#A cleaner way to achieve this is through TUPLE UNPACKING
for index, (name, sex, age) in enumerate(people):
    print(str((index + 1)) + ":", "%s is a %s, and is %d years old." % (name, sex, age))
print()
print("-" *20)

#-------------------------
#ENUMERATE A STRING
#-------------------------

#An item in a string is a single character, so enumerating over a string will return the index and value of each character
words = "Cool beans"
print("Enumerate a String:")

for index, letter in enumerate(words):
    print(index, letter)
print()
print("-" *20)

#-------------------------
#AUTOMATIC COUNTER
#-------------------------

#Enumerate for the (sole) purpose of counting each iteration
print("Count Fruit:")
for counter, value in enumerate(fruit):
    if (counter < len(fruit) - 1):
        print(counter, value, end=", ")
    else:
        print(counter, value, "\n")

#We can also store the counter via enumerate
print("Total Fruit:")
for counter, value in enumerate(fruit):
    if (counter < len(fruit) - 1):
        counter +=1
        print(value, end=", ")
    else:
        print(value, end=". ")
print("That make's", (counter + 1), "fruit.")
print()
print("-" *20)

#-------------------------
#CUSTOM STARTING INDEX
#-------------------------

#Use a custom start parameter (optional)
print("Custom Start Parameter:")
for index, value in enumerate(fruit, start=11):
    print(index, value, end=", ")
print("\n")
print("-" *20)

#Use this to be more efficient with our loops
print("Re-Print Total Fruit:")
for index, value in enumerate(fruit, start=1):
    print(index, value, end=", ")
print("\n")
print("-" *20)

#-------------------------
#DON'T ENUMERATE DICTS
#-------------------------

#Dictionaries and sets (not sequences) - their items don't have an index (and don't need one)
#To iterate over the 'keys and values' of a dictionary (a common operation) use the following:

#Create a dictinary with stock prices, and iterate over it ...
my_stocks  = {"apple": 400, "amazon": 3000, "tesla": 1200, "facebook": 320}

#Use variable.items()
print("Stocks from a Dictionary:")
for key, value in my_stocks.items():
  # k is now the key, v is the value
  print(key, ":", value)
print()
print("-" *20)

#----- Note -----

#Since sets are unordered, we cannot access items using indexes like we do in lists
#To iterate over a set just use a regular loop
    # my_set = {"a", "b", "c", "d", "e", "f", "g"}
    # for value in my_set:
    #     print(value, end=", ")

#-------------------------
#ADVANCED: DEEP DIVE
#-------------------------

# In Python, the enumerate function returns a Python object of type enumerate

# Yes, there is an enumerate built-in function and an enumerate object 🙂

# >>> type(enumerate([1, 2, 3]))
# <class 'enumerate'>

#Now let’s go to Github and check how the enumerate object is implemented.
# https://github.com/python/cpython/blob/master/Objects/enumobject.c


# As you can see, the enumerate object stores an index en_index, an iterator en_sit, and a result tuple en_result

# en_sit is actually the input parameter that we passed to the enumerate function.

# It must be an iterable object.

# At a given index, the result is a tuple of two elements.

# The first element is the index and the second one is the item in en_sit with that index.

# enumerate objects themselves are also iterables with each item being the mentioned result tuple.

# >>> list(enumerate(['a', 'b', 'c']))
# [(0, 'a'), (1, 'b'), (2, 'c')]
# That’s why when we iterate over the enumerate object with a for loop like this:

# >>> for idx, val in enumerate(['a', 'b']):
# ...   print(idx, val)
# ...
# 0 a
# 1 b
# We are effectively unpacking these tuples to an index and a value.

# But there is nothing that prevents you from doing this (but don’t do it :))

# >>> for i in enumerate(['a', 'b']):
# ...   print(i[0], i[1])
# ...
# 0 a
# 1 b
# Finally, have fun enumerating 🙂








print()
print("-" *20)