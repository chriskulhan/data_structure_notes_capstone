#Data Structures in Python: Introduction

#Data structures are essential components in programming that allow you to 
# efficiently organize and manipulate data. In Python, there are various data 
# structures available, each with its own characteristics and use cases. This 
# topic will introduce you to some of the fundamental data structures in Python, 
# including dictionaries, tuples, lists, and sets.

#Creating a dictionary
employee = {
    'name': 'John Doe',
    'age': 30,
    'department': 'IT'
}

# Accessing values in a dictionary
print(employee['name'])
print(employee.get('age'))

#Tuples
#Tuples in Python are immutable sequences, meaning their elements cannot be 
# changed once they are defined. Tuples are typically used to store collections 
# of related data that should not be modified. Tuples are created by enclosing 
# elements in parentheses ( ).

# Creating a tuple
colors = ('red', 'green', 'blue')

# Accessing elements in a tuple
print(colors[0])

#Lists
#Lists are mutable collections of elements in Python, allowing you to add, 
# remove, or modify elements as needed. Lists are created by enclosing elements 
# in square brackets [ ]. Lists are versatile data structures that can store a 
# mix of different data types.

# Creating a list
numbers = [1, 2, 3, 4, 5]

# Modifying a list
numbers.append(6)

#Sets
#Sets in Python are unordered collections of unique elements. Sets are commonly 
# used when you need to perform operations such as union, intersection, or 
# difference between multiple sets. Sets are created by enclosing elements 
# in curly braces { }.

# Creating a set
fruits = {'apple', 'banana', 'orange'}

 # Performing set operations
vegetables = {'carrot', 'spinach'}

 # Union of sets
print(fruits.union(vegetables))

#By understanding and utilizing these data structures effectively, 
# you can enhance the efficiency and performance of your Python programs 
# when working with different types of data. Practice implementing these 
# data structures in various scenarios to solidify your understanding and 
# improve your programming skills.