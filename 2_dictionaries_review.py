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

#use the key inside of square brackets to get at the value:
print(my_dict['name'])  
# Output: John

#use the get method to access keys:
#TODO question: can you access values this way also? 2/6/25
print(my_dict.get('age'))  
# Output: 30

#Modifying Values in a Dictionary
#Dictionaries in Python are mutable, meaning you can modify the values associated with keys. 
# You can update the value of a specific key in a dictionary as follows:

#update the age of John. Was 30 years old in old dictionary, now is 35 years old:
my_dict['age'] = 35
print(my_dict)  
# Output: {'name': 'John', 'age': 35, 'city': 'New York'}

#Adding and Removing Items
#To add a new key-value pair to a dictionary, you can simply assign a value to a new key. 
# To remove an item, you can use the pop() method or the del keyword.

# Adding a new item
my_dict['gender'] = 'Male'  
print("\nAfter adding gender")
print(my_dict)
#output: {'name': 'John', 'age': 35, 'city': 'New York', 'gender': 'Male'}

# Removing the 'city' key
my_dict.pop('city')  
print("\nAfter removing city:")
print(my_dict)
#output: {'name': 'John', 'age': 35, 'gender': 'Male'}

 # Another way to remove an item
del my_dict['age'] 
print("\nAfter removing age:")
print(my_dict)
#output: {'name': 'John', 'gender': 'Male'}

print("\nAfter adding gender, removing city key, and removing age:")
print(my_dict) 
#output:{'name': 'John', 'gender': 'Male'}

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
# and items(). 

# Here's an example of looping through a dictionary and printing key-value pairs:
print("\nWhat the dictionary looks like:")
print(my_dict)
print("\nExample of looping through a dictionary and printing key-value pairs:")
for key in my_dict:
    print(key, my_dict[key])
    #output: 
    #name John
    #gender Male

#Nested Dictionaries
#Dictionaries in Python can also contain nested dictionaries, allowing you to store more complex 
# data structures. Nested dictionaries are useful for representing hierarchical data. 

# Here's an example of a nested dictionary:
nested_dict = {'person1': {'name': 'Alice', 'age': 25}, 'person2': {'name': 'Bob', 'age': 30}}
print("\nHere's the nested_dictionary printout:")
print(nested_dict)
#output: {'person1': {'name': 'Alice', 'age': 25}, 'person2': {'name': 'Bob', 'age': 30}}


