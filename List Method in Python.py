# Let's say we have a list of random numbers
numbers = [23, 4, 7, 123, 90, 71, 32, 40]

# This is a 1-d list.
## There are a lot of List methods that we can use to manipulate the data.

# Firstly - 'APPEND' method can be used to add more elements into the list.
numbers.append(256)
print(numbers) # If you run the program, you'll see that the new element is placed at the very last

# Use 'INDEX' to locate the index of the number
print(numbers.index(7))

# If we not sure of the element, use 'IN' operator
print(100 in numbers)

# So if the placement is important, you need to use 'INSERT' method
numbers.insert(1, 77) # here we add another element at the 1st index (second item)
print(numbers)

# If we wan to remove an item from the list, use 'REMOVE' method
numbers.remove(90)
print(numbers)

# Use 'POP' method to remove the last element/item
numbers.pop()
print(numbers)

# 'SORT' method is used to sort the data in ascending order
numbers.sort()
print(numbers)

# Meanwhile 'REVERSE' method is used to put the list in descinding order
numbers.reverse()
print(numbers)

numbers.append(77)

# Use 'COUNT' method to calculate similar element
print(numbers.count(77))

# Use 'COPY' method to easily duplicate a list
# In order to delete all elements inside a list, use 'CLEAR' method

numbers2 = numbers.copy()
numbers.clear()
print(numbers2)
print(numbers) # You will find that all of the elements will be gone!


