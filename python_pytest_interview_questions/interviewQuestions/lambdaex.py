def add(x,y):
    return x + y

add = lambda  x,y : x + y

"""
    consider a list, now what does map function do?
    Can the whole list and multiply each element by 2 and return a new list? 
        traditional way to iterate elements through for loop and multiple by 2
        but with lambda and map function it can be done in one single line
"""

numbers = [1, 2, 3, 4, 5]

answerMap = map(lambda x: x * 2, numbers)  # Output: [2, 4, 6, 8, 10]
print(list(answerMap))

# tuple
test = (1, 2, 3, 4, 5)
cube = map(lambda x : x * 3, test)
print(tuple(cube))
"""
    filter function is used to filter out elements from a list based on a condition
    for example, we can filter out all the even numbers from a list using filter function
"""

even_numbers= list(filter(lambda x : x % 2 == 0, numbers))
print(even_numbers)

# sort list in python
num = [5, 2, 9, 1, 5, 6]
print(sorted(num))