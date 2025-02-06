#Manipulating Tuples and Other Data Structures in Python

#Tuples in Python
#In Python, a tuple is an immutable sequence of elements. Immutable means that once a tuple is created, 
# its elements cannot be modified. Tuples are defined using parentheses and can contain elements of 
# different data types. For example:

my_tuple = (1, 'apple', 3.14)

#Accessing Elements in a Tuple
#You can access individual elements in a tuple using indexing. Python uses zero-based indexing, 
# so the first element in a tuple has an index of 0. For example:

my_tuple = (1, 'apple', 3.14)
print(my_tuple[0])  
# Output: 1

#Manipulating Tuples
#While tuples are immutable, you can manipulate them by creating new tuples based on existing ones. 
# For example, you can concatenate two tuples using the + operator:

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
combined_tuple = tuple1 + tuple2
print(combined_tuple)  
# Output: (1, 2, 3, 'a', 'b', 'c')

#Other Data Structures
#In addition to tuples, Python supports a variety of data structures such as lists, dictionaries, and sets. 
# These data structures provide flexibility and efficiency for different types of operations.

#Lists
#Lists in Python are similar to tuples but are mutable, allowing you to modify elements after creation. 
# Lists are defined using square brackets and can be modified using methods like append(), insert(), and remove(). 
# For example:


my_list = [1, 2, 3]
print(my_list)

my_list.append(4)
print("\nAfter appending 4 to the list:")
print(my_list)  
# Output: [1, 2, 3, 4]

my_list.insert(0,12)
print("\nAfter inserting 12 before the 0 index using insert:")
print(my_list)
#output:[12, 1, 2, 3, 4]

my_list.remove(4)
print("\n After removing the *value* 4 from the list using remove:")
print(my_list)
#output: [12, 1, 2, 3]

# my_list.remove(13)
# print("\nIf I try to remove a value that's not in the list:")
# print(my_list)
#get a value error:
#output: ValueError: list.remove(x): x not in list

#Dictionaries
#Dictionaries in Python store key-value pairs and are implemented using curly braces {}. You can access, 
# modify, and delete elements in a dictionary based on their keys. For example:

my_dict = {'name': 'Alice', 'age': 30}
print(my_dict['name'])  
# Output: Alice

#Sets
#Sets in Python are collections of unique elements. Sets are defined using curly braces {} or the set() 
# function. Sets support mathematical operations like union, intersection, and difference. For example:

my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
union_set = my_set1.union(my_set2)
print("\nmy_set1")
print(my_set1)
print("\nmy_set2")
print(my_set2)
print("\nIf I make a union of the two, only the unique numbers will show:")
print(union_set)  
# Output: {1, 2, 3, 4, 5}

#intersection in sets:
intersection_set = my_set1.intersection(my_set2)
print("\nThis is an intersection between my_set1 and my_set2:")
print(intersection_set)
#output:{3}

#difference in sets: 
#TODO I don't understand this one. 
difference_set = my_set1.difference(my_set2)
print("\nThis is the difference between my_set1 and my_set2:")
print(difference_set)
#output: {1, 2}

#By understanding how to manipulate tuples and other data structures in Python, you can efficiently work 
# with different types of data and perform a wide range of operations within your programs.

