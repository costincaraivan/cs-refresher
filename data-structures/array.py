# Will only simulate C-like array behavior.
# Some of these operations don't really make sense on Python "arrays" are actually
# a more complex data structure based on lists. Still, will go through the steps
# just as "practice".

# Creation. O(1).
myArray = []
print("myArray created: {}".format("myArray" in dir()))

# Deletion. O(1).
del myArray
print("myArray deleted: {}".format("myArray" not in dir()))
# Re-creating the array as we'll keep using it.
myArray = [ 1, 2, 3 ]

# Search - will not be included here, will move it to its own category (search).

# Insert at the start. O(1)
# Doesn't really make sense for Python array. For normal, fixed-sized arrays
# every insert requires creating a new array and copying the existing contents
# "around" the insert.
myArray = [ 0 ] + myArray
print("myArray is: {}".format(myArray))

# Alternativelly, if insert at the start is interpreted as 
# "replace the first element".
myArray[0] = 1
print("myArray is: {}".format(myArray))

# Insert at the middle. O(1).
arrayLength = len(myArray)
myArray = myArray[:arrayLength // 2] + [ 5 ] + myArray[arrayLength // 2:]
print("myArray is: {}".format(myArray))
# Alternatively, if it's replace element.
myArray[arrayLength // 2] = 6
print("myArray is: {}".format(myArray))

# Insert at the end. O(1).
myArray = myArray + [ 4 ]
arrayLength = len(myArray)
print("myArray is: {}".format(myArray))
# Alternatively, if it's replace element.
myArray[arrayLength - 1] = 5
print("myArray is: {}".format(myArray))

# Join with fixed-sized arrays imply creating a new array with size M + N.
# With Python we "cheat".
myArray = myArray + [ 6, 7, 8 ]
print("myArray is: {}".format(myArray))
