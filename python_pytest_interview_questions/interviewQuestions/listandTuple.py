#explain difference between list and tuple in python

# In Python, both lists and tuples are used to store collections of items, but they have some key differences:
# List are mutable > they can be modified after creation (you can add, remove, or change items).
# Tuples are immutable > once created, they cannot be changed (you cannot add, remove, or change items).


#List -> stores collection of elements
#List are created using square breackets [] and can contain elements of different data types.  
myList = [1, 2, 3, 4, 5, 'rutu']

myList[0] = 100

print("List after modification:", myList)  # Output: List after modification: [100, 2, 3, 4, 5]

myList.append(6)  # Adding an element to the list
print("list after appending element", myList)

myList.remove(100) # removes the element from the list
print("list after removing element", myList)


myList.pop(0) 
print("list after removing element at index 1", myList)

#Tuple -> stores collection of elements
#Tuples are created using parentheses () and can also contain elements of different data types.
# tuples are immutable, so we cannot modify them after creation.

my_tuple = (1, 2, 3, 4, 5, 'rutu')
# my_tuple[0] = 100  # This will raise a TypeError because tuples are immutable
# print(my_tuple)