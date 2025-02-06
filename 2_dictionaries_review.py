#Introduction
#Dictionaries in Python are one of the fundamental built-in data structures that allow 
# storing and organizing data in key-value pairs. They are mutable, unordered collections 
# of items where each item is accessed by a unique key. Dictionaries are highly flexible 
# and efficient data structures in Python, offering fast lookups and easy manipulation of data.

#Creating a Dictionary
#In Python, dictionaries are defined using curly braces {} and key-value pairs separated 
# by a colon :. Here is an example of creating a dictionary:

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

#Accessing Values in a Dictionary
#You can access the values in a dictionary using the keys. To access a specific value, 
# you can use the key inside square brackets [] or the get() method.

print(my_dict['name'])  # Output: John
print(my_dict.get('age'))  # Output: 30

#Modifying Values in a Dictionary
#Dictionaries in Python are mutable, meaning you can modify the values associated with keys. 
# You can update the value of a specific key in a dictionary as follows:

my_dict['age'] = 35
print(my_dict)  # Output: {'name': 'John', 'age': 35, 'city': 'New York'}

#Adding and Removing Items
#To add a new key-value pair to a dictionary, you can simply assign a value to a new key. 
# To remove an item, you can use the pop() method or the del keyword.

my_dict['gender'] = 'Male'  # Adding a new item
my_dict.pop('city')  # Removing the 'city' key
del my_dict['age']  # Another way to remove an item

#Dictionary Methods
#Python dictionaries come with a variety of built-in methods to manipulate and extract 
# information. Some commonly used methods include:

#keys(): Returns a list of all the keys in the dictionary.
#values(): Returns a list of all the values in the dictionary.
#items(): Returns a list of key-value pairs as tuples.
#update(): Merges one dictionary into another.
#clear(): Removes all items from the dictionary.

#Looping Through a Dictionary
#You can loop through a dictionary using various methods such as for loops, keys(), values(), 
# and items(). Here's an example of looping through a dictionary and printing key-value pairs:

for key in my_dict:
    print(key, my_dict[key])

#Nested Dictionaries
#Dictionaries in Python can also contain nested dictionaries, allowing you to store more complex 
# data structures. Nested dictionaries are useful for representing hierarchical data. Here's an 
# example of a nested dictionary:

nested_dict = {'person1': {'name': 'Alice', 'age': 25}, 'person2': {'name': 'Bob', 'age': 30}}
