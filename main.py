#-------------------------
# ABOUT ENUMERATE
#-------------------------

# Python iterates directly over the values of a list - (does not require us to index variables manually beforehand)
# In other languages you iterate over the length of an array by an index, then use the index to get the value at that location

# Enumerate is a built in function
# It returns both the index and value of an element while iterating

#-------------------------
# ENUMERATE LISTS
#-------------------------

# Create a list to enumerate
fruit = ["apple", "pear", "orange", "cherry", "grape", "watermelon", "banana", "grapefruit"]
print("Enumerated List Below:")

# Use two arguments in the for loop (index, value)
for index, value in enumerate(fruit):
    # using if, else to prevent a comma for the last item
    if (index < len(fruit) - 1):
        print(index, value, end=", ")
    else:
        print(index, value)
# Print spacing
print()
print("-" *20)

#-------------------------
# ENUMERATE TUPLES
#-------------------------

# Convert the list into a tuple - sort ascending (to differentiate during print)
more_fruit = tuple(fruit)
more_fruit = sorted(more_fruit)
print("Enumerated Tuple Below:")

# Enumerate a tuple (same way)
for index, value in enumerate(more_fruit):
    if (index < len(more_fruit) - 1):
        print(index, value, end=", ")
    else:
        print(index, value)
# Print spacing
print()
print("-" *20)

#-------------------------
# ENUMERATE A LIST OF TUPLES
#-------------------------

# If there are tuples in your lists you do things a bit differently
people = [("John", "Boy", 34), ("James", "Boy", 36), ("Jamie", "Girl", 4)]

# One way to enumerate is like this ...
for index, value in enumerate(people):
    name = value[0]
    sex = value[1]
    age = value[2]
    print(str((index + 1)) + ":", "%s is a %s, and is %d years old." % (name, sex, age))
print()

# A cleaner way is through 'TUPLE UNPACKING'
for index, (name, sex, age) in enumerate(people, start=1):  # Note, start=1 (we'll cover later)
    print(str(index) + ":", "%s is a %s, and is %d years old." % (name, sex, age))
# Print spacing
print()
print("-" *20)

#------------------------------
# ENUMERATE STRINGS
#------------------------------

# An item in a string is a single character, so enumerating over a string will return the index and value of each character
words = "Cool beans"
print("Enumerate a String:")

for index, letter in enumerate(words):
    print(index, letter)
# Print spacing
print()
print("-" *20)

#------------------------------
# CREATE AN AUTOMATIC COUNTER
#------------------------------

# Enumerate for the sole purpose of DISPLAYING each iteration
print("Count Fruit:")
for counter, value in enumerate(fruit):
    if (counter < len(fruit) - 1):
        print(counter, value, end=", ")
    else:
        print(counter, value, "\n")

# Enumerate for the sole purpose of STORING a counter
print("Total Fruit:")
for counter, value in enumerate(fruit):
    if (counter < len(fruit) - 1):
        counter +=1
        print(value, end=", ")
    else:
        print(value, end=". ")
print("That make's", (counter + 1), "fruit.")
# Print spacing
print()
print("-" *20)

#-------------------------
# CUSTOM STARTING INDEX
#-------------------------

# Use a custom start parameter (optional)
print("Custom Start Parameter:")
for index, value in enumerate(fruit, start=11):
    print(index, value, end=", ")
print("\n")
print("-" *20)

# Use this to be more efficient with our loops
print("Re-Print Total Fruit:")
for index, value in enumerate(fruit, start=1):
    print(index, value, end=", ")
print("\n")
print("-" *20)

#-------------------------
# NO DICTIONARIES
#-------------------------

# Dictionaries and sets are not sequences - their items don't have an index (and don't need one)
# To iterate over 'keys and values' of a dictionary (a common operation) use the following:

# Create a dictinary to iterate over...
my_stocks  = {"apple": 400, "amazon": 3000, "tesla": 1200, "facebook": 320}

# Use variable.items()
print("Stocks From Dictionary:")
for key, value in my_stocks.items():
  # k is now the key, v is the value
  print(key, ":", value)
print()
print("-" *20)

#-------------------------
# NO SETS
#-------------------------

# Sets are unordered, so we can't access items using indices (like a list)
# To iterate over a set just use a regular loop
    # my_set = {"a", "b", "c", "d", "e"}
    # for value in my_set:
    #     print(value)

#-------------------------
# THE ENUMERATE OBJECT
#-------------------------

# In Python, the enumerate function returns a Python object of type enumerate
# Yes, there is an enumerate built-in function and an enumerate object

# Consider the following code:
print("Type of Function:")
print(type(enumerate([1, 2, 3])))

# It returns returns <class 'enumerate'>

# Print spacing
print()
print("-" *20)

# ----- REFERENCE -----

# The enumerate object stores an index (en_index), an iterator (en_sit), and a result tuple (en_result)
    #typedef struct {
        #PyObject_HEAD
        #Py_ssize_t en_index;           - current index of enumeration
        #PyObject* en_sit;              - secondary iterator of enumeration
        #PyObject* en_result;           - result tuple
        #PyObject* en_longindex;        - index for sequences >= PY_SSIZE_T_MAX
    #} enumobject;

# en_sit is actually the input parameter we passed to the enumerate function
# It must be an iterable object. At a given index, the result is a tuple of two elements
# The first element is the index, the second is the item (in en_sit with that index)

# ----- ENUMERATE OBJECTS ARE ITERABLE -----

# Enumerate objects themselves are iterable - each item being the mentioned result tuple
# Create a list, enumerate it (add indices), store it in "temp"
temp = list(enumerate(["a", "b", "c"]))
print("Generate Indices:")
print(temp)
# Print spacing
print()
print("-" *20)

# temp is now a tuple ...
# That’s why when we iterate over enumerate objects with for loops:
    #for index, value in enumerate(['a', 'b']):
        #print(index, value)

# We are effectively unpacking these tuples to an index and a value
# Finally, have fun enumerating 🙂